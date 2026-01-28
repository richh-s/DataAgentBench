code = """import json, re
from collections import defaultdict

# Load patent data
patent_file = globals()['var_functions.query_db:36']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Debug date parsing
year_pattern = re.compile(r'\b(20\d{2})\b')

print('Debugging date format:')
for i in range(min(5, len(patent_data))):
    record = patent_data[i]
    pub_date = record.get('publication_date', '')
    date_str = str(pub_date)
    
    print('\nRecord {}:'.format(i))
    print('  publication_date field:', repr(pub_date))
    print('  Converted to string:', repr(date_str))
    
    # Test different regex approaches
    year_match = year_pattern.search(date_str)
    print('  Year regex match:', year_match.group(1) if year_match else 'None')
    
    # Alternative: just look for 4 digits starting with 20
    alt_match = re.search(r'(20\d{2})', date_str)
    print('  Alternative match:', alt_match.group(1) if alt_match else 'None')

# Now process all data with working regex
cpc_year_counts = defaultdict(lambda: defaultdict(int))
level5_cpc_to_full = defaultdict(set)

year_pattern = re.compile(r'(20\d{2})')

records_processed = 0
for record in patent_data:
    try:
        cpc_str = record.get('cpc', '[]')
        if not cpc_str or cpc_str == 'null':
            continue
        
        cpc_list = json.loads(cpc_str)
        pub_date_str = record.get('publication_date', '')
        
        # Extract year
        year_match = year_pattern.search(str(pub_date_str))
        if not year_match:
            continue
        
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:
            continue
        
        for cpc_item in cpc_list:
            full_code = cpc_item.get('code', '')
            if full_code and '/' in full_code:  # Must be a full CPC code
                cpc_year_counts[full_code][year] += 1
                
                # Extract level 5 group (e.g., H01M from H01M10/0525)
                group_part = full_code.split('/')[0]
                if len(group_part) == 4 and re.match(r'^[A-Z]\d{2}[A-Z]$', group_part):
                    level5_cpc_to_full[group_part].add(full_code)
        
        records_processed += 1
        
    except Exception as e:
        continue

print('\n\nProcessing complete:')
print('Records processed:', records_processed)
print('Full CPC codes:', len(cpc_year_counts))
print('Level 5 CPC groups:', len(level5_cpc_to_full))

# Sample results
print('\nSample level 5 CPC groups:', list(level5_cpc_to_full.keys())[:10])

# Ready for EMA calculation
output = {
    'cpc_year_counts': {cpc: dict(years) for cpc, years in cpc_year_counts.items()},
    'level5_cpc_to_full': {k: list(v) for k, v in level5_cpc_to_full.items()},
    'records_processed': records_processed
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'cpc_year_counts': {}, 'cpc_level5_to_full': {}, 'total_records': 277813}, 'var_functions.execute_python:46': {'records_checked': 1000, 'cpc_parse_success': 1000, 'year_match_success': 0, 'level5_patterns': 11181}}

exec(code, env_args)
