code = """import json
import re
import pandas as pd

# Access the stored results using locals()
books_result = locals()['var_functions.query_db:12']
reviews_result = locals()['var_functions.query_db:5']

# Handle file paths
if isinstance(books_result, str) and books_result.endswith('.json'):
    with open(books_result, 'r') as f:
        books = json.load(f)
else:
    books = books_result

if isinstance(reviews_result, str) and reviews_result.endswith('.json'):
    with open(reviews_result, 'r') as f:
        reviews = json.load(f)
else:
    reviews = reviews_result

# Parse publication year from details string
def extract_year(details):
    if not details:
        return None
    
    # Look for patterns like "January 1, 2004", "May 20, 1996", "July 1, 2003"
    patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})\b',
        r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\bin\s+(its\s+)?(?:first|second|third|fourth)?\s+edition\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'published\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details, re.IGNORECASE)
        if match:
            year_str = match.groups()[-1]
            try:
                year = int(year_str)
                if 1800 <= year <= 2025:
                    return year
            except ValueError:
                continue
    
    return None

# Extract years from books
books_with_info = []
for book in books:
    year = extract_year(book.get('details', ''))
    books_with_info.append({
        'book_id': book['book_id'],
        'year': year
    })

# Get list of book_ids from reviews
review_book_ids = set(review['purchase_id'] for review in reviews)

# Filter books that have publication year and reviews
books_with_years = [b for b in books_with_info if b['year'] is not None]
books_with_years_ids = set(b['book_id'] for b in books_with_years)

common_ids = books_with_years_ids.intersection(review_book_ids)

print(f"Books with parseable publication years: {len(books_with_years)}")
print(f"Total review records: {len(reviews)}")
print(f"Books with reviews (unique): {len(review_book_ids)}")
print(f"Books with both parsed years and reviews: {len(common_ids)}")

print('__RESULT__:')
print(json.dumps({
    'books_with_years': len(books_with_years),
    'total_reviews': len(reviews),
    'books_with_reviews': len(review_book_ids),
    'books_with_both': len(common_ids),
    'sample_books': list(books_with_years_ids)[:5]
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
