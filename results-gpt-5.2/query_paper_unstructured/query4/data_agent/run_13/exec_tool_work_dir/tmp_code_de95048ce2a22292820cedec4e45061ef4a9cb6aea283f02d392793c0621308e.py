code = """import json, re
import pandas as pd

path = var_call_UeanCZ2Ph1Wzzih08kqWsV9x
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# citations totals
cpath = var_call_0Mro7YzlxkD4BgEGQLoRp8hz
with open(cpath, 'r', encoding='utf-8') as f:
    cit = json.load(f)
cit_df = pd.DataFrame(cit)
# normalize title
if 'title' not in cit_df.columns:
    # sometimes may be 'TITLE'
    for col in cit_df.columns:
        if col.lower()=='title':
            cit_df = cit_df.rename(columns={col:'title'})
            break
if 'total_citations' not in cit_df.columns:
    for col in cit_df.columns:
        if col.lower()=='total_citations':
            cit_df = cit_df.rename(columns={col:'total_citations'})
            break
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text):
    head = text[:3000]
    if re.search(r'\b2016\b', head):
        return 2016
    if re.search(r"'\s*16\b", head) and re.search(r'\b(chi|ubicomp|cscw|dis|www|iui|ozchi|tei|ah|pervasivehealth)\b', head, flags=re.I):
        return 2016
    m2 = re.search(r'\b(19|20)\d{2}\b', head)
    return int(m2.group(0)) if m2 else None

def is_physical_activity_domain(text):
    head = text[:4000]
    if re.search(r'(?i)domain\s*[:\-]\s*.*physical\s+activity', head):
        return True
    if re.search(r'(?i)author\s+keywords[\s\S]{0,600}physical\s+activity', head):
        return True
    if re.search(r'(?i)physical\s+activity', text):
        return True
    return False

rows=[]
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if not is_physical_activity_domain(text):
        continue
    if extract_year(text)==2016:
        rows.append({'title': title})

paper_df = pd.DataFrame(rows).drop_duplicates()

out = paper_df.merge(cit_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0Mro7YzlxkD4BgEGQLoRp8hz': 'file_storage/call_0Mro7YzlxkD4BgEGQLoRp8hz.json', 'var_call_UeanCZ2Ph1Wzzih08kqWsV9x': 'file_storage/call_UeanCZ2Ph1Wzzih08kqWsV9x.json'}

exec(code, env_args)
