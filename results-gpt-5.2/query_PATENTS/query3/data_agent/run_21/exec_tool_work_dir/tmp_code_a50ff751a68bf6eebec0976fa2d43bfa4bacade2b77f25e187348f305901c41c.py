code = """import json
import pandas as pd

res = var_call_qufD8tU2l4wwr5AedziTTnZ1
pairs = pd.DataFrame(res['pairs'])
sub_map = {r['symbol']: r['titleFull'] for r in var_call_ykYT26jYHBQfJ9nbkiB0vMfp}

pairs['cpc_subclass_title'] = pairs['cpc_subclass'].map(sub_map)
pairs['citing_assignee'] = pairs['citing_assignee'].str.replace(r'\s+and has publication.*$', '', regex=True)

pairs = pairs.drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
lines=[]
for _, r in pairs.iterrows():
    lines.append(str(r['citing_assignee']) + "\\t" + str(r['cpc_subclass']) + " - " + str(r['cpc_subclass_title']))
answer = "\\n".join(lines) if lines else "No citing assignees found (excluding UNIV CALIFORNIA)."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_ky9p28bfw6ZzpdkIpcICy6Ul': ['publicationinfo'], 'var_call_9FjvG9K7GEUQ2jOWlZFfSjSr': ['cpc_definition'], 'var_call_FPczLPUeIyYnvaQzIKLNGXAr': [], 'var_call_E6tbXMkCCY50UNQlzqQSeEjh': 'file_storage/call_E6tbXMkCCY50UNQlzqQSeEjh.json', 'var_call_JuEFYCQ1kR51VnVGUHBz75aP': 'file_storage/call_JuEFYCQ1kR51VnVGUHBz75aP.json', 'var_call_4XGmYMbVJ7u6IZ4sJG6aFSf1': [{'name': 'publicationinfo'}], 'var_call_65uPjKCFaiNNd7bRcSfrJwgT': 'file_storage/call_65uPjKCFaiNNd7bRcSfrJwgT.json', 'var_call_qufD8tU2l4wwr5AedziTTnZ1': {'pairs': [{'citing_assignee': 'CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1', 'cpc_subclass': 'E04H'}, {'citing_assignee': 'CRYSTAL IS INC and has publication no', 'cpc_subclass': 'H01L'}, {'citing_assignee': 'SCHOWALTER LEO J', 'cpc_subclass': 'H01L'}], 'subclasses': ['E04H', 'H01L']}, 'var_call_ykYT26jYHBQfJ9nbkiB0vMfp': [{'symbol': 'E04H', 'titleFull': 'BUILDINGS OR LIKE STRUCTURES FOR PARTICULAR PURPOSES; SWIMMING OR SPLASH BATHS OR POOLS; MASTS; FENCING; TENTS OR CANOPIES, IN GENERAL'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}]}

exec(code, env_args)
