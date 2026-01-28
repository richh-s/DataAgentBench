code = """import json
import re
import pandas as pd

# Load the publication data
storage_key = 'var_functions.query_db:8'
file_path = locals().get(storage_key, None)

if file_path is None:
    print('File path not accessible, need to re-query')
else:
    # Read the data
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    print('Total publications loaded:', len(publications))
    
    # Extract CPC codes and years
    extracted_data = []
    for pub in publications:
        cpc_json = pub.get('cpc', '[]')
        pub_date = pub.get('publication_date', '')
        
        # Get year from date
        year = None
        if pub_date:
            match = re.search(r'(\d{4})', pub_date)
            if match:
                year = int(match.group(1))
        
        if not year:
            continue
        
        # Parse CPC codes
        try:
            if isinstance(cpc_json, str):
                cpc_list = json.loads(cpc_json)
            else:
                cpc_list = cpc_json
                
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                # Check if level 5: has subgroup and length is appropriate
                if code and '/' in code and len(code.split('/')[0]) >= 3:
                    extracted_data.append({'cpc_code': code, 'year': year})
        except:
            continue
    
    print('Extracted CPC-year pairs:', len(extracted_data))
    
    if extracted_data:
        df = pd.DataFrame(extracted_data)
        print('DataFrame shape:', df.shape)
        print('Year range:', df['year'].min(), 'to', df['year'].max())
        print('Unique CPC codes:', df['cpc_code'].nunique())
        
        # Show first few rows
        print('Sample data:')
        print(df.head())
        
        # Get publications per year
        yearly_counts = df['year'].value_counts().sort_index()
        print('Publications per year:')
        for year, count in yearly_counts.items():
            print(year, ':', count)
    else:
        print('No data extracted')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
