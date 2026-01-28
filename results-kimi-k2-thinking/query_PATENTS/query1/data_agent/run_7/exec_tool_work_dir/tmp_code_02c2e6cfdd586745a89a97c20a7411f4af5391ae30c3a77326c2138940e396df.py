code = """import json
import ast

# Access the file path from storage
file_path = locals()['var_functions.query_db:10']
print('File path:', file_path)

# Read the full result file
with open(file_path, 'r') as f:
    records = json.load(f)

print('Loaded', len(records), 'patent records')
print('First record date:', records[0].get('publication_date'))

# Parse CPC codes and extract years
patent_data = []
years_found = set()
cpc_patterns = {}

for record in records:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '[]')
    
    # Parse publication year
    year = None
    if pub_date:
        try:
            parts = pub_date.split(', ')
            if len(parts) >= 2:
                year = int(parts[1])
                years_found.add(year)
        except:
            pass
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_data)
    except:
        try:
            cpc_list = ast.literal_eval(cpc_data)
        except:
            cpc_list = []
    
    # Extract CPC codes
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code and year:
            patent_data.append({'cpc_code': code, 'year': year})
            if '/' in code:
                parts = code.split('/')
                pattern = parts[0] + '/X' * len(parts[1])
                cpc_patterns[pattern] = cpc_patterns.get(pattern, 0) + 1

print('Extracted', len(patent_data), 'CPC-year entries')
print('Years found:', sorted(years_found))

if patent_data:
    print('Sample entries:', patent_data[:3])

print('Top CPC patterns:')
for pattern, count in sorted(cpc_patterns.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(' ', pattern + ':', count)

# Analyze CPC code structure
from collections import Counter
unique_codes = [p['cpc_code'] for p in patent_data]
code_counter = Counter(unique_codes)
print('Top 10 most frequent CPC codes:')
for code, count in code_counter.most_common(10):
    print(' ', code + ':', count)

print('Analyzing CPC code structure:')
for code, count in code_counter.most_common(5):
    if '/' in code:
        main_part = code.split('/')[0]
        print(' ', code + ': main_group=' + main_part)
    else:
        print(' ', code + ': no slash')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
