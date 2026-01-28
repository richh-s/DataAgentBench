code = """import json
import re

# Load MongoDB result
mongo_var = var_call_iadWh4OB6bg2uiIqVVydcwaq
if isinstance(mongo_var, str):
    with open(mongo_var, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_var

# Load SQL aggregation result
sql_var = var_call_cnOc51KmNvR9wGy5TJ1vqKxt
if isinstance(sql_var, str):
    with open(sql_var, 'r', encoding='utf-8') as f:
        sql_rows = json.load(f)
else:
    sql_rows = sql_var

# Build title -> citations map
title_to_citations = {}
for row in sql_rows:
    t = row.get('title')
    val = row.get('total_citations', 0)
    try:
        c = int(val)
    except:
        try:
            c = int(float(val))
        except:
            c = 0
    title_to_citations[t] = c

# regex to find year 2000-2029
year_re = re.compile(r"\b20[0-2][0-9]\b")

results = []
for doc in mongo_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    if 'empirical' not in text.lower():
        # also allow if title mentions empirical
        if 'empirical' not in title.lower():
            continue
    # extract first year occurrence
    m = year_re.search(text)
    pub_year = None
    if m:
        try:
            pub_year = int(m.group(0))
        except:
            pub_year = None
    if pub_year is None or pub_year <= 2016:
        continue
    # find citation count by matching title
    cit = None
    if title in title_to_citations:
        cit = title_to_citations[title]
    else:
        # normalize function: lower, remove quotes and extra spaces
        def normalize(s):
            if s is None:
                return ''
            s2 = re.sub(r"[\"'\\]+", ' ', s)
            s2 = re.sub(r"\s+", ' ', s2).strip().lower()
            return s2
        ntitle = normalize(title)
        for t,c in title_to_citations.items():
            if normalize(t) == ntitle:
                cit = c
                break
    if cit is None:
        continue
    results.append({'title': title, 'total_citations': cit, 'year': pub_year})

# sort by citations desc
results.sort(key=lambda x: x['total_citations'], reverse=True)
final = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_iadWh4OB6bg2uiIqVVydcwaq': 'file_storage/call_iadWh4OB6bg2uiIqVVydcwaq.json', 'var_call_cnOc51KmNvR9wGy5TJ1vqKxt': 'file_storage/call_cnOc51KmNvR9wGy5TJ1vqKxt.json'}

exec(code, env_args)
