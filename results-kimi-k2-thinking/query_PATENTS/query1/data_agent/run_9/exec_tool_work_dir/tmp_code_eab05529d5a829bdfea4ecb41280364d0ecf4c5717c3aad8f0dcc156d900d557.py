code = """# Access data using globals() with the exact key name
import json
import pandas as pd
import re

# Get the data file path from storage
key = "var_functions.query_db_48"
if key in globals():
    data_file = globals()[key]
    print("Found data file:", data_file)
else:
    print("Key not found, trying alternatives...")
    # List all globals with query_db
    for k in globals().keys():
        if "query_db" in str(k):
            print("  ", k)
    data_file = globals().get(key, None)

if data_file:
    with open(data_file, 'r') as f:
        pub_data = json.load(f)
    
    print("Loaded records:", len(pub_data))
    
    # Process data
    records = []
    for item in pub_data:
        try:
            cpc_json = item['cpc']
            pub_date = item['publication_date']
            
            year_match = re.search(r'(\d{4})', pub_date)
            if year_match:
                year = int(year_match.group(1))
                
                cpc_list = json.loads(cpc_json)
                for entry in cpc_list:
                    code = entry.get('code', '')
                    if len(code) >= 5:
                        group_5 = code[:5]
                        records.append({'year': year, 'cpc_group_5': group_5, 'count': 1})
        except:
            continue
    
    df = pd.DataFrame(records)
    print("Records:", len(df))
    print("Years:", sorted(df['year'].unique()))
    print("Groups:", df['cpc_group_5'].nunique())
    
    result = {'records': len(df), 'years': len(df['year'].unique()), 'groups': df['cpc_group_5'].nunique()}
else:
    result = {'error': 'No data file found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:51': []}

exec(code, env_args)
