code = """import json, re
from collections import defaultdict

# Load patent data
patent_file = globals()['var_functions.query_db:36']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

records_checked = 0
cpc_parse_success = 0
year_match_success = 0
level5_patterns = 0

year_pattern = re.compile(r'\b(20\d{2})\b')

for record in patent_data:
    records_checked += 1
    
    cpc_str = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    try:
        if cpc_str and cpc_str != 'null':
            cpc_list = json.loads(cpc_str)
            cpc_parse_success += 1
            
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code and len(code) >= 4:
                    level5 = code[:4]
                    if re.match(r'^[A-Z]\d{2}[A-Z]$', level5):
                        level5_patterns += 1
    except:
        pass
    
    if year_pattern.search(str(pub_date)):
        year_match_success += 1
    
    if records_checked >= 1000:
        break

print('Records checked:', records_checked)
print('CPC parse success:', cpc_parse_success)
print('Year match success:', year_match_success)
print('Level 5 pattern matches:', level5_patterns)
print('__RESULT__:')
print(json.dumps({
    'records_checked': records_checked,
    'cpc_parse_success': cpc_parse_success,
    'year_match_success': year_match_success,
    'level5_patterns': level5_patterns
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'cpc_year_counts': {}, 'cpc_level5_to_full': {}, 'total_records': 277813}}

exec(code, env_args)
