code = """import json, re, pandas as pd

cit_path = var_call_FgKC21nLbw6AhCiJqsmmRrZ4
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
df_cit['citations_2020'] = pd.to_numeric(df_cit.get('citations_2020'), errors='coerce').fillna(0).astype(int)

paper_path = var_call_dNAZ4AVMUspUeq7emmNBPyS7
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

df_p = pd.DataFrame(papers)

def title_from_filename(fn):
    return re.sub(r'\\.txt$', '', fn if isinstance(fn,str) else '')

df_p['title'] = df_p['filename'].map(title_from_filename)

# avoid curly apostrophes in code literals
APOS = "'"

def is_chi(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    patterns = [
        r"\\bchi\\s*['\\"]?\\d{2}\\b",
        r"\\bchi\\s+conference\\b",
        r"\\bproceedings of the .*chi\\b",
        r"\\bconference on human factors in computing systems\\b",
        r"\\bchi\\s*\\d{4}\\b",
    ]
    return any(re.search(p, t) for p in patterns)

df_p['is_CHI'] = df_p['text'].map(is_chi)
chi_titles = set(df_p.loc[df_p['is_CHI'], 'title'])

df_chi_cit = df_cit[df_cit['title'].isin(chi_titles)].copy()

out = {
    'total_citations_2020_for_CHI_papers': int(df_chi_cit['citations_2020'].sum()),
    'num_CHI_papers_cited_in_2020': int(df_chi_cit.shape[0]),
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FgKC21nLbw6AhCiJqsmmRrZ4': 'file_storage/call_FgKC21nLbw6AhCiJqsmmRrZ4.json', 'var_call_dNAZ4AVMUspUeq7emmNBPyS7': 'file_storage/call_dNAZ4AVMUspUeq7emmNBPyS7.json'}

exec(code, env_args)
