code = """import json
import re
import pandas as pd

# Load files
file_path_books = locals()['var_function-call-5762601890028283317']
file_path_reviews = locals()['var_function-call-5861420824831990695']

with open(file_path_books, 'r') as f:
    books_data = json.load(f)
with open(file_path_reviews, 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Extract IDs
def extract_id(s):
    if not s: return None
    parts = s.split('_')
    if len(parts) > 1:
        return parts[-1]
    return s

df_books['id_num'] = df_books['book_id'].apply(extract_id)
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

# Extract Year
def extract_year(text):
    if not isinstance(text, str): return None
    
    # Regex to find 4 digit years (19xx or 20xx) not surrounded by digits
    # Using [0-9] to avoid \d issues if any
    # Lookbehind (?<![0-9]) and lookahead (?![0-9])
    
    # We want to capture the year.
    # Pattern: (?<![0-9])((?:19|20)[0-9]{2})(?![0-9])
    
    # Also prioritize years after "published" or "released"
    # Pattern: (published|released).*?((?:19|20)[0-9]{2})
    
    # Let's find all isolated years first
    years = re.findall(r'(?<![0-9])((?:19|20)[0-9]{2})(?![0-9])', text)
    
    if not years:
        return None
        
    # If multiple years, try to find one associated with publication keywords
    # We verify if any of the found years appear after "published" or "released"
    # Note: re.findall returns a list of strings
    
    # Let's try to match specific pattern with priority
    # Case insensitive
    text_lower = text.lower()
    
    # Simple heuristic: The first valid isolated year is often the pub year, 
    # unless it's mentioned as "reprint" or something later.
    # But usually ISBNs are the main source of other numbers, and we handled them with isolation.
    # Page counts (e.g. 196 pages) are not 4 digits usually (unless very big book).
    # Dimensions (e.g. 19.2 mm) usually have decimal or are small.
    # File size (e.g. 2048 KB) might be caught.
    
    # Let's look for context.
    # Regex for year with context
    context_match = re.search(r'(?:published|released|edition).*?((?:19|20)[0-9]{2})', text_lower)
    if context_match:
        y = context_match.group(1)
        # Check if y is in our isolated years list (to avoid "published 123456")
        if y in years:
            return int(y)
            
    # Fallback: return the first isolated year found
    return int(years[0])

df_books['year'] = df_books['details'].apply(extract_year)
df_books_valid = df_books.dropna(subset=['year']).copy()

def to_decade(year):
    return f"{int(year // 10 * 10)}s"

df_books_valid['decade'] = df_books_valid['year'].apply(to_decade)

# Join
# Check id types
# df_reviews['id_num'] and df_books_valid['id_num'] are strings.
df_merged = pd.merge(df_reviews, df_books_valid, on='id_num', how='inner')

# Rating to float
df_merged['rating'] = pd.to_numeric(df_merged['rating'])

# Group
grouped = df_merged.groupby('decade').agg(
    distinct_books=('id_num', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter
filtered = grouped[grouped['distinct_books'] >= 10].copy()

# Find max
if not filtered.empty:
    best = filtered.sort_values('avg_rating', ascending=False).iloc[0]
    result = {
        "decade": best['decade'],
        "avg_rating": best['avg_rating'],
        "distinct_books": int(best['distinct_books'])
    }
else:
    result = {
        "error": "No decade meets criteria",
        "grouped_data": grouped.to_dict(orient='records')
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4991624145889692617': ['books_info'], 'var_function-call-17824524347429052940': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-6644222601643079336': [{'count': '200'}], 'var_function-call-10449438570185145554': ['review'], 'var_function-call-2425197519240266821': [{'COUNT(*)': '1833'}], 'var_function-call-5762601890028283317': 'file_storage/function-call-5762601890028283317.json', 'var_function-call-5861420824831990695': 'file_storage/function-call-5861420824831990695.json', 'var_function-call-18194477350139040333': 'No decade meets criteria', 'var_function-call-2906622808988997365': {'total_books': 200, 'books_with_valid_year': 0, 'sample_years': [], 'books_per_decade': {}, 'total_reviews': 1833, 'sample_book_ids': ['1', '2', '3', '4', '5'], 'sample_review_ids': ['186', '191', '190', '8', '178']}, 'var_function-call-15828801288682271034': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'debug': 'Candidates: []'}, {'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'debug': 'Candidates: []'}, {'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'debug': 'Candidates: []'}, {'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'debug': 'Candidates: []'}, {'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'debug': 'Candidates: []'}], 'var_function-call-12824700704638120737': ["Digits: ['2004', '0701', '1698', '0701', '1698'], Repr: 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is", "Digits: ['1996', '0435', '0886', '0435', '0886'], Repr: 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and i", "Digits: ['2012', '9780', '3161', '8536', '0316', '1853'], Repr: 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available", "Digits: ['2013', '0545', '4255', '0545', '4255'], Repr: 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written ", "Digits: ['2014', '1542'], Repr: 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB "]}

exec(code, env_args)
