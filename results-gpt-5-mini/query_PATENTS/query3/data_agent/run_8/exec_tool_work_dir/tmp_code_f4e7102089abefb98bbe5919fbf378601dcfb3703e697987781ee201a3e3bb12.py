code = """import json
# load previous result
res = var_call_wHtUi4EGdP6HsGumOvLGOCFU
# load cpc definitions
defs = var_call_x50y7221q6z31TgjdRv8SaWd
# build mapping symbol->title
sym2title = {d['symbol']: d['titleFull'] for d in defs}

# prepare final list mapping citing assignee to title
final = []
for item in res['pairs']:
    assg = item['citing_assignee']
    sym = item['primary_subclass']
    title = sym2title.get(sym) if sym else None
    final.append({'citing_assignee': assg, 'cpc_subclass': sym, 'titleFull': title})

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json', 'var_call_uhZPtxfUJEEwobfhVN8uLJfv': {'pairs': [], 'subclasses': []}, 'var_call_B8JJOFd47fc03V6045GS9Gbw': 'file_storage/call_B8JJOFd47fc03V6045GS9Gbw.json', 'var_call_iSikYemGpJjCyiuMbOeMopAo': {'count': 113, 'sample': {'US-202117472182-A': 'UNIV CALIFORNIA', 'TW-107142982-A': 'UNIV CALIFORNIA', 'US-201916454755-A': 'UNIV CALIFORNIA', 'AU-2019275518-A': 'UNIV CALIFORNIA', 'US-201515313510-A': 'UNIV CALIFORNIA', 'JP-13313985-A': 'UNIV CALIFORNIA', 'US-201715625819-A': 'UNIV CALIFORNIA', 'EP-00992018-A': 'UNIV CALIFORNIA', 'EP-21763795-A': 'THE REGENTS OF UNIV OF CALIFORNIA', 'US-55161904-A': 'UNIV CALIFORNIA'}}, 'var_call_uxK6ufKP7sP5MNcbECREGAlY': 'file_storage/call_uxK6ufKP7sP5MNcbECREGAlY.json', 'var_call_JbQY1XbRgmizlgigvQtExcn3': {'pairs': [], 'subclasses': [], 'pub_to_assignee_count': 1267}, 'var_call_wHtUi4EGdP6HsGumOvLGOCFU': {'pairs': [{'citing_assignee': 'CALIFORNIA INST OF TECHN', 'primary_subclass': 'G01M'}, {'citing_assignee': 'CRYSTAL IS INC', 'primary_subclass': 'H01L'}, {'citing_assignee': 'ETHICON LLC', 'primary_subclass': 'A61B'}, {'citing_assignee': 'SCHOWALTER LEO J', 'primary_subclass': 'H01L'}, {'citing_assignee': 'The US patent application', 'primary_subclass': 'A61B'}, {'citing_assignee': 'The US patent application', 'primary_subclass': 'H01M'}], 'subclasses': ['A61B', 'G01M', 'H01L', 'H01M']}, 'var_call_x50y7221q6z31TgjdRv8SaWd': [{'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01M', 'titleFull': 'PROCESSES OR MEANS, e.g. BATTERIES, FOR THE DIRECT CONVERSION OF CHEMICAL ENERGY INTO ELECTRICAL ENERGY'}, {'symbol': 'A61B', 'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION'}, {'symbol': 'G01M', 'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}]}

exec(code, env_args)
