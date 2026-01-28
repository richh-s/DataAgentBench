code = """import json
import pandas as pd
import re
from datetime import datetime
import numpy as np

# Read the patent data from the file
file_path = locals()['var_functions.query_db:38']

with open(file_path, 'r') as f:
    patent_data = json.load(f)

# Extract CPC codes and dates
cpc_records = []

for record in patent_data:
    pub_date = record['publication_date']
    cpc_json = record['cpc']
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            full_code = cpc_item['code']
            # Extract level 4 CPC (everything before the slash, e.g., H01L31 from H01L31/036)
            if '/' in full_code:
                level4_code = full_code.split('/')[0]
                # Ensure it's at least 4 characters (section + class + subclass + group)
                if len(level4_code) >= 4:
                    cpc_records.append({
                        'cpc_code': level4_code,
                        'publication_date': pub_date
                    })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(cpc_records)

# Extract month numbers (July-December 2019)
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

df['month'] = df['publication_date'].apply(extract_month)
df = df.dropna(subset=['month'])

# Count patents per CPC code per month
cpc_month_counts = df.groupby(['cpc_code', 'month']).size().reset_index(name='count')

# Create complete time series for each CPC code (all months 7-12 in order)
all_months = [7, 8, 9, 10, 11, 12]
ema_results = []

for cpc_code in cpc_month_counts['cpc_code'].unique():
    # Get counts for this CPC code in chronological order
    cpc_data = cpc_month_counts[cpc_month_counts['cpc_code'] == cpc_code]
    
    # Create full monthly counts array
    monthly_counts = []
    for month in all_months:
        count = cpc_data[cpc_data['month'] == month]['count'].sum() if not cpc_data[cpc_data['month'] == month].empty else 0
        monthly_counts.append(count)
    
    # Calculate Exponential Moving Average (EMA) with alpha=0.1
    alpha = 0.1
    ema_values = []
    
    # Initialize EMA with first value
    ema = monthly_counts[0]
    ema_values.append(ema)
    
    # Calculate EMA for remaining months
    for i in range(1, len(monthly_counts)):
        ema = alpha * monthly_counts[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    # Find the month with highest EMA
    max_ema_idx = ema_values.index(max(ema_values))
    best_month = all_months[max_ema_idx]
    best_ema = ema_values[max_ema_idx]
    best_count = monthly_counts[max_ema_idx]
    
    ema_results.append({
        'cpc_code': cpc_code,
        'best_month': best_month,
        'best_month_name': datetime(2019, best_month, 1).strftime('%B'),
        'best_month_count': int(best_count),
        'best_month_ema': float(best_ema),
        'total_2019': int(sum(monthly_counts)),
        'monthly_counts': monthly_counts,
        'ema_values': [float(x) for x in ema_values]
    })

# Create DataFrame and sort by best EMA
results_df = pd.DataFrame(ema_results)
results_df = results_df.sort_values('best_month_ema', ascending=False)

# Get top 10 CPC codes
top_10 = results_df.head(10)

print('__RESULT__:')
print(top_10[['cpc_code', 'best_month', 'best_month_name', 'best_month_count', 'best_month_ema', 'total_2019']].to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'publication_date': '21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'publication_date': 'December the 5th, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'publication_date': 'on August 22nd, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:18': [], 'var_functions.execute_python:26': [{'cpc_code': 'H01L31', 'best_month': 7, 'best_month_count': 17, 'best_month_ema': 17.0, 'total_2019': 17}, {'cpc_code': 'G06V10', 'best_month': 7, 'best_month_count': 8, 'best_month_ema': 8.0, 'total_2019': 10}, {'cpc_code': 'H02M1', 'best_month': 7, 'best_month_count': 7, 'best_month_ema': 7.0, 'total_2019': 7}, {'cpc_code': 'F02M61', 'best_month': 7, 'best_month_count': 6, 'best_month_ema': 6.0, 'total_2019': 6}, {'cpc_code': 'G02B15', 'best_month': 7, 'best_month_count': 5, 'best_month_ema': 5.0, 'total_2019': 5}, {'cpc_code': 'G02B23', 'best_month': 7, 'best_month_count': 5, 'best_month_ema': 5.0, 'total_2019': 5}, {'cpc_code': 'G06V20', 'best_month': 7, 'best_month_count': 4, 'best_month_ema': 4.0, 'total_2019': 6}, {'cpc_code': 'A61B1', 'best_month': 7, 'best_month_count': 3, 'best_month_ema': 3.0, 'total_2019': 3}, {'cpc_code': 'B01D29', 'best_month': 7, 'best_month_count': 3, 'best_month_ema': 3.0, 'total_2019': 3}, {'cpc_code': 'G01M11', 'best_month': 7, 'best_month_count': 3, 'best_month_ema': 3.0, 'total_2019': 3}], 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'symbol': 'H01L2924/01069', 'titleFull': 'Thulium [Tm]', 'level': '9.0'}, {'symbol': 'H01L2924/01085', 'titleFull': 'Astatine [At]', 'level': '9.0'}, {'symbol': 'H01L2924/01023', 'titleFull': 'Vanadium [V]', 'level': '9.0'}, {'symbol': 'H01L2221/1068', 'titleFull': 'Formation and after-treatment of conductors', 'level': '9.0'}, {'symbol': 'H01L2221/1005', 'titleFull': 'Formation and after-treatment of dielectrics', 'level': '9.0'}, {'symbol': 'H01L2221/683', 'titleFull': 'Apparatus for handling semiconductor or electric solid state devices during manufacture or treatment thereof; Apparatus for handling wafers during manufacture or treatment of semiconductor or electric solid state devices or components; Apparatus not specifically provided for elsewhere for supporting or gripping', 'level': '9.0'}, {'symbol': 'H01L2223/64', 'titleFull': 'Impedance arrangements', 'level': '9.0'}, {'symbol': 'H01L2224/18', 'titleFull': 'High density interconnect [HDI] connectors; Manufacturing methods related thereto', 'level': '9.0'}, {'symbol': 'H01L2224/02', 'titleFull': 'Bonding areas; Manufacturing methods related thereto', 'level': '9.0'}, {'symbol': 'H01L2224/63', 'titleFull': 'Connectors not provided for in any of the groups H01L2224/10\xa0-\xa0H01L2224/50 and subgroups; Manufacturing methods related thereto', 'level': '9.0'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
