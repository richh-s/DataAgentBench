code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-13254562038986312463'], 'r') as f:
    books_data = json.load(f)
with open(locals()['var_function-call-11177499545297105580'], 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

def extract_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

books_df['id_num'] = books_df['book_id'].apply(extract_id)
reviews_df['id_num'] = reviews_df['purchase_id'].apply(extract_id)

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(?:published|released).*?(\d{4})', text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    matches = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if matches:
        return int(matches[0])
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df['decade'] = (books_df['year'] // 10) * 10

merged = pd.merge(reviews_df, books_df, on='id_num', how='inner')
merged['rating'] = pd.to_numeric(merged['rating'])

grouped = merged.groupby('decade').agg(
    distinct_books=('id_num', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

filtered = grouped[grouped['distinct_books'] >= 10]
best_decade = filtered.loc[filtered['avg_rating'].idxmax()]
result = str(int(best_decade['decade'])) + 's'

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7150800685504257560': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-2073144111115022869': ['review'], 'var_function-call-4856845848597656984': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-15506834118636238395': [{'count': '200'}], 'var_function-call-2306275579934153915': [{'COUNT(*)': '1833'}], 'var_function-call-13254562038986312463': 'file_storage/function-call-13254562038986312463.json', 'var_function-call-11177499545297105580': 'file_storage/function-call-11177499545297105580.json', 'var_function-call-4705099490345864553': None, 'var_function-call-340492421812804622': {'books_count': 200, 'books_with_year_count': 189, 'reviews_count': 1833, 'merged_count': 1833, 'grouped': [{'decade': 1880.0, 'distinct_books': 1, 'avg_rating': 4.25, 'count_reviews': 4}, {'decade': 1930.0, 'distinct_books': 2, 'avg_rating': 5.0, 'count_reviews': 3}, {'decade': 1940.0, 'distinct_books': 1, 'avg_rating': 5.0, 'count_reviews': 2}, {'decade': 1970.0, 'distinct_books': 2, 'avg_rating': 4.285714285714286, 'count_reviews': 7}, {'decade': 1980.0, 'distinct_books': 11, 'avg_rating': 4.208333333333333, 'count_reviews': 72}, {'decade': 1990.0, 'distinct_books': 16, 'avg_rating': 3.8208955223880596, 'count_reviews': 67}, {'decade': 2000.0, 'distinct_books': 47, 'avg_rating': 4.276223776223776, 'count_reviews': 286}, {'decade': 2010.0, 'distinct_books': 88, 'avg_rating': 4.608591885441528, 'count_reviews': 1257}, {'decade': 2020.0, 'distinct_books': 21, 'avg_rating': 4.663636363636364, 'count_reviews': 110}]}}

exec(code, env_args)
