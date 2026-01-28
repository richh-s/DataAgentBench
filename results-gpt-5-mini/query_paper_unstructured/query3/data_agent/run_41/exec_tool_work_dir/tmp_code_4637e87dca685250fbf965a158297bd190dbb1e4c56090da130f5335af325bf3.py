code = """import json

# Access stored tool results
mongo_var = var_call_iadWh4OB6bg2uiIqVVydcwaq
sql_var = var_call_cnOc51KmNvR9wGy5TJ1vqKxt

# Load JSON files if variables are file paths
if isinstance(mongo_var, str):
    with open(mongo_var, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_var

if isinstance(sql_var, str):
    with open(sql_var, 'r', encoding='utf-8') as f:
        sql_rows = json.load(f)
else:
    sql_rows = sql_var

# Build mapping from title to total citations
title_to_citations = {}
for row in sql_rows:
    title = row.get('title')
    total = row.get('total_citations', 0)
    try:
        total_int = int(total)
    except Exception:
        try:
            total_int = int(float(total))
        except Exception:
            total_int = 0
    title_to_citations[title] = total_int

# Years to consider (after 2016)
years = [str(y) for y in range(2017, 2030)]

results = []
for doc in mongo_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check for empirical mention
    if 'empirical' not in text.lower() and 'empirical' not in title.lower():
        continue
    # check publication year occurrence
    pub_year = None
    for y in years:
        if y in text:
            pub_year = int(y)
            break
    if pub_year is None or pub_year <= 2016:
        continue
    # find citation count by exact title match or case-insensitive match
    cit = None
    if title in title_to_citations:
        cit = title_to_citations[title]
    else:
        t_low = title.lower().strip()
        for t, c in title_to_citations.items():
            if t is None:
                continue
            if t.lower().strip() == t_low:
                cit = c
                break
    if cit is None:
        continue
    results.append({'title': title, 'total_citations': cit})

# sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_iadWh4OB6bg2uiIqVVydcwaq': 'file_storage/call_iadWh4OB6bg2uiIqVVydcwaq.json', 'var_call_cnOc51KmNvR9wGy5TJ1vqKxt': 'file_storage/call_cnOc51KmNvR9wGy5TJ1vqKxt.json'}

exec(code, env_args)
