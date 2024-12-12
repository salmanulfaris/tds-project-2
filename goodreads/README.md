# The Literary Landscape: Unveiling a Rich Dataset of Book Insights

The world of literature encompasses billions of stories, worlds, and characters waiting to be explored. Our dataset, a treasure trove of literary data, seeks to unravel trends, author dynamics, and readers' engagements. Let’s dive into the details and discover what this dataset has to tell us about published books, author popularity, and reader preferences.

## 📊 Data Description

Our dataset is large and comprehensive, comprising:

- **Total Rows:** 10,000
- **Total Columns:** 23

These columns include important identifiers and attributes like `book_id`, `authors`, `original_publication_year`, and various ratings. Here’s a brief overview of some of the key column types:

| Column                       | Description                                       |
|------------------------------|---------------------------------------------------|
| `book_id`                    | Unique identifier for each book                   |
| `authors`                    | Names of the book's authors                       |
| `average_rating`             | Average reader rating from 1 to 5                |
| `ratings_count`              | Total count of ratings received                   |
| `original_publication_year`  | Year when the book was first published            |
| `work_text_reviews_count`    | Number of textual reviews provided by readers     |

However, like many datasets, it has some missing values—most notably:

- `isbn`: 700 missing
- `isbn13`: 585 missing
- `original_publication_year`: 21 missing
- `language_code`: 1084 missing

Despite these gaps, the dataset is robust enough to yield significant insights.

## 🔍 Key Insights

### 1. **Rating Dynamics**
The average rating across the dataset is **4.00**, suggesting that books generally resonate well with readers. However, the wide range in `ratings_count` (from 3 to 4,780,653) indicates that while some books are universally loved, others remain undiscovered stray gems amidst the literary cosmos.

### 2. **Publication Trends**
The dataset reveals publication years from a maximum of **2017** down to **1750**. The **mean** publication year is around **1981.99**, showcasing a strong presence of modern literature. Analyzing trends in publication time could provide insights into the evolution of genres and reader preferences through the decades.

### 3. **Author Popularity**
The `work_ratings_count` and `ratings_count` stand out as the most important features in determining the popularity and engagement of books, with importance values of **1.0582** and **1.0502** respectively. This emphasizes the role of both the total number of ratings and the aggregated insights from reviews in gauging a book's appeal.

### 4. **Diversity in Ratings**
While the average rating is favorable, the distribution of ratings shows slight disparities. For example, the **ratings for 1 star** (342.6) are significantly outnumbered by **5 stars** (19965.7). This disparity in extremes suggests that the majority of readers are polarized: they either love or loathe certain books.

### 5. **Language Code Distribution**
With **1,084 missing values** in `language_code`, there’s potential for exploring the hidden richness of global literature. Identifying missing language codes can lead to understanding which languages are underserved in the dataset.

## 🚀 Potential Implications

### 1. **For Readers and Book Lovers**
This dataset can serve as a powerful recommendation engine for readers. By analyzing average ratings, total ratings, and reviews, one can easily identify blockbuster books or hidden gems in various genres.

### 2. **For Publishers and Authors**
Understanding trends regarding `work_ratings_count` and `average_rating` can help publishers market books better. Insights regarding peak publication years can inform strategic release timelines.

### 3. **For Researchers**
Scholars delving into the cultural significance of literature can utilize this data to analyze changes over decades. It could elucidate how societal shifts influence reading habits and preferences.

### 4. **For Linguistic Diversity**
The high number of missing `language_code` entries suggests an opportunity for enhancing the dataset to cover more languages, thereby promoting global literature and increasing cross-cultural dialogue.

## 🌟 Conclusion

In a universe of words, this dataset offers a poignant glimpse into the reading preferences and dynamics surrounding literature. The insights unveiled here can empower readers, writers, and scholars alike, shaping the present and future of the literary domain. Embracing data storytelling allows us to weave evidence into narratives that enrich our understanding and appreciation of books, reminding us that every dataset tells a story waiting to be uncovered. 📚✨

## Visualizations

### Analysis Visualizations
![Analysis Visualizations](analysis_visualizations.png)

### Pairwise Distribution
![Pairwise Distribution](distribution_pairplot.png)


## Descriptive Statistics

| Statistic | book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn13 | original_publication_year | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| count | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 9415.00 | 9979.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 | 10000.00 |
| mean | 5000.50 | 5264696.51 | 5471213.58 | 8646183.42 | 75.71 | 9755044298883.46 | 1981.99 | 4.00 | 54001.24 | 59687.32 | 2919.96 | 1345.04 | 3110.89 | 11475.89 | 19965.70 | 23789.81 |
| std | 2886.90 | 7575461.86 | 7827329.89 | 11751060.82 | 170.47 | 442861920665.57 | 152.58 | 0.25 | 157369.96 | 167803.79 | 6124.38 | 6635.63 | 9717.12 | 28546.45 | 51447.36 | 79768.89 |
| min | 1.00 | 1.00 | 1.00 | 87.00 | 1.00 | 195170342.00 | -1750.00 | 2.47 | 2716.00 | 5510.00 | 3.00 | 11.00 | 30.00 | 323.00 | 750.00 | 754.00 |
| 25% | 2500.75 | 46275.75 | 47911.75 | 1008841.00 | 23.00 | 9780316192995.00 | 1990.00 | 3.85 | 13568.75 | 15438.75 | 694.00 | 196.00 | 656.00 | 3112.00 | 5405.75 | 5334.00 |
| 50% | 5000.50 | 394965.50 | 425123.50 | 2719524.50 | 40.00 | 9780451528640.00 | 2004.00 | 4.02 | 21155.50 | 23832.50 | 1402.00 | 391.00 | 1163.00 | 4894.00 | 8269.50 | 8836.00 |
| 75% | 7500.25 | 9382225.25 | 9636112.50 | 14517748.25 | 67.00 | 9780830777175.00 | 2011.00 | 4.18 | 41053.50 | 45915.00 | 2744.25 | 885.00 | 2353.25 | 9287.00 | 16023.50 | 17304.50 |
| max | 10000.00 | 33288638.00 | 35534230.00 | 56399597.00 | 3455.00 | 9790007672390.00 | 2017.00 | 4.82 | 4780653.00 | 4942365.00 | 155254.00 | 456191.00 | 436802.00 | 793319.00 | 1481305.00 | 3011543.00 |

## Feature Importance

| Feature | Importance |
|---|---|
| work_ratings_count | 1.0582 |
| ratings_count | 1.0502 |
| book_id | 0.8818 |
| ratings_4 | 0.8362 |
| ratings_3 | 0.4896 |
| ratings_2 | 0.3643 |
| ratings_1 | 0.3426 |
| work_text_reviews_count | 0.3040 |
| average_rating | 0.1722 |
| books_count | 0.1091 |
| goodreads_book_id | 0.0326 |
| best_book_id | 0.0311 |
| work_id | 0.0209 |
| original_publication_year | 0.0125 |
| isbn13 | 0.0053 |

## Correlation Matrix

| Feature | book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn13 | original_publication_year | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| book_id | 1.00 | 0.12 | 0.10 | 0.11 | -0.26 | -0.01 | 0.05 | -0.04 | -0.37 | -0.38 | -0.42 | -0.24 | -0.35 | -0.41 | -0.41 | -0.33 |
| goodreads_book_id | 0.12 | 1.00 | 0.97 | 0.93 | -0.16 | -0.05 | 0.13 | -0.02 | -0.07 | -0.06 | 0.12 | -0.04 | -0.06 | -0.08 | -0.06 | -0.06 |
| best_book_id | 0.10 | 0.97 | 1.00 | 0.90 | -0.16 | -0.05 | 0.13 | -0.02 | -0.07 | -0.06 | 0.13 | -0.03 | -0.05 | -0.07 | -0.05 | -0.05 |
| work_id | 0.11 | 0.93 | 0.90 | 1.00 | -0.11 | -0.04 | 0.11 | -0.02 | -0.06 | -0.05 | 0.10 | -0.03 | -0.05 | -0.07 | -0.05 | -0.05 |
| books_count | -0.26 | -0.16 | -0.16 | -0.11 | 1.00 | 0.02 | -0.32 | -0.07 | 0.32 | 0.33 | 0.20 | 0.23 | 0.33 | 0.38 | 0.35 | 0.28 |
| isbn13 | -0.01 | -0.05 | -0.05 | -0.04 | 0.02 | 1.00 | -0.00 | -0.03 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| original_publication_year | 0.05 | 0.13 | 0.13 | 0.11 | -0.32 | -0.00 | 1.00 | 0.02 | -0.02 | -0.03 | 0.03 | -0.02 | -0.04 | -0.04 | -0.03 | -0.02 |
| average_rating | -0.04 | -0.02 | -0.02 | -0.02 | -0.07 | -0.03 | 0.02 | 1.00 | 0.04 | 0.05 | 0.01 | -0.08 | -0.12 | -0.07 | 0.04 | 0.12 |
| ratings_count | -0.37 | -0.07 | -0.07 | -0.06 | 0.32 | 0.01 | -0.02 | 0.04 | 1.00 | 1.00 | 0.78 | 0.72 | 0.85 | 0.94 | 0.98 | 0.96 |
| work_ratings_count | -0.38 | -0.06 | -0.06 | -0.05 | 0.33 | 0.01 | -0.03 | 0.05 | 1.00 | 1.00 | 0.81 | 0.72 | 0.85 | 0.94 | 0.99 | 0.97 |
| work_text_reviews_count | -0.42 | 0.12 | 0.13 | 0.10 | 0.20 | 0.01 | 0.03 | 0.01 | 0.78 | 0.81 | 1.00 | 0.57 | 0.70 | 0.76 | 0.82 | 0.76 |
| ratings_1 | -0.24 | -0.04 | -0.03 | -0.03 | 0.23 | 0.01 | -0.02 | -0.08 | 0.72 | 0.72 | 0.57 | 1.00 | 0.93 | 0.80 | 0.67 | 0.60 |
| ratings_2 | -0.35 | -0.06 | -0.05 | -0.05 | 0.33 | 0.01 | -0.04 | -0.12 | 0.85 | 0.85 | 0.70 | 0.93 | 1.00 | 0.95 | 0.84 | 0.71 |
| ratings_3 | -0.41 | -0.08 | -0.07 | -0.07 | 0.38 | 0.01 | -0.04 | -0.07 | 0.94 | 0.94 | 0.76 | 0.80 | 0.95 | 1.00 | 0.95 | 0.83 |
| ratings_4 | -0.41 | -0.06 | -0.05 | -0.05 | 0.35 | 0.01 | -0.03 | 0.04 | 0.98 | 0.99 | 0.82 | 0.67 | 0.84 | 0.95 | 1.00 | 0.93 |
| ratings_5 | -0.33 | -0.06 | -0.05 | -0.05 | 0.28 | 0.01 | -0.02 | 0.12 | 0.96 | 0.97 | 0.76 | 0.60 | 0.71 | 0.83 | 0.93 | 1.00 |
