code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_records(var_call_Rh03hn8MMsUehuNAqDEgW5RI)
docs = load_records(var_call_qxLlvmH3g6olf6Jjgz9WIWws)

cit_df = pd.DataFrame(cit)
# coerce citation_count to int
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# build set of CHI titles from docs by regex on text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','') or ''
    # match CHI as venue marker; allow e.g., "CHI '20" or "Proceedings of the SIGCHI" etc.
    if re.search(r'\bCHI\b', text) or re.search(r'SIGCHI', text, flags=re.I):
        # but avoid obvious non-CHI venues like UBICOMP, CSCW, DIS, etc if present without CHI
        # if both CHI and another venue appear, still keep as CHI per question (presented at CHI)
        chi_titles.add(title)

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

total = int(chi_cit_df['citation_count'].sum())
result = {
    "total_citation_count_2020_for_CHI_papers": total,
    "num_CHI_papers_cited_in_2020": int(chi_cit_df['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Rh03hn8MMsUehuNAqDEgW5RI': 'file_storage/call_Rh03hn8MMsUehuNAqDEgW5RI.json', 'var_call_qxLlvmH3g6olf6Jjgz9WIWws': 'file_storage/call_qxLlvmH3g6olf6Jjgz9WIWws.json'}

exec(code, env_args)
