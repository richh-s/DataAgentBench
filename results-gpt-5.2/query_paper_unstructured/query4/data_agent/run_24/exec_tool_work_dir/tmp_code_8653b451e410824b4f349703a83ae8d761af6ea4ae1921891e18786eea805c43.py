code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_ZjAkTSdwoqJbLuHfgc7bUzpj)
docs = load_records(var_call_zxmP2N1ythXvq4sZsdHCsF1q)

cit_df = pd.DataFrame(cit)
# normalize types
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Build doc df with extracted title from filename
rows = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$', '', fn)
    text = d.get('text','') or ''
    rows.append({'title': title, 'text': text})
doc_df = pd.DataFrame(rows)

# heuristics to extract year and domain
# year: look for 2016 as publication year; try to detect a 4-digit year near venue lines; simplest: if contains 2016 and not only in references? We'll take first occurrence of 20xx in first 2000 chars.

def extract_year(t):
    head = t[:3000]
    m = re.search(r'\b(20\d{2})\b', head)
    return int(m.group(1)) if m else None


def is_physical_activity(t):
    return re.search(r'physical\s+activity', t, flags=re.IGNORECASE) is not None


doc_df['year'] = doc_df['text'].apply(extract_year)
doc_df['is_physical_activity'] = doc_df['text'].apply(is_physical_activity)

filtered = doc_df[(doc_df['year']==2016) & (doc_df['is_physical_activity'])][['title']]

out = filtered.merge(cit_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True]).reset_index(drop=True)
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZjAkTSdwoqJbLuHfgc7bUzpj': 'file_storage/call_ZjAkTSdwoqJbLuHfgc7bUzpj.json', 'var_call_zxmP2N1ythXvq4sZsdHCsF1q': 'file_storage/call_zxmP2N1ythXvq4sZsdHCsF1q.json'}

exec(code, env_args)
