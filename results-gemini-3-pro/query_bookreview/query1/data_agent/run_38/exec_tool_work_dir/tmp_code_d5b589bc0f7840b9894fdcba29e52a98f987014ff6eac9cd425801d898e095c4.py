code = """import json
import pandas as pd
import re

# Load books
# Use locals() or get matching key
key_books = 'var_function-call-9535784037106745214'
with open(locals()[key_books], 'r') as f:
    books_data = json.load(f)
books_df = pd.DataFrame(books_data)

# Load reviews
key_reviews = 'var_function-call-13255568804086674968'
with open(locals()[key_reviews], 'r') as f:
    reviews_data = json.load(f)
reviews_df = pd.DataFrame(reviews_data)

# Function to extract year
def extract_year(details):
    if not isinstance(details, str):
        return None
    # Regex for Month Day, Year
    match = re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})', details)
    if match:
        date_str = match.group(1)
        # Extract the year part
        return int(date_str.split(',')[-1].strip())
    
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Filter out books with no year
books_with_year = books_df.dropna(subset=['year']).copy()
books_with_year['year'] = books_with_year['year'].astype(int)

# Create decade
books_with_year['decade'] = (books_with_year['year'] // 10) * 10
books_with_year['decade_str'] = books_with_year['decade'].astype(str) + 's'

# Extract join IDs
def extract_id_num(id_str):
    if pd.isna(id_str): return None
    nums = re.findall(r'\d+', id_str)
    if nums:
        return nums[0]
    return None

books_with_year['join_id'] = books_with_year['book_id'].apply(extract_id_num)
reviews_df['join_id'] = reviews_df['purchase_id'].apply(extract_id_num)

# Join
merged_df = pd.merge(reviews_df, books_with_year, on='join_id', how='inner')

# Convert rating
merged_df['rating'] = pd.to_numeric(merged_df['rating'], errors='coerce')

# Group by decade
decade_stats = merged_df.groupby('decade_str').agg(
    distinct_books=('book_id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter
filtered_decades = decade_stats[decade_stats['distinct_books'] >= 10]

# Find best
if not filtered_decades.empty:
    best_decade = filtered_decades.loc[filtered_decades['avg_rating'].idxmax()]
    result = {
        "best_decade": best_decade['decade_str'],
        "avg_rating": best_decade['avg_rating'],
        "distinct_books": int(best_decade['distinct_books']),
        "all_decades": decade_stats.to_dict(orient='records')
    }
else:
    result = {
        "best_decade": None,
        "all_decades": decade_stats.to_dict(orient='records')
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4420274034771021576': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-4583334481166262733': [{'count': '200'}], 'var_function-call-16551330801499451707': ['review'], 'var_function-call-16138809042932621867': [{'count(*)': '1833'}], 'var_function-call-9535784037106745214': 'file_storage/function-call-9535784037106745214.json', 'var_function-call-13255568804086674968': 'file_storage/function-call-13255568804086674968.json'}

exec(code, env_args)
