code = """import re, json, pandas as pd, os, textwrap

# Load full mongo and sql results
mongo_path = var_call_JrvCkgZlVyQIh8mF21biU9gs
sql_path = var_call_ju9InGP20lZd1uAjGF4LYxx9

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

# Heuristic extract year, contribution from text
empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # contribution: require word empirical
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        # year: look for CHI 2018, 2019, 2020... or standalone 2017+
        years = re.findall(r'(20[1-9][0-9])', text)
        year = None
        if years:
            # choose smallest plausible publication year >=2017
            cand = sorted(int(y) for y in years)
            for y in cand:
                if y >= 2017:
                    year = y
                    break
        # Default skip if no year
        if year is None or year <= 2016:
            continue
        title = (doc.get('filename') or '').replace('.txt','')
        if not title:
            continue
        empirical_papers.append({'title': title, 'year': year})

# Join with citation totals
emp_df = pd.DataFrame(empirical_papers).drop_duplicates(subset=['title'])
cit_df = pd.DataFrame(sql_records)
# citation totals come as strings; convert
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, how='left', on='title')
merged = merged[['title','total_citations','year']].sort_values(['year','title'])

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JrvCkgZlVyQIh8mF21biU9gs': 'file_storage/call_JrvCkgZlVyQIh8mF21biU9gs.json', 'var_call_ju9InGP20lZd1uAjGF4LYxx9': 'file_storage/call_ju9InGP20lZd1uAjGF4LYxx9.json'}

exec(code, env_args)
