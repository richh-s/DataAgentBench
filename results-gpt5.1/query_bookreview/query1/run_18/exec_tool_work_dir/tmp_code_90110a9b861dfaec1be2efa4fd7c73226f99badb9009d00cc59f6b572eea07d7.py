code = """import pandas as pd, json, re
from pathlib import Path

# Load large review data
path = Path(var_call_GTDSsDqjRi8VstsV1jOSVNuG)
reviews = pd.read_json(path)
reviews['rating'] = reviews['rating'].astype(float)

# Load books details data
path_books = Path(var_call_mQbz6VGSb7mZKrtbB9j7ZeUD)
books = pd.read_json(path_books)

# Extract publication year from details text
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # look for patterns like 'on January 1, 2004' or plain years
    m = re.search(r'on [A-Za-z]+ \d{1,2}, ((19|20)\d{2})', text)
    if m:
        return int(m.group(1))
    m2 = year_pattern.search(text)
    if m2:
        return int(m2.group(0))
    return None

books['year'] = books['details'].apply(extract_year)
books = books.dropna(subset=['year'])
books['year'] = books['year'].astype(int)
books['decade'] = (books['year'] // 10) * 10

# Fuzzy join: purchaseid_Xxx to bookid_Xxx via numeric/id part

def base_id(x):
    if not isinstance(x, str):
        return None
    m = re.search(r'(\d+)$', x)
    return m.group(1) if m else None

reviews['base'] = reviews['purchase_id'].apply(base_id)
books['base'] = books['book_id'].apply(base_id)

merged = pd.merge(reviews, books[['book_id','base','decade']], on='base', how='inner')

# Compute per-book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, compute average of book average ratings, only decades with at least 10 distinct books
dec_stats = book_avg.groupby('decade').agg(
    n_books=('book_id','nunique'),
    decade_avg_rating=('book_avg_rating','mean')
).reset_index()

eligible = dec_stats[dec_stats['n_books'] >= 10]

if eligible.empty:
    result = None
else:
    best = eligible.sort_values('decade_avg_rating', ascending=False).iloc[0]
    result = {
        'decade': int(best['decade']),
        'decade_label': f"{int(best['decade'])}s",
        'average_rating': round(float(best['decade_avg_rating']), 3),
        'n_distinct_books': int(best['n_books'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mQbz6VGSb7mZKrtbB9j7ZeUD': 'file_storage/call_mQbz6VGSb7mZKrtbB9j7ZeUD.json', 'var_call_7CC4LLtL8nBg0cJgIKy6Ah3Z': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_CmBrRpP7dngvEJAWoTXJdCJB': ['review'], 'var_call_GTDSsDqjRi8VstsV1jOSVNuG': 'file_storage/call_GTDSsDqjRi8VstsV1jOSVNuG.json'}

exec(code, env_args)
