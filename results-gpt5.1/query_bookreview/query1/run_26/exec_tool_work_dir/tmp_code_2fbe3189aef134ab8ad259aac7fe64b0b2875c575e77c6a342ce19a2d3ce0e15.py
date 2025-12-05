code = """import json, re, pandas as pd

# Load full datasets from files
with open(var_call_sLYGdfoOXyyw1eQKfwseBqIY, 'r') as f:
    reviews = json.load(f)
with open(var_call_8oNTUK3841JuvfrBWBTw9DAn, 'r') as f:
    books = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Extract publication year from 'details' using regex like 'on <Month> <day>, <year>' or 'on <year>' or 'on January 1, 2004' etc.
# We'll search for a 4-digit year between 1500 and 2100 and take the first occurrence in details.

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = re.search(r'(1[5-9]\d{2}|20\d{2}|2100)', details)
    if m:
        return int(m.group(0))
    return None

df_books['year'] = df_books['details'].apply(extract_year)

# Derive decade label like '1980s'
def year_to_decade(y):
    if pd.isna(y):
        return None
    decade_start = int(y) // 10 * 10
    return f"{decade_start}s"

df_books['decade'] = df_books['year'].apply(year_to_decade)

# Join reviews with books on purchase_id == book_id
merged = pd.merge(df_reviews, df_books[['book_id', 'decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Coerce rating to float
merged['rating'] = merged['rating'].astype(float)

# Group by decade, but only consider decades with at least 10 distinct books that have been rated
agg = merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('book_id', pd.Series.nunique)
).reset_index()

eligible = agg[agg['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    top_row = eligible.sort_values('avg_rating', ascending=False).iloc[0]
    result = {
        'decade': top_row['decade'],
        'average_rating': round(float(top_row['avg_rating']), 4),
        'distinct_books': int(top_row['distinct_books'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mn7mC4MQBsgQNP0suUjB3TZ1': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_45H8ET25Q0URFaeuT9lx2Hoe': ['review'], 'var_call_YFjUJsLkgLWGVnxqleNCo37z': [{'rating': '4', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'purchase_id': 'purchaseid_178'}], 'var_call_qPZlBelOCCJBeP9hz9nbd83C': 'file_storage/call_qPZlBelOCCJBeP9hz9nbd83C.json', 'var_call_sLYGdfoOXyyw1eQKfwseBqIY': 'file_storage/call_sLYGdfoOXyyw1eQKfwseBqIY.json', 'var_call_8oNTUK3841JuvfrBWBTw9DAn': 'file_storage/call_8oNTUK3841JuvfrBWBTw9DAn.json'}

exec(code, env_args)
