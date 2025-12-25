code = """import json
import pandas as pd
import re

# Load data (using previous variable names)
# I need to reload because I didn't return the dataframes, just printed the result.
# Actually I can't access local variables from previous execution easily unless I saved them or re-run.
# But I can just copy the loading logic.

with open(locals()['var_function-call-7266083921109746468'], 'r') as f:
    books = json.load(f)

with open(locals()['var_function-call-10072965068991537289'], 'r') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_')
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

def extract_year_safe(details):
    if not isinstance(details, str):
        return None
    matches = re.findall(r'([A-Z][a-z]+ \d{1,2},? (\d{4}))', details)
    for match in matches:
        y = int(match[1])
        if 1900 <= y <= 2024:
            return y
    m = re.search(r'(?:published|released).*?(\b(19|20)\d{2}\b)', details, re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1900 <= y <= 2024:
            return y
    candidates = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    valid_years = [int(y) for y in candidates if 1900 <= int(y) <= 2024]
    if valid_years:
        return valid_years[0]
    return None

df_books['year'] = df_books['details'].apply(extract_year_safe)
books_with_year = df_books.dropna(subset=['year']).copy()
books_with_year['decade'] = (books_with_year['year'] // 10 * 10).astype(int).astype(str) + 's'

merged = pd.merge(df_reviews, books_with_year[['book_id', 'decade']], on='book_id', how='inner')

# Calculate average rating per book first
book_stats = merged.groupby(['decade', 'book_id']).agg(
    book_avg=('rating', 'mean')
).reset_index()

# Calculate average of book averages per decade
decade_stats_2 = book_stats.groupby('decade').agg(
    avg_of_book_avgs=('book_avg', 'mean'),
    unique_books=('book_id', 'count') # count is distinct because we grouped by book_id
).reset_index()

filtered_decades_2 = decade_stats_2[decade_stats_2['unique_books'] >= 10].sort_values('avg_of_book_avgs', ascending=False)

print("__RESULT__:")
print(json.dumps(filtered_decades_2.to_dict(orient='records')))"""

env_args = {'var_function-call-3600458308634325854': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-5045419460847510275': [{'count': '200'}], 'var_function-call-6749438513669462977': ['review'], 'var_function-call-14243022033857224439': [{'count(*)': '1833'}], 'var_function-call-7266083921109746468': 'file_storage/function-call-7266083921109746468.json', 'var_function-call-10072965068991537289': 'file_storage/function-call-10072965068991537289.json', 'var_function-call-2225101699388499718': '2020s', 'var_function-call-2543523654711074760': [{'decade': '2020s', 'avg_rating': 4.663636363636364, 'unique_books': 21, 'review_count': 110}, {'decade': '2010s', 'avg_rating': 4.608591885441528, 'unique_books': 88, 'review_count': 1257}, {'decade': '2000s', 'avg_rating': 4.273684210526316, 'unique_books': 46, 'review_count': 285}, {'decade': '1980s', 'avg_rating': 4.208333333333333, 'unique_books': 11, 'review_count': 72}, {'decade': '1990s', 'avg_rating': 3.838235294117647, 'unique_books': 17, 'review_count': 68}]}

exec(code, env_args)
