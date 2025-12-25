code = """import json
import pandas as pd
import re

books_file = locals()['var_function-call-17470195624660244328']
reviews_file = locals()['var_function-call-6253168881237040463']

with open(books_file, 'r') as f:
    books = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

def extract_id(s):
    if pd.isna(s): return None
    m = re.search(r'(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

df_books['id_num'] = df_books['book_id'].apply(extract_id)
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

df = pd.merge(df_reviews, df_books, on='id_num', how='inner')

def extract_year(details):
    if not isinstance(details, str): return None
    # Try simpler regex
    years = re.findall(r'(19\d{2}|20\d{2})', details)
    if years:
        # Return the first one
        return int(years[0])
    return None

df['year'] = df['details'].apply(extract_year)
df = df.dropna(subset=['year'])

df['decade'] = (df['year'] // 10) * 10
df['decade_str'] = df['decade'].astype(int).astype(str) + 's'

df['rating'] = df['rating'].astype(float)

stats = df.groupby('decade_str').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('id_num', 'nunique')
).reset_index()

filtered_stats = stats[stats['distinct_books'] >= 10]

if not filtered_stats.empty:
    best_decade = filtered_stats.loc[filtered_stats['avg_rating'].idxmax()]
    result = best_decade['decade_str']
else:
    result = {"status": "No decade meets criteria", "stats": stats.to_dict(orient='records')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9545217224331018128': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-9699813864465939762': ['review'], 'var_function-call-17314963110901189043': [{'COUNT(*)': '1833'}], 'var_function-call-8911477973423827957': [{'count': '200'}], 'var_function-call-17470195624660244328': 'file_storage/function-call-17470195624660244328.json', 'var_function-call-6253168881237040463': 'file_storage/function-call-6253168881237040463.json', 'var_function-call-3687315787474654688': 'No decade meets criteria', 'var_function-call-18090995782316736953': {'n_books': 200, 'n_reviews': 1833, 'n_merged': 1833, 'n_with_year': 0, 'unique_books_merged': 200, 'stats': {}}, 'var_function-call-13230612840399670530': [{'detail': 'Published by Spiegel & Grau on September 4, 2012, this book is written in English and features a hardcover format with 256 pages. It has an ISBN-10 of 0385529813 and an ISBN-13 of 978-0385529815. The item weighs 1.15 pounds and has dimensions of 6.5 x 0.75 x 9.5 inches.', 'years': []}, {'detail': "This special edition of the book, published by St. Martin's Paperbacks on June 2, 2015, is available in English and comes in a mass market paperback format with a total of 352 pages. It has an ISBN-10 of 1250074274 and an ISBN-13 of 978-1250074270. The item weighs 6.4 ounces and measures 4.2 inches in width, 0.93 inches in depth, and 6.83 inches in height.", 'years': []}, {'detail': 'The book, published by Dog Ear Publishing, LLC on October 3, 2012, is available in English and consists of 276 pages. It has an ISBN-10 of 1457514575 and an ISBN-13 of 978-1457514579. The item weighs 12.5 ounces and its dimensions are 5.51 x 0.62 x 8.5 inches.', 'years': []}, {'detail': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'years': []}, {'detail': "This book, published by Builder's Book Inc. in its 2010th edition on February 14, 2010, is available in both English and Ukrainian. It comprises a pamphlet of 6 pages and has an ISBN-10 of 1889892742 and an ISBN-13 of 978-1889892740. The item weighs 2.4 ounces.", 'years': []}]}

exec(code, env_args)
