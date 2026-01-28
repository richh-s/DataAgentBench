code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:2']

# Load the full results from the query
with open(file_path, 'r') as f:
    patents_2019 = json.load(f)

print('Total patents granted in 2019:', len(patents_2019))

# Function to parse grant dates in various formats
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    date_str = date_str.strip()
    
    # Common patterns
    patterns = [
        (r'(\d{1,2})\w{2} (\w+) (\d{4})', lambda m: (m.group(2), m.group(1), m.group(3))),  # 14th Mar 2019
        (r'(\w+) (\d{1,2})\w{2}, (\d{4})', lambda m: (m.group(1), m.group(2), m.group(3))),  # Mar 19th, 2019
    ]
    
    month_map = {
        'Jan': 1, 'January': 1, 'Feb': 2, 'February': 2, 'Mar': 3, 'March': 3,
        'Apr': 4, 'April': 4, 'May': 5, 'Jun': 6, 'June': 6, 'Jul': 7, 'July': 7,
        'Aug': 8, 'August': 8, 'Sep': 9, 'September': 9, 'Oct': 10, 'October': 10,
        'Nov': 11, 'November': 11, 'Dec': 12, 'December': 12
    }
    
    for pattern, extractor in patterns:
        match = re.match(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                month_str, day_str, year_str = extractor(match)
                month_num = month_map.get(month_str.strip())
                if month_num:
                    return datetime(int(year_str), month_num, int(day_str))
            except:
                continue
    
    return None

# Parse dates and extract country code (DE for Germany)
patents_de = []
for patent in patents_2019:
    parsed_date = parse_grant_date(patent['grant_date'])
    if parsed_date:
        patents_info = patent['Patents_info']
        is_germany = 'DE-' in patents_info or ' from DE,' in patents_info
        
        if is_germany:
            patents_de.append({
                'Patents_info': patents_info,
                'grant_date': patent['grant_date'],
                'parsed_date': parsed_date,
                'cpc': patent['cpc'],
                'month': parsed_date.month
            })

print('Total Germany patents in 2019:', len(patents_de))

# Filter for second half of 2019 (July - December)
if patents_de:
    df_de = pd.DataFrame(patents_de)
    patents_de_h2 = df_de[df_de['month'] >= 7].copy()
    print('Germany patents granted in second half 2019:', len(patents_de_h2))
    
    result = {
        'total_de_patents_2019': len(df_de),
        'de_patents_h2_2019': len(patents_de_h2)
    }
else:
    result = {'total_de_patents_2019': 0, 'de_patents_h2_2019': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}}

exec(code, env_args)
