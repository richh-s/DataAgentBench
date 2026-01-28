code = """import json
import os
import re
from datetime import datetime

# Load the German patents data from the query result
data_file = 'var_functions.query_db:5'
print('Attempting to load from:', data_file)

german_patents = []
if isinstance(data_file, str) and os.path.exists(data_file):
    with open(data_file, 'r') as f:
        german_patents = json.load(f)
else:
    # Try to use it directly as data
    print('Data file not found, checking variable directly')
    # This means the data might be passed as a variable
    german_patents = data_file

print('Data loaded, type:', type(german_patents))
if isinstance(german_patents, list):
    print('Length:', len(german_patents))
else:
    print('Data is not a list')

# If german_patents is still a string, try to parse it
if isinstance(german_patents, str):
    try:
        german_patents = json.loads(german_patents)
        print('Parsed string as JSON, new length:', len(german_patents))
    except:
        print('Could not parse as JSON')

if isinstance(german_patents, list) and len(german_patents) > 0:
    # Parse dates to find patents from second half of 2019
    def parse_grant_date(date_str):
        if not date_str:
            return None
        
        patterns = [
            r'(\d{1,2})\w*\s+(January|February|March|April|May|June|July|August|September|October|November|December)[\s,]+(\d{4})',
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?[\s,]+(\d{4})',
            r'\b(\d{4})\b'
        ]
        
        months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6,
                  'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}
        
        date_str_lower = date_str.lower()
        
        for pattern in patterns:
            match = re.search(pattern, date_str_lower, re.IGNORECASE)
            if match:
                groups = match.groups()
                try:
                    if len(groups) == 3 and groups[1].isdigit():
                        # DD Month YYYY
                        day = int(groups[0])
                        month = months.get(groups[1].lower())
                        year = int(groups[2])
                        if month:
                            return datetime(year, month, day)
                    elif len(groups) == 3 and groups[0].isdigit():
                        # Month DD YYYY
                        day = int(groups[1])
                        month = months.get(groups[0].lower())
                        year = int(groups[2])
                        if month:
                            return datetime(year, month, day)
                    elif len(groups) == 1 and groups[0].isdigit():
                        # Just year
                        year = int(groups[0])
                        return datetime(year, 1, 1)
                except:
                    continue
        
        return None
    
    # Filter patents granted in second half of 2019
    patents_2019_h2 = []
    for patent in german_patents:
    	grant_date_str = patent.get('grant_date', '')
        parsed_date = parse_grant_date(grant_date_str)
        if parsed_date and parsed_date.year == 2019 and parsed_date.month >= 7:
            patents_2019_h2.append(patent)
    
    print('Found %d patents in H2 2019' % len(patents_2019_h2))
    
    if len(patents_2019_h2) > 0:
        cpc_codes = []
        cpc_counts = {}
        
        for patent in patents_2019_h2:
            cpc_data = patent.get('cpc', '')
            if cpc_data:
                try:
                    cpc_list = json.loads(cpc_data)
                    for item in cpc_list:
                        code = item.get('code', '')
                        if code:
                            cpc_codes.append(code)
                            cpc_counts[code] = cpc_counts.get(code, 0) + 1
                except:
                    code_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
                    for code in code_matches:
                        cpc_codes.append(code)
                        cpc_counts[code] = cpc_counts.get(code, 0) + 1
        
        result_dict = {
            'patents_h2_2019': len(patents_2019_h2),
            'unique_cpc_codes': len(set(cpc_codes)),
            'total_cpc_occurrences': len(cpc_codes),
            'top_cpc': sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        }
    else:
        result_dict = {'patents_h2_2019': 0, 'unique_cpc_codes': 0, 'total_cpc_occurrences': 0, 'top_cpc': []}
else:
    result_dict = {'error': 'No German patents data loaded'}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}}

exec(code, env_args)
