code = """import json, re
from collections import defaultdict

# Get patent data
file_path = globals()['var_functions.query_db:36']
if isinstance(file_path, str) and '.json' in file_path:
    with open(file_path, 'r') as f:
        patent_data = json.load(f)
else:
    patent_data = file_path

# Process patents
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_level5_codes = set()

year_pattern = re.compile(r'\b(20\d{2})\b')

for record in patent_data[:10000]:  # Process subset first for debugging
    try:
        cpc_str = record.get('cpc', '[]')
        if not cpc_str or cpc_str == 'null':
            continue
        
        cpc_list = json.loads(cpc_str)
        pub_date_str = record.get('publication_date', '')
        
        year_match = year_pattern.search(pub_date_str)
        if year_match:
            year = int(year_match.group(1))
            for cpc_item in cpc_list:
                full_code = cpc_item.get('code', '')
                if full_code:
                    cpc_year_counts[full_code][year] += 1
                    
                    # Extract level 5 code (first 4 chars: A01B, H01M, etc.)
                    if len(full_code) >= 4:
                        level5 = full_code[:4]
                        if re.match(r'^[A-Z]\d{2}[A-Z]$', level5):
                            cpc_level5_codes.add(level5)
    except:
        continue

print('Full CPC codes:', len(cpc_year_counts))
print('Level 5 CPC codes:', len(cpc_level5_codes))
print('Sample level 5 codes:', list(cpc_level5_codes)[:10])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
