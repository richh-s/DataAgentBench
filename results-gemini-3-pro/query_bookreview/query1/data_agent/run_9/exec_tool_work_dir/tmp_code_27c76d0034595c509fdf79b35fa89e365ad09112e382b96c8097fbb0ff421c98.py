code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-3261298035479939975'], 'r') as f:
    reviews = json.load(f)
with open(locals()['var_function-call-8731750039132877044'], 'r') as f:
    books = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Extract numeric ID
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'(\d+)').astype(int)
df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)').astype(int)

# Extract year
def extract_year(text):
    if not text:
        return None
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},\s+)?(\d{4})', text)
    if match:
        return int(match.group(1))
    match = re.search(r'published.*?(\d{4})', text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books = df_books.dropna(subset=['year'])
df_books['year'] = df_books['year'].astype(int)
df_books['decade'] = (df_books['year'] // 10 * 10).astype(str) + 's'

# Convert rating
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Join
merged = pd.merge(df_reviews, df_books, on='id_num')

# Group by decade
stats = merged.groupby('decade').agg(
    distinct_books=('id_num', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter
filtered = stats[stats['distinct_books'] >= 10].sort_values('avg_rating', ascending=False)

print("__RESULT__:")
print(filtered.to_json(orient='records'))"""

env_args = {'var_function-call-17682976538640268274': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-672206950049772720': ['review'], 'var_function-call-8470034851744981094': [{'COUNT(*)': '1833'}], 'var_function-call-7408255989208608993': [{'count': '200'}], 'var_function-call-3261298035479939975': 'file_storage/function-call-3261298035479939975.json', 'var_function-call-8731750039132877044': 'file_storage/function-call-8731750039132877044.json', 'var_function-call-2008552167001785793': 'No decade met the criteria', 'var_function-call-8491952257252478736': {'total_books': 200, 'books_with_year': 189, 'merged_rows': 0, 'unique_books_in_merge': 0, 'decade_counts': {}}, 'var_function-call-15138202091816277060': {'decade': '2020.0s', 'average_rating': 4.663636363636364, 'distinct_books': 21}}

exec(code, env_args)
