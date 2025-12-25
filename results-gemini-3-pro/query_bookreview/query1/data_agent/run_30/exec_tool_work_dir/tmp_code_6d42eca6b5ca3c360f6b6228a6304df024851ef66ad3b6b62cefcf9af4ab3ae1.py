code = """import json
import pandas as pd
import re
import numpy as np

file_reviews = locals()['var_function-call-8003413839602542900']
file_books = locals()['var_function-call-12230880538750893406']

with open(file_reviews, 'r') as f:
    reviews = json.load(f)
with open(file_books, 'r') as f:
    books = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

debug_info = {}
debug_info['total_reviews'] = int(len(df_reviews))
debug_info['total_books'] = int(len(df_books))

review_ids = set(df_reviews['purchase_id'].unique())
book_ids = set(df_books['book_id'].unique())
intersection = review_ids.intersection(book_ids)
debug_info['intersection_count'] = int(len(intersection))

def extract_year_loose(details):
    if not isinstance(details, str):
        return None
    # Regex for Year near keywords
    m = re.search(r'(?:published|released|edition|copyright|©).*?(\b(19|20)\d{2}\b)', details, re.IGNORECASE)
    if m:
        return int(m.group(1))
    
    # Regex for "Month Day, Year" anywhere (pretty safe)
    m2 = re.search(r'[A-Z][a-z]+\s+\d{1,2},?\s+(\d{4})', details)
    if m2:
        y = int(m2.group(1))
        if 1800 <= y <= 2024:
            return y
            
    return None

df_books['year'] = df_books['details'].apply(extract_year_loose)
debug_info['books_with_year'] = int(df_books['year'].notnull().sum())

merged = pd.merge(df_books, df_reviews, left_on='book_id', right_on='purchase_id', how='inner')
merged = merged.dropna(subset=['year'])
debug_info['merged_with_year'] = int(len(merged))

if not merged.empty:
    merged['decade'] = (merged['year'] // 10 * 10).astype(int).astype(str) + 's'
    
    # Calculate stats
    stats = merged.groupby('decade').agg(
        book_count=('book_id', 'nunique'),
        average_rating=('avg_rating', 'mean') # Wait, avg_rating in reviews is string or float?
    ).reset_index()
    
    # ensure numeric
    if 'avg_rating' in df_reviews.columns:
         # In previous step I converted to numeric, here I reloaded.
         # df_reviews loaded from JSON, avg_rating might be string.
         pass # handled below

    # Convert avg_rating column to numeric in merged
    merged['avg_rating'] = pd.to_numeric(merged['avg_rating'])
    
    stats = merged.groupby('decade').agg(
        book_count=('book_id', 'nunique'),
        average_rating=('avg_rating', 'mean')
    ).reset_index()

    debug_info['decades'] = stats.to_dict(orient='records')
    
    # Filter
    filtered = stats[stats['book_count'] >= 10]
    if not filtered.empty:
        best = filtered.sort_values('average_rating', ascending=False).iloc[0]
        debug_info['best_decade'] = best.to_dict()
    else:
        debug_info['best_decade'] = "None"

print("__RESULT__:")
# Custom encoder for numpy types
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

print(json.dumps(debug_info, cls=NpEncoder))"""

env_args = {'var_function-call-9636641086377978641': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4069087491551052511': ['review'], 'var_function-call-8003413839602542900': 'file_storage/function-call-8003413839602542900.json', 'var_function-call-12230880538750893406': 'file_storage/function-call-12230880538750893406.json', 'var_function-call-7507660314583586869': 'No decade meets criteria', 'var_function-call-13986530731642715435': 'None'}

exec(code, env_args)
