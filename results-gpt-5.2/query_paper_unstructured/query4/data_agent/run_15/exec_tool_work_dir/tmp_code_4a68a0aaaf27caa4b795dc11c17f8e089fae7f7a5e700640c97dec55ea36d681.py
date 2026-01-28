code = """import json, re
import pandas as pd

def load_mongo_result(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

papers = load_mongo_result(var_call_NB3Maq1dVPeh4msKKn1SEtew)
cits = load_mongo_result(var_call_sbVyc8J6367gQ2BeFEB5P5uJ)

df_p = pd.DataFrame(papers)
df_c = pd.DataFrame(cits)

# Extract year near top of paper text (first 4000 chars)
def extract_year(txt):
    if not isinstance(txt, str):
        return None
    head = txt[:4000]
    # Prefer explicit conference header year like "CHI 2016" or "Ubicomp 2016"
    m = re.search(r'\b(19|20)\d{2}\b', head)
    if m:
        return int(m.group(0))
    return None

def filename_to_title(fn):
    if not isinstance(fn, str):
        return None
    return re.sub(r'\.txt$', '', fn)

# Domain filter: must contain phrase physical activity (already filtered) but ensure not just references
# We'll accept as domain if in title keywords or in author keywords section.

def is_domain_physical_activity(title, txt):
    t = (title or '').lower()
    if 'physical activity' in t:
        return True
    if not isinstance(txt, str):
        return False
    head = txt[:6000].lower()
    # check author keywords block
    if 'author keywords' in head and 'physical activity' in head:
        return True
    # otherwise require multiple mentions in head
    return head.count('physical activity') >= 2

# Build paper metadata
if not df_p.empty:
    df_p['title'] = df_p['filename'].apply(filename_to_title)
    df_p['pub_year'] = df_p['text'].apply(extract_year)
    df_p['is_pa_domain'] = [is_domain_physical_activity(t, x) for t, x in zip(df_p['title'], df_p['text'])]

# Filter papers published in 2016 and physical activity domain
pa2016 = df_p[(df_p['pub_year'] == 2016) & (df_p['is_pa_domain'])][['title']].dropna().drop_duplicates()

# Join to total citations
if df_c.empty or pa2016.empty:
    out = []
else:
    df_c['total_citations'] = pd.to_numeric(df_c['total_citations'])
    merged = pa2016.merge(df_c, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_NB3Maq1dVPeh4msKKn1SEtew': 'file_storage/call_NB3Maq1dVPeh4msKKn1SEtew.json', 'var_call_sbVyc8J6367gQ2BeFEB5P5uJ': 'file_storage/call_sbVyc8J6367gQ2BeFEB5P5uJ.json'}

exec(code, env_args)
