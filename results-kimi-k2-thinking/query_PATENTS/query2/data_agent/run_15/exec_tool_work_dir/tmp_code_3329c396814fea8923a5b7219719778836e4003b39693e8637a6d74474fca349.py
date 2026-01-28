code = """import json
import re
from datetime import datetime
import math

# Load German patent data
patents_file = var_functions.query_db:26
with open(patents_file, 'r') as f:
    patents = json.load(f)

print(f'Loaded {len(patents)} German patents granted in second half of 2019')

# Step 1: Extract year and month from grant_date, and parse CPC codes
patent_records = []
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

for patent in patents:
    grant_date = patent['grant_date'].lower()
    
    # Extract year
    year_match = re.search(r'2019', grant_date)
    if not year_match:
        continue
    year = int(year_match.group())
    
    # Extract month
    month = None
    for month_name, month_num in month_map.items():
        if month_name in grant_date:
            month = month_num
            break
    
    if month is None or month < 7:  # Only second half of 2019
        continue
    
    # Parse CPC codes
    if isinstance(patent['cpc'], str):
        try:
            cpc_list = json.loads(patent['cpc'])
            for cpc in cpc_list:
                code = cpc['code']
                # Extract parent at level 4 (format: Section/Class/Subclass/Group)
                parts = code.split('/')
                if len(parts) >= 2:
                    section_class = parts[0]
                    if len(section_class) >= 3:
                        section = section_class[0]
                        class_num = section_class[1:3]
                        subclass = section_class[3:] if len(section_class) > 3 else ''
                        
                        # For level 4, we take Section+Class+Subclass+Main group
                        # CPC format is usually like A61M1/3496
                        main_group = parts[1][:4] if len(parts[1]) >= 4 else parts[1]
                        level4_code = f"{section}{class_num}{subclass}/{main_group}"
                        
                        patent_records.append({
                            'year': year,
                            'month': month,
                            'cpc_code': code,
                            'cpc_level4': level4_code
                        })
        except json.JSONDecodeError:
            continue

print(f'Processed {len(patent_records)} patent-CPC combinations')

# Step 2: Count filings per year for each level 4 CPC
from collections import defaultdict

yearly_counts = defaultdict(lambda: defaultdict(int))
for record in patent_records:
    yearly_counts[record['cpc_level4']][record['year']] += 1

print('Yearly counts for top CPC groups:')
sorted_groups = sorted(yearly_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)
for cpc, years in sorted_groups[:10]:
    print(f"{cpc}: {dict(years)}")

# Save processed data
result = {
    'total_patents': len(patents),
    'total_records': len(patent_records),
    'unique_cpc_level4': len(yearly_counts),
    'yearly_counts': {k: dict(v) for k, v in yearly_counts.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:18': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 3}

exec(code, env_args)
