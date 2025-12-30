code = """import re, json, pandas as pd

# Load full mongo and citations results
with open(var_call_olLcGzpHLt5tCj2TGPDJyEMn, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_NdiSsuuSfkiGchj4B88O5KCF, 'r') as f:
    citation_records = json.load(f)

# Extract approximate publication year from text by searching for conference lines like 'CHI 2018' or any 20xx near 'CHI' etc.
conf_pattern = re.compile(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\D{0,20}?((19|20)\d{2})', re.IGNORECASE)

def infer_year(text):
    m = conf_pattern.search(text)
    if m:
        return int(m.group(2))
    # fallback: search any year 2000-2025 and take the max
    years = re.findall(r'(19|20)\d{2}', text)
    cand = []
    for y in years:
        if isinstance(y, tuple):
            y = ''.join(y)
        cand.append(int(y))
    cand = [y for y in cand if 1990 <= y <= 2025]
    return max(cand) if cand else None

# Build dataframe of papers with contribution 'empirical' (substring match in text) and year>2016
rows = []
for doc in mongo_records:
    text = doc.get('text','')
    if 'empirical' not in text.lower():
        continue
    year = infer_year(text)
    if year is None or year <= 2016:
        continue
    filename = doc.get('filename','')
    title = filename.replace('.txt','')
    rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Citations dataframe
cit_df = pd.DataFrame(citation_records)
# total_citations already aggregated and may be strings
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title (exact match)
merged = pd.merge(papers_df, cit_df, on='title', how='inner')

result = merged[['title','total_citations']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_olLcGzpHLt5tCj2TGPDJyEMn': 'file_storage/call_olLcGzpHLt5tCj2TGPDJyEMn.json', 'var_call_NdiSsuuSfkiGchj4B88O5KCF': 'file_storage/call_NdiSsuuSfkiGchj4B88O5KCF.json'}

exec(code, env_args)
