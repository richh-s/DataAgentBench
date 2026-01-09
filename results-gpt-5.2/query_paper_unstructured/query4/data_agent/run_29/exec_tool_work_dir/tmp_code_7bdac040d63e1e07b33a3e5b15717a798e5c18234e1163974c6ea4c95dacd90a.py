code = """import json, re
import pandas as pd

def load_large(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

paper_docs = load_large(var_call_BW98amLhBde79shV1uZfDXuX)
citations = load_large(var_call_2vHF50rivPHk1kUoUp21jfPJ)

# normalize citations records
cit_rows=[]
for r in citations:
    if isinstance(r, dict):
        t = r.get('title') if 'title' in r else r.get('TITLE')
        tc = r.get('total_citations') if 'total_citations' in r else r.get('TOTAL_CITATIONS')
        if t is None:
            continue
        cit_rows.append({'title': t, 'total_citations': tc})

cit_df=pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce')


def is_2016_pub(text):
    patterns = [
        r'\bCHI\s*2016\b', r'\bUbiComp\s*2016\b', r'\bUbicomp\s*2016\b', r'\bCSCW\s*2016\b', r'\bDIS\s*2016\b',
        r'\bCopyright\s*\u00a9\s*2016\b', r'\b\u00a9\s*2016\b', r'\b2016\s*ACM\b', r'\bProceedings\b.*\b2016\b'
    ]
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE|re.DOTALL):
            return True
    head = text[:8000]
    return bool(re.search(r'\b2016\b', head))

paper_titles=set()
for d in paper_docs:
    filename=d.get('filename','') or ''
    title=re.sub(r'\.txt$','',filename)
    text=d.get('text','') or ''
    if 'physical activity' not in text.lower():
        continue
    if not is_2016_pub(text):
        continue
    paper_titles.add(title)

paper_df=pd.DataFrame({'title': sorted(paper_titles)})

out=paper_df.merge(cit_df, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)
out=out.sort_values(['total_citations','title'], ascending=[False, True])
result=out[['title','total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BW98amLhBde79shV1uZfDXuX': 'file_storage/call_BW98amLhBde79shV1uZfDXuX.json', 'var_call_2vHF50rivPHk1kUoUp21jfPJ': 'file_storage/call_2vHF50rivPHk1kUoUp21jfPJ.json'}

exec(code, env_args)
