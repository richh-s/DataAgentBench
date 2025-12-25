code = """import json
import re
import pandas as pd

# Load data again (simulated by reading variables, actually I need to read files again or if they are in memory... the tool environment clears locals so I must reload)
with open(locals()['var_function-call-4812979085553352235'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-10585015522802858518'], 'r') as f:
    reviews_data = json.load(f)

def extract_id(s):
    # Extract digits from the end or just digits
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

def extract_year(details):
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})', details)
    if match:
        return int(match.group(1))
    match = re.search(r'\b(19\d{2}|20\d{2})\b', details)
    if match:
        return int(match.group(1))
    return None

books = []
for b in books_data:
    y = extract_year(b['details'])
    bid = extract_id(b['book_id'])
    if y and bid is not None:
        books.append({'id': bid, 'year': y})

df_books = pd.DataFrame(books)

reviews = []
for r in reviews_data:
    pid = extract_id(r['purchase_id'])
    if pid is not None:
        reviews.append({'id': pid, 'rating': float(r['rating'])})

df_reviews = pd.DataFrame(reviews)

# Merge on id
merged = pd.merge(df_reviews, df_books, on='id')

# Decade
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(str) + 's'

# Filter
decade_counts = merged.groupby('decade_str')['id'].nunique()
valid_decades = decade_counts[decade_counts >= 10].index.tolist()

# Avg rating
avg_ratings = merged[merged['decade_str'].isin(valid_decades)].groupby('decade_str')['rating'].mean()

if not avg_ratings.empty:
    best_decade = avg_ratings.idxmax()
    best_val = avg_ratings.max()
else:
    best_decade = "None"
    best_val = 0

print("__RESULT__:")
print(json.dumps({
    "best_decade": best_decade,
    "average_rating": best_val,
    "stats": avg_ratings.to_dict(),
    "counts": decade_counts.to_dict()
}))"""

env_args = {'var_function-call-16705125164776531882': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4806420106219150557': [{'count': '200'}], 'var_function-call-3685845373781983756': ['review'], 'var_function-call-9177159680172499476': [{'count(*)': '1833'}], 'var_function-call-4812979085553352235': 'file_storage/function-call-4812979085553352235.json', 'var_function-call-10585015522802858518': 'file_storage/function-call-10585015522802858518.json', 'var_function-call-12310340119155167955': {'best_decade': 'None', 'average_rating': 0, 'stats': {}, 'counts': {}}}

exec(code, env_args)
