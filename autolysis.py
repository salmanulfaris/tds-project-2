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
# Grouped global constants for API Call to LLM
API_CONFIG = {
    "LLM_ENDPOINT": "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    "AIPROXY_TOKEN": os.getenv("AIPROXY_TOKEN")
}

if not API_CONFIG['AIPROXY_TOKEN']:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)


# Function for sending text to LLM
def send_text_to_llm(prompt, max_tokens=1000):
    headers = {"Authorization": f"Bearer {API_CONFIG['AIPROXY_TOKEN']}"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    try:
        response = httpx.post(API_CONFIG['LLM_ENDPOINT'], json=data, headers=headers, timeout=40)
        print(response.json())
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return None


def analyze_data(df):
    """
    Analyzes a DataFrame and returns a dictionary containing various statistical and structural insights.

    Parameters:
    df (pandas.DataFrame): The DataFrame to be analyzed.

    Returns:
    dict: A dictionary containing the following information:
        - 'columns': Information about the DataFrame's columns (data types, non-null counts, etc.).
        - 'column_names': A list of the DataFrame's column names.
        - 'values_counts': A dictionary where each key is a column name and each value is the count of unique values in that column.
        - 'unique_values': A dictionary where each key is a column name and each value is an array of unique values in that column.
        - 'summary_stats': A DataFrame containing summary statistics for each column (e.g., mean, std, min, max).
        - 'missing_values': A Series with the count of missing (NaN) values for each column.
        - 'correlation_matrix': A DataFrame showing correlation coefficients between numeric columns.

    This function provides a comprehensive overview of the DataFrame's structure, distributions, and relationships.

    Example:
        result = analyze_data(df)
        print(result["summary_stats"])  # Print summary statistics of the DataFrame
    """

    # Generate summary statistics for all columns (numerical and categorical)
    summary_stats = df.describe(include="all").transpose()

    # Count the missing values in each column
    missing_values = df.isnull().sum()

    # Generate the correlation matrix for numeric columns
    correlation_matrix = df.corr(numeric_only=True)

    # Initialize dictionaries to store value counts and unique values for each column
    values_counts = {}
    unique_values = {}

    # Loop through each column in the DataFrame to get value counts and unique values
    for col in df.columns:
        values_counts[col] = df[col].value_counts()  # Store counts of unique values for each column
        unique_values[col] = df[col].unique()  # Store unique values for each column

    # Return a dictionary containing all the collected insights
    return {
        "columns": df.info(),  # Information about the DataFrame's columns (including types and non-null counts)
        "column_names": df.columns,  # List of column names
        "values_counts": values_counts,  # Dictionary of value counts per column
        "unique_values": unique_values,  # Dictionary of unique values per column
        "summary_stats": summary_stats,  # Summary statistics for all columns
        "missing_values": missing_values,  # Missing values count for each column
        "correlation_matrix": correlation_matrix,  # Correlation matrix for numeric columns
    }


def visualize_data(df, output_dir):
    """
    Generates histograms for numeric columns in the given DataFrame and saves them as PNG images.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be visualized.
    output_dir (str): The directory where the output images will be saved.

    This function iterates through all numeric columns in the DataFrame, generates a histogram (with KDE)
    for each column, and saves the resulting plot as a PNG file in the specified output directory.

    The saved images will be stored under a subdirectory 'static' within the given `output_dir`.

    Example:
        visualize_data(df, "/path/to/save/plots")
    """

    # Select numeric columns in the DataFrame
    numeric_cols = df.select_dtypes(include="number").columns

    # Iterate over each numeric column to generate and save the plot
    sns.set_palette("tab10")

    # Create a figure with a grid of subplots
    num_cols = len(numeric_cols)
    n_rows = (num_cols // 3) + (num_cols % 3 > 0)  # Adjust the number of rows based on the number of columns
    n_cols = 3  # You can change this to suit the number of columns per row

    # Create a single figure with subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    # Flatten axes array for easier iteration (in case of multi-dimensional grid)
    axes = axes.flatten()

    # Iterate over numeric columns and plot on each subplot
    for i, col in enumerate(numeric_cols):
        # Plot a histogram with a Kernel Density Estimate (KDE) for the current column
        sns.histplot(df[col].dropna(), kde=True, ax=axes[i])

        # Set the title and axis labels for the plot
        axes[i].set_title(f"Distribution of {col}")
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Frequency")

    # Remove any unused subplots (in case the number of columns isn't a perfect multiple of 3)
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    # Adjust layout for better spacing between subplots
    plt.tight_layout()

    # Generate the file path where the plot will be saved
    output_path = os.path.join(output_dir, "all_distributions.png")

    # Save the combined plot as a PNG file
    plt.savefig(output_path)

    # Close the plot to avoid memory issues
    plt.close()


def generate_story(df, analysis_results, output_dir):
    """
    Generates an analysis story, visualizations, and a report for a given DataFrame.

    Parameters:
    df (pandas.DataFrame): The dataset to analyze.
    analysis_results (dict): The results of previous data analysis containing various statistics and data insights.
    output_dir (str): The directory where the analysis results, visualizations, and README will be saved.

    This function creates a comprehensive analysis report by:
    - Sending a prompt to a language model (LLM) to generate a story summarizing the data.
    - Requesting code from the LLM to create visualizations of the data.
    - Executing the visual code and saving the visualizations as image files.
    - Writing the analysis, story, and visualizations into a markdown README file.

    Example:
        generate_story(df, analysis_results, "/path/to/output")
    """

    # Prepare a common summary of the dataset, including:
    # - First 5 rows of the DataFrame
    # - Summary statistics
    # - Column information (types, non-null counts, etc.)
    # - Value counts and unique values for each column
    # - Missing values and correlation matrix
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

    # Generate a prompt to request the LLM to create a story summarizing the data
    summary_prompt = (
            common_data_for_prompt + "\n\n"
                                     "Write a story summarizing the data, analysis, and potential insights and tabular infos about missing values, data types (if any). Use emoji in the content to make it more stylish and readable."
    )
    # Send the prompt to the LLM to generate a story
    story = send_text_to_llm(summary_prompt)

    # Generate a prompt to request the LLM to write code for visualizations and Most important EDA relevant for data available
    visualisation_prompt = (
            common_data_for_prompt + "\n\n"
                                     f"Write code to generate visual analysis for a DataFrame. Return only the Python code. Assume 'df' is the variable holding the dataset, 'plt' is available as matplotlib, and 'sns' as seaborn. Save the images directory ./{output_dir}/static ."
    )
    # Send the prompt to the LLM to generate the visualization code
    visualisation_code = send_text_to_llm(visualisation_prompt)

    # If visualization code was generated successfully, clean and execute it
    if visualisation_code:
        # Clean the code by removing code block formatting and fixing dataframe correlation function
        visualisation_code = visualisation_code.replace("```python\n", "").replace("```", "").replace("df.corr()",
                                                                                                      "df.corr(numeric_only=True)")
        try:
            # Execute the visualization code and necessary EDA Code from LLM
            exec(visualisation_code)
        except Exception as e:
            # Log any errors that occur while executing the visualization code
            print(f"AI Visualization code failed, {e}")

    # Write the analysis results and generated content to a README markdown file
    with open(os.path.join(output_dir, "README.md"), "w") as f:
        # Start the report with a title and an overview
        f.write("# 🤖 Automated Analysis Report\n\n")

        # Write the list of columns available in the dataset
        f.write("#### 📦 Column(s) Available \n\n")
        f.write(f"`{'`,`'.join(analysis_results['column_names'].to_list())}` \n\n")

        # Write the columns that have missing values
        f.write("#### 🪫 Column(s) with Missing Values \n\n")
        f.write(analysis_results['missing_values'][analysis_results['missing_values'] > 0].to_markdown())
        f.write("\n\n")

        # If the story was generated, write it in the README
        if story:
            f.write("## 💡 Story\n")
            f.write(story)

        # Add a section for visual analysis
        f.write("\n\n### 🌉 Visual Analysis 2.0 \n")
        # Include generated visualizations (if any)
        for img_file in os.listdir(output_dir):
            if img_file.endswith(".png"):
                f.write(f"![{img_file}](static/{img_file.replace(' ', '_')})\n")

        # Add section for visualizations of distributions from the 'static' folder
        f.write("\n\n### 🌉 Visualizations of Distribution \n")
        for img_file in os.listdir(output_dir):
            if img_file.endswith(".png"):
                f.write(f"![{img_file}]({img_file.replace(' ', '_')})\n")


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
        visualize_data(df, output_dir)
        generate_story(df, analysis_results, output_dir)
        print(f"Analysis completed. Results saved in '{output_dir}' directory.")
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
