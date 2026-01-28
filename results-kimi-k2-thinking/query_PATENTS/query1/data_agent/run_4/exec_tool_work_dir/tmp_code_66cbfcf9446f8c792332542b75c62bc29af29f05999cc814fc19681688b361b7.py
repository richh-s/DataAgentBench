code = """import json
import re

# Get file path for query_db_28
file_path = '/tmp/tmp6y9g1h9v.json'
print('Loading publications from:', file_path)

try:
    with open(file_path, 'r') as f:
        publications = json.load(f)
    print(f'Successfully loaded {len(publications)} publications')
    
    # Show sample data structure
    if publications:
        print('\nSample record:')
        print('Keys:', list(publications[0].keys()))
        print('Publication date:', publications[0].get('publication_date'))
        print('CPC codes snippet:', str(publications[0].get('cpc', ''))[:200])
    
    # Extract CPC codes and count patents per CPC group per year
    patent_counts = {}
    year_range = set()
    
    for pub in publications:
        pub_date_str = pub.get('publication_date', '')
        if pub_date_str:
            # Extract year
            year_match = re.search(r'\d{4}', pub_date_str)
            if year_match:
                year = int(year_match.group())
                year_range.add(year)
                
                # Parse CPC codes
                cpc_str = pub.get('cpc', '')
                if cpc_str:
                    try:
                        cpc_list = json.loads(cpc_str)
                        for cpc_item in cpc_list:
                            code = cpc_item.get('code', '')
                            if code:
                                # Extract level 5 CPC group (main symbol)
                                # Format: A01B33/00 -> A01B33 (level depends on structure)
                                group_code = code.split('/')[0].split()[0]
                                
                                # Initialize counters
                                if group_code not in patent_counts:
                                    patent_counts[group_code] = {}
                                patent_counts[group_code][year] = patent_counts[group_code].get(year, 0) + 1
                                
                    except (json.JSONDecodeError, TypeError) as e:
                        continue
    
    print(f'\nYear range: {sorted(year_range)}')
    print(f'Total CPC groups found: {len(patent_counts)}')
    
    # Show sample CPC counts
    sample_codes = list(patent_counts.keys())[:5]
    for code in sample_codes:
        counts = patent_counts[code]
        print(f'  {code}: {counts}')
    
    result = {
        'status': 'success',
        'publication_count': len(publications),
        'cpc_groups_found': len(patent_counts),
        'year_range': sorted(year_range),
        'sample_data': {code: patent_counts[code] for code in sample_codes}
    }
    
except Exception as e:
    print('Error:', e)
    result = {'status': 'error', 'message': str(e)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
