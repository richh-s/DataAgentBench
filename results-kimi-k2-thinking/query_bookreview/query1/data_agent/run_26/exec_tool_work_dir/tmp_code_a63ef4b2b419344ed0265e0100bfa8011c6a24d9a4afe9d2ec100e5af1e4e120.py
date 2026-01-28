code = """import json, re, os

# Get file paths from the stored results
# The results contain file paths since they were too large
books_result = var_functions.query_db:22
reviews_result = var_functions.query_db:5

# The results are actual file paths when the data is large
books_file = books_result
reviews_file = reviews_result

print('Books file path:', str(books_file)[:100])
print('Reviews file path:', str(reviews_file)[:100])

# Check if these are strings (file paths) or already loaded data
if isinstance(books_file, str) and os.path.exists(books_file):
    with open(books_file) as f:
        books = json.load(f)
else:
    books = books_file

if isinstance(reviews_file, str) and os.path.exists(reviews_file):
    with open(reviews_file) as f:
        reviews = json.load(f)
else:
    reviews = reviews_file

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))
print('First 3 book IDs:', [b['book_id'] for b in books[:3]])
print('First 3 review book IDs:', [r['purchase_id'] for r in reviews[:3]])

# Try to extract years and calculate
year_map = {}
for b in books:
    details = b.get('details', '')
    year = None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(2))
    else:
        m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
        if m:
            year = int(m.group(1))
    if year:
        decade = str(year // 10 * 10) + 's'
        year_map[b['book_id']] = decade

print('Extracted years for {} books.'.format(len(year_map)))

# Group reviews
decade_info = {}
for r in reviews:
    pid = r['purchase_id']
    if pid in year_map:
        decade = year_map[pid]
        if decade not in decade_info:
            decade_info[decade] = {'books': set(), 'sum': 0.0, 'cnt': 0}
        decade_info[decade]['books'].add(pid)
        decade_info[decade]['sum'] += float(r['rating'])
        decade_info[decade]['cnt'] += 1

valid = []
for d, info in decade_info.items():
    if len(info['books']) >= 10:
        avg = info['sum'] / info['cnt']
        valid.append((d, avg, len(info['books']), info['cnt']))

valid.sort(key=lambda x: x[1], reverse=True)
print('Found {} valid decades: {}'.format(len(valid), valid[:3]))

result = valid[0] if valid else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
