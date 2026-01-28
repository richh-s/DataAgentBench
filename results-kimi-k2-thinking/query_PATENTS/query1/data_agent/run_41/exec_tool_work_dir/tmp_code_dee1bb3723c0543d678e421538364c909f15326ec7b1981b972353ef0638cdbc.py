code = """import json
import re
from collections import Counter

pub_file = locals()['var_functions.query_db:12']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print('Total records:', len(pub_data))

year_counts = Counter()
cpc_samples = []
cpc_total = 0

for item in pub_data:
    pub_date = item.get('publication_date', '')
    if pub_date:
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            year_counts[year] += 1
    
    cpc_str = item.get('cpc', '[]')
    if cpc_str and cpc_str != '[]':
        try:
            cpc_list = json.loads(cpc_str)
            cpc_total += len(cpc_list)
            for cpc in cpc_list:
                code = cpc.get('code', '')
                if code and len(cpc_samples) < 20:
                    cpc_samples.append(code)
        except:
            pass

print('Year range:', min(year_counts.keys()), 'to', max(year_counts.keys()))
print('Top years:', dict(year_counts.most_common(5)))
print('Total CPC entries:', cpc_total)
print('Sample CPCs:', cpc_samples[:10])

result = {
    'years': sorted(year_counts.keys()),
    'top_years': dict(year_counts.most_common(5)),
    'cpc_total': cpc_total,
    'samples': cpc_samples[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'count': 0, 'groups': []}}

exec(code, env_args)
