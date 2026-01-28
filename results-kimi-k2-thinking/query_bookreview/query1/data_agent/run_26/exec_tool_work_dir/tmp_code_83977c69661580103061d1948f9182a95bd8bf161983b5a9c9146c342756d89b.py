code = """import json, re

# Load the data
with open(var_functions.query_db:22) as f:
    books = json.load(f)
with open(var_functions.query_db:5) as f:
    reviews = json.load(f)

# Debug book data
print('Total books:', len(books))
print('First 2 books details:')
for i in range(min(2, len(books))):
    print(books[i]['book_id'])
    print(books[i]['details'][:200])
    print('---')

# Parse years
years = {}
for b in books:
    d = b.get('details','')
    y = None
    # Look for "Month day, year"
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', d)
    if m:
        y = int(m.group(2))
    else:
        # Look for "on ... year" or last 4-digit year
        m = re.search(r'\bon\s+(?:[A-Za-z]+[^\d]+)?(\d{4})\b', d)
        if m:
            y = int(m.group(1))
    if y:
        years[b['book_id']] = '{0}s'.format((y//10)*10)

print('Extracted years for {} books'.format(len(years)))
print('Sample:', list(years.items())[:5])

# Debug reviews
print('\nTotal reviews:', len(reviews))
print('Review book IDs:', set([r['purchase_id'] for r in reviews]))

print('__RESULT__:')
print(json.dumps({
    'extracted_years': len(years),
    'total_reviews': len(reviews),
    'sample_books': list(years.items())[:5]
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
