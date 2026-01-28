code = """import json, re
import pandas as pd

# load citations 2020
path_cit = var_call_quzaY48A3cf5l4WwprqBp1Y0
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# load paper docs
path_docs = var_call_o0stEGZXIlezuSRVYUG0CL8r
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# build title->text map
text_by_title = {}
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text_by_title[title] = d.get('text','') or ''

# heuristics to detect CHI venue
chi_patterns = [r"\bCHI\b", r"\bCHI '\d{2}\b", r"\bCHI \d{4}\b", r"\bProceedings of the SIGCHI\b", r"\bSIGCHI\b"]
chi_re = re.compile('|'.join(chi_patterns), re.IGNORECASE)

rows=[]
for r in cit:
    title = r.get('title')
    if title not in text_by_title:
        continue
    txt = text_by_title[title]
    if not chi_re.search(txt):
        continue
    try:
        cc = int(r.get('citation_count') or 0)
    except:
        cc = 0
    rows.append({'title': title, 'citation_count_2020': cc})

df = pd.DataFrame(rows)
if df.empty:
    out = {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers': 0}
else:
    out = {
        'total_citations_2020_for_CHI_papers': int(df['citation_count_2020'].sum()),
        'num_CHI_papers': int(df['title'].nunique())
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_quzaY48A3cf5l4WwprqBp1Y0': 'file_storage/call_quzaY48A3cf5l4WwprqBp1Y0.json', 'var_call_o0stEGZXIlezuSRVYUG0CL8r': 'file_storage/call_o0stEGZXIlezuSRVYUG0CL8r.json'}

exec(code, env_args)
