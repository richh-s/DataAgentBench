code = """import json
import pandas as pd
import re

# Load data (re-using keys from previous context)
with open(locals()['var_function-call-7567474922900922189'], 'r') as f:
    books_data = json.load(f)
with open(locals()['var_function-call-7567474922900921020'], 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

def extract_id(s):
    m = re.search(r'(\d+)', str(s))
    if m:
        return int(m.group(1))
    return None

books_df['id'] = books_df['book_id'].apply(extract_id)
reviews_df['id'] = reviews_df['purchase_id'].apply(extract_id)
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

merged_df = pd.merge(reviews_df, books_df, on='id', how='inner')

def extract_year(details):
    if not isinstance(details, str):
        return None
    dates = re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+(\d{4})', details)
    if dates:
        return int(dates[0])
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    if years:
        return int(years[0])
    return None

merged_df['year'] = merged_df['details'].apply(extract_year)
merged_df = merged_df.dropna(subset=['year'])
merged_df['decade'] = (merged_df['year'] // 10) * 10
merged_df['decade_str'] = merged_df['decade'].astype(int).astype(str) + 's'

decade_stats = merged_df.groupby('decade_str').agg(
    distinct_books=('id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

filtered_decades = decade_stats[decade_stats['distinct_books'] >= 10].sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(filtered_decades.to_json(orient='records'))"""

env_args = {'var_function-call-2504176446766605017': ['books_info'], 'var_function-call-2504176446766604662': ['review'], 'var_function-call-17802082905884756457': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-17802082905884755314': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-2638143596723834494': [{'count': '200'}], 'var_function-call-2638143596723834511': [{'count(*)': '1833'}], 'var_function-call-7567474922900922189': 'file_storage/function-call-7567474922900922189.json', 'var_function-call-7567474922900921020': 'file_storage/function-call-7567474922900921020.json', 'var_function-call-9226346158984576322': {'decade': '2020s', 'average_rating': 4.663636363636364, 'distinct_books': 21}}

exec(code, env_args)
