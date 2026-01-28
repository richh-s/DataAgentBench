code = """import json
import re

# Try to access the data from the file path we know about
file_path = '/tmp/tmp3s5v9f5z.json'
print('Attempting to load from:', file_path)

try:
    with open(file_path, 'r') as f:
        publications = json.load(f)
    print('Successfully loaded publications')
    print('Total publications:', len(publications))
    
    if publications:
        print('Sample publication_date:', publications[0].get('publication_date'))
        print('Sample cpc snippet:', str(publications[0].get('cpc', ''))[:150])
    
    # Now process the data to count patents per CPC per year
    patent_counts = {}
    
    for pub in publications:
        # Parse publication date
        pub_date_str = pub['publication_date']
        if pub_date_str:
            # Extract year using regex
            year_match = re.search(r'\d{4}', pub_date_str)
            if year_match:
                year = int(year_match.group())
                
                # Parse CPC codes (JSON string)
                cpc_str = pub['cpc']
                if cpc_str:
                    try:
                        cpc_list = json.loads(cpc_str)
                        for cpc_item in cpc_list:
                            code = cpc_item.get('code')
                            if code:
                                # Extract CPC group at level 5 (first part before / or space)
                                group_code = code.split('/')[0].split()[0]
                                
                                # Initialize if needed
                                if group_code not in patent_counts:
                                    patent_counts[group_code] = {}
                                
                                # Count patents per year
                                if year not in patent_counts[group_code]:
                                    patent_counts[group_code][year] = 0
                                patent_counts[group_code][year] += 1
                                
                    except (json.JSONDecodeError, TypeError):
                        # Skip malformed entries
                        continue
    
    # Show sample results
    sample_codes = list(patent_counts.keys())[:5]
    print('\nSample CPC codes processed:', sample_codes)
    for code in sample_codes:
        print(f'  {code}: {dict(list(patent_counts[code].items())[:3])}')
    
    print(f"\nTotal unique CPC groups: {len(patent_counts)}")
    print(f"Year range: {min([min(years.keys()) for years in patent_counts.values() if years])} to {max([max(years.keys()) for years in patent_counts.values() if years])}")
    
    result = {
        'status': 'success',
        'total_cpc_groups': len(patent_counts),
        'sample_data': {code: dict(list(patent_counts[code].items())[:3]) for code in sample_codes}
    }
    
except FileNotFoundError:
    print('File not found, will use variable approach')
    result = {'status': 'file_not_found', 'message': 'Need to use variable approach'}

except Exception as e:
    print('Error:', e)
    result = {'status': 'error', 'message': str(e)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
