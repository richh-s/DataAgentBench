code = """import json, os, re

# The previous tool call stored the result in a variable, let's access it
# Check what variables are available
print("Variables available:", [k for k in locals().keys() if k.startswith('var_')])

# Access the query result
patents_data = locals().get('var_functions.query_db:9')
if isinstance(patents_data, str):
    # It's a file path
    with open(patents_data, 'r') as f:
        patents_data = json.load(f)
elif patents_data is None:
    # Try to find it
    for key in locals().keys():
        if 'query_db' in key and '9' in key:
            patents_data = locals()[key]
            print(f"Using variable: {key}")
            break

print(f"Total patents: {len(patents_data) if isinstance(patents_data, list) else 'Not loaded'}")

# If we have the data, let's process it
if isinstance(patents_data, list):
    # Filter for German patents in second half of 2019
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
    german_patents = []
    
    for patent in patents_data:
        grant_date = patent.get('grant_date', '')
        patents_info = patent.get('Patents_info', '')
        
        # Check if second half of 2019
        is_second_half = any(month in grant_date for month in second_half_months) and '2019' in grant_date
        
        # Check if German patent
        is_german = ' DE ' in patents_info or ' DE-' in patents_info or patents_info.startswith('The DE ') or 'from DE' in patents_info
        
        if is_second_half and is_german:
            german_patents.append(patent)
    
    print(f"German patents in second half 2019: {len(german_patents)}")
    
    # Debug: show first few German patents
    for i, p in enumerate(german_patents[:5]):
        print(f"  {i+1}. {p['grant_date']} - {p['Patents_info'][:100]}...")
else:
    # The variable contains the file path directly
    file_path = patents_data
    print(f"File path: {file_path}")
    if os.path.exists(str(file_path)):
        with open(str(file_path), 'r') as f:
            patents_data = json.load(f)
        print(f"Loaded {len(patents_data)} patents")
    else:
        print("File not found", file_path)"""

env_args = {'var_functions.list_db:0': ['cpc_definition'], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
