code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_R9IgLCM12ettU72Jx9kIe7Oo)
cits = load_maybe_path(var_call_gUBeyYOL6Gmwdwug8MRO0GZQ)

# Heuristic: determine if a paper is 2016 and in physical activity domain by text cues.
# Publication year: look for patterns like '2016' near venue line or copyright.
# Domain: look for 'physical activity' phrase (or related like 'exercise', 'steps', 'fitness tracker') in abstract/keywords.

def is_2016(text):
    # strong signals
    if re.search(r'\bCHI\s*2016\b', text):
        return True
    if re.search(r'\bUbiComp\s*2016\b', text, flags=re.I):
        return True
    if re.search(r'\bCSCW\s*2016\b', text):
        return True
    if re.search(r'\bDIS\s*2016\b', text):
        return True
    if re.search(r'\b2016\b', text) and re.search(r'\bCopyright\b.*\b2016\b', text, flags=re.I|re.S):
        return True
    # avoid false positives with citation years etc by requiring 2016 appears in first 2k chars
    head = text[:2000]
    return bool(re.search(r'\b2016\b', head))

def is_physical_activity_domain(text):
    t = text.lower()
    if 'physical activity' in t:
        return True
    # proxy terms
    pa_terms = ['fitness tracker', 'activity tracker', 'step count', 'steps', 'exercise', 'workout', 'gym', 'running', 'walking', 'sedentary']
    score = sum(1 for term in pa_terms if term in t)
    return score >= 2

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn)

rows=[]
for d in docs:
    fn=d.get('filename','')
    text=d.get('text','') or ''
    title=title_from_filename(fn)
    if is_2016(text) and is_physical_activity_domain(text):
        rows.append({'title': title})

pa2016 = pd.DataFrame(rows).drop_duplicates()

cits_df = pd.DataFrame(cits)
# total_citations may be string
if not cits_df.empty:
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = pa2016.merge(cits_df, on='title', how='left').fillna({'total_citations':0})
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_R9IgLCM12ettU72Jx9kIe7Oo': 'file_storage/call_R9IgLCM12ettU72Jx9kIe7Oo.json', 'var_call_gUBeyYOL6Gmwdwug8MRO0GZQ': 'file_storage/call_gUBeyYOL6Gmwdwug8MRO0GZQ.json'}

exec(code, env_args)
