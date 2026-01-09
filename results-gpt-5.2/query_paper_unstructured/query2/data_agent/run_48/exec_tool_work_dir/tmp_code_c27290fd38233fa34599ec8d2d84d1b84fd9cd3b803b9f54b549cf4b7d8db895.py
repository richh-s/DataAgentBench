code = """import json, re
import pandas as pd

def load_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cit = load_maybe_path(var_call_XrfRt9qgt0V43jXN4poJuERt)
docs = load_maybe_path(var_call_QwjlxW7DiIdqVAVFxRGbn9z8)

cit_df = pd.DataFrame(cit)
if cit_df.empty:
    avg = None
else:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# Build set of ACM titles by scanning docs text
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$', '', fn).strip()
    text = d.get('text','') or ''
    if re.search(r'\bCopyright\s*\d{4}\s*©\s*ACM\b', text) or re.search(r'\bACM\b', text) and re.search(r'\bpermissions@acm\.org\b', text):
        acm_titles.add(title)

# Join
if not cit_df.empty:
    merged = cit_df[cit_df['title'].isin(acm_titles)].copy()
    avg = float(merged['citation_count'].mean()) if not merged.empty else None
    n = int(merged.shape[0])
else:
    avg = None
    n = 0

out = {'average_citation_count_2018_acm_papers': avg, 'num_papers': n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XrfRt9qgt0V43jXN4poJuERt': 'file_storage/call_XrfRt9qgt0V43jXN4poJuERt.json', 'var_call_QwjlxW7DiIdqVAVFxRGbn9z8': 'file_storage/call_QwjlxW7DiIdqVAVFxRGbn9z8.json'}

exec(code, env_args)
