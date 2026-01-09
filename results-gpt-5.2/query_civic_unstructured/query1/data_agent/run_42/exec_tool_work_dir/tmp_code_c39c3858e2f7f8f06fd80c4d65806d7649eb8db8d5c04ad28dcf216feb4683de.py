code = """import json, re

# Load extracted list from previous python output file
path_proj = var_call_mfMMasceQd3Zy3ion5rSFGtl
with open(path_proj, 'r', encoding='utf-8') as f:
    proj_obj = json.load(f)
proj_list = proj_obj['projects_design_capital']

# Filter out schedule/paragraph noise: keep lines that look like project titles
bad_prefix = re.compile(r"^(Advertise|Award|Begin|Began|Bids|Complete|Construction|Consultant|Council|County|Final|Funding|In |Interviews|Letters|March|Metro\.|Next |October|Page |Plans |Project Description|Project is|Resources|September|Staff |The |a |advertised|agreement|Awaiting|Caltrans|City |Commission|Contractor)", re.IGNORECASE)

clean_projects = []
for p in proj_list:
    if bad_prefix.search(p):
        continue
    # drop if contains ':'
    if ':' in p:
        continue
    # drop if too long
    if len(p) > 80:
        continue
    # require at least one letter and no full sentence period at end
    if not re.search(r"[A-Za-z]", p):
        continue
    if p.endswith('.'):
        continue
    clean_projects.append(p)

clean_set = set(clean_projects)

# Load funding project names > 50000
path_f = var_call_ToMhE2pSNmLx69ea1ndpRu5w
with open(path_f, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_set = set([r['Project_Name'] for r in fund])

# Intersection count
inter = sorted(clean_set & fund_set)

print('__RESULT__:')
print(json.dumps({'count': len(inter), 'projects': inter}))"""

env_args = {'var_call_KFAXzxfc3ZpVXH46fYupleAa': [{'cnt': '276'}], 'var_call_kmcAa0Vk1QVOQrIeBD8TN7W3': 'file_storage/call_kmcAa0Vk1QVOQrIeBD8TN7W3.json', 'var_call_mfMMasceQd3Zy3ion5rSFGtl': 'file_storage/call_mfMMasceQd3Zy3ion5rSFGtl.json', 'var_call_ToMhE2pSNmLx69ea1ndpRu5w': 'file_storage/call_ToMhE2pSNmLx69ea1ndpRu5w.json'}

exec(code, env_args)
