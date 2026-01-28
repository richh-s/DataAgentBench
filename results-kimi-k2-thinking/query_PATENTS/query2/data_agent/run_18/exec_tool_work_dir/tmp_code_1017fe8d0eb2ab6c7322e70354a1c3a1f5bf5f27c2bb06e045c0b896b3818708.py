code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the data from the file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and dates
cpc_records = []

for record in data:
    pub_date = record['publication_date']
    
    # Parse CPC codes
    cpc_json = record['cpc']
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            full_code = cpc_item['code']
            # Extract level 4 CPC (e.g., A01B1 from A01B1/002)
            parts = full_code.split('/')
            if len(parts) >= 2 and len(parts[0]) >= 4:
                level4_code = parts[0]
                cpc_records.append({
                    'cpc_code': level4_code,
                    'month': pub_date
                })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(cpc_records)

# Extract month numbers
month_map = {
    'July': 7, 'Jul': 7,
    'August': 8, 'Aug': 8,
    'September': 9, 'Sep': 9,
    'October': 10, 'Oct': 10,
    'November': 11, 'Nov': 11,
    'December': 12, 'Dec': 12
}

def extract_month(date_str):
    for month_name, month_num in month_map.items():
        if month_name.lower() in date_str.lower():
            return month_num
    return None

df['month_num'] = df['month'].apply(extract_month)
df = df.dropna(subset=['month_num'])

# Count patents per CPC code per month
cpc_counts = df.groupby(['cpc_code', 'month_num']).size().reset_index(name='count')

# Create complete time series for each CPC code (all months 7-12)
all_months = [7, 8, 9, 10, 11, 12]
result_data = []

for cpc_code in cpc_counts['cpc_code'].unique():
    # Get counts for this CPC code
    cpc_data = cpc_counts[cpc_counts['cpc_code'] == cpc_code]
    
    # Create full time series
    monthly_counts = []
    for month in all_months:
        count = cpc_data[cpc_data['month_num'] == month]['count'].sum()
        monthly_counts.append(count)
    
    # Calculate EMA
    alpha = 0.1
    ema_values = []
    ema = monthly_counts[0]
    ema_values.append(ema)
    
    for i in range(1, len(monthly_counts)):
        ema = alpha * monthly_counts[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    # Find best month (highest EMA)
    best_idx = ema_values.index(max(ema_values))
    best_month = all_months[best_idx]
    best_ema = ema_values[best_idx]
    best_count = monthly_counts[best_idx]
    
    result_data.append({
        'cpc_code': cpc_code,
        'best_month': best_month,
        'best_month_count': best_count,
        'best_month_ema': best_ema,
        'total_2019': sum(monthly_counts)
    })

# Sort by EMA and get top results
result_df = pd.DataFrame(result_data)
top_cpc = result_df.nlargest(10, 'best_month_ema')

print('__RESULT__:')
print(top_cpc.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'publication_date': '21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'publication_date': 'December the 5th, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'publication_date': 'on August 22nd, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:18': []}

exec(code, env_args)
