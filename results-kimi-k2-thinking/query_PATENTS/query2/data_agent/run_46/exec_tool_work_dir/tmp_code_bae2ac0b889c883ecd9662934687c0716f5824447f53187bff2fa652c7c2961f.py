code = """import json
import re
from datetime import datetime
import pandas as pd

# Load the query result from the stored file
result_file = var_functions.query_db:2

# Read the JSON file
with open(result_file, 'r') as f:
    patents_data = json.load(f)

print(f"Total patents loaded: {len(patents_data)}")

# Filter for Germany (DE) patents granted in second half of 2019
german_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    # Check if it's a Germany patent
    if patents_info and ('DE-' in patents_info or 'from DE' in patents_info or 'assigned to' in patents_info and 'DE' in patents_info):
        # Parse grant date
        try:
            # Extract month from grant_date
            date_patterns = [
                r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)(?:,\s+|\s+)?(2019)',
                r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?(?:,\s+|\s+)?(2019)',
                r'(\d{1,2})/\d{1,2}/2019'
            ]
            
            month = None
            for pattern in date_patterns:
                match = re.search(pattern, grant_date, re.IGNORECASE)
                if match:
                    if pattern == date_patterns[0]:
                        month_str = match.group(2)
                        try:
                            month_num = datetime.strptime(month_str, '%B').month
                            month = month_num
                        except:
                            month_num = datetime.strptime(month_str, '%b').month
                            month = month_num
                    elif pattern == date_patterns[1]:
                        month_str = match.group(1)
                        try:
                            month_num = datetime.strptime(month_str, '%B').month
                            month = month_num
                        except:
                            month_num = datetime.strptime(month_str, '%b').month
                            month = month_num
                    elif pattern == date_patterns[2]:
                        month = int(match.group(1))
                    break
            
            # Check if in second half (July-December)
            if month and month >= 7:
                # Parse CPC codes
                if cpc_data and cpc_data.strip():
                    try:
                        cpc_list = json.loads(cpc_data)
                        for cpc_entry in cpc_list:
                            code = cpc_entry.get('code', '')
                            if code and len(code.split('/')[0]) >= 4:
                                # Extract level 4 CPC group (first 4 characters of main class)
                                main_class = code.split('/')[0]
                                group_4 = main_class[:4]
                                
                                german_patents.append({
                                    'patent_info': patents_info,
                                    'cpc_code': code,
                                    'cpc_group_4': group_4,
                                    'grant_date': grant_date,
                                    'month': month,
                                    'year': 2019
                                })
                    except:
                        # Skip if JSON parsing fails
                        continue
        except Exception as e:
            # Skip if date parsing fails
            continue

# Create DataFrame
df = pd.DataFrame(german_patents)
print(f"Total German patents in second half 2019: {len(df)}")

if not df.empty:
    print(f"Sample data:")
    print(df.head())
    print(f"CPC codes extracted: {df['cpc_code'].nunique()} unique codes")
    print(f"CPC groups (level 4): {df['cpc_group_4'].nunique()} unique groups")
else:
    print("No German patents found for second half of 2019")

# Save intermediate results
result_summary = {
    'total_patents': len(df),
    'sample_patents': german_patents[:5] if german_patents else [],
    'unique_cpc_codes': df['cpc_code'].nunique() if not df.empty else 0,
    'unique_cpc_groups': df['cpc_group_4'].nunique() if not df.empty else 0
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
