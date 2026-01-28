code = """import json, re

# Load the JSON files
with open(var_functions.query_db_22) as f:
    books = json.load(f)
with open(var_functions.query_db_5) as f:
    reviews = json.load(f)

# Extract publication years from details strings
year_map = {}
for b in books:
    details = b.get('details', '')
    year = None
    
    # Try to find "Month day, year" pattern
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if match:
        year = int(match.group(2))
    else:
        # Try to find "on ... year" pattern
        match = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
        if match:
            year = int(match.group(1))
    
    if year and 1900 <= year <= 2025:
        decade = str(year // 10 * 10) + 's'
        year_map[b['book_id']] = decade

# Group reviews by decade
decade_data = {}
for review in reviews:
    book_id = review['purchase_id']
    rating = float(review['rating'])
    
    if book_id in year_map:
        decade = year_map[book_id]
        if decade not in decade_data:
            decade_data[decade] = {'books': set(), 'sum_ratings': 0.0, 'count': 0}
        decade_data[decade]['books'].add(book_id)
        decade_data[decade]['sum_ratings'] += rating
        decade_data[decade]['count'] += 1

# Find decades with at least 10 distinct books and calculate average ratings
valid_decades = []
for decade, data in decade_data.items():
    if len(data['books']) >= 10:
        avg_rating = data['sum_ratings'] / data['count']
        valid_decades.append((decade, avg_rating, len(data['books']), data['count']))

# Sort by average rating (highest first)
valid_decades.sort(key=lambda x: x[1], reverse=True)

# Get the top decade
top_decade = valid_decades[0] if valid_decades else None

print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
