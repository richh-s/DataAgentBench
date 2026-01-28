code = """import json, re
books_file = locals()['var_functions.query_db:22']
reviews_file = locals()['var_functions.query_db:5']

with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

def extract_year(d):
    if not d:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', d)
    if m:
        return int(m.group(2))
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', d)
    if m:
        return int(m.group(1))
    return None

book_years = {}
for b in books:
    y = extract_year(b.get('details',''))
    if y:
        book_years[b['book_id']] = '{}s'.format((y//10)*10)

decade_info = {}
for r in reviews:
    pid = r['purchase_id']
    if pid in book_years:
        d = book_years[pid]
        if d not in decade_info:
            decade_info[d] = {'books':set(), 'total':0.0, 'count':0}
        decade_info[d]['books'].add(pid)
        decade_info[d]['total'] += float(r['rating'])
        decade_info[d]['count'] += 1

valid = []
for d, info in decade_info.items():
    if len(info['books']) >= 10:
        avg = info['total']/info['count']
        valid.append((d, avg, len(info['books']), info['count']))

valid.sort(key=lambda x:x[1], reverse=True)
print('__RESULT__:')
print(json.dumps(valid[0] if valid else None))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}]}

exec(code, env_args)
