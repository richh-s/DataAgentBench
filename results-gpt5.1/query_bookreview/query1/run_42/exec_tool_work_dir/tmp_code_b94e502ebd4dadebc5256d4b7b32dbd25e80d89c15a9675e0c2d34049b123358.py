code = """import json, re, pandas as pd

# Load full results from file paths
with open(var_call_mao3OilWd6kh4DobTAtxCWf8, 'r') as f:
    review_avgs = json.load(f)
with open(var_call_NdYAkwuwS3RnbjqNJYT7XNg1, 'r') as f:
    books_details = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(review_avgs)
df_books = pd.DataFrame(books_details)

# Ensure numeric
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'])

# Extract publication year from details using regex; many formats like 'on January 1, 2004', 'on May 20, 1996', 'on March 20, 1995', 'on January 1, 1945', or 'on May 18, 2014', etc.
# We'll search for a 4-digit year between 1800 and 2099 and assume it's the publication year when associated with 'on' or a date context.

year_pattern = re.compile(r'(?:on\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)?\s*\d{0,2},?\s*(19\d{2}|20\d{2})')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # prioritize patterns like 'on <Month> <day>, <year>' or 'on <Month> <year>' etc.
    m = year_pattern.search(text)
    if m:
        return int(m.group(1))
    # fallback: any 4-digit year 18xx-20xx
    m2 = re.search(r'(18\d{2}|19\d{2}|20\d{2})', text)
    if m2:
        return int(m2.group(1))
    return None

df_books['pub_year'] = df_books['details'].apply(extract_year)

# Drop rows without pub_year
df_books = df_books.dropna(subset=['pub_year'])

# Compute decade label like '1980s'
df_books['decade'] = (df_books['pub_year'].astype(int) // 10) * 10

# Join reviews with books on purchase_id ~ book_id (exact match of IDs)
merged = pd.merge(df_reviews, df_books, left_on='purchase_id', right_on='book_id', how='inner')

# Now, we want decades with at least 10 distinct books that have been rated
# distinct books per decade
books_per_decade = merged.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = books_per_decade[books_per_decade['n_books'] >= 10]['decade']

filtered = merged[merged['decade'].isin(valid_decades)]

if filtered.empty:
    result = None
else:
    decade_avg = filtered.groupby('decade')['avg_rating'].mean().reset_index()
    # Get decade with highest avg rating; tie-breaker: earliest decade
    max_avg = decade_avg['avg_rating'].max()
    top_decades = decade_avg[decade_avg['avg_rating'] == max_avg]
    best_decade_val = int(top_decades['decade'].min())
    # format as '1980s'
    result = f"{best_decade_val}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NdYAkwuwS3RnbjqNJYT7XNg1': 'file_storage/call_NdYAkwuwS3RnbjqNJYT7XNg1.json', 'var_call_7ZLwpafFPZ2Id4S5uxWJf3CK': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_y3qpxEUHMpZwNgJsXWAXWYzx': ['review'], 'var_call_mao3OilWd6kh4DobTAtxCWf8': 'file_storage/call_mao3OilWd6kh4DobTAtxCWf8.json'}

exec(code, env_args)
