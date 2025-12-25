code = """import json
import pandas as pd
import re

# Load review data (avg rating per book)
# Key: var_function-call-8003413839602542900 (file)
with open('var_function-call-8003413839602542900.json', 'r') as f:
    reviews = json.load(f)

# Load books data (details)
# Key: var_function-call-12230880538750893406 (file)
with open('var_function-call-12230880538750893406.json', 'r') as f:
    books = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'])

df_books = pd.DataFrame(books)

# Function to extract year
def extract_year(details):
    if not isinstance(details, str):
        return None
    # Pattern 1: published/released on Month Day, Year
    match = re.search(r'(?:published|released).*?on\s+[A-Z][a-z]+\s+\d{1,2},?\s+(\d{4})', details, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Pattern 2: published in Year (less reliable, but useful)
    match = re.search(r'(?:published|released).*?in\s+(?:[a-zA-Z\s]+)?(\d{4})', details, re.IGNORECASE)
    if match:
        # Check if it's not a future year or too old
        y = int(match.group(1))
        if 1800 < y <= 2025:
            return y
            
    return None

df_books['year'] = df_books['details'].apply(extract_year)

# Merge
# review: purchase_id, books: book_id
merged = pd.merge(df_books, df_reviews, left_on='book_id', right_on='purchase_id', how='inner')

# Drop books without year
merged = merged.dropna(subset=['year'])

# Define decade
def get_decade(year):
    return f"{int(year // 10) * 10}s"

merged['decade'] = merged['year'].apply(get_decade)

# Aggregation
# We need decades with at least 10 distinct books
decade_stats = merged.groupby('decade').agg(
    book_count=('book_id', 'nunique'),
    average_rating=('avg_rating', 'mean')
).reset_index()

# Filter
filtered_decades = decade_stats[decade_stats['book_count'] >= 10]

# Find max
if not filtered_decades.empty:
    best_decade = filtered_decades.loc[filtered_decades['average_rating'].idxmax()]
    result = best_decade.to_dict()
else:
    result = "No decade meets criteria"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9636641086377978641': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4069087491551052511': ['review'], 'var_function-call-8003413839602542900': 'file_storage/function-call-8003413839602542900.json', 'var_function-call-12230880538750893406': 'file_storage/function-call-12230880538750893406.json'}

exec(code, env_args)
