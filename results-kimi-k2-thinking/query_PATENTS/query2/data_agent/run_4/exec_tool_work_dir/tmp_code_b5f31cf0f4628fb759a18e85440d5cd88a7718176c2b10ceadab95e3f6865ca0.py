code = """import json
import pandas as pd
from datetime import datetime
import re
import numpy as np

# Load German patent data
german_patents_file = var_functions.query_db:16

with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

# Filter for second half of 2019 (July - December)
def parse_grant_date(date_str):
    if not date_str:
        return None
    # Normalize date string
    date_str = date_str.lower().replace('dated', '').replace('on', '').replace('the', '').strip()
    
    # Try to extract month and year
    patterns = [
        r'(\d{1,2})[^a-z]*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[^\d]*(2019)',
        r'(\d{1,2})[^\d]+(2019)',
        r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[^\d]+(\d{1,2})[^\d]*(2019)',
        r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[^\d]*(2019)'
    ]
    
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            groups = match.groups()
            if len(groups) == 3 and groups[0].isdigit():
                day = int(groups[0])
                month_str = groups[1][:3].lower()
                year = int(groups[2])
                if month_str in month_map:
                    month = month_map[month_str]
                    return datetime(year, month, day)
            elif len(groups) == 2 and groups[0].isdigit():
                day = int(groups[0])
                year = int(groups[1])
                # Default to July for ambiguous dates in second half
                return datetime(year, 7, day)
            elif len(groups) == 3 and groups[1].isdigit():
                month_str = groups[0][:3].lower()
                day = int(groups[1])
                year = int(groups[2])
                if month_str in month_map:
                    month = month_map[month_str]
                    return datetime(year, month, day)
            elif len(groups) == 2:
                month_str = groups[0][:3].lower()
                year = int(groups[1])
                if month_str in month_map:
                    month = month_map[month_str]
                    return datetime(year, month, 1)
    
    return None

# Parse CPC codes from JSON string
def extract_cpc_codes(cpc_json):
    try:
        cpc_list = json.loads(cpc_json)
        return [item['code'] for item in cpc_list if 'code' in item]
    except:
        return []

# Process patents
patent_data = []
for patent in german_patents:
    grant_date = parse_grant_date(patent['grant_date'])
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        cpc_codes = extract_cpc_codes(patent['cpc'])
        for cpc in cpc_codes:
            # Get level 4 CPC (first 4 characters or up to first space/slash)
            cpc_level4 = cpc.split('/')[0][:4]
            if len(cpc_level4) >= 3:  # Valid CPC code
                patent_data.append({
                    'cpc_level4': cpc_level4,
                    'cpc_full': cpc,
                    'grant_date': grant_date,
                    'month': grant_date.month,
                    'patent_info': patent['Patents_info']
                })

# Create DataFrame
df = pd.DataFrame(patent_data)
print("German patents in second half 2019:", len(df))
print("Unique CPC level 4 codes:", df['cpc_level4'].nunique())

print("__RESULT__:")
print(json.dumps({"patent_count": len(df), "cpc_count": df['cpc_level4'].nunique(), "sample_data": df.head().to_dict('records')}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
