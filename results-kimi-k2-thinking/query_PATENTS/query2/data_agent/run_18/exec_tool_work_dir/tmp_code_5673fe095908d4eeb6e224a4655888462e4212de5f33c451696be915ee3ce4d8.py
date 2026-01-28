code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read the data from the file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and dates
cpc_data = []

for record in data:
    # Parse publication date to get year and month
    pub_date = record['publication_date']
    # Extract year from the date string
    year_match = re.search(r'2019', pub_date)
    if year_match:
        year = 2019
        # Try to extract month
        month_patterns = [
            (r'July|Jul', 7),
            (r'August|Aug', 8),
            (r'September|Sep', 9),
            (r'October|Oct', 10),
            (r'November|Nov', 11),
            (r'December|Dec', 12)
        ]
        
        month = None
        for pattern, month_num in month_patterns:
            if re.search(pattern, pub_date, re.IGNORECASE):
                month = month_num
                break
        
        # Parse CPC codes (JSON string)
        cpc_json = record['cpc']
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                full_code = cpc_item['code']
                # Extract level 4 CPC (group level, e.g., A01B1/00 from A01B1/002)
                # Level 4 is the group before the last slash group
                parts = full_code.split('/')
                if len(parts) >= 2:
                    # Take the subclass + group (e.g., A01B1)
                    subclass_part = parts[0]
                    if len(subclass_part) >= 4:
                        # This should be level 4: subclass + group
                        level4_code = subclass_part
                        cpc_data.append({
                            'year': year,
                            'month': month,
                            'cpc_code': level4_code,
                            'full_code': full_code
                        })
        except:
            continue

# Create DataFrame
df = pd.DataFrame(cpc_data)

# Count patents by CPC code and month
cpc_month_counts = df.groupby(['cpc_code', 'month']).size().reset_index(name='count')

# Create a complete dataframe with all months and CPC codes
all_months = [7, 8, 9, 10, 11, 12]
all_cpc_codes = cpc_month_counts['cpc_code'].unique()

complete_df = []
for cpc_code in all_cpc_codes:
    for month in all_months:
        count = cpc_month_counts[(cpc_month_counts['cpc_code'] == cpc_code) & 
                                 (cpc_month_counts['month'] == month)]['count'].sum()
        complete_df.append({
            'cpc_code': cpc_code,
            'month': month,
            'count': count
        })

complete_df = pd.DataFrame(complete_df)

# Sort by cpc_code and month
complete_df = complete_df.sort_values(['cpc_code', 'month'])

# Function to calculate exponential moving average
def calculate_ema(counts, alpha=0.1):
    """Calculate exponential moving average"""
    ema_values = []
    if not counts:
        return ema_values
    
    # Initialize with first value
    ema = counts[0]
    ema_values.append(ema)
    
    for i in range(1, len(counts)):
        ema = alpha * counts[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    return ema_values

# Calculate EMA for each CPC code
ema_results = []

for cpc_code in all_cpc_codes:
    # Get counts in chronological order
    cpc_months = complete_df[complete_df['cpc_code'] == cpc_code].copy()
    cpc_months = cpc_months.sort_values('month')
    
    # Extract counts as list
    counts = cpc_months['count'].tolist()
    
    # Calculate EMA
    ema_values = calculate_ema(counts, alpha=0.1)
    
    # Store results with months
    for i, month in enumerate(cpc_months['month'].tolist()):
        ema_results.append({
            'cpc_code': cpc_code,
            'month': month,
            'count': counts[i],
            'ema': ema_values[i]
        })

ema_df = pd.DataFrame(ema_results)

# Find best month (highest EMA) for each CPC code
best_months = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Get top 20 CPC codes by maximum EMA
top_cpc = best_months.nlargest(20, 'ema')

# Get CPC definitions for top codes
cpc_codes_list = top_cpc['cpc_code'].tolist()
print('__RESULT__:')
print(json.dumps({
    'top_cpc_codes': cpc_codes_list,
    'total_results': len(best_months)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'publication_date': '21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'publication_date': 'December the 5th, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'publication_date': 'on August 22nd, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:18': []}

exec(code, env_args)
