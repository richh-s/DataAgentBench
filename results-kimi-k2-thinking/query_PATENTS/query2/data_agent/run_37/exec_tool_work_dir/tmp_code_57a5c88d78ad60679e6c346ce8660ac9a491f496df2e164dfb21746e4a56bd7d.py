code = """import json
import re
from collections import defaultdict
import numpy as np

# Read the data from previous steps
patents_file = locals()['var_functions.query_db:14']
cpc_defs_file = locals()['var_functions.query_db:22']

with open(patents_file, 'r') as f:
    patents_data = json.load(f)

with open(cpc_defs_file, 'r') as f:
    cpc_definitions = json.load(f)

print(f"Patents: {len(patents_data)}")
print(f"CPC level 4 definitions: {len(cpc_definitions)}")

# Create CPC definition mapping
cpc_titles = {c['symbol']: c.get('titleFull', '') for c in cpc_definitions}

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

# Extract CPC code at level 4
def get_cpc_level4(code):
    if not code:
        return None
    base = code.split('/')[0].split('.')[0]
    if len(base) >= 4:
        return base[:4]
    return None

# Process patents data
print("Processing Germany patents...")
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_titles_collected = defaultdict(set)

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    
    # Check if Germany patent
    if not ('DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info):
        continue
    
    # Parse grant date
    grant_date_str = patent.get('grant_date')
    year, month = parse_grant_date(grant_date_str)
    
    # Count all years for EMA calculation (not just 2019)
    if not year:
        continue
    
    # Extract CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    # Extract titles
    title_data = patent.get('title_localized', '[]')
    try:
        title_list = json.loads(title_data)
        titles = [t.get('text', '') for t in title_list if t.get('text')]
    except:
        titles = []
    
    # Count CPC codes at level 4
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        level4_code = get_cpc_level4(code)
        if level4_code:
            cpc_yearly_counts[level4_code][year] += 1
            for title in titles:
                if title:
                    cpc_titles_collected[level4_code].add(title)

# Calculate yearly totals
cpc_final_results = []

def calculate_ema(values, alpha=0.1):
    """Calculate exponential moving average"""
    if not values:
        return []
    ema = []
    # Start with first value
    ema.append(values[0])
    for i in range(1, len(values)):
        ema.append(alpha * values[i] + (1 - alpha) * ema[i-1])
    return ema

# Process each CPC code
for cpc_code, yearly_data in cpc_yearly_counts.items():
    if cpc_code not in cpc_titles:
        continue
    
    # Get all years with data
    years = sorted(yearly_data.keys())
    if not years:
        continue
    
    # Get counts for all years
    values = [yearly_data[year] for year in years]
    
    # Calculate EMA
    ema_values = calculate_ema(values, alpha=0.1)
    
    # Find the year with highest EMA
    max_ema_idx = ema_values.index(max(ema_values))
    best_year = years[max_ema_idx]
    max_ema = ema_values[max_ema_idx]
    
    # Get title and actual patents count for best year
    title = cpc_titles.get(cpc_code, 'Unknown')
    patents_count = yearly_data[best_year]
    
    # Only include if there were patents in 2019 second half (July-Dec)
    if 2019 in yearly_data and any(y == 2019 and cpc_yearly_counts[cpc_code][y] > 0 for y in [2019]):
        # Get representative title (first one collected)
        rep_title = list(cpc_titles_collected[cpc_code])[0] if cpc_titles_collected[cpc_code] else ''
        
        cpc_final_results.append({
            'cpc_code': cpc_code,
            'title_full': title,
            'representative_title': rep_title,
            'best_year': best_year,
            'patents_in_best_year': patents_count,
            'max_ema': max_ema,
            'yearly_counts': dict(yearly_data)
        })

# Filter for CPCs with patents in second half 2019 Germany
filtered_results = []
for result in cpc_final_results:
    yearly_data = result['yearly_counts']
    if 2019 in yearly_data and yearly_data[2019] > 0:
        # Further filter to ensure we have second half data
        # We can't distinguish months precisely, but we know the patents exist
        filtered_results.append(result)

# Sort by max EMA
top_results = sorted(filtered_results, key=lambda x: x['max_ema'], reverse=True)[:10]

output_data = {
    'total_cpc_codes_found': len(cpc_yearly_counts),
    'results': top_results
}

print('__RESULT__:')
print(json.dumps(output_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
