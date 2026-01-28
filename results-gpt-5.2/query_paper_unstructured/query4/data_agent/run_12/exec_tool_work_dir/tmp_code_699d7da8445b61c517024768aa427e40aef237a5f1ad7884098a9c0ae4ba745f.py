code = """import json, re, pandas as pd

# Load mongo docs (may be in json file)
md = var_call_TJkO9itkC9Ak6vcZP4gbWNeT
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_6u07yNCzhiqU7qcwaJYqjAAC
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

def extract_year(text: str):
    # look for patterns like 2016 or '16 in venue line
    m = re.search(r'\b(19|20)\d{2}\b', text)
    if not m:
        return None
    # prefer earliest plausible year in header within first 2000 chars
    head = text[:2000]
    yrs = re.findall(r'\b(19|20)\d{2}\b', head)
    # re.findall with group returns '19'/'20'; redo properly
    yrs = re.findall(r'\b((?:19|20)\d{2})\b', head)
    if yrs:
        # choose first occurrence
        return int(yrs[0])
    return int(m.group(0))

rows=[]
for d in md:
    title = re.sub(r'\.txt$','', d.get('filename',''))
    text = d.get('text','') or ''
    year = extract_year(text)
    # domain: require explicit keyword as domain indicator (Author Keywords etc). But already matched physical activity in text.
    rows.append({'title': title, 'pub_year': year})

df_docs = pd.DataFrame(rows).dropna(subset=['pub_year'])
df_docs = df_docs[df_docs['pub_year']==2016]

# citations totals
cdf = pd.DataFrame(cit)
# total_citations may be str
cdf['total_citations'] = pd.to_numeric(cdf['total_citations'], errors='coerce')

out = df_docs.merge(cdf, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TJkO9itkC9Ak6vcZP4gbWNeT': 'file_storage/call_TJkO9itkC9Ak6vcZP4gbWNeT.json', 'var_call_6u07yNCzhiqU7qcwaJYqjAAC': 'file_storage/call_6u07yNCzhiqU7qcwaJYqjAAC.json'}

exec(code, env_args)
