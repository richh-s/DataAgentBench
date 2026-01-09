code = """import json, pandas as pd, re

# Load citations 2020
cit_path = var_call_QwXHnviWGHvxp3BHStJ60P5t
with open(cit_path,'r',encoding='utf-8') as f:
    cit = json.load(f)

# Load paper docs
docs_path = var_call_fAOlzqeTui3L2sEa3xKjtxjh
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

def title_from_filename(fn):
    return re.sub(r'\.txt$','',fn)

def is_chi(text):
    if text is None:
        return False
    t = text.upper()
    # Common CHI header patterns
    return ('CHI \' in t) or ('CHI\u2019' in t) or ('CHI ' in t and 'ACM' in t and 'SIGCHI' in t) or ('PROCEEDINGS OF THE SIGCHI' in t) or ('CHI' in t and 'SIGCHI' in t)

chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = title_from_filename(fn)
    if is_chi(d.get('text','')):
        chi_titles.add(title)

# compute total citations in 2020 for CHI papers
rows = []
for r in cit:
    title = r.get('title')
    if title in chi_titles:
        try:
            cc = int(r.get('citation_count'))
        except Exception:
            cc = None
        rows.append({'title': title, 'citation_count_2020': cc})

# group by title in case duplicates
import pandas as pd
if rows:
    df = pd.DataFrame(rows)
    df = df.groupby('title', as_index=False)['citation_count_2020'].sum().sort_values('citation_count_2020', ascending=False)
    total = int(df['citation_count_2020'].sum())
    out = {
        'total_citations_2020_for_CHI_papers': total,
        'paper_count': int(df.shape[0]),
        'per_paper_citations_2020': df.to_dict(orient='records')
    }
else:
    out = {'total_citations_2020_for_CHI_papers': 0, 'paper_count': 0, 'per_paper_citations_2020': []}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_QwXHnviWGHvxp3BHStJ60P5t': 'file_storage/call_QwXHnviWGHvxp3BHStJ60P5t.json', 'var_call_fAOlzqeTui3L2sEa3xKjtxjh': 'file_storage/call_fAOlzqeTui3L2sEa3xKjtxjh.json'}

exec(code, env_args)
