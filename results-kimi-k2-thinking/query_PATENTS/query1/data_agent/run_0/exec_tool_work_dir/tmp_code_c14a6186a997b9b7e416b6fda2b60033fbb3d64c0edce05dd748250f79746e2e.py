code = """import json
import re
import pandas as pd

# Get the file path from storage
storage_key = 'var_functions.query_db:8'
if storage_key in locals():
    file_path = locals()[storage_key]
else:
    print(f"Storage key {storage_key} not found")
    print(f"Available locals: {list(locals().keys())}")
    file_path = None

if file_path:
    with open(file_path, 'r') as f:
        publications = json.load(f)

    print(f"Total publications loaded: {len(publications)}")

    # Extract CPC codes and years
    extracted_data = []
    for pub in publications:
        cpc_json = pub.get('cpc', '[]')
        pub_date = pub.get('publication_date', '')
        
        # Parse publication date to extract year
        year = None
        if pub_date:
            # Match year pattern (4 digits)
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
                if code and '/' in code:
                    # This is a level 5 code (has subgroup)
                    extracted_data.append({
                        'cpc_code': code,
                        'year': year
                    })
        except:
            # Skip malformed JSON
            continue

    print(f"Total CPC code-year entries extracted: {len(extracted_data)}")
    
    if extracted_data:
        df = pd.DataFrame(extracted_data)
        print(f"DataFrame shape: {df.shape}")
        print(f"Year range: {df['year'].min()} - {df['year'].max()}")
        print(f"Unique CPC codes: {df['cpc_code'].nunique()}")
        print(f"Sample data: {df.head().to_dict('records')}")
else:
    print("No file path available")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
