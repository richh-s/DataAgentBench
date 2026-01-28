code = """import json, re

# Access the data from the storage variable directly
# The file path is provided in the previous message
publications = []

# Try multiple approaches to get the data
import os
import glob

# Look for the JSON file in /tmp directory
tmp_files = glob.glob('/tmp/*.json')
print('JSON files in /tmp:', tmp_files)

if tmp_files:
    # Use the most recent file
    tmp_files.sort(key=os.path.getctime, reverse=True)
    file_path = tmp_files[0]
    print('Using file:', file_path)
    
    try:
        with open(file_path, 'r') as f:
            publications = json.load(f)
        print('Successfully loaded', len(publications), 'publications')
    except Exception as e:
        print('Error loading file:', e)
else:
    print('No JSON files found')

# Process the data
if publications:
    patent_counts = {}
    
    for pub in publications:
        pub_date_str = pub['publication_date']
        if pub_date_str:
            year_match = re.search(r'\d{4}', pub_date_str)
            if year_match:
                year = int(year_match.group())
                cpc_str = pub['cpc']
                if cpc_str:
                    try:
                        cpc_list = json.loads(cpc_str)
                        for cpc_item in cpc_list:
                            code = cpc_item.get('code')
                            if code:
                                group_code = code.split('/')[0].split()[0]
                                if group_code not in patent_counts:
                                    patent_counts[group_code] = {}
                                patent_counts[group_code][year] = patent_counts[group_code].get(year, 0) + 1
                    except:
                        continue
    
    print('Processed', len(patent_counts), 'CPC groups')
    
    # Find year range
    all_years = []
    for years_dict in patent_counts.values():
        all_years.extend(years_dict.keys())
    
    if all_years:
        min_year = min(all_years)
        max_year = max(all_years)
        print(f'Year range: {min_year} to {max_year}')
    
    # Show sample
    sample = dict(list(patent_counts.items())[:3])
    print('Sample:', json.dumps(sample))
    
    # Save to file for next steps
    with open('/tmp/patent_counts.json', 'w') as f:
        json.dump(patent_counts, f)
    
    result = {'status': 'success', 'cpc_count': len(patent_counts), 'year_range': [min_year, max_year]}
else:
    result = {'status': 'no_data'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
