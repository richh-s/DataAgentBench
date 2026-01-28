code = """import json, re
import pandas as pd

cit_path = var_call_zqbhld7KWH0SyWZClF94YQSM
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

paper_path = var_call_QjNkS9jNg19inwvCAipHBOQF
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

def is_chi(text):
    if not text:
        return False
    t = text.upper()
    # CHI 'YY, CHI YY, CHI CONFERENCE, PROCEEDINGS OF THE CHI
    if re.search(r"\bCHI\s*['’]?\s*\d{2}\b", t):
        return True
    if re.search(r"\bCHI\s+CONFERENCE\b", t):
        return True
    if re.search(r"\bPROCEEDINGS\s+OF\s+THE\s+CHI\b", t):
        return True
    return False

chi_titles = set()
for d in papers:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_chi(d.get('text','')):
        chi_titles.add(title)

if df_cit.empty:
    total = 0
    n_cited = 0
else:
    mask = df_cit['title'].isin(chi_titles)
    total = int(df_cit.loc[mask, 'citation_count'].sum())
    n_cited = int(mask.sum())

out = json.dumps({"total_citations_2020_for_CHI_papers": total, "num_CHI_papers_cited_in_2020": n_cited, "num_CHI_papers_in_docs": int(len(chi_titles))})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zqbhld7KWH0SyWZClF94YQSM': 'file_storage/call_zqbhld7KWH0SyWZClF94YQSM.json', 'var_call_QjNkS9jNg19inwvCAipHBOQF': 'file_storage/call_QjNkS9jNg19inwvCAipHBOQF.json'}

exec(code, env_args)
