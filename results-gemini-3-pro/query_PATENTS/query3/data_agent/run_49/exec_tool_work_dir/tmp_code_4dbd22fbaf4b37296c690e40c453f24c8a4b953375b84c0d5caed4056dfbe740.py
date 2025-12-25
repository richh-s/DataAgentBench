code = """import json

with open(locals()['var_function-call-1286936377843854032'], 'r') as f:
    chunk = json.load(f)

# Find a record with cpc
for rec in chunk:
    if rec.get('cpc'):
        print("__RESULT__:")
        print(rec['cpc'])
        break"""

env_args = {'var_function-call-12868220818788144791': 'file_storage/function-call-12868220818788144791.json', 'var_function-call-2492118762681271268': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_function-call-18177144468656687824': [{'COUNT(*)': '277813'}], 'var_function-call-6015838364880532085': [{'COUNT(*)': '0'}], 'var_function-call-3627068258271379600': 'file_storage/function-call-3627068258271379600.json', 'var_function-call-12921287316337246279': {'count': 167, 'sample': ['US-10900049-B2', 'AU-7724398-A', 'KR-20200084864-A', 'CN-101584047-A', 'US-2021282642-A1']}, 'var_function-call-1286936377843854032': 'file_storage/function-call-1286936377843854032.json'}

exec(code, env_args)
