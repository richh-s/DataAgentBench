code = """import json
import re
import pandas as pd

# Load the full query results from storage file paths
with open(var_call_616mkaFHuQZqEBFT88jXpXxA, 'r', encoding='utf-8') as f:
    papers = json.load(f)

with open(var_call_xwqLOf4jXrwb4YAVfkQY8dXS, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a citations mapping
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # citation totals may be strings; convert to int when possible
    try:
        total = int(rec.get('total_citations'))
    except Exception:
        try:
            total = int(float(rec.get('total_citations')))
        except Exception:
            total = 0
    cit_map[title] = total

# Process papers to extract title, year, and whether empirical
results = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = doc.get('text', '') or ''
    # Find first plausible year between 1990 and 2026 in the first 1000 chars
    head = text[:2000]
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', head)
    year = None
    for y in years:
        yi = int(y)
        if 1990 <= yi <= 2026:
            year = yi
            break
    # Check for the word 'empirical' anywhere in the document
    empirical = bool(re.search(r'\bempirical\b', text, flags=re.I))
    if year is not None and year > 2016 and empirical:
        total_citations = cit_map.get(title, 0)
        results.append({
            'title': title,
            'total_citations': total_citations,
            'year': year
        })

# Sort results by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Reduce to required output: title and total citation count
out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

import json as _json
print("__RESULT__:")
print(_json.dumps(out))"""

env_args = {'var_call_Ysschk5zy47u6A8ni2l60zhn': ['paper_docs'], 'var_call_616mkaFHuQZqEBFT88jXpXxA': 'file_storage/call_616mkaFHuQZqEBFT88jXpXxA.json', 'var_call_TB8VVDY8ebHM0T2kws4yweeX': ['Citations', 'sqlite_sequence'], 'var_call_xwqLOf4jXrwb4YAVfkQY8dXS': 'file_storage/call_xwqLOf4jXrwb4YAVfkQY8dXS.json'}

exec(code, env_args)
