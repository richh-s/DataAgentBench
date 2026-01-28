code = """import json
import os
import re
from datetime import datetime

# Load the German patents data from the query result
# The result was stored in a JSON file, let's try to load it
data_file = '/tmp/tmp8v9d3d4q.json'

if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        german_patents = json.load(f)
    
    print('Loaded %d German patents' % len(german_patents))
    
    # Parse dates to find patents from second half of 2019
    def parse_grant_date(date_str):
        if not date_str:
            return None
        
        # Try to extract year, month from various formats
        # Format patterns: "7th October 2004", "dated 6th October 2020", "2006 on Apr 27th"
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
n                        day = int(groups[1])
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
        if grant_date_str:
            parsed_date = parse_grant_date(grant_date_str)
            if parsed_date and parsed_date.year == 2019 and parsed_date.month >= 7:
                patents_2019_h2.append(patent)
    
    print('Found %d patents granted in H2 2019' % len(patents_2019_h2))
    
    if len(patents_2019_h2) > 0:
        # Extract CPC codes
        cpc_codes = []
        cpc_counts = {}
        
        for patent in patents_2019_h2:
            cpc_data = patent.get('cpc', '')
            if cpc_data:
                try:
                    # Try to parse as JSON
                    cpc_list = json.loads(cpc_data)
                    for item in cpc_list:
                        code = item.get('code', '')
                        if code:
                            cpc_codes.append(code)
                            cpc_counts[code] = cpc_counts.get(code, 0) + 1
                except:
                    # Fallback: extract with regex
                    code_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
                    for code in code_matches:
                        cpc_codes.append(code)
                        cpc_counts[code] = cpc_counts.get(code, 0) + 1
        
        print('Extracted %d CPC code occurrences' % len(cpc_codes))
        print('Found %d unique CPC codes' % len(set(cpc_codes)))
        
        result_dict = {
            'patents_2019_h2_count': len(patents_2019_h2),
            'total_cpc_occurrences': len(cpc_codes),
            'unique_cpc_codes': len(set(cpc_codes)),
            'top_cpc_codes': sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        }
        
        print('__RESULT__:')
        print(json.dumps(result_dict))
    else:
        print('__RESULT__:')
        print(json.dumps({'error': 'No patents found for H2 2019'}))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Data file not found'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}}

exec(code, env_args)
