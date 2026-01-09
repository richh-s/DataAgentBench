code = """import json, pandas as pd, re

# Load citations 2020
p_cit = var_call_Dx5TFSxWjgFDHFLAEQizbitJ
if isinstance(p_cit, str):
    with open(p_cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)
else:
    cit = p_cit

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"total_citations_2020_for_CHI_papers": 0, "paper_count": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_cit['citations_2020'] = pd.to_numeric(df_cit['citations_2020'], errors='coerce').fillna(0).astype(int)

# Load paper docs
p_docs = var_call_t7zwAGxQQRHAzCFXMUqQY9I0
if isinstance(p_docs, str):
    with open(p_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = p_docs

df_docs = pd.DataFrame(docs)
if df_docs.empty:
    out = {"error": "No paper docs available"}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

def title_from_filename(fn):
    if fn is None:
        return None
    return re.sub(r'\.txt$', '', fn).strip()

def is_chi(text):
    if not isinstance(text, str):
        return False
    t = text.upper()
    # Match CHI conference markers, avoid matching within words
    patterns = [r'\bCHI\b', r'\bCHI\s*\d{2,4}\b', r'\bCHI\s*\xE2\x80\x99?\d{2}\b']
    return any(re.search(p, t) for p in patterns) or ('SIGCHI' in t) or ('CHI CONFERENCE' in t) or ('CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS' in t)

df_docs['title'] = df_docs['filename'].map(title_from_filename)
df_docs['is_chi'] = df_docs['text'].map(is_chi)

chi_titles = set(df_docs.loc[df_docs['is_chi'] == True, 'title'].dropna().tolist())

# Join
chi_cit = df_cit[df_cit['title'].isin(chi_titles)].copy()

total = int(chi_cit['citations_2020'].sum())
count = int(chi_cit.shape[0])

out = {
    "total_citations_2020_for_CHI_papers": total,
    "chi_papers_cited_in_2020": count
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Dx5TFSxWjgFDHFLAEQizbitJ': 'file_storage/call_Dx5TFSxWjgFDHFLAEQizbitJ.json', 'var_call_t7zwAGxQQRHAzCFXMUqQY9I0': 'file_storage/call_t7zwAGxQQRHAzCFXMUqQY9I0.json'}

exec(code, env_args)
