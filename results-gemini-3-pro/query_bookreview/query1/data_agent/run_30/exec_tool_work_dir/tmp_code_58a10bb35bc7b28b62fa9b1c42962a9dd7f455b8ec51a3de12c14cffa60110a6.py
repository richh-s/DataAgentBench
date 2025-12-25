code = """import json
import pandas as pd
import re

file_reviews = locals()['var_function-call-8003413839602542900']
file_books = locals()['var_function-call-12230880538750893406']

with open(file_reviews, 'r') as f:
    reviews = json.load(f)
with open(file_books, 'r') as f:
    books = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

print(f"Total reviews (books rated): {len(df_reviews)}")
print(f"Total books metadata: {len(df_books)}")

# Improved extraction
def extract_year_debug(details):
    if not isinstance(details, str):
        return None
    
    # Strategy: Find 'published' or 'released' and look for date-like structures
    # 1. Look for Month DD, YYYY
    m1 = re.search(r'(?:published|released).*?([A-Z][a-z]+ \d{1,2}, \d{4})', details, re.IGNORECASE)
    if m1:
        # Extract year from the date string
        d = m1.group(1)
        y = re.search(r'\d{4}', d)
        if y: return int(y.group(0))

    # 2. Look for just a year closely following published/released if no full date
    # Be careful of ISBNs. ISBNs are usually labeled "ISBN" or appear later.
    # Let's look for "published ... 19XX" or "20XX"
    # But often "published by ... in 1998"
    m2 = re.search(r'(?:published|released).*?\b((?:19|20)\d{2})\b', details, re.IGNORECASE)
    if m2:
        return int(m2.group(1))

    return None

df_books['year'] = df_books['details'].apply(extract_year_debug)
print(f"Books with extracted year: {df_books['year'].notnull().sum()}")

merged = pd.merge(df_books, df_reviews, left_on='book_id', right_on='purchase_id', how='inner')
print(f"Merged books (rated + metadata): {len(merged)}")
print(f"Merged books with year: {merged['year'].notnull().sum()}")

merged['avg_rating'] = pd.to_numeric(merged['avg_rating'])
merged = merged.dropna(subset=['year'])

def get_decade(year):
    return f"{int(year // 10) * 10}s"

merged['decade'] = merged['year'].apply(get_decade)

decade_counts = merged['decade'].value_counts()
print("Decade counts:")
print(decade_counts)

# Calculate stats
decade_stats = merged.groupby('decade').agg(
    book_count=('book_id', 'nunique'),
    average_rating=('avg_rating', 'mean')
).reset_index()

filtered = decade_stats[decade_stats['book_count'] >= 10]
print("Filtered Decades:")
print(filtered)

if not filtered.empty:
    best = filtered.sort_values('average_rating', ascending=False).iloc[0]
    res = best.to_dict()
else:
    res = "None"

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-9636641086377978641': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4069087491551052511': ['review'], 'var_function-call-8003413839602542900': 'file_storage/function-call-8003413839602542900.json', 'var_function-call-12230880538750893406': 'file_storage/function-call-12230880538750893406.json', 'var_function-call-7507660314583586869': 'No decade meets criteria'}

exec(code, env_args)
