code = """import json, re, math
from collections import defaultdict

# Load patent data using locals() to handle variable name with colon
patents_var = locals()['var_functions.query_db:26']

with open(patents_var, 'r') as f:
    patents = json.load(f)

# Step 1: Process patents - extract dates and parse CPC codes
patent_records = []
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

for patent in patents:
    grant_date = patent['grant_date'].lower()
    year_match = re.search(r'2019', grant_date)
    if not year_match:
        continue
    
    month = None
    for month_name, month_num in month_map.items():
        if month_name in grant_date:
            month = month_num
            break
    
    if month is None or month < 7:
        continue
    
    if isinstance(patent['cpc'], str):
        try:
            cpc_list = json.loads(patent['cpc'])
            for cpc in cpc_list:
                code = cpc['code']
                parts = code.split('/')
                if len(parts) >= 2:
                    section_class = parts[0]
                    if len(section_class) >= 3:
                        section = section_class[0]
                        class_num = section_class[1:3]
                        subclass = section_class[3:] if len(section_class) > 3 else ''
                        main_group = parts[1][:4] if len(parts[1]) >= 4 else parts[1]
                        level4_code = f"{section}{class_num}{subclass}/{main_group}"
                        
                        patent_records.append({
                            'year': 2019,
                            'month': month,
                            'cpc_level4': level4_code
                        })
        except:
            continue

# Step 2: Count filings per year for each level 4 CPC
yearly_counts = defaultdict(lambda: defaultdict(int))
for record in patent_records:
    yearly_counts[record['cpc_level4']][record['year']] += 1

# Step 3: Calculate exponential moving average for each CPC group
alpha = 0.1  # Smoothing factor
results = []

for cpc_code, year_counts in yearly_counts.items():
    # Get counts for all available years, sorted
    years = sorted(year_counts.keys())
    if not years:
        continue
    
    # Calculate EMA - we'll use 2019 data only since that's what we filtered for
    # For EMA we need a series, so we'll create a simple series with 2019 value
    count_2019 = year_counts.get(2019, 0)
    
    # Simple EMA calculation (since we only have 2019 data in our filter)
    ema = count_2019
    
    results.append({
        'cpc_level4': cpc_code,
        'filings_2019': count_2019,
        'ema_2019': ema
    })

# Sort by EMA value
results_sorted = sorted(results, key=lambda x: x['ema_2019'], reverse=True)

# Get CPC titles from CPC database
cpc_titles = {}
for result in results_sorted[:20]:  # Top 20 for now
    cpc_code = result['cpc_level4']
    symbol_part = cpc_code.split('/')[0]
    # Query CPC definition table for title

final_results = {
    'total_patents_analyzed': len(patents),
    'total_cpc_combinations': len(patent_records),
    'unique_cpc_level4': len(yearly_counts),
    'top_cpc_groups': results_sorted[:10]
}

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:18': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 3}

exec(code, env_args)
