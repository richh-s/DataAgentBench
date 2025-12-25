code = """import pandas as pd
import json
import re

# Load data
# Using the keys provided in the prompts
with open(locals()['var_function-call-7801495957954305071'], 'r') as f:
    books = json.load(f)
with open(locals()['var_function-call-7801495957954302942'], 'r') as f:
    reviews = json.load(f)

# Process books
book_years = []
for b in books:
    bid_str = b.get('book_id', '')
    details = b.get('details', '')
    
    # Extract ID number
    bid_match = re.search(r'(\d+)$', bid_str)
    if not bid_match:
        continue
    bid_num = int(bid_match.group(1))
    
    # Extract Year
    year = None
    # Look for 4 digits that represent a year (19xx or 20xx) associated with published/released.
    match = re.search(r'(?:published|released).*?(\d{4})', details, re.IGNORECASE)
    if match:
        year = int(match.group(1))
    else:
        # Fallback: just find a year in 1900-2023 range?
        match_y = re.search(r'\b(19\d{2}|20[0-1]\d|202[0-3])\b', details)
        if match_y:
            year = int(match_y.group(1))
            
    if year:
        book_years.append({'id_num': bid_num, 'year': year})

df_books = pd.DataFrame(book_years)
df_books['decade'] = (df_books['year'] // 10) * 10
df_books['decade_str'] = df_books['decade'].astype(str) + 's'

# Process reviews
review_data = []
for r in reviews:
    pid_str = r.get('purchase_id', '')
    rating = r.get('rating')
    
    # Extract ID number
    pid_match = re.search(r'(\d+)$', pid_str)
    if not pid_match:
        continue
    pid_num = int(pid_match.group(1))
    
    if rating is not None:
        review_data.append({'id_num': pid_num, 'rating': float(rating)})

df_reviews = pd.DataFrame(review_data)

# Merge
merged = pd.merge(df_reviews, df_books, on='id_num', how='inner')

# Aggregation
stats = merged.groupby('decade_str').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('id_num', 'nunique')
).reset_index()

# Filter
filtered = stats[stats['distinct_books'] >= 10]

# Find max
if not filtered.empty:
    best_decade = filtered.loc[filtered['avg_rating'].idxmax()]['decade_str']
    # If there's a tie, usually the first one is returned, but let's check max value and list ties if any? 
    # But question asks for "the decade", implying unique or just one.
else:
    best_decade = "None"

print("__RESULT__:")
print(json.dumps(best_decade))"""

env_args = {'var_function-call-16436105270370816678': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-12372100282322186920': ['review'], 'var_function-call-15689616086069158974': [{'count': '200'}], 'var_function-call-15689616086069159081': [{'count(*)': '1833'}], 'var_function-call-7801495957954305071': 'file_storage/function-call-7801495957954305071.json', 'var_function-call-7801495957954302942': 'file_storage/function-call-7801495957954302942.json'}

exec(code, env_args)
