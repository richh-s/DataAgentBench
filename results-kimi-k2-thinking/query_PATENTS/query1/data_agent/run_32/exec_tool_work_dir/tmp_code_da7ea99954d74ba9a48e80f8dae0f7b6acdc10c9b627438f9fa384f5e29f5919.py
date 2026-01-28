code = """import json
import re

# Load patent data
patent_data_file = globals()['var_functions.query_db:36']
with open(patent_data_file, 'r') as f:
    patent_data = json.load(f)

# Debug first 10 records
print('Debugging first 10 records:')
for i in range(min(10, len(patent_data))):
    record = patent_data[i]
    cpc_str = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    print('\nRecord {}:'.format(i))
    print('  CPC field present:', bool(cpc_str))
    print('  Publication date:', pub_date)
    
    if cpc_str:
        print('  CPC preview:', cpc_str[:100])
        try:
            cpc_list = json.loads(cpc_str)
            print('  Parsed CPC count:', len(cpc_list))
            if cpc_list:
                print('  First CPC code:', cpc_list[0].get('code'))
        except Exception as e:
            print('  CPC parse error:', e)
    
    # Check year pattern
    year_match = re.search(r'\b(20\d{2})\b', str(pub_date))
    print('  Year found:', year_match.group(1) if year_match else 'None')

# Debug a level 5 code extraction
sample_codes = ['H01M10/0525', 'C01B33/00', 'F16H47/04', 'B29C70/48']
print('\nLevel 5 code extraction test:')
for code in sample_codes:
    if len(code) >= 4:
        level5 = code[:4]
        import re
        matches = bool(re.match(r'^[A-Z]\d{2}[A-Z]$', level5))
        print('  {} -> {} (matches pattern: {})'.format(code, level5, matches))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'cpc_year_counts': {}, 'cpc_level5_to_full': {}, 'total_records': 277813}}

exec(code, env_args)
