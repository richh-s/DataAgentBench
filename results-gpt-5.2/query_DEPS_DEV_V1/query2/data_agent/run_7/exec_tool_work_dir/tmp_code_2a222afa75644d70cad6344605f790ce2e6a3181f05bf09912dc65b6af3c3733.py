code = """import json, pandas as pd

pkg_src = var_call_f6UmnHm9tLgbcTWK5VBMfZzV
ppv_src = var_call_FZ9C0DUWeVO3ERu0JmBuDl5s
pi_src  = var_call_U2j8WjgCLNqYbofEeqERkDrU

def load_records(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load_records(pkg_src)
ppv = load_records(ppv_src)
pi  = load_records(pi_src)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(m['ProjectName'].dropna().drop_duplicates())

pi_df = pd.DataFrame(pi)
pi_df['ProjectName'] = pi_df['ProjectName'].astype(str).str.strip()
pi_df = pi_df[pi_df['ProjectName'].isin(projects)]

result = {
  'matched_pkg_versions': int(len(m)),
  'distinct_projects_from_join': int(m['ProjectName'].nunique()),
  'project_info_rows_matching_projects': int(len(pi_df)),
  'sample_projects_from_join': list(sorted(list(projects))[:20]),
  'sample_project_info_projectnames': pi_df['ProjectName'].head(20).tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_f6UmnHm9tLgbcTWK5VBMfZzV': 'file_storage/call_f6UmnHm9tLgbcTWK5VBMfZzV.json', 'var_call_FZ9C0DUWeVO3ERu0JmBuDl5s': 'file_storage/call_FZ9C0DUWeVO3ERu0JmBuDl5s.json', 'var_call_b4vxqe2IjkAeUso3a7dupFw3': 'file_storage/call_b4vxqe2IjkAeUso3a7dupFw3.json', 'var_call_yyGel3uqTKeIgIupFmQdPAWY': [], 'var_call_U2j8WjgCLNqYbofEeqERkDrU': 'file_storage/call_U2j8WjgCLNqYbofEeqERkDrU.json', 'var_call_EOxbVYJe2r0MltQSEsWxjULe': [], 'var_call_ZdeIHn5KFEWpS36xQK8gBG46': [{'cnt': '176170'}], 'var_call_2FyPi0eHYAMlJd2RQrGh56gu': [{'cnt': '591699'}], 'var_call_ihCSkQNdQ8t7LOHZxiEwrEzL': [{'cnt': '770'}]}

exec(code, env_args)
