code = """import json
import pandas as pd
from datetime import datetime
import re

# Get file paths
patents_file_path = locals()['var_functions.query_db:14']
level5_file_path = locals()['var_functions.query_db:6']

# Load data
with open(patents_file_path, 'r') as f:
    patents_data = json.load(f)

with open(level5_file_path, 'r') as f:
    level5_data = json.load(f)

level5_symbols = {item['symbol'] for item in level5_data}

# Process patents data
processed_data = []

for patent in patents_data:
    # Parse publication date
    date_str = patent.get('publication_date', '')
    if not date_str:
        continue
    
    # Extract year from date string like "Aug 3rd, 2021"
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Parse CPC codes
    cpc_str = patent.get('cpc', '')
    if not cpc_str:
        continue
    
    try:
        # The CPC field is a JSON string
        cpc_list = json.loads(cpc_str)
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code:
                continue
            
            # Extract level 5 CPC group (first part before/)
            # Format is like "C01B33/00", "A61Q", "H01M10/0565"
            group_match = re.match(r'^([A-HY][0-9]{2}[A-Z])', code)
            if group_match:
                group_code = group_match.group(1)
                # Check if it's a level 5 CPC group
                if group_code in level5_symbols:
                    processed_data.append({
                        'cpc_group': group_code,
                        'year': year,
                        'full_code': code
                    })
    except:
        # Skip if parsing fails
        continue

# Create DataFrame
df = pd.DataFrame(processed_data)

print('__RESULT__:')
print(json.dumps({
    'total_records': len(processed_data),
    'unique_cpc_groups': len(df['cpc_group'].unique()),
    'year_range': {
        'min': int(df['year'].min()),
        'max': int(df['year'].max())
    },
    'sample_data': df.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'level5_count': 677, 'sample_level5': ['G06D', 'C01C', 'H03G', 'A01F', 'A23F', 'G03F', 'B25D', 'D06L', 'F01C', 'C23D']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_patents': 277813, 'sample_data': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': 'Aug 3rd, 2021'}, {'cpc': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0893",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0886",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H3/76",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'publication_date': 'Oct 6th, 2020'}]}, 'var_functions.execute_python:18': {'total_patents': 277813, 'level5_cpc_count': 677, 'sample_level5': ['A61Q', 'B25J', 'G06V', 'C08F', 'F21L', 'F22D', 'G10D', 'F26B', 'B62C', 'F04F']}}

exec(code, env_args)
