code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_SF2gOP4IN48fNKlnKM9sXKOC)
ppv = load_records(var_call_IwE5HzAxCnJOblCeWUcvFTnb)

# join on (System, Name, Version)
df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')

projects = sorted(df['ProjectName'].dropna().unique().tolist())

# get project_info rows that likely contain these ProjectName strings
# project_info has only Project_Information plus some metadata; parse fork counts from that text

# query all project_info Project_Information
# can't query here; use list_db? not available within python. We'll rely on separate query results not present.

print('__RESULT__:')
print(json.dumps({'need_project_info_query': True, 'unique_projects_count': len(projects), 'sample_projects': projects[:20]}))"""

env_args = {'var_call_SF2gOP4IN48fNKlnKM9sXKOC': 'file_storage/call_SF2gOP4IN48fNKlnKM9sXKOC.json', 'var_call_IwE5HzAxCnJOblCeWUcvFTnb': 'file_storage/call_IwE5HzAxCnJOblCeWUcvFTnb.json'}

exec(code, env_args)
