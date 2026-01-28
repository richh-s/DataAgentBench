code = """import json, re
with open(var_call_uoQBgM6xZLvCULtDUAjY1i45,'r',encoding='utf-8') as f:
    books = json.load(f)

samples = []
for i, b in enumerate(books[:20]):
    details = b.get('details')
    found = None
    if isinstance(details, str):
        m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", details)
        if m:
            found = int(m.group(0))
    samples.append({'index': i, 'book_id': b.get('book_id'), 'details_preview': (details[:200] if isinstance(details,str) else None), 'year_found': found})

print('__RESULT__:')
print(json.dumps(samples))"""

env_args = {'var_call_TmxbjPq0NdaugFpHVwIbt13H': ['books_info'], 'var_call_qtfordLX0oPiqP3bTJAZLsTQ': ['review'], 'var_call_uoQBgM6xZLvCULtDUAjY1i45': 'file_storage/call_uoQBgM6xZLvCULtDUAjY1i45.json', 'var_call_3TFu4u2EsLD3NZx9UVOjCJLb': 'file_storage/call_3TFu4u2EsLD3NZx9UVOjCJLb.json', 'var_call_gbfV8WSCwCdXgmhfDxEEK8nr': {'decade': None, 'average_rating': None, 'distinct_books_in_decade_with_ratings': None}, 'var_call_lpBSqG0FRTwOdTlteXvQtyr1': {'stats': {'num_books_rows': 200, 'num_reviews_rows': 1833, 'num_unique_books_in_books': 200, 'num_unique_books_in_reviews': 200, 'num_books_with_year': 0, 'merged_rows': 1833, 'unique_books_in_merged': 200, 'unique_years_in_merged': []}, 'book_year_counts': [], 'decade_groups': []}}

exec(code, env_args)
