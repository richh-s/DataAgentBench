code = """import json, re
import pandas as pd

# Load full Mongo and SQL results
with open(var_call_SYKYxDGuEzyAlNKCQTEOAdDx, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_KDuMcrUXmHujGlHIVRBncISC, 'r') as f:
    sql_records = json.load(f)

# Helper to extract year from text (favor 2010-2025, venue-like context)
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text)]
    # year_pattern with groups -> fix
    years = []
    for m in year_pattern.finditer(text):
        years.append(int(m.group(0)))
    years = [y for y in years if 1990 <= y <= 2025]
    if not years:
        return None
    # Heuristic: max year in doc
    return max(years)

# Filter empirical papers and extract title, year
papers = []
for doc in mongo_records:
    text = doc.get('text','')
    if 'empirical' not in text.lower():
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    filename = doc.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    papers.append({'title': title, 'year': year})

papers_df = pd.DataFrame(papers).drop_duplicates('title')

cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on exact title match
merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')

result = merged[['title','total_citations']].fillna(0).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SYKYxDGuEzyAlNKCQTEOAdDx': 'file_storage/call_SYKYxDGuEzyAlNKCQTEOAdDx.json', 'var_call_KDuMcrUXmHujGlHIVRBncISC': 'file_storage/call_KDuMcrUXmHujGlHIVRBncISC.json'}

exec(code, env_args)
