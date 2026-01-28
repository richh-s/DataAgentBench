code = """import json
import re
from collections import defaultdict

# Read the data from previous steps
patents_data = []
cpc_definitions = []

# Load patents data
patents_path = locals()['var_functions.query_db:14']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

# Load CPC definitions
cpc_path = locals()['var_functions.query_db:22']
with open(cpc_path, 'r') as f:
    cpc_definitions = json.load(f)

print(f'Loaded {len(patents_data)} patents and {len(cpc_definitions)} CPC definitions')

# Create CPC definition mapping
cpc_titles = {}
for cpc_def in cpc_definitions:
    symbol = cpc_def.get('symbol')
    if symbol:
        cpc_titles[symbol] = cpc_def.get('titleFull', '')

# Month mapping
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

def parse_grant_date(date_str):
    if not date_str:
        return None, None
    
    patterns = [
        r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})',
        r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})',
        r'dated\s+(\d{1,2})(?:st|nd|rd|th)\s+([A-Za-z]+)\s+(20\d{2})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            if pattern.count('([A-Za-z]+)') == 1:
                if match.group(1).isdigit():
                    month_str = match.group(2)
                    year = int(match.group(3))
                else:
                    month_str = match.group(1)
                    year = int(match.group(3))
            else:
                month_str = match.group(1)
                year = int(match.group(3))
            
            month = None
            for key, val in month_map.items():
                if month_str.lower().startswith(key.lower()):
                    month = val
                    break
            
            if month and year:
                return year, month
    
    return None, None

def get_cpc_level4(code):
    if not code:
        return None
    base = code.split('/')[0].split('.')[0]
    if len(base) >= 4:
        return base[:4]
    return None

# Process patents data
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
germany_patents_2019_h2 = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if not ('DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info):
        continue
    
    grant_date_str = patent.get('grant_date')
    year, month = parse_grant_date(grant_date_str)
    if not year:
        continue
    
    # Track all Germany patents for historical EMA
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        level4_code = get_cpc_level4(code)
        if level4_code:
            cpc_yearly_counts[level4_code][year] += 1
            
            # Collect patents specifically from 2019 H2
            if year == 2019 and month and month >= 7:
                germany_patents_2019_h2.append({
                    'cpc_code': level4_code,
                    'patent': patent,
                    'month': month
                })

# Calculate EMA for each CPC code
def calculate_ema(values, alpha=0.1):
    if not values:
        return []
    ema = [values[0]]
    for i in range(1, len(values)):
        ema.append(alpha * values[i] + (1 - alpha) * ema[i-1])
    return ema

# Get CPC codes that have patents in 2019 H2
relevant_cpc_codes = set(p['cpc_code'] for p in germany_patents_2019_h2)

# Calculate results
results = []
for cpc_code in relevant_cpc_codes:
    title = cpc_titles.get(cpc_code, '')
    if not title:
        continue
    
    # Get yearly counts
    yearly_data = cpc_yearly_counts[cpc_code]
    sorted_years = sorted(yearly_data.keys())
    values = [yearly_data[y] for y in sorted_years]
    
    # Calculate EMA
    ema_values = calculate_ema(values, alpha=0.1)
    
    # Find best year (year with highest EMA)
    max_ema_idx = ema_values.index(max(ema_values))
    best_year = sorted_years[max_ema_idx]
    
    # Count patents in 2019 H2
    pat_2019_h2 = sum(1 for p in germany_patents_2019_h2 if p['cpc_code'] == cpc_code)
    
    results.append({
        'cpc_code': cpc_code,
        'title_full': title,
        'best_year': best_year,
        'patents_in_best_year': yearly_data[best_year],
        'ema_value': ema_values[max_ema_idx],
        'patents_2019_h2': pat_2019_h2
    })

# Sort by EMA value
top_results = sorted(results, key=lambda x: x['ema_value'], reverse=True)

output = {
    'total_cpc_codes_evaluated': len(relevant_cpc_codes),
    'top_cpc_codes': top_results
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
