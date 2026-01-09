code = """import json, re
import pandas as pd

# Load mongo docs
mongo_src = var_call_9UaSCGBA7BBYoJxhYGrpUJej
if isinstance(mongo_src, str) and mongo_src.endswith('.json'):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = mongo_src

# Load citations
cit_src = var_call_9eUXFR6bXtdUjhpwhcGGHd4N
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_src

# helper to extract pub year from text
year_patterns = [
    re.compile(r'\b(19|20)\d{2}\b')
]

def extract_pub_year(text):
    # prioritize copyright year
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(\d{4})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'\b(19|20)\d{2}\b', text)
    if m:
        return int(m.group(0))
    return None

# Determine physical activity domain: if explicit keyword appears

def is_physical_activity_domain(text, title):
    t = (text or '').lower()
    # look for common domain tags in Author Keywords or elsewhere
    if 'physical activity' in t:
        return True
    # include activity tracker phrasing
    if 'activity tracking' in t or 'activity tracker' in t:
        return True
    return False

records = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_pub_year(text)
    if year == 2016 and is_physical_activity_domain(text, title):
        records.append({'title': title})

pa2016_titles = sorted(set(r['title'] for r in records))

# citations sum per title (all years)
df_c = pd.DataFrame(cits)
if not df_c.empty:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)
    df_sum = df_c.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    df_sum = pd.DataFrame(columns=['title','total_citations'])

out_df = pd.DataFrame({'title': pa2016_titles})
out_df = out_df.merge(df_sum, on='title', how='left')
out_df['total_citations'] = out_df['total_citations'].fillna(0).astype(int)
out_df = out_df.sort_values(['total_citations','title'], ascending=[False, True])

result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_9UaSCGBA7BBYoJxhYGrpUJej': 'file_storage/call_9UaSCGBA7BBYoJxhYGrpUJej.json', 'var_call_9eUXFR6bXtdUjhpwhcGGHd4N': 'file_storage/call_9eUXFR6bXtdUjhpwhcGGHd4N.json'}

exec(code, env_args)
