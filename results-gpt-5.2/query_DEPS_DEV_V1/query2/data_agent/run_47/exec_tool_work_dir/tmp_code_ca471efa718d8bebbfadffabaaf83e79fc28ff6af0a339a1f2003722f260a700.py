code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_fKlTE0T7lF5Y89BM48f2LLXq)
ppv = load(var_call_afmN941eN6tWheh5nbAhq4Fb)
projinfo = load(var_call_qe8r26cJ8XYETNw9tjBZNyQI)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(projinfo)

# join packages to project-packageversion mapping
m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# keep only MIT packages (robust)
# Licenses field is a JSON-like array string; check token MIT
m = m[m['Licenses'].fillna('').str.contains(r'\bMIT\b', regex=True)]

# project_info join via exact ProjectName match already present in pi_df
m2 = m.merge(pi_df, on='ProjectName', how='inner')

# extract forks count from Project_Information
fork_re = re.compile(r'forks?\s*(?:count\s*of\s*)?(\d[\d,]*)', re.IGNORECASE)

def extract_forks(s):
    if not isinstance(s, str):
        return None
    # common phrasing: 'and it has garnered X stars and 67 forks'
    m = fork_re.search(s)
    if not m:
        # alternate: 'has been forked 227 times'
        m2 = re.search(r'forked\s*(\d[\d,]*)\s*times', s, re.IGNORECASE)
        if m2:
            return int(m2.group(1).replace(',',''))
        return None
    return int(m.group(1).replace(',',''))

m2['forks'] = m2['Project_Information'].apply(extract_forks)

# dedupe by ProjectName take max forks
proj_forks = (m2.dropna(subset=['forks'])
               .groupby('ProjectName', as_index=False)['forks'].max())

top5 = proj_forks.sort_values('forks', ascending=False).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qe8r26cJ8XYETNw9tjBZNyQI': 'file_storage/call_qe8r26cJ8XYETNw9tjBZNyQI.json', 'var_call_fKlTE0T7lF5Y89BM48f2LLXq': 'file_storage/call_fKlTE0T7lF5Y89BM48f2LLXq.json', 'var_call_afmN941eN6tWheh5nbAhq4Fb': 'file_storage/call_afmN941eN6tWheh5nbAhq4Fb.json'}

exec(code, env_args)
