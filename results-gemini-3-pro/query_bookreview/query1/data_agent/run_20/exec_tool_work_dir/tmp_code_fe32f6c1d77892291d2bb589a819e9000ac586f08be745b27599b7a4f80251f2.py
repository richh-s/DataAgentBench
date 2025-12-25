code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-7266083921109746468'], 'r') as f:
    books = json.load(f)

with open(locals()['var_function-call-10072965068991537289'], 'r') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Clean IDs
# book_id is like "bookid_X"
# purchase_id is like "purchaseid_X"
# Normalize purchase_id to book_id format
df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_')

# Convert rating to float
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Join
# We need to assign each review to a decade based on the book's publication year.
# First, extract year from details in df_books.

def extract_year(details):
    if not isinstance(details, str):
        return None
    # Common patterns:
    # "released on January 1, 2004"
    # "published ... on May 20, 1996"
    # "published on ... 2021"
    # Look for a 4-digit year following a month
    match = re.search(r'(?:released|published).*?([A-Z][a-z]+ \d{1,2},? \d{4})', details)
    if match:
        date_str = match.group(1)
        # Extract year from the end
        year_match = re.search(r'\d{4}', date_str)
        if year_match:
            return int(year_match.group(0))
    
    # Fallback: look for "YYYYth edition" or just any "published ... YYYY"
    # Regex for "published ... YYYY" not followed by "-" (to avoid ISBNs mostly, though ISBNs usually don't follow 'published')
    match = re.search(r'published.*?(\d{4})', details, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Last resort: just find the first valid year (1900-2024) in the string?
    # This is risky because of ISBNs. ISBNs often start with 978... or other digits.
    # But ISBNs are usually labeled.
    # Let's try to be specific.
    return None

df_books['year'] = df_books['details'].apply(extract_year)

# Filter out books with no year
books_with_year = df_books.dropna(subset=['year']).copy()
books_with_year['decade'] = (books_with_year['year'] // 10 * 10).astype(int).astype(str) + 's'

# Merge reviews with books (inner join to keep only rated books)
merged = pd.merge(df_reviews, books_with_year[['book_id', 'decade']], on='book_id', how='inner')

# Calculate metrics per decade
decade_stats = merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    unique_books=('book_id', 'nunique')
).reset_index()

# Filter decades with at least 10 distinct books
filtered_decades = decade_stats[decade_stats['unique_books'] >= 10]

# Find the one with highest average rating
if not filtered_decades.empty:
    best_decade = filtered_decades.loc[filtered_decades['avg_rating'].idxmax()]
    result = best_decade['decade']
else:
    result = "No decade meets criteria"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3600458308634325854': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5045419460847510275': [{'count': '200'}], 'var_function-call-6749438513669462977': ['review'], 'var_function-call-14243022033857224439': [{'count(*)': '1833'}], 'var_function-call-7266083921109746468': 'file_storage/function-call-7266083921109746468.json', 'var_function-call-10072965068991537289': 'file_storage/function-call-10072965068991537289.json'}

exec(code, env_args)
