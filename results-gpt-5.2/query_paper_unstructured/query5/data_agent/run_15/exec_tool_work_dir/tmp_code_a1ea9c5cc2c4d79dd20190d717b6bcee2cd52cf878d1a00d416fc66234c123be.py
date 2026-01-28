code = """import json, re
import pandas as pd

# Load citations 2020
cit_path = var_call_zqbhld7KWH0SyWZClF94YQSM
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    total = 0
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
paper_path = var_call_QjNkS9jNg19inwvCAipHBOQF
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

def is_chi(text):
    if not text:
        return False
    t = text.upper()
    # Match common CHI proceedings header patterns
    return (re.search(r'\bCHI\s*(?:\’|\'|)\s*\d{2}\b', t) is not None) or (re.search(r'\bCHI\s+CONFERENCE\b', t) is not None) or (re.search(r'\bPROCEEDINGS\s+OF\s+THE\s+CHI\b', t) is not None)

chi_titles = set()
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_chi(d.get('text','')):
        chi_titles.add(title)

if df_cit.empty:
    total = 0
else:
    total = int(df_cit[df_cit['title'].isin(chi_titles)]['citation_count'].sum())

out = json.dumps({"total_citations_2020_for_CHI_papers": total, "num_CHI_papers_cited_in_2020": int(df_cit[df_cit['title'].isin(chi_titles)].shape[0]), "num_CHI_papers_in_docs": len(chi_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zqbhld7KWH0SyWZClF94YQSM': 'file_storage/call_zqbhld7KWH0SyWZClF94YQSM.json', 'var_call_QjNkS9jNg19inwvCAipHBOQF': 'file_storage/call_QjNkS9jNg19inwvCAipHBOQF.json'}

exec(code, env_args)
