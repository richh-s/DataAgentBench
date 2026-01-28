code = """import json, re
import pandas as pd

cit_path = var_call_hexVleAUQrLdNPBalvXLHSB6
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

paper_path = var_call_uMUqAOMGMjjwTYLrXAwoe2JI
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

def is_acm(text):
    if not text:
        return False
    t = text.lower()
    if re.search(r"\bcopyright\s*\d{4}[^\\n]{0,80}\\bacm\\b", t):
        return True
    if 'acm classification keywords' in t:
        return True
    if re.search(r"\bassociation for computing machinery\b", t):
        return True
    if re.search(r"\bpermissions@acm\\.org\b", t):
        return True
    if re.search(r"\bhttp://dx\\.doi\\.org/10\\.1145/", t):
        return True
    return False

rows = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    rows.append({'title': title, 'is_acm': bool(is_acm(d.get('text','')))})
df_p = pd.DataFrame(rows)

if df_cit.empty:
    out = {'average_citation_count': None, 'n_papers': 0}
else:
    df = df_cit.merge(df_p[df_p['is_acm']], on='title', how='inner')
    avg = float(df['citation_count'].mean()) if len(df) else None
    out = {'average_citation_count': avg, 'n_papers': int(len(df))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hexVleAUQrLdNPBalvXLHSB6': 'file_storage/call_hexVleAUQrLdNPBalvXLHSB6.json', 'var_call_3villHa5jFMJPUNcw9pYaqch': 'file_storage/call_3villHa5jFMJPUNcw9pYaqch.json', 'var_call_uMUqAOMGMjjwTYLrXAwoe2JI': 'file_storage/call_uMUqAOMGMjjwTYLrXAwoe2JI.json'}

exec(code, env_args)
