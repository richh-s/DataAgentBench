code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# Read German patent data from file
file_path = 'var_functions.query_db:16'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        german_patents = json.load(f)
else:
    # Fallback - assume it's a variable
    german_patents = globals().get('var_functions.query_db:16', [])
    if isinstance(german_patents, str) and os.path.exists(german_patents):
        with open(german_patents, 'r') as f:
            german_patents = json.load(f)

print(f"Loaded {len(german_patents)} German patents")

# Simple date parsing for second half 2019
def is_second_half_2019(date_str):
    if not date_str or '2019' not in str(date_str):
        return False
    
    date_lower = str(date_str).lower()
    
    # Check for months July-December
    second_half_months = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for month in second_half_months:
        if month in date_lower:
            return True
    
    # Try to extract month number
    month_patterns = [
        r'(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*2019',
        r'2019\s*-\s*(\d{1,2})\s*-\s*(\d{1,2})',
    ]
    
    for pattern in month_patterns:
        match = re.search(pattern, date_lower)
        if match and len(match.groups()) >= 1:
            try:
                month = int(match.group(1))
                if month >= 7:
                    return True
            except:
                pass
    
    return False

# Parse CPC codes
def extract_cpc_codes(cpc_json):
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
        return [item.get('code', '') for item in cpc_list if item.get('code')]
    except:
        return []

# Extract level 4 CPC
def get_cpc_level4(cpc_code):
    if not cpc_code:
        return None
    # Extract up to 4 characters before any separator
    parts = cpc_code.split('/')[0]
    # Take first 4 characters, but at least 3
    if len(parts) >= 4:
        return parts[:4]
    elif len(parts) >= 3:
        return parts
    return None

# Process patents
patent_data = []
for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    
    if is_second_half_2019(grant_date):
        cpc_codes = extract_cpc_codes(patent.get('cpc', '[]'))
        
        for cpc in cpc_codes:
            cpc_level4 = get_cpc_level4(cpc)
            if cpc_level4:
                patent_data.append({
                    'cpc_level4': cpc_level4,
                    'cpc_full': cpc,
                    'patent_info': patent.get('Patents_info', '')
                })

# Create DataFrame
df = pd.DataFrame(patent_data)

print(f"Total patent-CPC combinations: {len(df)}")
print(f"Unique CPC level 4 codes: {df['cpc_level4'].nunique()}")

if len(df) > 0:
    # Count filings per CPC level 4
    cpc_counts = df.groupby('cpc_level4').size().reset_index(name='filings')
    top_cpc = cpc_counts.nlargest(10, 'filings')
    print("Top CPC level 4 codes:")
    print(top_cpc)
else:
    print("No patents found in second half 2019")
    cpc_counts = pd.DataFrame()

result = {
    'total_combinations': len(df),
    'unique_cpc_level4': df['cpc_level4'].nunique() if len(df) > 0 else 0,
    'top_cpc': top_cpc.to_dict('records') if len(df) > 0 else []
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
