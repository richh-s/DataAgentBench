code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-16015471312777995800'], 'r') as f:
    reviews_data = json.load(f)
with open(locals()['var_function-call-1834763118537945514'], 'r') as f:
    books_data = json.load(f)

df_reviews = pd.DataFrame(reviews_data)
df_books = pd.DataFrame(books_data)

df_reviews['total_rating'] = pd.to_numeric(df_reviews['total_rating'])
df_reviews['num_reviews'] = pd.to_numeric(df_reviews['num_reviews'])
df_reviews['book_avg'] = df_reviews['total_rating'] / df_reviews['num_reviews']

df_reviews['id'] = df_reviews['purchase_id'].apply(lambda x: int(x.split('_')[1]))
df_books['id'] = df_books['book_id'].apply(lambda x: int(x.split('_')[1]))

merged = pd.merge(df_books, df_reviews, on='id', how='inner')
date_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},)?\s*(\d{4})'
merged['extracted_year'] = merged['details'].str.extract(date_pattern, expand=False)
merged['year'] = pd.to_numeric(merged['extracted_year'])
merged = merged.dropna(subset=['year'])
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(int).astype(str) + 's'

# Mean of Means
decade_stats = merged.groupby('decade_str').agg(
    distinct_books=('id', 'count'),
    mean_of_means=('book_avg', 'mean')
).reset_index()

filtered = decade_stats[decade_stats['distinct_books'] >= 10].sort_values('mean_of_means', ascending=False)

print("__RESULT__:")
print(filtered.to_json(orient='records'))"""

env_args = {'var_function-call-401990921581386706': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5217107774192796842': ['review'], 'var_function-call-8116449033455958544': ['books_info'], 'var_function-call-16015471312777995800': 'file_storage/function-call-16015471312777995800.json', 'var_function-call-1834763118537945514': 'file_storage/function-call-1834763118537945514.json', 'var_function-call-7838163647825068507': {'decade': '2020s', 'average_rating': 4.663636363636364, 'book_count': 21}, 'var_function-call-2313742800709161559': [{'decade_str': '2020s', 'distinct_books': 21, 'sum_rating': 513, 'sum_reviews': 110, 'avg_rating': 4.6636363636}, {'decade_str': '2010s', 'distinct_books': 88, 'sum_rating': 5793, 'sum_reviews': 1257, 'avg_rating': 4.6085918854}, {'decade_str': '2000s', 'distinct_books': 47, 'sum_rating': 1223, 'sum_reviews': 286, 'avg_rating': 4.2762237762}, {'decade_str': '1980s', 'distinct_books': 11, 'sum_rating': 303, 'sum_reviews': 72, 'avg_rating': 4.2083333333}, {'decade_str': '1990s', 'distinct_books': 16, 'sum_rating': 256, 'sum_reviews': 67, 'avg_rating': 3.8208955224}]}

exec(code, env_args)
