code = """import json
import re
import os

# Load the full datasets
books_file = locals()['var_functions.query_db:22']
reviews_file = locals()['var_functions.query_db:5']

with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

# Extract numeric ID from strings like "bookid_123" or "purchaseid_456"
def extract_number_id(id_string):
    if not id_string:
        return None
    match = re.search(r'(\d+)$', id_string)
    return int(match.group(1)) if match else None

# Extract publication year from book details
def extract_publication_year(details_text):
    if not details_text or not isinstance(details_text, str):
        return None
    
    # Look for patterns like "January 1, 2004" or "released on May 20, 1996"
    patterns = [
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details_text, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            if 1900 <= year <= 2025:
                return year
    
    return None

# Map numeric book IDs to their publication decades
book_id_to_decade = {}
for book in books:
    book_id = book.get('book_id')
    details = book.get('details', '')
    
    year = extract_publication_year(details)
    if year and book_id:
        decade = str((year // 10) * 10) + 's'
        numeric_id = extract_number_id(book_id)
        if numeric_id:
            book_id_to_decade[numeric_id] = decade

# Group reviews by decade using numeric ID matching
decade_statistics = {}
for review in reviews:
    purchase_id = review.get('purchase_id')
    rating_str = review.get('rating', '0')
    
    try:
        rating = float(rating_str)
    except (ValueError, TypeError):
        continue
    
    numeric_id = extract_number_id(purchase_id)
    if numeric_id and numeric_id in book_id_to_decade:
        decade = book_id_to_decade[numeric_id]
        
        if decade not in decade_statistics:
            decade_statistics[decade] = {'books': set(), 'sum_ratings': 0.0, 'review_count': 0}
        
        decade_statistics[decade]['books'].add(numeric_id)
        decade_statistics[decade]['sum_ratings'] += rating
        decade_statistics[decade]['review_count'] += 1

# Find decades with at least 10 distinct books and calculate average ratings
eligible_decades = []
for decade, stats in decade_statistics.items():
    distinct_book_count = len(stats['books'])
    if distinct_book_count >= 10:
        average_rating = stats['sum_ratings'] / stats['review_count']
        eligible_decades.append((decade, average_rating, distinct_book_count, stats['review_count']))

# Sort by average rating descending to find the highest
eligible_decades.sort(key=lambda x: x[1], reverse=True)

# Get the top decade
top_decade = eligible_decades[0][0] if eligible_decades else None

print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}], 'var_functions.execute_python:90': None, 'var_functions.execute_python:92': None}

exec(code, env_args)
