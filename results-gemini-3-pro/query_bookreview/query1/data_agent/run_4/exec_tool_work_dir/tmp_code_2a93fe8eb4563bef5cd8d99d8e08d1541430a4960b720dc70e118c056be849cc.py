code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-9460108322324116834'], 'r') as f:
    books_data = json.load(f)
    
with open(locals()['var_function-call-12255960221478311343'], 'r') as f:
    ratings_data = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_data)
ratings_df = pd.DataFrame(ratings_data)

# Process ratings
# Extract ID from purchase_id
def extract_id(s):
    match = re.search(r'(\d+)$', s)
    if match:
        return int(match.group(1))
    return None

ratings_df['id'] = ratings_df['purchase_id'].apply(extract_id)
ratings_df['avg_rating'] = ratings_df['avg_rating'].astype(float)

# Process books
books_df['id'] = books_df['book_id'].apply(extract_id)

# Extract year from details
def extract_year(details):
    # Regex to capture year in "published ... on ... Year" or "released ... on ... Year"
    # We look for "on [Month] [Day], [Year]" or "on [Month] [Year]"
    # Common formats seen: "on January 1, 2004", "on May 20, 1996"
    # Sometimes month is not full name? Assuming full name based on samples.
    
    # Let's try to find a year that comes after "published" or "released"
    # and is associated with a date pattern.
    
    # Matches: "on January 1, 2004" -> 2004
    # "on May 18, 2014" -> 2014
    # "in January 2004" -> 2004
    
    match = re.search(r'(?:published|released).*?on\s+(?:[A-Za-z]+\s+\d{1,2},?\s+)?([12]\d{3})', details, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Fallback: look for "in [Month] [Year]" if "on" didn't match or for general year close to published
    match = re.search(r'(?:published|released).*?in\s+(?:[A-Za-z]+\s+)?([12]\d{3})', details, re.IGNORECASE)
    if match:
        return int(match.group(1))
        
    # Fallback: just find the first year? might match ISBN or something.
    # Let's be stricter first.
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Join
merged_df = pd.merge(books_df, ratings_df, on='id', how='inner')

# Calculate decade
merged_df['decade'] = (merged_df['year'] // 10) * 10

# Group by decade
decade_stats = merged_df.groupby('decade').agg(
    book_count=('id', 'nunique'),
    avg_rating=('avg_rating', 'mean')
).reset_index()

# Filter
filtered_stats = decade_stats[decade_stats['book_count'] >= 10]

# Find max
if not filtered_stats.empty:
    best_decade_row = filtered_stats.loc[filtered_stats['avg_rating'].idxmax()]
    best_decade = int(best_decade_row['decade'])
    best_rating = best_decade_row['avg_rating']
    count = int(best_decade_row['book_count'])
    result = f"{best_decade}s"
else:
    result = "None"
    best_decade = None
    best_rating = None
    count = 0

print("__RESULT__:")
print(json.dumps({
    "best_decade": result,
    "rating": best_rating,
    "book_count": count,
    "all_decades": decade_stats.to_dict(orient='records')
}))"""

env_args = {'var_function-call-11154569947528999744': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-1739547636167266092': ['review'], 'var_function-call-11844282501900911510': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-4542548580664024702': [{'count': '200'}], 'var_function-call-2254253683607105706': [{'count(*)': '1833'}], 'var_function-call-9460108322324116834': 'file_storage/function-call-9460108322324116834.json', 'var_function-call-12255960221478311343': 'file_storage/function-call-12255960221478311343.json'}

exec(code, env_args)
