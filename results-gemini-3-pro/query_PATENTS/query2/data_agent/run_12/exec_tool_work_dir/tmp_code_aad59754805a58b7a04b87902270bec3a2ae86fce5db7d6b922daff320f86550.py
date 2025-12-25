code = """import json
import re

with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    data = json.load(f)

de_dates = []
for row in data:
    p_info = row.get('Patents_info', '')
    if re.search(r'\bDE[- ]', p_info) or "from DE" in p_info or "In DE" in p_info or "Germany" in p_info:
        de_dates.append(row.get('grant_date', 'MISSING'))

print("__RESULT__:")
print(json.dumps(de_dates[:10]))"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': [], 'var_function-call-8691657811473980173': [], 'var_function-call-5507538740903062421': {'total_records': 4833, 'de_matches_count': 32, 'sample_de_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'sample_de_grant_date': '14th Mar 2019', 'parsed_sample_date': 'Parse Error', 'de_h2_2019_count': 0}, 'var_function-call-1410127800540734811': {'debug_dates': [], 'msg': 'No data after filtering'}}

exec(code, env_args)
