code = """import json, re, pandas as pd
import os

path = var_call_XmGrPfgZs7xQP3tCEsxhtYxP
with open(path, 'r') as f:
    books = json.load(f)

rows = []
for b in books:
    d = b.get('details') or ''
    # look for patterns like 'on Month DD, YYYY' or 'on Month YYYY' or 'on YYYY'
    m = re.search(r'on\s+([A-Za-z]+\s+\d{1,2},\s+\d{4}|[A-Za-z]+\s+\d{4}|\d{4})', d)
    year = None
    if m:
        part = m.group(1)
        ym = re.search(r'(\d{4})', part)
        if ym:
            year = int(ym.group(1))
    if year:
        decade = int(year // 10 * 10)
    else:
        decade = None
    rows.append({'book_id': b.get('book_id'), 'year': year, 'decade': decade})

df = pd.DataFrame(rows)
result = df.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_XmGrPfgZs7xQP3tCEsxhtYxP': 'file_storage/call_XmGrPfgZs7xQP3tCEsxhtYxP.json', 'var_call_Q33oo2x09EwxgliChtHzRuEp': ['books_info'], 'var_call_3EzG2U5B7dNHHDgjq1coF5Yo': ['review'], 'var_call_84741IAQnDTggqEcb887lfDm': 'file_storage/call_84741IAQnDTggqEcb887lfDm.json'}

exec(code, env_args)
