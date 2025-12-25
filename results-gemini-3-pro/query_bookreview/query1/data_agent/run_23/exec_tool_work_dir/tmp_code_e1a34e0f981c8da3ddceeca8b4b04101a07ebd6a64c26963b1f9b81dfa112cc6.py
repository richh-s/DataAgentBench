code = """import json
import pandas as pd
import re

# Load data using locals() for variable names with hyphens
books_file = locals()['var_function-call-17470195624660244328']
reviews_file = locals()['var_function-call-6253168881237040463']

with open(books_file, 'r') as f:
    books = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Extract integer ID from book_id and purchase_id
def extract_id(s):
    if pd.isna(s): return None
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

df_books['id_num'] = df_books['book_id'].apply(extract_id)
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

# Merge
df = pd.merge(df_reviews, df_books, on='id_num', how='inner')

# Extract year from details
def extract_year(details):
    if not isinstance(details, str): return None
    # Find all 4-digit numbers looking like years
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    if years:
        return int(years[0])
    return None

df['year'] = df['details'].apply(extract_year)

# Drop rows where year is missing
df = df.dropna(subset=['year'])

# Calculate decade
df['decade'] = (df['year'] // 10) * 10
df['decade_str'] = df['decade'].astype(int).astype(str) + 's'

# Convert rating to float
df['rating'] = df['rating'].astype(float)

# Group by decade
stats = df.groupby('decade_str').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('id_num', 'nunique')
).reset_index()

# Filter
filtered_stats = stats[stats['distinct_books'] >= 10]

# Find max
if not filtered_stats.empty:
    best_decade = filtered_stats.loc[filtered_stats['avg_rating'].idxmax()]
    result = best_decade.to_dict()
else:
    result = "No decade meets criteria"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9545217224331018128': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-9699813864465939762': ['review'], 'var_function-call-17314963110901189043': [{'COUNT(*)': '1833'}], 'var_function-call-8911477973423827957': [{'count': '200'}], 'var_function-call-17470195624660244328': 'file_storage/function-call-17470195624660244328.json', 'var_function-call-6253168881237040463': 'file_storage/function-call-6253168881237040463.json'}

exec(code, env_args)
