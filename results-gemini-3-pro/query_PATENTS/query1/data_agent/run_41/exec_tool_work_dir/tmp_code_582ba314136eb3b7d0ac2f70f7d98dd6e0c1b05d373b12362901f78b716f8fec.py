code = """import json
import re
from collections import defaultdict

key2 = 'var_function-call-14088919373237143530'
with open(locals()[key2], 'r') as f:
    data = json.load(f)

p = re.compile(r'(19|20)\d{2}')
year_counts = defaultdict(int)

for row in data:
    m = p.search(row.get('filing_date', ''))
    if m:
        y = int(m.group(0))
        year_counts[y] += 1

print("__RESULT__:")
print(json.dumps(year_counts))"""

env_args = {'var_function-call-12010284986386434738': 'file_storage/function-call-12010284986386434738.json', 'var_function-call-12010284986386434717': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-7040256387500827623': [{'count(*)': '277813'}], 'var_function-call-5357179191043032962': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-2320558758355266598': [{'len': '4', 'count': '677'}], 'var_function-call-14088919373237144211': 'file_storage/function-call-14088919373237144211.json', 'var_function-call-14088919373237143530': 'file_storage/function-call-14088919373237143530.json', 'var_function-call-9751743124835996596': [], 'var_function-call-17846582241492215229': [], 'var_function-call-836893753941726447': {'sample_date_0': 'dated 5th March 2019', 'match_0': '2019', 'total_matches': 273258, 'total_rows': 277813}}

exec(code, env_args)
