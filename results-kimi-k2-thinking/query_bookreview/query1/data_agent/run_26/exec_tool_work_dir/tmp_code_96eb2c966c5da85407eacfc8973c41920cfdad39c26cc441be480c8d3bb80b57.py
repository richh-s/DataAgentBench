code = """import json
import re
from datetime import datetime

# Load the results from storage
books_path = var_functions.query_db:12
reviews_path = var_functions.query_db:5

# Read the full data
with open(books_path, 'r') as f:
    books = json.load(f)

with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Parse publication year from details string
def extract_year(details):
    if not details:
        return None
    
    # Look for patterns like "January 1, 2004", "May 20, 1996", "July 1, 2003"
    # Also look for patterns like "released on January 1, 2004"
    patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})\b',
        r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\bin\s+(its\s+)?(?:first|second|third|fourth)?\s+edition\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'published\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details, re.IGNORECASE)
        if match:
            year_str = match.groups()[-1]  # Get the last group which should be the year
            try:
                year = int(year_str)
                if 1800 <= year <= 2025:
                    return year
            except ValueError:
                continue
    
    return None

# Extract years from books
books_with_years = []
for book in books:
    year = extract_year(book.get('details', ''))
    if year:
        books_with_years.append({
            'book_id': book['book_id'],
            'title': book['title'],
            'year': year,
            'decade': f"{year//10*10}s"
        })

# Get list of book_ids from reviews
review_book_ids = set(review['purchase_id'] for review in reviews)

# Analyze which books have reviews
print(f"Total books in database: {len(books)}")
print(f"Books with parseable publication years: {len(books_with_years)}")
print(f"Total review records: {len(reviews)}")
print(f"Books with reviews (unique): {len(review_book_ids)}")

# Check if IDs match exactly
books_with_years_ids = set(b['book_id'] for b in books_with_years)
common_ids = books_with_years_ids.intersection(review_book_ids)
print(f"Books with both parsed years and reviews: {len(common_ids)}")

# Look at sample book_id patterns
book_id_sample = list(books_with_years_ids)[:5]
review_id_sample = list(review_book_ids)[:5]
print(f"Sample book_ids: {book_id_sample}")
print(f"Sample purchase_ids: {review_id_sample}")

# Check for matching patterns
for book_id in list(books_with_years_ids)[:20]:
    if book_id in review_book_ids:
        print(f"Match: {book_id}")
        break

# List some IDs that don't match
book_ids_not_in_reviews = books_with_years_ids - review_book_ids
review_ids_not_in_books = review_book_ids - books_with_years_ids
print(f"Books without reviews: {len(book_ids_not_in_reviews)}")
print(f"Reviews with unknown books: {len(review_ids_not_in_books)}")
# Show first few if non-empty
if book_ids_not_in_reviews:
    print(f"Sample books without reviews: {list(book_ids_not_in_reviews)[:5]}")
if review_ids_not_in_books:
    print(f"Sample reviews for unknown books: {list(review_ids_not_in_books)[:5]}")

print('__RESULT__:')
print(json.dumps({
    'books_with_years': len(books_with_years),
    'total_reviews': len(reviews),
    'books_with_reviews': len(common_ids),
    'sample_books': book_id_sample,
    'sample_reviews': review_id_sample
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
