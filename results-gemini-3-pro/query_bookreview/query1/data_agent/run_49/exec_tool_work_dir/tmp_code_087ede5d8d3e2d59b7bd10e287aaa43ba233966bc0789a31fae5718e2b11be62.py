code = """import json
import re
import pandas as pd

# Load books
with open('var_function-call-16212672584058288689.json', 'r') as f:
    books_data = json.load(f)

# Load reviews
with open('var_function-call-11346292082118706141.json', 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Process book IDs
# book_id: "bookid_1" -> 1
def extract_id(s, prefix):
    if pd.isna(s): return None
    if s.startswith(prefix):
        return int(s[len(prefix):])
    return None

books_df['id_num'] = books_df['book_id'].apply(lambda x: extract_id(x, 'bookid_'))
reviews_df['id_num'] = reviews_df['purchase_id'].apply(lambda x: extract_id(x, 'purchaseid_'))

# Extract year from details
# Pattern: Month Day, Year (e.g., "January 1, 2004")
# Pattern: Month Year (e.g., "January 2004")
# Pattern: Just Year (if it appears in a context implying date)

# Regex for "Month Day, Year" or "Month, Year"
date_pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})', re.IGNORECASE)
# Fallback: Just look for 19xx or 20xx but try to avoid ISBNs if possible.
# Actually, the texts are quite verbose.
# Let's extract all 4-digit numbers starting with 19 or 20.
# And filter out ones that are likely not years if multiple found?
# Usually the publication year is the first one or part of "published ... on ..."
# Let's prioritize the pattern with month.

def get_year(details):
    if not isinstance(details, str):
        return None
    
    # Try explicit date format
    match = date_pattern.search(details)
    if match:
        return int(match.group(1))
    
    # Fallback: look for year-like numbers
    # We want 1900-2023.
    candidates = re.findall(r'\b(19\d{2}|20[0-2]\d)\b', details)
    if candidates:
        # If multiple, which one?
        # Example: "8082nd edition from January 1, 1994" -> 1994 is good.
        # "ISBN ... 2004..." -> 2004 might be ISBN part.
        # But usually ISBN is clearly labeled.
        # Let's take the first one that is reasonable?
        # Or maybe filter out numbers that appear in ISBNs?
        # A simple heuristic: take the one that appears after "published" or "released"?
        # For now, let's take the first one.
        return int(candidates[0])
    return None

books_df['year'] = books_df['details'].apply(get_year)

# Filter out books with no year
books_with_year = books_df.dropna(subset=['year'])

# Calculate decade
# Decade: 1980s for 1980-1989.
# Formula: (year // 10) * 10
books_with_year['decade'] = (books_with_year['year'] // 10) * 10
books_with_year['decade_str'] = books_with_year['decade'].astype(int).astype(str) + 's'

# Merge reviews with books
merged = pd.merge(reviews_df, books_with_year[['id_num', 'decade_str']], on='id_num', how='inner')

# Convert rating to float
merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')
merged = merged.dropna(subset=['rating'])

# Group by decade
decade_stats = merged.groupby('decade_str').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('id_num', 'nunique'),
    count=('rating', 'count') # just for info
).reset_index()

# Filter: at least 10 distinct books
qualified_decades = decade_stats[decade_stats['distinct_books'] >= 10]

# Find max avg rating
if not qualified_decades.empty:
    best_decade = qualified_decades.loc[qualified_decades['avg_rating'].idxmax()]
    result = best_decade.to_dict()
else:
    result = "No qualified decades"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9607707979099280481': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-13230780156441272159': ['review'], 'var_function-call-2103188382748939807': [{'count(*)': '1833'}], 'var_function-call-6878541484741589626': [{'count': '200'}], 'var_function-call-16212672584058288689': 'file_storage/function-call-16212672584058288689.json', 'var_function-call-11346292082118706141': 'file_storage/function-call-11346292082118706141.json'}

exec(code, env_args)
