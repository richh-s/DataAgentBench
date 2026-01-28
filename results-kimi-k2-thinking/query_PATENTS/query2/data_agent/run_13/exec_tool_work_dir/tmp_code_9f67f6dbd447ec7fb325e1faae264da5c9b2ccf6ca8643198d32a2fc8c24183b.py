code = """import json
import re
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:11']

# Read the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse grant dates to extract month and year
def parse_grant_date(date_str):
    if not date_str:
        return None
    # Extract month and year from various formats
    patterns = [
        r'(\w+)\s+(\d+)(?:st|nd|rd|th)?,?\s+(\d{4})',  # "July 8th, 2019"
        r'(\w+)\s+(\d{4})',  # "July 2019"
        r'(\d{1,2})\w*\s+(\w+)\s+(\d{4})',  # "23rd of July, 2019"
        r'(?:on\s+)?(\w+)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})'  # "on March 14th, 2019"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                if len(match.groups()) == 3:
                    # Has day, month, year
                    month_str = match.group(1) if match.group(1).isalpha() else match.group(2)
                    year = int(match.group(3))
                else:
                    # Has month and year
                    month_str = match.group(1)
                    year = int(match.group(2))
                
                # Convert month string to number
                month_str = month_str.lower()
                month_map = {
                    'jan': 1, 'january': 1,
                    'feb': 2, 'february': 2,
                    'mar': 3, 'march': 3,
                    'apr': 4, 'april': 4,
                    'may': 5,
                    'jun': 6, 'june': 6,
                    'jul': 7, 'july': 7,
                    'aug': 8, 'august': 8,
                    'sep': 9, 'sept': 9, 'september': 9,
                    'oct': 10, 'october': 10,
                    'nov': 11, 'november': 11,
                    'dec': 12, 'december': 12
                }
                
                for key, val in month_map.items():
                    if month_str.startswith(key):
                        return year, val
            except:
                continue
    return None

# Check if patent is German based on Patents_info
def is_german(patent_info):
    if not patent_info:
        return False
    # Look for country codes - patterns like "DE-", "DE:", "Germany", etc.
    patterns = [
        r'\bDE\b[-:]',
        r'Germany',
        r'German',
        r'\bDE\d{2}',
        r'\((?:country|nation):?\s*DE\)'
    ]
    
    for pattern in patterns:
        if re.search(pattern, patent_info, re.IGNORECASE):
            return True
    return False

# Extract CPC codes from the JSON-like string
def extract_cpc_codes(cpc_str):
    try:
        # The string looks like a JSON array but might have issues
        # Try to clean it up
        cpc_str_clean = cpc_str.strip()
        if not cpc_str_clean or cpc_str_clean == '[]':
            return []
        
        # Try to parse as JSON
        cpc_data = json.loads(cpc_str_clean)
        codes = []
        for entry in cpc_data:
            if isinstance(entry, dict) and 'code' in entry:
                codes.append(entry['code'])
        return codes
    except:
        # If JSON parsing fails, try regex extraction
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
        return codes

# Filter for German patents granted in second half of 2019
german_patents = []
for record in data:
    patent_info = record.get('Patents_info', '')
    cpc_str = record.get('cpc', '')
    grant_date_str = record.get('grant_date', '')
    
    # Check if German
    if not is_german(patent_info):
        continue
    
    # Parse grant date
    date_info = parse_grant_date(grant_date_str)
    if not date_info:
        continue
    
    year, month = date_info
    # Check if in second half of 2019
    if year == 2019 and month >= 7:
        # Extract CPC codes
        cpc_codes = extract_cpc_codes(cpc_str)
        if cpc_codes:
            german_patents.append({
                'patent_info': patent_info,
                'grant_date': grant_date_str,
                'month': month,
                'cpc_codes': cpc_codes
            })

print('__RESULT__:')
print(json.dumps({
    'total_german_patents_h2_2019': len(german_patents),
    'sample_patents': german_patents[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.execute_python:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'grant_date': '10th Apr 1883'}, {'grant_date': '10th Apr 1888'}, {'grant_date': '10th Apr 1923'}, {'grant_date': '10th Apr 1945'}, {'grant_date': '10th Apr 1952'}, {'grant_date': '10th Apr 1969'}, {'grant_date': '10th Apr 1974'}, {'grant_date': '10th Apr 1979'}, {'grant_date': '10th Apr 1980'}, {'grant_date': '10th Apr 1984'}, {'grant_date': '10th Apr 1990'}, {'grant_date': '10th Apr 2001'}, {'grant_date': '10th Apr 2006'}, {'grant_date': '10th Apr 2008'}, {'grant_date': '10th Apr 2018'}, {'grant_date': '10th Apr 2019'}, {'grant_date': '10th Apr 2020'}, {'grant_date': '10th Apr 2023'}, {'grant_date': '10th Apr 2024'}, {'grant_date': '10th April 1956'}, {'grant_date': '10th April 1962'}, {'grant_date': '10th April 1964'}, {'grant_date': '10th April 1973'}, {'grant_date': '10th April 1979'}, {'grant_date': '10th April 1990'}, {'grant_date': '10th April 2000'}, {'grant_date': '10th April 2001'}, {'grant_date': '10th April 2002'}, {'grant_date': '10th April 2005'}, {'grant_date': '10th April 2007'}, {'grant_date': '10th April 2012'}, {'grant_date': '10th April 2013'}, {'grant_date': '10th April 2014'}, {'grant_date': '10th April 2018'}, {'grant_date': '10th April 2020'}, {'grant_date': '10th April 2023'}, {'grant_date': '10th Aug 1948'}, {'grant_date': '10th Aug 1954'}, {'grant_date': '10th Aug 1959'}, {'grant_date': '10th Aug 1970'}, {'grant_date': '10th Aug 1973'}, {'grant_date': '10th Aug 1974'}, {'grant_date': '10th Aug 1976'}, {'grant_date': '10th Aug 1993'}, {'grant_date': '10th Aug 2004'}, {'grant_date': '10th Aug 2006'}, {'grant_date': '10th Aug 2011'}, {'grant_date': '10th Aug 2014'}, {'grant_date': '10th Aug 2016'}, {'grant_date': '10th Aug 2018'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:10': 'Loaded 1929 records'}

exec(code, env_args)
