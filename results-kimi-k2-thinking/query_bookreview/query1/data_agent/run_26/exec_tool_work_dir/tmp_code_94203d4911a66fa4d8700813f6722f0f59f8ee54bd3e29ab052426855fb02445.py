code = """import json
import re
import pandas as pd

# Access the stored results using locals()
books_result = locals()['var_functions.query_db:12']

# Handle file paths
if isinstance(books_result, str) and books_result.endswith('.json'):
    with open(books_result, 'r') as f:
        books = json.load(f)[:20]  # Limit to first 20 for debugging
else:
    books = books_result[:20]

# Let's examine the actual details field
def debug_year_extraction(details):
    if not details:
        return None
    
    print(f"Details: {details[:200]}")
    
    patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})\b',
        r'(?:released|published|edition)\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b'
    ]
    
    for i, pattern in enumerate(patterns):
        match = re.search(pattern, details, re.IGNORECASE)
        if match:
            print(f"Pattern {i+1} matched: {match.group()}")
            year_str = match.groups()[-1]
            print(f"Year string: {year_str}")
            try:
                year = int(year_str)
                if 1800 <= year <= 2025:
                    print(f"Valid year: {year}")
                    return year
            except ValueError:
                print(f"Invalid year: {year_str}")
                continue
    
    print("No year found")
    return None

# Test on first few books
sample_books = []
for book in books[:10]:
    print(f"\n--- Book: {book.get('book_id')} ---")
    year = debug_year_extraction(book.get('details', ''))
    sample_books.append(book.get('book_id'))

print('__RESULT__:')
print(json.dumps({'sample_books_checked': sample_books, 'total_books': len(books)}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}}

exec(code, env_args)
