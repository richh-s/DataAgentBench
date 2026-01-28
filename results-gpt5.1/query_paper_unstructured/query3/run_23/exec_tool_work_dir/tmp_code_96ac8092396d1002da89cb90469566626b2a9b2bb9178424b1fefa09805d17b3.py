code = """import re, json, pandas as pd, os

# Load full Mongo results
path = var_call_3L41Xwzhponi5EkxqJIaJoRF
with open(path, 'r') as f:
    mongo_records = json.load(f)

full_year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

def guess_year(text):
    yrs = [int(y) for y in full_year_pattern.findall(text)]
    if not yrs:
        return None
    yrs = [y for y in yrs if 1900 <= y <= 2025]
    return max(yrs) if yrs else None

papers = []
for doc in mongo_records:
    text = doc.get('text', '')
    year = guess_year(text)
    if 'empirical' in text.lower() and year and year > 2016:
        title = os.path.splitext(doc.get('filename', ''))[0]
        papers.append({'title': title, 'year': year})

# Load citations aggregate
path2 = var_call_kpXE96xX3DgetaLmUaZDNAAL
with open(path2, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(papers)

if papers_df.empty:
    result = []
else:
    merged = papers_df.merge(cit_df, how='left', on='title')
    merged = merged[['title', 'total_citations']].fillna(0)
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3L41Xwzhponi5EkxqJIaJoRF': 'file_storage/call_3L41Xwzhponi5EkxqJIaJoRF.json', 'var_call_kpXE96xX3DgetaLmUaZDNAAL': 'file_storage/call_kpXE96xX3DgetaLmUaZDNAAL.json'}

exec(code, env_args)
