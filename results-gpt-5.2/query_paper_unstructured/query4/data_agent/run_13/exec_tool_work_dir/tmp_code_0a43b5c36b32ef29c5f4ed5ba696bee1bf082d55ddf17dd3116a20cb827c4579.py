code = """import json, re
import pandas as pd

# Load Mongo paper docs
path = var_call_UeanCZ2Ph1Wzzih08kqWsV9x
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_year(text):
    # Prefer explicit year near venue lines or copyright
    m = re.search(r'\b(19|20)\d{2}\b', text)
    # but better: search for 2016 specifically in first 2000 chars
    head = text[:3000]
    m2016 = re.search(r'\b2016\b', head)
    if m2016:
        return 2016
    # look for pattern like CHI '16
    if re.search(r"'\s*16\b", head) and re.search(r'\b(chi|ubicomp|cscw|dis|www|iui|ozchi|tei|ah)\b', head, flags=re.I):
        return 2016
    # fallback: first year in head
    m2 = re.search(r'\b(19|20)\d{2}\b', head)
    if m2:
        return int(m2.group(0))
    if m:
        return int(m.group(0))
    return None

def is_physical_activity_domain(text):
    # Use heuristic: contains 'Domain' line OR keyword occurrences
    head = text[:4000]
    if re.search(r'(?i)domain\s*[:\-]\s*.*physical\s+activity', head):
        return True
    # also accept if keywords / author keywords include physical activity
    if re.search(r'(?i)author\s+keywords[\s\S]{0,500}physical\s+activity', head):
        return True
    # fallback keyword anywhere
    if re.search(r'(?i)physical\s+activity', text):
        return True
    return False

rows=[]
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if not is_physical_activity_domain(text):
        continue
    year = extract_year(text)
    if year == 2016:
        rows.append({'title': title})

paper_df = pd.DataFrame(rows).drop_duplicates()

# Load citations totals
cpath = var_call_0Mro7YzlxkD4BgEGQLoRp8hz
with open(cpath, 'r', encoding='utf-8') as f:
    cit = json.load(f)
cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = paper_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0Mro7YzlxkD4BgEGQLoRp8hz': 'file_storage/call_0Mro7YzlxkD4BgEGQLoRp8hz.json', 'var_call_UeanCZ2Ph1Wzzih08kqWsV9x': 'file_storage/call_UeanCZ2Ph1Wzzih08kqWsV9x.json'}

exec(code, env_args)
