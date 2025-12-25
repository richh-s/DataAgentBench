code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-16015471312777995800'], 'r') as f:
    reviews_data = json.load(f)

with open(locals()['var_function-call-1834763118537945514'], 'r') as f:
    books_data = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_books = pd.DataFrame(books_data)

# Convert columns to numeric
df_reviews['total_rating'] = pd.to_numeric(df_reviews['total_rating'])
df_reviews['num_reviews'] = pd.to_numeric(df_reviews['num_reviews'])

# Extract ID
# review: purchaseid_X -> X
# book: bookid_X -> X
df_reviews['id'] = df_reviews['purchase_id'].apply(lambda x: int(x.split('_')[1]))
df_books['id'] = df_books['book_id'].apply(lambda x: int(x.split('_')[1]))

# Merge
merged = pd.merge(df_books, df_reviews, on='id', how='inner')

# Extract Year
# Pattern: Month (Day, ) Year
# Examples: "January 1, 2004", "May 20, 1996", "January 2004"
date_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},)?\s*(\d{4})'
merged['extracted_year'] = merged['details'].str.extract(date_pattern, expand=False)

# Convert to numeric
merged['year'] = pd.to_numeric(merged['extracted_year'])

# Drop rows where year is null
merged = merged.dropna(subset=['year'])

# Calculate Decade
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(int).astype(str) + 's'

# Aggregation
# We need distinct books count. Since 'id' is unique in books, count of rows is distinct books.
decade_stats = merged.groupby('decade_str').agg(
    distinct_books=('id', 'count'),
    sum_rating=('total_rating', 'sum'),
    sum_reviews=('num_reviews', 'sum')
).reset_index()

# Filter >= 10 books
filtered_decades = decade_stats[decade_stats['distinct_books'] >= 10].copy()

# Calculate Average Rating
# Average of reviews = Sum of all ratings / Sum of all reviews
filtered_decades['avg_rating'] = filtered_decades['sum_rating'] / filtered_decades['sum_reviews']

# Find max
if not filtered_decades.empty:
    best_decade = filtered_decades.loc[filtered_decades['avg_rating'].idxmax()]
    result = {
        "decade": best_decade['decade_str'],
        "average_rating": best_decade['avg_rating'],
        "book_count": best_decade['distinct_books']
    }
else:
    result = "No decade met the criteria"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-401990921581386706': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5217107774192796842': ['review'], 'var_function-call-8116449033455958544': ['books_info'], 'var_function-call-16015471312777995800': 'file_storage/function-call-16015471312777995800.json', 'var_function-call-1834763118537945514': 'file_storage/function-call-1834763118537945514.json'}

exec(code, env_args)
