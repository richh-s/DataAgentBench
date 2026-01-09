code = """import json, re, pandas as pd

# Load UC-assigned publications
path_uc = var_call_uvI2aAReL1EIyoQzvdd975yY
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# Helper to extract publication number from Patents_info
pub_re = re.compile(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)')

def extract_pub(pinfo:str):
    if not pinfo:
        return None
    m = pub_re.search(pinfo)
    if m:
        return m.group(1)
    # fallback: sometimes "publication number" wording
    m2 = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pinfo)
    return m2.group(1) if m2 else None

uc_pubs = []
for r in uc_rows:
    pn = extract_pub(r.get('Patents_info',''))
    if pn:
        uc_pubs.append(pn)
uc_pubs_set = set(uc_pubs)

# Now scan all publications to find those citing any UC pub
# Query all Patents_info,cpc,citation

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs_set)}))"""

env_args = {'var_call_YgowPBKHhXY5o2brkI4UJaYV': [], 'var_call_PJuXR6cD4jOjJNzoV5V1CUJU': 'file_storage/call_PJuXR6cD4jOjJNzoV5V1CUJU.json', 'var_call_v4YEqqXSReRaZdU3Iv4eBvOJ': ['publicationinfo'], 'var_call_SRdGpWawm7GMalN0gLjD3xat': ['cpc_definition'], 'var_call_uvI2aAReL1EIyoQzvdd975yY': 'file_storage/call_uvI2aAReL1EIyoQzvdd975yY.json'}

exec(code, env_args)
