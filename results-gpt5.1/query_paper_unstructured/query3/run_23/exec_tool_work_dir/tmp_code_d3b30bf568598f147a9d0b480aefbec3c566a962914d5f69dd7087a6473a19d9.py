code = """import re, json, pandas as pd, os, pathlib

# Load full Mongo results
path = var_call_3L41Xwzhponi5EkxqJIaJoRF
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Helper to extract year from text
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text.replace('\n',' ')) if int(y[0]+y[1])>=1900]
    # Above is wrong due to tuple; instead just search directly again

# Simpler: search all 4-digit years and pick plausible publication year near 'CHI' etc.

def guess_year(text):
    years = re.findall(r'(19|20)\d{2}', text)
    years_full = []
    for y in years:
        # y is like '20' or '19' due to grouping; recompute via different regex
        pass

# Let's just use another regex without groups
full_year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

def guess_year2(text):
    yrs = [int(y) for y in full_year_pattern.findall(text)]
    if not yrs:
        return None
    # heuristic: max year <= 2025
    yrs = [y for y in yrs if 1900 <= y <= 2025]
    return max(yrs) if yrs else None

papers = []
for doc in mongo_records:
    text = doc.get('text','')
    year = guess_year2(text)
    # contribution: require 'empirical' substring
    if 'empirical' in text.lower() and year and year > 2016:
        title = os.path.splitext(doc.get('filename',''))[0]
        papers.append({'title': title, 'year': year})

# Load citations aggregate
path2 = var_call_kpXE96xX3DgetaLmUaZDNAAL
with open(path2, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
# ensure numeric
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(papers)

if papers_df.empty:
    result = []
else:
    merged = papers_df.merge(cit_df, how='left', left_on='title', right_on='title')
    merged = merged[['title','total_citations']].fillna(0)
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3L41Xwzhponi5EkxqJIaJoRF': 'file_storage/call_3L41Xwzhponi5EkxqJIaJoRF.json', 'var_call_kpXE96xX3DgetaLmUaZDNAAL': 'file_storage/call_kpXE96xX3DgetaLmUaZDNAAL.json'}

exec(code, env_args)
