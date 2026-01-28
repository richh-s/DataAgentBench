code = """import json, re
import pandas as pd

def load_large(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

paper_docs = load_large(var_call_BW98amLhBde79shV1uZfDXuX)
citations = load_large(var_call_2vHF50rivPHk1kUoUp21jfPJ)

# Heuristic extraction from text
# Domain: contains 'physical activity' explicitly
# Year: 2016 must appear as publication year; check common patterns near copyright/venue

def is_2016_pub(text):
    t = text
    # strong signals
    patterns = [
        r'\bCHI\s*2016\b', r'\bUbiComp\s*2016\b', r'\bUbicomp\s*2016\b', r'\bCSCW\s*2016\b', r'\bDIS\s*2016\b',
        r'\bCopyright\s*\u00a9\s*2016\b', r'\b\u00a9\s*2016\b', r'\b2016\s*ACM\b', r'\bProceedings\b.*\b2016\b'
    ]
    for pat in patterns:
        if re.search(pat, t, flags=re.IGNORECASE|re.DOTALL):
            return True
    # fallback: look for standalone 2016 but avoid citations sections by checking first 2 pages (~8000 chars)
    head = t[:8000]
    if re.search(r'\b2016\b', head):
        return True
    return False

rows=[]
for d in paper_docs:
    filename=d.get('filename','')
    title=re.sub(r'\.txt$','',filename)
    text=d.get('text','') or ''
    if 'physical activity' not in text.lower():
        continue
    if not is_2016_pub(text):
        continue
    rows.append({'title': title})

paper_df=pd.DataFrame(rows).drop_duplicates()
cit_df=pd.DataFrame(citations)
# ensure numeric
cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce')

out=paper_df.merge(cit_df, on='title', how='left')
out=out.sort_values(['total_citations','title'], ascending=[False, True])
result=out.fillna({'total_citations':0})[['title','total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BW98amLhBde79shV1uZfDXuX': 'file_storage/call_BW98amLhBde79shV1uZfDXuX.json', 'var_call_2vHF50rivPHk1kUoUp21jfPJ': 'file_storage/call_2vHF50rivPHk1kUoUp21jfPJ.json'}

exec(code, env_args)
