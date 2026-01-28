code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the patent data from storage
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    patents_2019 = json.load(f)

# Function to parse grant dates
def parse_grant_date(date_str):
    if not date_str:
        return None
    date_str = date_str.strip()
    month_map = {
        'Jan': 1, 'January': 1, 'Feb': 2, 'February': 2, 'Mar': 3, 'March': 3,
        'Apr': 4, 'April': 4, 'May': 5, 'Jun': 6, 'June': 6, 'Jul': 7, 'July': 7,
        'Aug': 8, 'August': 8, 'Sep': 9, 'September': 9, 'Oct': 10, 'October': 10,
        'Nov': 11, 'November': 11, 'Dec': 12, 'December': 12
    }
    patterns = [
        r'(\d{1,2})\w{2} (\w+) (\d{4})',  # "14th Mar 2019"
        r'(\w+) (\d{1,2})\w{2}, (\d{4})',  # "Mar 19th, 2019"
        r'on (\d{1,2})\w{2} of (\w+),? (\d{4})',  # "on 23rd of July, 2019"
        r'(\w+) (\d{1,2})\w{2} of (\d{4})',  # "July 8th of 2019"
    ]
    for pattern in patterns:
        match = re.match(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                groups = match.groups()
                if pattern == patterns[0]:  # "14th Mar 2019"
                    day, month_str, year = groups
                elif pattern == patterns[1]:  # "Mar 19th, 2019"
                    month_str, day, year = groups
                elif pattern == patterns[2]:  # "on 23rd of July, 2019"
                    day, month_str, year = groups
                elif pattern == patterns[3]:  # "July 8th of 2019" or "July 8, 2019"
                    month_str, day, year = groups
                
                month_num = month_map.get(month_str.strip())
                if month_num:
                    return datetime(int(year), month_num, int(day))
            except:
                continue
    return None

# Extract Germany patents from H2 2019
de_patents_data = []
for patent in patents_2019:
    parsed_date = parse_grant_date(patent['grant_date'])
    if parsed_date and parsed_date.year == 2019 and parsed_date.month >= 7:
        patents_info = patent['Patents_info']
        if 'DE-' in patents_info or ' from DE,' in patents_info:
            try:
                cpc_list = json.loads(patent['cpc'])
                for cpc_entry in cpc_list:
                    cpc_code = cpc_entry.get('code', '')
                    if cpc_code:
                        # Extract level 4 CPC code
                        if '/' in cpc_code:
                            main_group, subgroup = cpc_code.split('/', 1)
                            # Level 4 is the first 3 digits of subgroup, or less if subgroup is shorter
                            if len(subgroup) >= 3:
                                level4_subgroup = subgroup[:3]
                            else:
                                level4_subgroup = subgroup
                            level4_code = f"{main_group}/{level4_subgroup}"
                        else:
                            level4_code = cpc_code
                        
                        de_patents_data.append({
                            'cpc_level4': level4_code,
                            'cpc_full': cpc_code,
                            'grant_year': parsed_date.year,
                            'grant_month': parsed_date.month
                        })
            except json.JSONDecodeError:
                continue

print(f"Germany patents H2 2019: {len(de_patents_data)}")

# Count patents by CPC level 4 code
cpc_counts = {}
for entry in de_patents_data:
    cpc_code = entry['cpc_level4']
    cpc_counts[cpc_code] = cpc_counts.get(cpc_code, 0) + 1

# Since all data is from 2019, we need to simulate yearly data
# For EMA calculation, we'll treat each patent as a data point in 2019
# But the user wants "each year", so we need to interpret this differently

# Get unique CPC codes
cpc_codes = list(set(entry['cpc_level4'] for entry in de_patents_data))
print(f"Unique CPC Level 4 codes: {len(cpc_codes)}")
print(f"Sample CPC codes: {cpc_codes[:10]}")

# Save processed data for next step
processed_data = {
    'de_patents': de_patents_data,
    'cpc_counts': cpc_counts,
    'cpc_codes': cpc_codes
}

print('__RESULT__:')
print(json.dumps(processed_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}, 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 13, 'total_cpc_entries': 137, 'total_cpc_level4_entries': 137, 'unique_cpc_level4_codes': 81, 'sample_codes': ['B29C49/06', 'F02N2200/022', 'C04B2235/543', 'H01R35/04', 'H01J49/003', 'B29C49/58', 'H02J7/34', 'A61B90/70', 'F02N11/04', 'H01J49/421']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition']}

exec(code, env_args)
