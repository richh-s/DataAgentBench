code = """# Load required libraries
import json
import pandas as pd
import re
from datetime import datetime
import numpy as np

# Read the patent data file
with open('/tmp/tmp6x9a2b2b.json', 'r') as f:
    patent_data = json.load(f)

print(f"Total records: {len(patent_data)}")
print("Sample record structure:")
print(json.dumps(patent_data[0], indent=2)[:500])

# Initialize list to store processed data
processed_patents = []

# Process each patent record
for record in patent_data:
    try:
        # Parse CPC field (JSON-like string)
        cpc_str = record.get('cpc', '[]')
        if not cpc_str or cpc_str == 'null':
            continue
            
        cpc_list = json.loads(cpc_str)
        
        # Parse publication date
        pub_date_str = record.get('publication_date', '')
        if not pub_date_str:
            continue
            
        # Extract year from date like "Aug 3rd, 2021"
        date_match = re.search(r'(\d{4})', pub_date_str)
        if date_match:
            year = int(date_match.group(1))
        else:
            continue
            
        # Extract CPC codes
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code', '')
            if cpc_code:
                processed_patents.append({
                    'cpc_code': cpc_code,
                    'year': year,
                    'patent_id': len(processed_patents)  # for counting
                })
    except Exception as e:
        # Skip problematic records
        continue

print(f"\nTotal processed CPC assignments: {len(processed_patents)}")
if processed_patents:
    print(f"Sample: {processed_patents[:3]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
