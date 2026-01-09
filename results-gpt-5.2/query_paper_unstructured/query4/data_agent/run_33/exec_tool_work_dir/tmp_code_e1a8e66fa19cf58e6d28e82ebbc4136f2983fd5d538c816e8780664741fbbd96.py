code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_R9IgLCM12ettU72Jx9kIe7Oo)
cits = load_maybe_path(var_call_gUBeyYOL6Gmwdwug8MRO0GZQ)

# normalize citations titles
cits_df = pd.DataFrame(cits)
if not cits_df.empty:
    # strip surrounding quotes if present
    cits_df['title'] = cits_df['title'].astype(str).str.strip()
    cits_df['title_norm'] = cits_df['title'].str.replace(r'^"|"$', '', regex=True)
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce').fillna(0).astype(int)


def is_2016(text):
    if not text:
        return False
    if re.search(r'\bCHI\s*2016\b', text):
        return True
    if re.search(r'\bUbiComp\s*2016\b', text, flags=re.I):
        return True
    if re.search(r'\bCSCW\s*2016\b', text):
        return True
    if re.search(r'\bDIS\s*2016\b', text):
        return True
    if re.search(r'\bCopyright\b[^\n]{0,200}\b2016\b', text, flags=re.I):
        return True
    head = text[:2000]
    return bool(re.search(r'\b2016\b', head))


def is_physical_activity_domain(text):
    if not text:
        return False
    t = text.lower()
    if 'physical activity' in t:
        return True
    pa_terms = ['fitness tracker', 'activity tracker', 'step count', 'steps', 'exercise', 'workout', 'gym', 'running', 'walking', 'sedentary']
    score = sum(1 for term in pa_terms if term in t)
    return score >= 2


def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn).strip()

rows=[]
for d in docs:
    title=title_from_filename(d.get('filename',''))
    text=d.get('text','') or ''
    if is_2016(text) and is_physical_activity_domain(text):
        rows.append({'title_norm': title})

pa2016 = pd.DataFrame(rows).drop_duplicates()

if pa2016.empty:
    result=[]
else:
    out = pa2016.merge(cits_df[['title_norm','total_citations','title']], on='title_norm', how='left')
    out['title'] = out['title'].fillna(out['title_norm'])
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out[['title','total_citations']].drop_duplicates().sort_values(['total_citations','title'], ascending=[False, True])
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_R9IgLCM12ettU72Jx9kIe7Oo': 'file_storage/call_R9IgLCM12ettU72Jx9kIe7Oo.json', 'var_call_gUBeyYOL6Gmwdwug8MRO0GZQ': 'file_storage/call_gUBeyYOL6Gmwdwug8MRO0GZQ.json'}

exec(code, env_args)
