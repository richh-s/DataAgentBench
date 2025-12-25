code = """import json, re, pandas as pd

# Load full datasets from files
with open(var_call_xKNqrQPCS6Eo4bJm7UXZnAB2, 'r') as f:
    reviews = json.load(f)
with open(var_call_mj3yYMkq9CU5LFHs91Vusqo4, 'r') as f:
    books = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Ensure rating is float
df_reviews['rating'] = df_reviews['rating'].astype(float)

# Extract publication year from details using regex patterns
patterns = [
    r"released on [A-Za-z]+ \d{1,2}, (\d{4})",
    r"on [A-Za-z]+ \d{1,2}, (\d{4})",
    r"on January 1, (\d{4})",
    r"on (\w+ \d{1,2}, \d{4})",  # fallback full date
    r"on (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})",
    r"on (\d{4})",  # year alone
    r"edition on (\w+ \d{1,2}, \d{4})",
    r"on (January 1, \d{4})",
    r"released on (\w+ \d{1,2}, \d{4})",
    r"in (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})",
    r"on (January 1,\s*\d{4})",
]

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Common direct year patterns first
    m = re.search(r"(19\d{2}|20\d{2})", text)
    if m:
        return int(m.group(1))
    return None

# Apply year extraction
df_books['pub_year'] = df_books['details'].apply(extract_year)

# Drop books without a year
df_books = df_books.dropna(subset=['pub_year'])

# Compute decade label, e.g., 1980s
df_books['decade'] = (df_books['pub_year'].astype(int) // 10 * 10).astype(int).astype(str) + 's'

# Fuzzy join between reviews.purchase_id and books.book_id: assume same IDs like purchaseid_123 -> bookid_123
# Map by matching numeric suffix

def to_numeric_suffix(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)$", s)
    return int(m.group(1)) if m else None

df_reviews['id_num'] = df_reviews['purchase_id'].apply(to_numeric_suffix)
df_books['id_num'] = df_books['book_id'].apply(to_numeric_suffix)

# Inner join on id_num
merged = pd.merge(df_reviews, df_books[['book_id', 'decade', 'id_num']], on='id_num', how='inner')

# We need at least 10 distinct books per decade that have been rated
# Calculate per book average rating first
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Count distinct books per decade
decade_stats = book_avg.groupby('decade').agg(
    num_books=('book_id', 'nunique'),
    avg_rating=('book_avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    # Get decade with highest average rating; in tie, choose earliest decade
    max_avg = eligible['avg_rating'].max()
    top = eligible[eligible['avg_rating'] == max_avg].sort_values('decade').iloc[0]
    result = top['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mbrwiPbD3eFuRX6GytKupR8P': 'file_storage/call_mbrwiPbD3eFuRX6GytKupR8P.json', 'var_call_EOhjQbYPB95th8tePTZ0U6aa': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_E1jUEHlnR8cjkCae45s37Gzf': ['review'], 'var_call_LjFpRKxVE6yBvdb4Jj8KMFyB': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_call_xKNqrQPCS6Eo4bJm7UXZnAB2': 'file_storage/call_xKNqrQPCS6Eo4bJm7UXZnAB2.json', 'var_call_mj3yYMkq9CU5LFHs91Vusqo4': 'file_storage/call_mj3yYMkq9CU5LFHs91Vusqo4.json', 'var_call_McDJsBDBPjPsn7xQt6LqVHCH': 'file_storage/call_McDJsBDBPjPsn7xQt6LqVHCH.json', 'var_call_DbYBdzxfZdVS8b4EyU15WtGg': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}]}

exec(code, env_args)
