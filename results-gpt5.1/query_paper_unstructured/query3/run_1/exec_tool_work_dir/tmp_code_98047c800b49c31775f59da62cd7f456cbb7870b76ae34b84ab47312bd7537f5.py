code = """import re, json, pandas as pd, os, io

# Load full mongo results
path = var_call_eX83EPONFDTakEldebA9Un53
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract year and contribution heuristically, and title from filename
empirical_papers = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    # title from filename
    title = re.sub(r'\.txt$', '', filename)
    # year: search for 19xx or 20xx, take first >= 2017
    years = re.findall(r'(19|20)\d{2}', text)
    pub_year = None
    for y in years:
        y_full = int(''.join(y)) if isinstance(y, tuple) else int(y)
        if y_full >= 2010:  # only consider recent years to avoid references
            pub_year = y_full
            break
    if pub_year is None:
        continue
    # contribution: check if 'empirical' appears near 'contribution' or 'paper makes an empirical'
    if re.search(r'empirical', text, re.IGNORECASE):
        # more specific heuristics could be added, but we already filtered by regex in Mongo
        contribution = 'empirical'
    else:
        continue
    if pub_year > 2016:
        empirical_papers.append({'title': title, 'year': pub_year})

# Load citation sums
path2 = var_call_CR1mHBu9DGedAI3AHqWo2YQt
with open(path2, 'r') as f:
    citation_records = json.load(f)

cit_df = pd.DataFrame(citation_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

emp_df = pd.DataFrame(empirical_papers)

if emp_df.empty:
    result = []
else:
    merged = emp_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title', 'total_citations']].fillna(0)
    result = merged.to_dict(orient='records')

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_eX83EPONFDTakEldebA9Un53': 'file_storage/call_eX83EPONFDTakEldebA9Un53.json', 'var_call_CR1mHBu9DGedAI3AHqWo2YQt': 'file_storage/call_CR1mHBu9DGedAI3AHqWo2YQt.json'}

exec(code, env_args)
