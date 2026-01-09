code = """import json, re, pandas as pd

# load UC-assigned patents rows
path = var_call_xNu75D1MsakbKFD0Cw620bkj
with open(path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# build set of UC publication_numbers
uc_pub_nums = set()
for r in uc_rows:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\.? number\s+([A-Z]{2,}-[^\s\.,]+)', pi, flags=re.I)
    if m:
        uc_pub_nums.add(m.group(1).upper())

# query all patents for potential citing ones (must have citations)
# We'll pull Patents_info,cpc,citation for all rows where citation not empty
# but here we only have uc rows; need another query -> handled outside

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pub_nums), 'sample': list(sorted(list(uc_pub_nums)))[0:10]}))"""

env_args = {'var_call_bn8TU9VmVk7pN006TU4zWS7v': ['publicationinfo'], 'var_call_4JOLYly9fdp0lGpLaOI60GYA': ['cpc_definition'], 'var_call_8mi1In3NOVkCaut8K4dmMMBZ': [], 'var_call_DQHDx6XuPUEqnb6zdY4YYVtE': [], 'var_call_hexwFqpBOYPl5UnOP4IVCFVL': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_xNu75D1MsakbKFD0Cw620bkj': 'file_storage/call_xNu75D1MsakbKFD0Cw620bkj.json'}

exec(code, env_args)
