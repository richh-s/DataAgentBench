code = """import json, re
from collections import defaultdict

# Get patent data file path
patent_data_file = globals()['var_functions.query_db:36']

# Load data from file
with open(patent_data_file, 'r') as f:
    patent_data = json.load(f)

# Process patents: Count filings per CPC code per year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_level5_to_full = defaultdict(set)

year_pattern = re.compile(r'\b(20\d{2})\b')

for record in patent_data:
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
                if full_code and len(full_code) >= 4:
                    cpc_year_counts[full_code][year] += 1
                    
                    # Extract level 5 code (first 4 chars)
                    level5 = full_code[:4]
                    if re.match(r'^[A-Z]\d{2}[A-Z]$', level5):
                        cpc_level5_to_full[level5].add(full_code)
    except:
        continue

print('Full CPC codes processed:', len(cpc_year_counts))
print('Level 5 CPC groups:', len(cpc_level5_to_full))

# Save to JSON for next steps
output_data = {
    'cpc_year_counts': {cpc: dict(years) for cpc, years in cpc_year_counts.items()},
    'cpc_level5_to_full': {k: list(v) for k, v in cpc_level5_to_full.items()},
    'total_records': len(patent_data)
}

print('__RESULT__:')
print(json.dumps(output_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
