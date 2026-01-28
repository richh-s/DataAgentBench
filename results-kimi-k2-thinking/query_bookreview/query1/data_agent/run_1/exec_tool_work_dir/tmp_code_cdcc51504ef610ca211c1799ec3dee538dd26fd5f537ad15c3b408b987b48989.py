code = """import json
import re
import pandas as pd

# Load books data
books_key = 'var_functions.query_db:8'
books_data = locals().get(books_key, [])

if isinstance(books_data, str) and '.json' in books_data:
    with open(books_data, 'r') as f:
        books_data = json.load(f)

# Load review data
review_key = 'var_functions.query_db:10'
review_data = locals().get(review_key, [])

if isinstance(review_data, str) and '.json' in review_data:
    with open(review_data, 'r') as f:
        review_data = json.load(f)

# Function to extract year from details
def extract_year(details):
    if not details:
        return None
    
    patterns = [
        r'on\s+\w+\s+\d{1,2},\s+(\d{4})',
        r'published\s+\w+\s+\d{1,2},\s+(\d{4})',
        r'Published\s*:\s*\w+\s+\d{1,2},\s+(\d{4})',
        r'\d{1,2},\s+(\d{4})',
        r'published\s+in\s+(\d{4})',
        r'published\s+on\s+\d{1,2}\s+\w+,?\s*(\d{4})',
        r'in\s+(\d{4})\s+(edition|reprint)',
        r'(\d{4})\s+(edition|reprint)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details, re.IGNORECASE)
        if match:
            try:
                groups = match.groups()
                if len(groups) == 2:
                    year = int(groups[1])
                else:
                    year = int(groups[0])
                if 1800 <= year <= 2025:
                    return year
            except:
                continue
    
    all_years = re.findall(r'(\d{4})', details)
    for year_str in all_years:
        try:
            year = int(year_str)
            if 1800 <= year <= 2025:
                return year
        except:
            continue
    
    return None

# Create books dataframe with extracted years
books_list = []
for book in books_data:
    book_id = book.get('book_id')
    details = book.get('details', '')
    year = extract_year(details)
    
    if book_id and year:
        books_list.append({
            'book_id': book_id,
            'publication_year': year,
            'decade': (year // 10) * 10
        })

books_df = pd.DataFrame(books_list)

# Create review dataframe
review_df = pd.DataFrame(review_data)
review_df['rating'] = pd.to_numeric(review_df['rating'], errors='coerce')

# Extract numeric part from IDs
review_df['purchase_num'] = review_df['purchase_id'].str.extract(r'(\d+)').astype(int)
books_df['book_num'] = books_df['book_id'].str.extract(r'(\d+)').astype(int)

# Join the dataframes
merged_df = review_df.merge(books_df, left_on='purchase_num', right_on='book_num', how='inner')

# Group by decade and calculate stats
decade_stats = merged_df.groupby('decade').agg({
    'rating': ['count', 'mean'],
    'book_id': 'nunique'
}).round(3)

decade_stats.columns = ['total_ratings', 'avg_rating', 'distinct_books']
decade_stats = decade_stats.reset_index()

# Filter for decades with at least 10 distinct books
decade_filtered = decade_stats[decade_stats['distinct_books'] >= 10].copy()
decade_filtered = decade_filtered.sort_values('avg_rating', ascending=False)

# Get the top decade
result = None
if not decade_filtered.empty:
    top_decade = decade_filtered.iloc[0]
    decade_str = str(int(top_decade['decade'])) + "s"
    result = {
        'decade': decade_str,
        'avg_rating': round(top_decade['avg_rating'], 2),
        'distinct_books': int(top_decade['distinct_books']),
        'total_ratings': int(top_decade['total_ratings'])
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': [{'title': 'Chaucer', 'year': 2004, 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is ...'}, {'title': 'Notes from a Kidwatcher', 'year': 1996, 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is...'}, {'title': 'Service: A Navy SEAL at War', 'year': 2012, 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available ...'}, {'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'year': 2013, 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written i...'}, {'title': 'Parker & Knight', 'year': 2014, 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB a...'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
