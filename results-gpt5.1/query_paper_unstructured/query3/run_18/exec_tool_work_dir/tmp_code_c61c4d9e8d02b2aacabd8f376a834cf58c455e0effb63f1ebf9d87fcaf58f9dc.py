code = """import re, json, pandas as pd
from datetime import datetime

# Load mongo results (may be file path or list)
raw_docs = var_call_Lkx1K3SO9WRqH6s4cC9G785b
if isinstance(raw_docs, str):
    import pathlib, json as _json
    with open(raw_docs, 'r') as f:
        docs = _json.load(f)
else:
    docs = raw_docs

# Extract title (from filename) and year (regex for 20xx or 19xx near conference header)
records = []
for d in docs:
    text = d.get('text','') or ''
    fn = d.get('filename','') or ''
    title = re.sub(r"\.txt$","", fn)
    # simple heuristic: find a year like 2017,2018,... and take earliest >=2000
    years = sorted({int(y) for y in re.findall(r"(19|20)\d{2}", text) if int(''.join(y))>=2000})
    # Oops previous regex wrong; redo
    years = re.findall(r"(19|20)\d{2}", text)
    years = [int(y) for y in re.findall(r"(19|20)\d{2}", text)]
    pub_year = None
    for y in years:
        if 2000 <= y <= datetime.now().year:
            pub_year = y
            break
    # very rough contribution detection
    contrib = 'empirical' if re.search(r"empirical", text, re.I) else ''
    records.append({"title": title, "year": pub_year, "contribution": contrib})

papers_df = pd.DataFrame(records)
empirical_recent = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)]

# Load citations aggregate
raw_cit = var_call_INb6WOfkDtp39uPDqiqO7ipd
if isinstance(raw_cit, str):
    import json as _json
    with open(raw_cit,'r') as f:
        cits = _json.load(f)
else:
    cits = raw_cit

cit_df = pd.DataFrame(cits)
# ensure numeric
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'])

merged = empirical_recent.merge(cit_df, on='title', how='inner')[['title','total_citations']]
result = merged.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Lkx1K3SO9WRqH6s4cC9G785b': 'file_storage/call_Lkx1K3SO9WRqH6s4cC9G785b.json', 'var_call_INb6WOfkDtp39uPDqiqO7ipd': 'file_storage/call_INb6WOfkDtp39uPDqiqO7ipd.json'}

exec(code, env_args)
