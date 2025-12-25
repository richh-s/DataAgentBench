code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10984118404756888588'], 'r') as f:
    books_data = json.load(f)
with open(locals()['var_function-call-10984118404756889591'], 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Extract Year
def extract_year(text):
    if not text:
        return None
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})', text)
    if match:
        return int(match.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books = df_books.dropna(subset=['year'])
df_books['year'] = df_books['year'].astype(int)
df_books['decade'] = (df_books['year'] // 10 * 10).astype(str) + 's'

# Create join keys
df_books['join_id'] = df_books['book_id'].apply(lambda x: re.findall(r'\d+', x)[0] if re.findall(r'\d+', x) else None)
df_reviews['join_id'] = df_reviews['purchase_id'].apply(lambda x: re.findall(r'\d+', x)[0] if re.findall(r'\d+', x) else None)

# Convert rating
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Merge
df_merged = pd.merge(df_reviews, df_books, on='join_id', how='inner')

# Method 1: Avg of all ratings
stats_m1 = df_merged.groupby('decade').agg(
    book_count=('join_id', 'nunique'),
    avg_rating_all=('rating', 'mean')
).reset_index()

# Method 2: Avg of book avgs
book_avgs = df_merged.groupby(['decade', 'join_id'])['rating'].mean().reset_index()
stats_m2 = book_avgs.groupby('decade').agg(
    avg_rating_books=('rating', 'mean')
).reset_index()

final = pd.merge(stats_m1, stats_m2, on='decade')
filtered = final[final['book_count'] >= 10].sort_values(by='avg_rating_all', ascending=False)

print("__RESULT__:")
print(filtered.to_json(orient='records'))"""

env_args = {'var_function-call-6791498673346843016': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-541313699914009693': [{'count': '200'}], 'var_function-call-2560629624198690838': ['review'], 'var_function-call-6360400991362587864': [{'COUNT(*)': '1833'}], 'var_function-call-10984118404756888588': 'file_storage/function-call-10984118404756888588.json', 'var_function-call-10984118404756889591': 'file_storage/function-call-10984118404756889591.json', 'var_function-call-8089198618867541088': [{'decade': '2020.0s', 'book_count': 21, 'avg_rating': 4.6636363636}, {'decade': '2010.0s', 'book_count': 88, 'avg_rating': 4.6085918854}, {'decade': '2000.0s', 'book_count': 46, 'avg_rating': 4.2736842105}, {'decade': '1980.0s', 'book_count': 11, 'avg_rating': 4.2083333333}, {'decade': '1990.0s', 'book_count': 17, 'avg_rating': 3.8382352941}]}

exec(code, env_args)
