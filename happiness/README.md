# The Global Happiness Index: Unveiling Life Satisfaction Across Borders

## Data Description

The dataset we’re exploring comprises **2363 rows** and **11 columns**, offering a robust collection of metrics related to people’s well-being across various countries and years. At its core, it provides a matrix of factors contributing to the **"Life Ladder,"** which is a representation of subjective well-being or happiness as perceived by individuals in different regions. 

### Key Features:
- **Country name**: The name of the country.
- **Year**: The year of the survey.
- **Life Ladder**: A numeric value expressing individuals' self-reported happiness.
- **Log GDP per capita**: A logarithmic transformation of the GDP per capita, indicating economic status.
- **Social support**: Metrics on the perceived level of support from friends or family.
- **Healthy life expectancy at birth**: The average expected number of years a newborn would live in a healthy state.
- **Freedom to make life choices**: A measure of individuals' perceived freedom in their decision-making.
- **Generosity**: Individuals' perception of charitable behavior in their country.
- **Perceptions of corruption**: Levels of perceived corruption in the government and businesses.
- **Positive affect** and **Negative affect**: Measures of the proportion of time individuals felt positive or negative emotions.

### Missing Values
While the dataset is rich, several columns contain missing values, with **Generosity** and **Perceptions of corruption** experiencing the most significant gaps. These missing entries can affect the overall analysis and should be handled with care.

---

## Key Insights

The dataset paints a vivid picture of global well-being, with several striking insights:

1. **Average Life Ladder**:
   - The average **Life Ladder** score is **5.48**, indicating a moderate level of self-reported happiness. The variability (standard deviation of **1.13**) suggests notable differences in life satisfaction among countries.

2. **Economic Indicators**:
   - The average **Log GDP per capita** stands at **9.40**, translating to an overall economic health that correlates positively with happiness scores. This is consistent with existing literature showing a relationship between economic prosperity and well-being.

3. **Social Support is Key**:
   - Among the features measured, **Social support** emerged as the most critical predictor of happiness, with an importance score of **0.1573**. This underscores the human need for connection and interaction in fostering contentment.

4. **Perceptions of Corruption Matter**:
   - The perceived levels of corruption significantly affect happiness, with a notable importance score of **0.1134**. Countries with lower corruption levels often reveal higher self-reported happiness.

5. **Life Choices and Happiness**:
   - The freedom to make personal choices ranks as another vital feature, reiterating that autonomy plays a crucial role in personal contentment.

---

## Potential Implications

The insights gained from this dataset offer remarkable implications for policymakers, researchers, and communities striving to enhance well-being:

1. **Focus on Social Infrastructure**:
   - Effective policies should prioritize building social networks and support systems. Governments can facilitate community programs that foster social ties, helping to uplift citizens’ happiness levels.

2. **Economic Development and GDP**:
   - With the evident link between GDP and happiness, strategies should aim at economic growth that is equitable and sustainable. Policies that enhance GDP while considering social welfare can yield a happier populace.

3. **Addressing Corruption**:
   - Reducing corruption not only builds trust in institutions but directly amplifies life satisfaction. Transparency and accountability measures should be at the forefront of governance reform.

4. **Holistic Well-being Programs**:
   - Initiatives that promote mental well-being and allow individuals to express their thoughts freely are vital. This includes emotional and psychological support avenues that counteract negative emotions, as reflected in the dataset.

5. **Further Research**:
   - The gaps in data concerning generosity and corruption should encourage more in-depth studies. Quantifying the effects of these factors could lead to tailored interventions aimed at boosting happiness.

In conclusion, the Global Happiness Index dataset unearthed invaluable insights that link economic indicators, social support, and governance with the well-being of individuals. Harnessing these insights can lead to meaningful changes that uplift happiness across nations, reinforcing the notion that happiness is a collective endeavor.

## Visualizations

### Analysis Visualizations
![Analysis Visualizations](analysis_visualizations.png)

### Pairwise Distribution
![Pairwise Distribution](distribution_pairplot.png)


## Descriptive Statistics

| Statistic | year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|---|---|---|---|---|---|---|---|---|---|---|
| count | 2363.00 | 2363.00 | 2335.00 | 2350.00 | 2300.00 | 2327.00 | 2282.00 | 2238.00 | 2339.00 | 2347.00 |
| mean | 2014.76 | 5.48 | 9.40 | 0.81 | 63.40 | 0.75 | 0.00 | 0.74 | 0.65 | 0.27 |
| std | 5.06 | 1.13 | 1.15 | 0.12 | 6.84 | 0.14 | 0.16 | 0.18 | 0.11 | 0.09 |
| min | 2005.00 | 1.28 | 5.53 | 0.23 | 6.72 | 0.23 | -0.34 | 0.04 | 0.18 | 0.08 |
| 25% | 2011.00 | 4.65 | 8.51 | 0.74 | 59.20 | 0.66 | -0.11 | 0.69 | 0.57 | 0.21 |
| 50% | 2015.00 | 5.45 | 9.50 | 0.83 | 65.10 | 0.77 | -0.02 | 0.80 | 0.66 | 0.26 |
| 75% | 2019.00 | 6.32 | 10.39 | 0.90 | 68.55 | 0.86 | 0.09 | 0.87 | 0.74 | 0.33 |
| max | 2023.00 | 8.02 | 11.68 | 0.99 | 74.60 | 0.98 | 0.70 | 0.98 | 0.88 | 0.70 |

## Feature Importance

| Feature | Importance |
|---|---|
| Social support | 0.1573 |
| Log GDP per capita | 0.1515 |
| Life Ladder | 0.1223 |
| Perceptions of corruption | 0.1134 |
| Positive affect | 0.0911 |
| Healthy life expectancy at birth | 0.0833 |
| Freedom to make life choices | 0.0723 |
| Generosity | 0.0629 |
| year | 0.0300 |

## Correlation Matrix

| Feature | year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|---|---|---|---|---|---|---|---|---|---|---|
| year | 1.00 | 0.05 | 0.08 | -0.04 | 0.17 | 0.23 | 0.03 | -0.08 | 0.01 | 0.21 |
| Life Ladder | 0.05 | 1.00 | 0.78 | 0.72 | 0.71 | 0.54 | 0.18 | -0.43 | 0.52 | -0.35 |
| Log GDP per capita | 0.08 | 0.78 | 1.00 | 0.69 | 0.82 | 0.36 | -0.00 | -0.35 | 0.23 | -0.26 |
| Social support | -0.04 | 0.72 | 0.69 | 1.00 | 0.60 | 0.40 | 0.07 | -0.22 | 0.42 | -0.45 |
| Healthy life expectancy at birth | 0.17 | 0.71 | 0.82 | 0.60 | 1.00 | 0.38 | 0.02 | -0.30 | 0.22 | -0.15 |
| Freedom to make life choices | 0.23 | 0.54 | 0.36 | 0.40 | 0.38 | 1.00 | 0.32 | -0.47 | 0.58 | -0.28 |
| Generosity | 0.03 | 0.18 | -0.00 | 0.07 | 0.02 | 0.32 | 1.00 | -0.27 | 0.30 | -0.07 |
| Perceptions of corruption | -0.08 | -0.43 | -0.35 | -0.22 | -0.30 | -0.47 | -0.27 | 1.00 | -0.27 | 0.27 |
| Positive affect | 0.01 | 0.52 | 0.23 | 0.42 | 0.22 | 0.58 | 0.30 | -0.27 | 1.00 | -0.33 |
| Negative affect | 0.21 | -0.35 | -0.26 | -0.45 | -0.15 | -0.28 | -0.07 | 0.27 | -0.33 | 1.00 |
