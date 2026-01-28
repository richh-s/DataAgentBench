code = """import json

# Load variables from storage
mongo_var = var_call_iadWh4OB6bg2uiIqVVydcwaq
sql_var = var_call_cnOc51KmNvR9wGy5TJ1vqKxt

# Load JSON if they are file paths
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

# Build mapping title -> total_citations
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

# years after 2016 to consider
years_list = [str(y) for y in range(2017, 2030)]

results = []
for doc in mongo_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check empirical in text or title
    if 'empirical' not in text.lower() and 'empirical' not in title.lower():
        continue
    # find any year occurrence from years_list
    pub_year = None
    for y in years_list:
        if y in text:
            try:
                pub_year = int(y)
                break
            except:
                pub_year = None
    if pub_year is None or pub_year <= 2016:
        continue
    # find citation count by exact match or normalized match
    cit = None
    if title in title_to_citations:
        cit = title_to_citations[title]
    else:
        def normalize(s):
            if s is None:
                return ''
            s2 = s.replace('\"', ' ').replace('\'', ' ')
            s2 = s2.replace('\\', ' ')
            s2 = ' '.join(s2.split()).lower()
            return s2
        ntitle = normalize(title)
        for t, c in title_to_citations.items():
            if normalize(t) == ntitle:
                cit = c
                break
    if cit is None:
        continue
    results.append({'title': title, 'total_citations': cit, 'year': pub_year})

# sort by citation desc
results.sort(key=lambda x: x['total_citations'], reverse=True)
final = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_iadWh4OB6bg2uiIqVVydcwaq': 'file_storage/call_iadWh4OB6bg2uiIqVVydcwaq.json', 'var_call_cnOc51KmNvR9wGy5TJ1vqKxt': 'file_storage/call_cnOc51KmNvR9wGy5TJ1vqKxt.json'}

exec(code, env_args)
