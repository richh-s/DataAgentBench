code = """import json
import re

path_pub_info = locals()['var_function-call-1274391543131155253']

with open(path_pub_info, 'r') as f:
    pub_data = json.load(f)

samples = []
for i, row in enumerate(pub_data):
    if i >= 10: break
    d = row.get('filing_date')
    match = re.search(r'\b(19|20)\d{2}\b', str(d))
    samples.append({"date": d, "match": match.group(0) if match else None})

print("__RESULT__:")
print(json.dumps(samples))"""

env_args = {'var_function-call-11820737813391212427': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-11820737813391208476': 'file_storage/function-call-11820737813391208476.json', 'var_function-call-18359320766515546987': [{'level': '2.0', 'sample_symbol': 'A', 'cnt': '9'}, {'level': '4.0', 'sample_symbol': 'A01', 'cnt': '137'}, {'level': '5.0', 'sample_symbol': 'A01B', 'cnt': '677'}, {'level': '7.0', 'sample_symbol': 'A01B1/00', 'cnt': '9816'}, {'level': '8.0', 'sample_symbol': 'A01B1/02', 'cnt': '48384'}, {'level': '9.0', 'sample_symbol': 'A01B1/022', 'cnt': '70250'}, {'level': '10.0', 'sample_symbol': 'A01B1/225', 'cnt': '62585'}, {'level': '11.0', 'sample_symbol': 'A01B3/421', 'cnt': '35084'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215', 'cnt': '17632'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843', 'cnt': '8015'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825', 'cnt': '3649'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446', 'cnt': '1521'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028', 'cnt': '1223'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823', 'cnt': '720'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444', 'cnt': '485'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137', 'cnt': '621'}], 'var_function-call-8333227560207613729': [{'len': '4', 'count': '677'}], 'var_function-call-1274391543131154232': 'file_storage/function-call-1274391543131154232.json', 'var_function-call-1274391543131155253': 'file_storage/function-call-1274391543131155253.json', 'var_function-call-8887395626434362746': [], 'var_function-call-9360059119577031059': {'years': []}}

exec(code, env_args)
