code = """import json
import re

# Load MongoDB result
data_mongo = var_call_iadWh4OB6bg2uiIqVVydcwaq
if isinstance(data_mongo, str):
    with open(data_mongo, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = data_mongo

# Load SQL aggregation result
data_sql = var_call_cnOc51KmNvR9wGy5TJ1vq
if isinstance(data_sql, str):
    with open(data_sql, 'r', encoding='utf-8') as f:
        sql_rows = json.load(f)
else:
    sql_rows = data_sql

# Build a mapping from title to total_citations (int)
title_to_citations = {}
for r in sql_rows:
    t = r.get('title')
    # some totals may be strings; convert
    try:
        c = int(r.get('total_citations') if r.get('total_citations') is not None else 0)
    except:
        try:
            c = int(float(r.get('total_citations')))
        except:
            c = 0
    title_to_citations[t] = c

# Helper to extract year from text: find first 4-digit year between 2000 and 2029
year_re = re.compile(r"\b(20(?:0[0-9]|1[0-9]|2[0-9]))\b")

results = []
for doc in mongo_docs:
    filename = doc.get('filename','')
    text = doc.get('text','')
    if not filename:
        continue
    # title is filename without .txt
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check contains 'empirical' (case-insensitive) in text
    if re.search(r'\bempirical\b', text, flags=re.IGNORECASE) is None and re.search(r'\bempiric(al)?\b', title, flags=re.IGNORECASE) is None:
        # skip if no empirical mention
        continue
    # extract year
    year_match = year_re.search(text)
    pub_year = None
    if year_match:
        try:
            pub_year = int(year_match.group(1))
        except:
            pub_year = None
    # filter published after 2016
    if pub_year is None or pub_year <= 2016:
        continue
    # find citation count
    # Titles in SQL may include exact title; try exact match, then try variants
    cit = None
    if title in title_to_citations:
        cit = title_to_citations[title]
    else:
        # try to find SQL title equal ignoring quotes and whitespace
        def normalize(s):
            return re.sub(r"[\"'\\s]+"," ", s).strip().lower()
        ntitle = normalize(title)
        for t,c in title_to_citations.items():
            if normalize(t) == ntitle:
                cit = c
                break
    if cit is None:
        # skip if no citation data
        continue
    results.append({"title": title, "total_citations": cit, "year": pub_year})

# Sort results by total_citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare final output: title and total citation count
final = [{"title": r['title'], "total_citations": r['total_citations']} for r in results]

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_iadWh4OB6bg2uiIqVVydcwaq': 'file_storage/call_iadWh4OB6bg2uiIqVVydcwaq.json', 'var_call_cnOc51KmNvR9wGy5TJ1vqKxt': 'file_storage/call_cnOc51KmNvR9wGy5TJ1vqKxt.json'}

exec(code, env_args)
