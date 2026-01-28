code = """import json, pandas as pd, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

cit = load_json_maybe(var_call_j1wPbsfPSxrY0vpr3Fj1aHhT)
files = load_json_maybe(var_call_ZsHVLYAtv4fKhP9Lmd0LrGWD)

cit_df = pd.DataFrame(cit)
# normalize types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# titles available in mongo (strip .txt)
titles = {re.sub(r'\.txt$','', d.get('filename','')) for d in files}

# ACM set: approximate as titles that exist in our paper_docs corpus (ACM HCI venues)
acm_cit_df = cit_df[cit_df['title'].isin(titles)].copy()

avg_val = float(acm_cit_df['citation_count'].mean()) if len(acm_cit_df) else None
out = {
    'average_citation_count_2018_acm': avg_val,
    'num_papers': int(acm_cit_df['title'].nunique()),
    'num_records': int(len(acm_cit_df))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_j1wPbsfPSxrY0vpr3Fj1aHhT': 'file_storage/call_j1wPbsfPSxrY0vpr3Fj1aHhT.json', 'var_call_ZsHVLYAtv4fKhP9Lmd0LrGWD': 'file_storage/call_ZsHVLYAtv4fKhP9Lmd0LrGWD.json'}

exec(code, env_args)
