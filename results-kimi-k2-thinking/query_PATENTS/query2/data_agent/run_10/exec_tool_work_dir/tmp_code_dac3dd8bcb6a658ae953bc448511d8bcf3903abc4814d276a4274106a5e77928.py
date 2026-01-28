code = """import json
import re
from datetime import datetime

# Load the data from the storage key
storage_key = 'var_functions.query_db:5'
if isinstance(storage_key, str) and storage_key.endswith('.json'):
    with open(storage_key, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = storage_key

print('Total German patents found: %d' % len(german_patents))

# Define date parsing patterns
date_patterns = [
    r'\b(\d{1,2})[\w\s]*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s*,?\s*(\d{4})\b',
    r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b',
    r'\b(\d{4})\b'
]

months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

def parse_date(date_str):
    if not date_str or date_str == 'null':
        return None
    
    date_str_lower = date_str.lower()
    
    for pattern in date_patterns:
        match = re.search(pattern, date_str_lower, re.IGNORECASE)
        if match:
            groups = match.groups()
            try:
                if len(groups) == 3:
                    if groups[0].isdigit() and groups[1].isalpha():
                        day = int(groups[0])
                        month = months.get(groups[1][:3].lower())
                        year = int(groups[2])
                        if month:
                            return datetime(year, month, day)
                    elif groups[0].isalpha() and groups[1].isdigit():
                        month = months.get(groups[0][:3].lower())
                        day = int(groups[1])
                        year = int(groups[2])
                        if month:
                            return datetime(year, month, day)
                elif len(groups) == 1 and groups[0].isdigit():
                    year = int(groups[0])
                    return datetime(year, 1, 1)
            except:
                continue
    
    return None

patents_2019 = []
for patent in german_patents:
    grant_date = parse_date(patent['grant_date'])
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        patents_2019.append({
            'patent_info': patent['Patents_info'],
            'grant_date': patent['grant_date'],
            'cpc': patent['cpc'],
            'parsed_grant_date': grant_date.isoformat()
        })

print('Second half 2019 patents: %d' % len(patents_2019))

if len(patents_2019) > 0:
    all_cpc_codes = []
    cpc_patent_counts = {}
    
    for patent in patents_2019:
        try:
            cpc_data = json.loads(patent['cpc'])
            if isinstance(cpc_data, list):
                for cpc_item in cpc_data:
                    code = cpc_item.get('code', '')
                    if code:
                        all_cpc_codes.append(code)
                        cpc_patent_counts[code] = cpc_patent_counts.get(code, 0) + 1
        except:
            cpc_matches = re.findall(r'"code":\s*"([^"]+)"', patent['cpc'])
            for code in cpc_matches:
                all_cpc_codes.append(code)
                cpc_patent_counts[code] = cpc_patent_counts.get(code, 0) + 1
    
    unique_codes = len(set(all_cpc_codes))
    print('Unique CPC codes: %d' % unique_codes)
    
    output = {
        'total_patents_2019': len(patents_2019),
        'cpc_codes': list(set(all_cpc_codes)),
        'cpc_counts': cpc_patent_counts
    }
else:
    output = {'total_patents_2019': 0, 'cpc_codes': [], 'cpc_counts': {}}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
