code = """import json
import pandas as pd
import numpy as np
import os
from datetime import datetime

# Load the publication data
storage_key = 'var_functions.query_db:8'
file_path = globals().get(storage_key) or locals().get(storage_key)

if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = file_path if isinstance(file_path, list) else []

print(f"Loaded {len(data)} records")

# Process CPC codes and extract years
cpc_years = []
for record in data:
    pub_date = record.get('publication_date', '')
    if not pub_date:
        continue
    
    # Extract year
    try:
        year = int(pub_date.split()[-1])
    except:
        continue
    
    # Parse CPC codes
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code', '')
            if cpc_code:
                cpc_years.append({'cpc_code': cpc_code, 'year': year})
    except:
        continue

print(f"Total CPC-year pairs: {len(cpc_years)}")

# Create DataFrame and save for later use
if cpc_years:
    df_cpc_years = pd.DataFrame(cpc_years)
    # Save to a known location
    output_file = '/tmp/cpc_years_full.json'
    df_cpc_years.to_json(output_file, orient='records')
    print(f"Saved to {output_file}")
    print("Year range:", df_cpc_years['year'].min(), "to", df_cpc_years['year'].max())
    print("Sample data:")
    print(df_cpc_years.head())
    result_msg = f"Processed {len(cpc_years)} records, years {df_cpc_years['year'].min()}-{df_cpc_years['year'].max()}"
else:
    result_msg = "No data processed"

print("__RESULT__:")
print(json.dumps(result_msg))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
