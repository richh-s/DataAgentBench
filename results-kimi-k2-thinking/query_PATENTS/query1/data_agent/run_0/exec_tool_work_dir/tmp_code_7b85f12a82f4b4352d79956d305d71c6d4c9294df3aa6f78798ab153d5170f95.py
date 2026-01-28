code = """import json
import re
import pandas as pd

print("Current variables in local scope:")
for key in locals().keys():
    print(f"  {key}")

# Check if we can get the result directly
result_keys = [k for k in locals().keys() if 'query_db' in k]
print(f"\nFound query_db keys: {result_keys}")

# Try to access the variable using the key
if 'var_functions.query_db:8' in locals():
    file_path = locals()['var_functions.query_db:8']
    print(f"\nFile path from key: {file_path}")
    
    # Load the data
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    print(f"Total publications loaded: {len(publications)}")
    
    # Extract CPC codes and years
    extracted_data = []
    for pub in publications[:1000]:  # Process a subset first to test
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
                    extracted_data.append({
                        'cpc_code': code,
                        'year': year
                    })
        except:
            continue

    print(f"Extracted {len(extracted_data)} CPC code-year pairs from first 1000 records")
    
    if extracted_data:
        df = pd.DataFrame(extracted_data)
        print(f"DataFrame shape: {df.shape}")
        print(f"Year range: {df['year'].min()} - {df['year'].max()}")
        print(f"Sample data:\n{df.head()}")
else:
    print("Cannot find the data key in local variables")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
