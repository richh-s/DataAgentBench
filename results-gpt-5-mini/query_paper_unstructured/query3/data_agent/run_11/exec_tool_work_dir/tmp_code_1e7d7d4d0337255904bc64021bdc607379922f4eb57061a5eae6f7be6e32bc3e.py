code = """import json
import re
import pandas as pd

# Load the large results from storage paths
with open(var_call_RE3PGT65xTQsAn7GcygbjMf6, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_VAJNrOiXN20qQMGilBqC0LiE, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a mapping from title to total citations (int)
cite_map = {}
for rec in citations:
    title = rec.get('title')
    tc = rec.get('total_citations')
    try:
        cite_map[title] = int(tc)
    except:
        # if it's already int or cannot parse, handle
        try:
            cite_map[title] = int(float(tc))
        except:
            cite_map[title] = None

results = []

year_pattern = re.compile(r'20\d{2}|19\d{2}')
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # try to find year in the first 600 chars first
    head = text[:1000]
    years = year_pattern.findall(head)
    year = None
    if years:
        # pick the first plausible year between 1990 and 2025
        for y in years:
            yi = int(y)
            if 1990 <= yi <= 2025:
                year = yi
                break
    if year is None:
        # search whole text
        years = year_pattern.findall(text)
        for y in years:
            yi = int(y)
            if 1990 <= yi <= 2025:
                year = yi
                break
    # contribution: check for substring 'empirical' in text (case-insensitive)
    contribution = 'empirical' if 'empirical' in text.lower() else None

    if contribution == 'empirical' and year is not None and year > 2016:
        total_citations = cite_map.get(title)
        # If no citation found, set to 0
        if total_citations is None:
            total_citations = 0
        results.append({'title': title, 'total_citations': total_citations, 'year': year})

# Sort results by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Prepare final list only with title and total citation
final = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

import json as _json
print("__RESULT__:")
print(_json.dumps(final))"""

env_args = {'var_call_J2RaiNlML0Ky5bdrg7xABZA9': ['paper_docs'], 'var_call_RE3PGT65xTQsAn7GcygbjMf6': 'file_storage/call_RE3PGT65xTQsAn7GcygbjMf6.json', 'var_call_VAJNrOiXN20qQMGilBqC0LiE': 'file_storage/call_VAJNrOiXN20qQMGilBqC0LiE.json'}

exec(code, env_args)
