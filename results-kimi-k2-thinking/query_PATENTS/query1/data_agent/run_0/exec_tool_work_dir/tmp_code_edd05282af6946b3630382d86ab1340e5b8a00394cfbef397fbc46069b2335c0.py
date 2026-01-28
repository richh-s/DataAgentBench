code = """import json
import re
import pandas as pd

# Try to get the file path
storage_key = 'var_functions.query_db:8'

# Iterate through available locals to find our key
found = False
for var_name in list(locals().keys()):
    if storage_key in var_name:
        file_path = locals()[var_name]
        print("Found file path:", file_path)
        found = True
        break

if not found:
    # If variable not in locals directly, we need to access it through the system
    # For now, let's try a different approach - re-query with a limit for testing
    print("File path variable not accessible, will need to re-query")
else:
    # Load and process the data
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    print("Total publications loaded:", len(publications))
    
    # Extract CPC codes and years
    extracted_data = []
    for pub in publications[:5000]:  # Start with smaller subset
        cpc_json = pub.get('cpc', '[]')
        pub_date = pub.get('publication_date', '')
        
        # Parse publication date to extract year
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
                if code and '/' in code and len(code.split('/')[0]) >= 3:
                    extracted_data.append({
                        'cpc_code': code,
                        'year': year
                    })
        except Exception as e:
            continue
    
    print("Extracted CPC code-year pairs:", len(extracted_data))
    
    if extracted_data:
        df = pd.DataFrame(extracted_data)
        print("DataFrame shape:", df.shape)
        print("Year range:", df['year'].min(), "to", df['year'].max())
        print("Sample data:")
        print(df.head().to_string())
        
        # Count per year
        yearly_counts = df['year'].value_counts().sort_index()
        print("\nPublication counts by year:")
        print(yearly_counts.to_string())"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
