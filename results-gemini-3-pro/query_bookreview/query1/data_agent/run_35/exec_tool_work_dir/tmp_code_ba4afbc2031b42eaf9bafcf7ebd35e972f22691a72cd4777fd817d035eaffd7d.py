code = """import json
import re
import pandas as pd

books_path = locals()['var_function-call-6325774532205901436']
reviews_path = locals()['var_function-call-9221213419928042691']

with open(books_path, 'r') as f: books_data = json.load(f)
with open(reviews_path, 'r') as f: reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

def extract_id(s):
    if not isinstance(s, str): return None
    m = re.search(r'(\d+)$', s)
    return int(m.group(1)) if m else None

books_df['id_num'] = books_df['book_id'].apply(extract_id)
reviews_df['id_num'] = reviews_df['purchase_id'].apply(extract_id)

month_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
date_pattern = re.compile(month_pattern + r'[\s,]+(?:(?:\d{1,2})[\s,]+)?(\d{4})', re.IGNORECASE)

def extract_year(details):
    if not isinstance(details, str): return None
    match = date_pattern.search(details)
    return int(match.group(1)) if match else None

books_df['year'] = books_df['details'].apply(extract_year)
books_with_year = books_df.dropna(subset=['year']).copy()
books_with_year['year'] = books_with_year['year'].astype(int)
books_with_year['decade'] = (books_with_year['year'] // 10) * 10
books_with_year['decade_str'] = books_with_year['decade'].astype(str) + "s"

merged_df = pd.merge(reviews_df, books_with_year[['id_num', 'book_id', 'decade_str']], on='id_num', how='inner')
merged_df['rating'] = pd.to_numeric(merged_df['rating'], errors='coerce')
merged_df = merged_df.dropna(subset=['rating'])

decade_stats = merged_df.groupby('decade_str').agg(
    distinct_books=('book_id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index().sort_values('avg_rating', ascending=False)

print("__RESULT__:")
print(json.dumps(decade_stats.to_dict(orient='records')))"""

env_args = {'var_function-call-13006791733557201821': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-15627107773603411334': ['review'], 'var_function-call-8627314569768500697': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-6325774532205901436': 'file_storage/function-call-6325774532205901436.json', 'var_function-call-9221213419928042691': 'file_storage/function-call-9221213419928042691.json', 'var_function-call-128572507644170288': {'decade': '2020s', 'avg_rating': 4.663636363636364, 'distinct_books': 21}}

exec(code, env_args)
