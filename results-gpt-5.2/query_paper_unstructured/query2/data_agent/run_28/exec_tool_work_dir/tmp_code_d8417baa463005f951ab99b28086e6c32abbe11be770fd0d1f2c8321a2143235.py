code = """import json, pandas as pd

# citations in 2018
with open(var_call_vnmIwSY1IigYEg6nNO64Zmuc, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
df_cit = df_cit.dropna(subset=['title','citation_count'])

# ACM papers inferred by presence of 'ACM' substring anywhere in text (proxy)
with open(var_call_UhxRcq2FOutPvIWFKqVbdVhW, 'r', encoding='utf-8') as f:
    acm_files = json.load(f)
df_acm = pd.DataFrame(acm_files)
df_acm['title'] = df_acm['filename'].str.replace(r'\.txt$', '', regex=True)
acm_titles = set(df_acm['title'].dropna().tolist())

# filter citations to those titles
mask = df_cit['title'].isin(acm_titles)
df = df_cit[mask].copy()

avg = float(df['citation_count'].mean()) if len(df) else None
out = {
    "average_citation_count": avg,
    "paper_count": int(len(df))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vnmIwSY1IigYEg6nNO64Zmuc': 'file_storage/call_vnmIwSY1IigYEg6nNO64Zmuc.json', 'var_call_aZ8KrJgWhhxjIfDu2jt2i8oh': 'file_storage/call_aZ8KrJgWhhxjIfDu2jt2i8oh.json', 'var_call_Sw4wj2zwRz7KSd92cDhgBOhX': {'error': 'Need paper source (ACM) per paper; requires querying paper_docs text/metadata. Please provide a structured source field or allow additional MongoDB queries filtered by filenames/titles.'}, 'var_call_UhxRcq2FOutPvIWFKqVbdVhW': 'file_storage/call_UhxRcq2FOutPvIWFKqVbdVhW.json'}

exec(code, env_args)
