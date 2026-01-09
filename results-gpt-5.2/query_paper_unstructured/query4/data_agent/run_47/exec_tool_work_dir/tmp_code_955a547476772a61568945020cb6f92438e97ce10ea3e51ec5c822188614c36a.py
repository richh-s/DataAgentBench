code = """import json, re
import pandas as pd

# load mongo docs
path_docs = var_call_EdI5tfxdG7NthR2A0PqHgMLO
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load citations
path_cit = var_call_saVRj1ZwzmtyAiRdfptdqatS
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

# parse year from text (look for Copyright YYYY or CHI '16 etc)

def extract_year(text):
    # prioritize explicit copyright year
    m = re.search(r'Copyright\s+(?:\(c\)\s*)?(\d{4})', text, re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    # ACM proceedings style: "CHI '16" etc
    m = re.search(r"\b[A-Z]{2,}\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    # fallback any 4-digit year near top
    head = text[:2000]
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', head)]
    years = [y for y in years if 1980 <= y <= 2030]
    return years[0] if years else None

rows = []
for d in docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text') or ''
    year = extract_year(text)
    # domain detection via keyword
    dom = bool(re.search(r'physical\s+activity', text, re.IGNORECASE))
    rows.append({'title': title, 'year': year, 'is_physical_activity': dom})

pdf = pd.DataFrame(rows)
# strict domain match: contains physical activity; strict year = 2016
pdf = pdf[(pdf['year']==2016) & (pdf['is_physical_activity'])]

cdf = pd.DataFrame(cits)
# normalize numeric
cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

# total citation count across all citation years
agg = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = pd.merge(pdf[['title']].drop_duplicates(), agg, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EdI5tfxdG7NthR2A0PqHgMLO': 'file_storage/call_EdI5tfxdG7NthR2A0PqHgMLO.json', 'var_call_saVRj1ZwzmtyAiRdfptdqatS': 'file_storage/call_saVRj1ZwzmtyAiRdfptdqatS.json'}

exec(code, env_args)
