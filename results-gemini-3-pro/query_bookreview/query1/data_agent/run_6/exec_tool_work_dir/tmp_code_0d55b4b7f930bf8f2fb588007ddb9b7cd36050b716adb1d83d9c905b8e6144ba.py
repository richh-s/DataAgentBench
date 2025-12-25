code = """import json
import re
import pandas as pd

# Load books data
with open(locals()['var_function-call-8731629691589576080'], 'r') as f:
    books_data = json.load(f)

# Load reviews data
with open(locals()['var_function-call-13722311535690932608'], 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)

def extract_year(details):
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if match:
        return int(match.group(1))
    match = re.search(r'published.*?(\d{4})', details, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books = df_books.dropna(subset=['year'])
df_books['decade'] = (df_books['year'] // 10) * 10
df_books['decade_str'] = df_books['decade'].astype(int).astype(str) + 's'
df_books['join_id'] = df_books['book_id'].apply(lambda x: int(x.replace('bookid_', '')))

df_reviews = pd.DataFrame(reviews_data)
df_reviews['join_id'] = df_reviews['purchase_id'].apply(lambda x: int(x.replace('purchaseid_', '')))
df_reviews['rating'] = df_reviews['rating'].astype(float)

merged = pd.merge(df_reviews, df_books, on='join_id', how='inner')

stats = merged.groupby('decade_str').agg(
    distinct_books=('book_id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

print("__RESULT__:")
print(stats.to_json(orient='records'))"""

env_args = {'var_function-call-15535935410887639536': ['books_info'], 'var_function-call-7470265999276532788': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-18392697609569529530': [{'count': '200'}], 'var_function-call-16647221747224859322': ['review'], 'var_function-call-8147390253975181392': [{'count(*)': '1833'}], 'var_function-call-17655738389528201345': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-8731629691589576080': 'file_storage/function-call-8731629691589576080.json', 'var_function-call-13722311535690932608': 'file_storage/function-call-13722311535690932608.json', 'var_function-call-10627394388862208959': '2020s'}

exec(code, env_args)
