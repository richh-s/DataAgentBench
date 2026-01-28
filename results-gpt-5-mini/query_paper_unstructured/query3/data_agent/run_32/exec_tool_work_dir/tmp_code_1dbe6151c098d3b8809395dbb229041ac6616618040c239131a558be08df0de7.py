code = """import json
import re
import pandas as pd

# Load citations data from storage file
with open(var_call_RKPlcQGZ5hGxOoc2Yw7S4kzh, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Normalize citations to dict: title -> total_citations (int)
cite_dict = {}
for rec in citations:
    title = rec.get('title')
    # citation count may be string; convert safely
    try:
        count = int(rec.get('total_citations'))
    except:
        try:
            count = int(float(rec.get('total_citations')))
        except:
            count = 0
    cite_dict[title] = count

# Load paper documents (result file path)
with open(var_call_WRLteHjxuDrDKTZYVrin676c, 'r', encoding='utf-8') as f:
    papers = json.load(f)

results = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    # title is filename without .txt
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # find first 4-digit year 2000-2029
    years = re.findall(r'(?<!\d)(20\d{2})(?!\d)', text)
    year = None
    if years:
        # choose first occurrence
        try:
            year = int(years[0])
        except:
            year = None
    # contribution: check if 'empirical' appears in text
    is_empirical = 'empirical' in text.lower()
    if year is not None and year > 2016 and is_empirical:
        total_citations = cite_dict.get(title, 0)
        results.append({'title': title, 'total_citations': total_citations})

# Sort results by total_citations desc
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_31TIkziNysar2RCNEzxSAjW8': ['paper_docs'], 'var_call_ncjARgiq7lfYFelROCKOi4NF': ['Citations', 'sqlite_sequence'], 'var_call_WRLteHjxuDrDKTZYVrin676c': 'file_storage/call_WRLteHjxuDrDKTZYVrin676c.json', 'var_call_RKPlcQGZ5hGxOoc2Yw7S4kzh': 'file_storage/call_RKPlcQGZ5hGxOoc2Yw7S4kzh.json'}

exec(code, env_args)
