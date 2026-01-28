code = """import json
import pandas as pd
import numpy as np
import re
from collections import defaultdict

# Load data from file
file_path = var_functions.query_db:34 if isinstance(var_functions.query_db:34, str) else '/tmp/tmpt7f2i29k.json'
with open(file_path, 'r', encoding='utf-8') as f:
    german_patents = json.load(f)

# Parse CPC codes
def extract_cpc_codes(cpc_field):
    try:
        if isinstance(cpc_field, str):
            return json.loads(cpc_field)
        return cpc_field if isinstance(cpc_field, list) else []
    except Exception:
        return []

# Extract month from grant date (focusing on second half 2019)
def extract_month_and_filter(date_str):
    if not date_str or '2019' not in str(date_str):
        return None
    
    date_lower = str(date_str).lower()
    
    # Check for second half months
    month_map = {
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    for month_name, month_num in month_map.items():
        if month_name in date_lower:
            return month_num
    
    # If no month found but it's 2019, check if it mentions second half
    if any(term in date_lower for term in ['september', 'october', 'november', 'december', 'july', 'august']):
        for month_name, month_num in {'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}.items():
            if month_name in date_lower:
                return month_num
    
    return None

# Process patents and count filings
cpc_month_data = []
successful_parses = 0

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = extract_month_and_filter(grant_date)
    
    if not month:  # Skip if not second half 2019
        continue
    
    successful_parses += 1
    cpc_codes = extract_cpc_codes(patent.get('cpc', '[]'))
    
    for cpc_item in cpc_codes:
        code = cpc_item.get('code', '') if isinstance(cpc_item, dict) else cpc_item.get('code', '')
        if not code:
            continue
        
        # Extract CPC level 4 (first 4 characters of main class)
        level4 = code.split('/')[0][:4] if '/' in code else code[:4]
        if len(level4) < 3:
            continue
        
        cpc_month_data.append({
            'cpc_level4': level4,
            'month': month,
            'year': 2019
        })

print(f"Successfully processed {successful_parses} patents from second half 2019")
print(f"Total CPC-month records: {len(cpc_month_data)}")

# Create DataFrame for analysis
df = pd.DataFrame(cpc_month_data)
if len(df) == 0:
    raise ValueError("No valid CPC data found for second half 2019")

df_counts = df.groupby(['cpc_level4', 'month']).size().reset_index(name='filings')
print(f"Unique CPC level 4 codes: {df['cpc_level4'].nunique()}")
print(f"Months covered: {sorted(df['month'].unique())}")

# Calculate EMA for each CPC code (July-December)
months = [7, 8, 9, 10, 11, 12]
alpha = 0.1

cpc_results = []
cpc_groups = df['cpc_level4'].unique()

for cpc in cpc_groups:
    # Get monthly filings
    monthly_filings = []
    for month in months:
        count = df_counts[(df_counts['cpc_level4'] == cpc) & (df_counts['month'] == month)]['filings'].sum()
        monthly_filings.append(count)
    
    total_filings = sum(monthly_filings)
    if total_filings == 0:
        continue
    
    # Calculate EMA manually
    ema = []
    current_ema = monthly_filings[0]
    ema.append(current_ema)
    
    for i in range(1, len(monthly_filings)):
        current_ema = alpha * monthly_filings[i] + (1 - alpha) * current_ema
        ema.append(current_ema)
    
    # Find best month (highest EMA)
    max_ema_idx = np.argmax(ema)
    best_month = months[max_ema_idx]
    best_ema = ema[max_ema_idx]
    
    # Store results
    cpc_results.append({
        'cpc_level4': cpc,
        'best_month': best_month,
        'best_ema': round(best_ema, 2),
        'total_filings': total_filings,
        'monthly_breakdown': dict(zip(months, monthly_filings))
    })

# Sort by best EMA value
cpc_results.sort(key=lambda x: x['best_ema'], reverse=True)

print(f"Calculated EMA for {len(cpc_results)} CPC groups")
print("\nTop 10 by EMA:")
for i, r in enumerate(cpc_results[:10]):
    print(f"{i+1}. {r['cpc_level4']} - EMA: {r['best_ema']} (Month {r['best_month']}, Total: {r['total_filings']})")

print("__RESULT__:")
print(json.dumps(cpc_results[:50]))  # Top 50 for title lookup"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'total_combinations': 439, 'unique_cpc_level4': 68, 'top_cpc': [{'cpc_level4': 'B01J', 'filings': 57}, {'cpc_level4': 'C04B', 'filings': 45}, {'cpc_level4': 'B01D', 'filings': 28}, {'cpc_level4': 'H01R', 'filings': 24}, {'cpc_level4': 'H04W', 'filings': 22}, {'cpc_level4': 'G02B', 'filings': 20}, {'cpc_level4': 'B29C', 'filings': 19}, {'cpc_level4': 'F02D', 'filings': 16}, {'cpc_level4': 'H04L', 'filings': 16}, {'cpc_level4': 'F01N', 'filings': 15}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
