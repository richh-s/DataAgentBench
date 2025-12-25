code = """import json
import re

with open(locals()['var_function-call-12636907471574372890'], 'r') as f:
    patents = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

print("__RESULT__:")
logs = []
for p in patents[:10]:
    d = p.get('filing_date')
    m = year_pattern.search(str(d))
    logs.append({"date": d, "match": m.group(0) if m else None})

print(json.dumps(logs))"""

env_args = {'var_function-call-7168665038669852193': 'file_storage/function-call-7168665038669852193.json', 'var_function-call-10792060600082410393': 'file_storage/function-call-10792060600082410393.json', 'var_function-call-17520737272150592810': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1418283475394270998': [{'count(*)': '277813'}], 'var_function-call-6985419727303954916': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12636907471574372890': 'file_storage/function-call-12636907471574372890.json', 'var_function-call-6477679623935836888': [], 'var_function-call-1446217851243151572': {'min_year': None, 'max_year': None, 'sample_counts': []}, 'var_function-call-16194099183484994991': {'sample_defs': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K'], 'sample_patents': ['C01B', 'H01M', 'C01G', 'C01P', 'Y02E', 'F16H', 'B29C', 'C08J', 'B32B', 'C09D'], 'patents_count': 544204, 'defs_count': 677}, 'var_function-call-8791923892856555197': {'intersection_count': 669, 'sample_intersection': ['B27D', 'A63H', 'A01D', 'C09G', 'E01F', 'B60J', 'F42B', 'D01C', 'B27G', 'A23G'], 'is_C01B_valid': True, 'is_H01M_valid': True}, 'var_function-call-5325882802358373616': {'global_max_year': 0, 'count_results_2022': 0, 'sample_best_years': [], 'results_2022': []}}

exec(code, env_args)
