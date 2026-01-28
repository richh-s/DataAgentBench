code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the query results using locals() to access the variable
file_path = locals()['var_functions.query_db:5']

with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Filter for German patents and second half of 2019
german_patents = []
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    
    # Check if it's a German patent
    if 'DE-' in patents_info:
        # Check if it's 2019
        if '2019' in grant_date:
            # Try to extract month
            month = None
            grant_date_lower = grant_date.lower()
            
            for month_name, month_num in month_map.items():
                if month_name in grant_date_lower:
                    month = month_num
                    break
            
            # If we found a month and it's in second half (July-Dec)
            if month and month >= 7:
                # Extract CPC codes
                try:
                    cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
                    cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
                except:
                    cpc_codes = []
                
                if cpc_codes:  # Only add if there are CPC codes
                    german_patents.append({
                        'patents_info': patents_info,
                        'grant_date': grant_date,
                        'grant_month': month,
                        'cpc_codes': cpc_codes
                    })

print('__RESULT__:')
print(json.dumps({
    'total_german_patents': len(german_patents),
    'sample_patents': german_patents[:5] if german_patents else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
