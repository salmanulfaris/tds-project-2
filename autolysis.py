# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "matplotlib",
#     "seaborn",
#     "httpx",
#     "tabulate",
#     "python-dotenv",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import httpx
from dotenv import load_dotenv

load_dotenv()

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

LLM_ENDPOINT = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)


def send_text_to_llm(prompt, max_tokens=1000):
    headers = {"Authorization": f"Bearer {AIPROXY_TOKEN}"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    try:
        response = httpx.post(LLM_ENDPOINT, json=data, headers=headers, timeout=40)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return None


def analyze_data(df):
    summary_stats = df.describe(include="all").transpose()
    missing_values = df.isnull().sum()
    correlation_matrix = df.corr(numeric_only=True)

    values_counts = {}
    unique_values = {}

    for col in df.columns:
        values_counts[col] = df[col].value_counts()
        unique_values[col] = df[col].unique()
    return {
        "columns": df.info(),
        "column_names": df.columns,
        "values_counts": values_counts,
        "unique_values": unique_values,
        "summary_stats": summary_stats,
        "missing_values": missing_values,
        "correlation_matrix": correlation_matrix,
    }


def visualize_data(df, correlation_matrix, output_dir):
    # Histogram for numeric columns
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        output_path = os.path.join(output_dir + '/static', f"{col}_distribution.png")
        plt.savefig(output_path)
        plt.close()


def generate_story(df, analysis_results, output_dir):
    common_data_for_prompt = ("Here is the summary of a dataset:\n\n"
                              f"{df.head(5).to_string(index=False)}\n\n"
                              "Summary Statistics:\n"
                              f"{analysis_results['summary_stats'].to_string()}\n\n"
                              "Column summary \n"
                              f"{analysis_results['columns']}\n\n"
                              "Values counts \n"
                              f"{analysis_results['values_counts']}\n\n"
                              "Unique Values \n"
                              f"{analysis_results['unique_values']}\n\n"
                              "Missing Values:\n"
                              f"{analysis_results['missing_values'].to_string()}\n\n"
                              "Correlation Matrix:\n"
                              f"{analysis_results['correlation_matrix'].to_string()}\n\n")

    summary_prompt = (
            common_data_for_prompt + "\n\n"
                                     "Write a story summarizing the data, analysis, and potential insights and tabular infos about missing values,data types (if any). use emoji in the content to make it more stylish and readable"
    )
    story = send_text_to_llm(summary_prompt)

    visualisation_prompt = (
            common_data_for_prompt + "\n\n"
                                     "write code to generate visual analysis for an data. return only the python code,df is the variable which "
                                     f"dataframe is present and plt is available as matplotlib and seaborn as sns and save those image to {output_dir} "
    )
    visualisation_code = send_text_to_llm(visualisation_prompt)

    if visualisation_code:
        visualisation_code = visualisation_code.replace("```python\n", "").replace("```", "").replace("df.corr()",
                                                                                                      "df.corr(numeric_only=True)")
        try:
            exec(visualisation_code)
        except Exception as e:
            print(f"AI Visualisation code failed , {e}")

    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write("# 🤖Automated Analysis Report\n\n")
        f.write("#### 📦 Column(s) Available \n\n")
        f.write(f"`{'`,`'.join(analysis_results['column_names'].to_list())}` \n\n")
        f.write("#### 🪫Column with missing Values \n\n")
        f.write(analysis_results['missing_values'][analysis_results['missing_values'] > 0].to_markdown())
        f.write("\n\n")
        if story:
            f.write("## 💡Story\n")
            f.write(story)

        f.write("\n\n### 🌉Visual Analysis 2.0 \n")
        for img_file in os.listdir(output_dir):
            if img_file.endswith(".png"):
                f.write(f"![{img_file}]({img_file.replace(' ' ,'_')})\n")

        f.write("\n\n### 🌉Visualizations of Distribution \n")
        for img_file in os.listdir(output_dir + '/static'):
            if img_file.endswith(".png"):
                f.write(f"![{img_file}](static/{img_file.replace(' ','_')})\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    output_dir = os.path.splitext(input_file)[0]
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(output_dir + '/static', exist_ok=True)

    try:
        df = pd.read_csv(input_file, encoding='latin-1')
        analysis_results = analyze_data(df)
        visualize_data(df, analysis_results["correlation_matrix"], output_dir)
        generate_story(df, analysis_results, output_dir)
        print(f"Analysis completed. Results saved in '{output_dir}' directory.")
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
