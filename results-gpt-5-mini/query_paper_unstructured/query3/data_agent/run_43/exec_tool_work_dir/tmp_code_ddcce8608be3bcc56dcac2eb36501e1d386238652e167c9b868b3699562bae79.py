code = """import json
from pathlib import Path

# Load results from previous tool calls
mongo_path = Path(var_call_dGKsopiuB8Ey2Sca842l6wbh)
sql_path = Path(var_call_ACmwFSPbu3xTcJx8EE1LDNo7)

with mongo_path.open('r', encoding='utf-8') as f:
    mongo_records = json.load(f)
with sql_path.open('r', encoding='utf-8') as f:
    sql_records = json.load(f)

# Build citation mapping: title -> total_citations (int)
citation_map = {}
for r in sql_records:
    title = r.get('title')
    # Some citation totals may be strings; convert to int safely
    try:
        total = int(r.get('total_citations', 0))
    except Exception:
        try:
            total = int(float(r.get('total_citations', 0)))
        except Exception:
            total = 0
    citation_map[title] = total

import re

def extract_year(text):
    # search for publication year in range 2017-2026
    m = re.search(r"\b(201[7-9]|202[0-6])\b", text)
    if m:
        return int(m.group(1))
    return None

results = []
for doc in mongo_records:
    filename = doc.get('filename','')
    if not filename:
        continue
    title = filename.rstrip().removesuffix('.txt') if hasattr(str, 'removesuffix') else (filename[:-4] if filename.lower().endswith('.txt') else filename)
    text = doc.get('text','') or ''
    # check for 'empirical' contribution mention
    if not re.search(r'\bempirical\b', text, re.IGNORECASE):
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    # Find citation count from citation_map; try exact match, then try some normalized matches
    cit_count = None
    if title in citation_map:
        cit_count = citation_map[title]
    else:
        # try replacing fancy quotes
        norm_title = title.replace('\u2019', "'").replace('\u201c','"').replace('\u201d','"')
        for k in citation_map.keys():
            if k == norm_title:
                cit_count = citation_map[k]
                break
        if cit_count is None:
            # try case-insensitive match
            for k in citation_map.keys():
                if k.lower() == title.lower():
                    cit_count = citation_map[k]
                    break
    if cit_count is None:
        cit_count = 0
    results.append({'title': title, 'total_citations': cit_count, 'year': year})

# Sort results by total_citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_dGKsopiuB8Ey2Sca842l6wbh': 'file_storage/call_dGKsopiuB8Ey2Sca842l6wbh.json', 'var_call_ACmwFSPbu3xTcJx8EE1LDNo7': 'file_storage/call_ACmwFSPbu3xTcJx8EE1LDNo7.json'}

exec(code, env_args)
