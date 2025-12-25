code = """import json
import re
import pandas as pd

# Load data
with open('var_function-call-12934756873881325682.json', 'r') as f:
    books_data = json.load(f)

with open('var_function-call-12934756873881328055.json', 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Extract ID number
def extract_id_num(s):
    match = re.search(r'(\d+)$', s)
    if match:
        return int(match.group(1))
    return None

books_df['id_num'] = books_df['book_id'].apply(extract_id_num)
reviews_df['id_num'] = reviews_df['purchase_id'].apply(extract_id_num)

# Extract year from details
def extract_year(text):
    if not isinstance(text, str):
        return None
    # Look for patterns like "published ... on ... YYYY" or just "YYYY"
    # The examples show the date usually follows "on" or "in".
    # But simply finding all 4-digit numbers and taking a plausible one is robust.
    # Plausible range: 1900 - 2023
    years = re.findall(r'\b(19\d{2}|20[0-2]\d)\b', text)
    if years:
        # If multiple years, usually the first one mentioned as publication date is best.
        # But sometimes "published in 2004... edition from 1994".
        # Let's try to find year associated with "published" or "released".
        # Regex for "published/released ... year"
        # Since the structure is somewhat consistent: "published ... on Month Day, Year"
        match = re.search(r'(?:published|released).*?(\d{4})', text, re.IGNORECASE)
        if match:
             y = int(match.group(1))
             if 1900 <= y <= 2024:
                 return y
        
        # Fallback: first valid year
        for y_str in years:
            y = int(y_str)
            if 1900 <= y <= 2024:
                return y
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Drop books with no year
books_df = books_df.dropna(subset=['year'])
books_df['decade'] = (books_df['year'] // 10) * 10
books_df['decade_str'] = books_df['decade'].astype(int).astype(str) + 's'

# Merge reviews
# Convert rating to float
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df = reviews_df.dropna(subset=['rating', 'id_num'])

# Merge on id_num
merged_df = pd.merge(reviews_df, books_df, on='id_num', how='inner')

# Calculate stats per decade
decade_stats = []
for decade, group in merged_df.groupby('decade_str'):
    distinct_books = group['id_num'].nunique()
    avg_rating = group['rating'].mean()
    decade_stats.append({
        'decade': decade,
        'distinct_books': distinct_books,
        'avg_rating': avg_rating
    })

results_df = pd.DataFrame(decade_stats)
results_df = results_df[results_df['distinct_books'] >= 10]
results_df = results_df.sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-10890240304113574444': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-928886376680201336': ['review'], 'var_function-call-928886376680199259': [{'count': '200'}], 'var_function-call-7724036594629075955': [{'count(*)': '1833'}], 'var_function-call-12934756873881325682': 'file_storage/function-call-12934756873881325682.json', 'var_function-call-12934756873881328055': 'file_storage/function-call-12934756873881328055.json'}

exec(code, env_args)
