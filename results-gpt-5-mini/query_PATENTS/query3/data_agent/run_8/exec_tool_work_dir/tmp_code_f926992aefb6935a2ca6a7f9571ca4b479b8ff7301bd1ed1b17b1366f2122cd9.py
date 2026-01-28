code = """import json
path = var_call_B8JJOFd47fc03V6045GS9Gbw
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# Let's build mapping pubnum->assignee for these Univ California records
pub_to_assignee = {}
for r in rows:
    p = r.get('Patents_info','')
    # crude: take leading word(s) before 'holds' or 'is owned by' etc
    if 'holds' in p:
        ass = p.split('holds',1)[0].strip()
    elif 'owned by' in p:
        ass = p.split('owned by',1)[1].split('and')[0].strip()
    elif 'assigned to' in p:
        ass = p.split('assigned to',1)[1].split('and')[0].strip()
    else:
        ass = None
    # extract pub number
    pub = None
    low = p.lower()
    if 'pub.' in low or 'publication number' in low or 'pub' in low:
        # find token like US-2022074631-A1 or TW-201925402-A
        import re
        m = re.search(r'([A-Z]{2}-\d{4,}[A-Z0-9\-]*)', p)
        if m:
            pub = m.group(1)
    if pub and ass:
        pub_to_assignee[pub] = ass

print('__RESULT__:')
print(json.dumps({'count':len(pub_to_assignee), 'sample': dict(list(pub_to_assignee.items())[:10])}))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json', 'var_call_uhZPtxfUJEEwobfhVN8uLJfv': {'pairs': [], 'subclasses': []}, 'var_call_B8JJOFd47fc03V6045GS9Gbw': 'file_storage/call_B8JJOFd47fc03V6045GS9Gbw.json'}

exec(code, env_args)
