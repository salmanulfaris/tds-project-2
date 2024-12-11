# 🤖Automated Analysis Report

#### 📦 Column(s) Available 

`book_id`,`goodreads_book_id`,`best_book_id`,`work_id`,`books_count`,`isbn`,`isbn13`,`authors`,`original_publication_year`,`original_title`,`title`,`language_code`,`average_rating`,`ratings_count`,`work_ratings_count`,`work_text_reviews_count`,`ratings_1`,`ratings_2`,`ratings_3`,`ratings_4`,`ratings_5`,`image_url`,`small_image_url` 

#### 🪫Column with missing Values 

|                           |    0 |
|:--------------------------|-----:|
| isbn                      |  700 |
| isbn13                    |  585 |
| original_publication_year |   21 |
| original_title            |  585 |
| language_code             | 1084 |

## 💡Story
### 📚 Story of the Book Dataset 📚

Once upon a time in the vast realm of literature, there existed a treasure trove of data encompassing a myriad of books. This dataset contained information about **10,000 books**, each a unique gateway into a world of knowledge, adventure, and imagination. The dataset was meticulously organized, featuring various attributes for each book. Let’s delve into the magic that the data reveals! ✨

---

#### 🔍 Key Attributes of Our Treasures:

- **Identifiers**:
  - ✅ **book_id**: Unique ID for each book (1-10,000)
  - ✅ **goodreads_book_id**: ID for Goodreads' records
  - ✅ **work_id**: Work-specific ID that links multiple editions
  
- **Book Details**:
  - 📖 **title**: The name of the book
  - 🖊️ **authors**: Who penned the masterpiece? (e.g., J.K. Rowling, Stephen King)
  - 📅 **original_publication_year**: The year the book was first published
  - 🌐 **language_code**: The language in which the book is written (e.g., English, Spanish)

- **Popularity Metrics**:
  - ⭐ **average_rating**: The average score given by readers (from 1 to 5 stars)
  - 📊 **ratings_count**: The total number of ratings
  - 💬 **work_text_reviews_count**: How many written reviews have been cast?

---

### 📊 Summary Insights

1. **Most Loved Books**:
   - The dataset reveals a range of average ratings. For instance, "Harry Potter and the Philosopher's Stone" has an average rating of **4.44**, showcasing its popularity! 🌟

2. **Authors with the Most Works**:
   - Notably, **Stephen King** tops the list with **60** unique titles, enchanting readers with his captivating storytelling. 

3. **Publication Era**:
   - Books span across time, with the earliest published as far back as **1811** and the most modern ones released as recently as **2017**. 📅

4. **Diverse Languages**:
   - This dataset boasts works from various languages, with **English (eng)** being the predominant one, along with others like **Spanish (spa)** and **French (fre)**. 🌍

---

### 📉 Analysis of Missing Values

The guardians of this dataset noticed that some entries were missing vital pieces of information. Here's the list of missing values, akin to pages torn from a book:

| Attribute                      | Missing Values |
|--------------------------------|----------------|
| isbn                           | 700            |
| isbn13                         | 585            |
| original_publication_year      | 21             |
| original_title                 | 585            |
| language_code                  | 1084           |

**Missing values** suggest opportunities for data cleanup and enhancement, potentially via references or additional queries to bibliographic databases. 📖

---

### 🧩 Data Types Overview

In the kingdom of data, each piece of information belongs to a certain type:

| Column                             | Data Type   |
|------------------------------------|-------------|
| book_id                            | Integer     |
| goodreads_book_id                  | Integer     |
| best_book_id                       | Integer     |
| work_id                            | Integer     |
| books_count                        | Integer     |
| isbn                               | Object      |
| isbn13                             | Float       |
| authors                            | Object      |
| original_publication_year          | Float       |
| original_title                     | Object      |
| title                              | Object      |
| language_code                      | Object      |
| average_rating                     | Float       |
| ratings_count                      | Integer     |
| work_ratings_count                 | Integer     |
| work_text_reviews_count            | Integer     |
| ratings_1                          | Integer     |
| ratings_2                          | Integer     |
| ratings_3                          | Integer     |
| ratings_4                          | Integer     |
| ratings_5                          | Integer     |
| image_url                          | Object      |
| small_image_url                    | Object      |

---

### 💡 Insights and Future Directions

- **Correlation Exploration**: Analyzing the correlation matrix presents intriguing patterns. For example, **ratings_count** and **work_ratings_count** are highly correlated (0.995068) 😮, indicating that higher total ratings often result in more reader ratings. 

- **Possible Recommendations**: By identifying the books with the most missing values (like isbn information), you could perform targeted data collection enhancement.

- **Future Visualizations**: Creating visual representations of author contributions, publication trends over time, and the impact of ratings on book popularity could provide a captivating narrative for potential readers and scholars alike! 📈

---

And thus, the tale of the book dataset concludes

### 🌉Visual Analysis 2.0 
![ratings_count_distribution.png](ai-charts/ratings_count_distribution.png)
![average_rating_vs_ratings_count.png](ai-charts/average_rating_vs_ratings_count.png)
![top_authors.png](ai-charts/top_authors.png)
![correlation_heatmap.png](ai-charts/correlation_heatmap.png)
![average_rating_distribution.png](ai-charts/average_rating_distribution.png)


### 🌉Visualizations of Distribution 
![ratings_count_distribution.png](static/ratings_count_distribution.png)
![book_id_distribution.png](static/book_id_distribution.png)
![work_id_distribution.png](static/work_id_distribution.png)
![goodreads_book_id_distribution.png](static/goodreads_book_id_distribution.png)
![original_publication_year_distribution.png](static/original_publication_year_distribution.png)
![ratings_4_distribution.png](static/ratings_4_distribution.png)
![ratings_1_distribution.png](static/ratings_1_distribution.png)
![ratings_5_distribution.png](static/ratings_5_distribution.png)
![best_book_id_distribution.png](static/best_book_id_distribution.png)
![ratings_2_distribution.png](static/ratings_2_distribution.png)
![books_count_distribution.png](static/books_count_distribution.png)
![work_text_reviews_count_distribution.png](static/work_text_reviews_count_distribution.png)
![work_ratings_count_distribution.png](static/work_ratings_count_distribution.png)
![isbn13_distribution.png](static/isbn13_distribution.png)
![average_rating_distribution.png](static/average_rating_distribution.png)
![ratings_3_distribution.png](static/ratings_3_distribution.png)
