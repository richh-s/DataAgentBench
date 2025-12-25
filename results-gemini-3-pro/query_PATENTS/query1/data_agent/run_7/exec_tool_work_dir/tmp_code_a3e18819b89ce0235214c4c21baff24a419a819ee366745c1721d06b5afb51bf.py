code = """import json

with open(locals()['var_function-call-7168665038669852193'], 'r') as f:
    definitions = json.load(f)
valid_cpcs = set(d['symbol'] for d in definitions)

with open(locals()['var_function-call-12636907471574372890'], 'r') as f:
    patents = json.load(f)

patent_cpcs = set(p.get('cpc_l5') for p in patents)
intersection = valid_cpcs.intersection(patent_cpcs)

print("__RESULT__:")
print(json.dumps({
    "intersection_count": len(intersection),
    "sample_intersection": list(intersection)[:10],
    "is_C01B_valid": "C01B" in valid_cpcs,
    "is_H01M_valid": "H01M" in valid_cpcs
}))"""

env_args = {'var_function-call-7168665038669852193': 'file_storage/function-call-7168665038669852193.json', 'var_function-call-10792060600082410393': 'file_storage/function-call-10792060600082410393.json', 'var_function-call-17520737272150592810': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1418283475394270998': [{'count(*)': '277813'}], 'var_function-call-6985419727303954916': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12636907471574372890': 'file_storage/function-call-12636907471574372890.json', 'var_function-call-6477679623935836888': [], 'var_function-call-1446217851243151572': {'min_year': None, 'max_year': None, 'sample_counts': []}, 'var_function-call-16194099183484994991': {'sample_defs': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K'], 'sample_patents': ['C01B', 'H01M', 'C01G', 'C01P', 'Y02E', 'F16H', 'B29C', 'C08J', 'B32B', 'C09D'], 'patents_count': 544204, 'defs_count': 677}}

exec(code, env_args)
