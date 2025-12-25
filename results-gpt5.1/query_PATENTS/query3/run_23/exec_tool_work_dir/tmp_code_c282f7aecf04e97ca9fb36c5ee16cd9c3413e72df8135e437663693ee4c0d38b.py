code = """import json, re, pandas as pd

# Load citing records from file
path = var_call_HNMvbM0HhJO4pQdpCpN18xf7
with open(path, 'r') as f:
    citing = json.load(f)

# Extract assignee and primary CPC code from each citing patent
records = []
for row in citing:
    info = row.get('Patents_info','') or ''
    m = re.search(r'assignee_harmonized: ([^,\.]+)', info)
    if not m:
        continue
    assignee = m.group(1).strip()
    if assignee.upper() == 'UNIV CALIFORNIA':
        continue
    cpc_raw = row.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    primary = None
    for entry in cpc_list:
        if entry.get('first'):
            primary = entry.get('code')
            break
    if not primary and cpc_list:
        primary = cpc_list[0].get('code')
    if not primary:
        continue
    records.append({'assignee': assignee, 'primary_cpc': primary})

rec_df = pd.DataFrame(records).drop_duplicates()

# Build CPC definitions DataFrame
path_def = var_call_g3NHqdwC5xuUGrfh0DgZZxrs
with open(path_def, 'r') as f:
    defs = json.load(f)

def_df = pd.DataFrame(defs)

merged = rec_df.merge(def_df, left_on='primary_cpc', right_on='symbol', how='left')

out = merged[['assignee','primary_cpc','titleFull']].drop_duplicates().sort_values(['assignee','primary_cpc'])

result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_f4wXoiFpQO8QqSbVIv3afzkw': [], 'var_call_HNMvbM0HhJO4pQdpCpN18xf7': 'file_storage/call_HNMvbM0HhJO4pQdpCpN18xf7.json', 'var_call_g3NHqdwC5xuUGrfh0DgZZxrs': 'file_storage/call_g3NHqdwC5xuUGrfh0DgZZxrs.json'}

exec(code, env_args)
