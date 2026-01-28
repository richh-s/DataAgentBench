code = """import json
import re
from collections import defaultdict
from datetime import datetime

# Load patent data
patents_file = var_functions.query_db:26
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

print(f'Processing {len(patents_data)} German patents from 2019 second half')

# Step 1: Extract filing data by year and CPC level 4
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

# Structure: cpc_level4 -> year -> count
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_monthly_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

for patent in patents_data:
    grant_date = patent['grant_date'].lower()
    
    # Check for 2019
    if '2019' not in grant_date:
        continue
    
    # Extract month
    month = None
    for month_name, month_num in month_map.items():
        if month_name in grant_date:
            month = month_num
            break
    
    if month is None or month < 7:  # Second half only
        continue
    
    # Parse CPC codes
    if isinstance(patent['cpc'], str) and patent['cpc'].strip().startswith('['):
        try:
            cpc_list = json.loads(patent['cpc'])
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if not code:
                    continue
                
                # Extract level 4 CPC
                parts = code.split('/')
                if len(parts) != 2:
                    continue
                
                section_class = parts[0]
                group = parts[1]
                
                # Level 4: Section + Class + Subclass + Main group (4 digits)
                if len(section_class) < 3 or len(group) < 4:
                    continue
                
                section = section_class[0]
                class_num = section_class[1:3]
                subclass = section_class[3:] if len(section_class) > 3 else ''
                main_group = group[:4]
                
                level4_code = f"{section}{class_num}{subclass}/{main_group}"
                
                # Count by year
                cpc_yearly_counts[level4_code][2019] += 1
                cpc_monthly_counts[level4_code][2019][month] += 1
                
        except json.JSONDecodeError:
            continue

print(f'Found {len(cpc_yearly_counts)} unique CPC level 4 groups')
print('Top groups by 2019 count:')
for cpc, years in sorted(cpc_yearly_counts.items(), key=lambda x: x[1][2019], reverse=True)[:5]:
    print(f'  {cpc}: {years[2019]}')

# Save intermediate results
result = {
    'cpc_yearly_counts': {k: dict(v) for k, v in cpc_yearly_counts.items()},
    'cpc_monthly_counts': {k: {y: dict(m) for y, m in v.items()} for k, v in cpc_monthly_counts.items()}
}

print('__RESULT__:')
print(json.dumps({'cpc_groups_count': len(cpc_yearly_counts), 'top_5_preview': list(cpc_yearly_counts.keys())[:5]}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:18': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 3, 'var_functions.execute_python:36': {'total_patents_analyzed': 66, 'total_cpc_combinations': 860, 'unique_cpc_level4': 432, 'top_cpc_groups': [{'cpc_level4': 'B01L3/5027', 'filings_2019': 16, 'ema_2019': 16}, {'cpc_level4': 'B01J2219/0086', 'filings_2019': 8, 'ema_2019': 8}, {'cpc_level4': 'B01J2219/0098', 'filings_2019': 7, 'ema_2019': 7}, {'cpc_level4': 'H04W52/0251', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'G01N27/622', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2869', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2806', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2821', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2872', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2812', 'filings_2019': 5, 'ema_2019': 5}]}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'symbol': 'B01J2219/00', 'titleFull': 'Chemical, physical or physico-chemical processes in general; Their relevant apparatus'}, {'symbol': 'B01J2219/00002', 'titleFull': 'Chemical plants'}, {'symbol': 'B01J2219/00004', 'titleFull': 'Scale aspects'}, {'symbol': 'B01J2219/00006', 'titleFull': 'Large-scale industrial plants'}, {'symbol': 'B01J2219/00009', 'titleFull': 'Pilot-scale plants'}, {'symbol': 'B01J2219/00011', 'titleFull': 'Laboratory-scale plants'}, {'symbol': 'B01J2219/00013', 'titleFull': 'Miniplants'}, {'symbol': 'B01J2219/00015', 'titleFull': 'Scale-up'}, {'symbol': 'B01J2219/00018', 'titleFull': 'Construction aspects'}, {'symbol': 'B01J2219/0002', 'titleFull': 'Plants assembled from modules joined together'}, {'symbol': 'B01J2219/00022', 'titleFull': 'Plants mounted on pallets or skids'}, {'symbol': 'B01J2219/00024', 'titleFull': 'Revamping, retrofitting or modernisation of existing plants'}, {'symbol': 'B01J2219/00027', 'titleFull': 'Process aspects'}, {'symbol': 'B01J2219/00029', 'titleFull': 'Batch processes'}, {'symbol': 'B01J2219/00031', 'titleFull': 'Semi-batch or fed-batch processes'}, {'symbol': 'B01J2219/00033', 'titleFull': 'Continuous processes'}, {'symbol': 'B01J2219/00036', 'titleFull': 'Intermittent processes'}, {'symbol': 'B01J2219/00038', 'titleFull': 'Processes in parallel'}, {'symbol': 'B01J2219/0004', 'titleFull': 'Processes in series'}, {'symbol': 'B01J2219/00042', 'titleFull': 'Features relating to reactants and process fluids'}, {'symbol': 'B01J2219/00045', 'titleFull': 'Green chemistry'}, {'symbol': 'B01J2219/00047', 'titleFull': 'Ionic liquids'}, {'symbol': 'B01J2219/00049', 'titleFull': 'Controlling or regulating processes'}, {'symbol': 'B01J2219/00051', 'titleFull': 'Controlling the temperature'}, {'symbol': 'B01J2219/00054', 'titleFull': 'Controlling or regulating the heat exchange system'}, {'symbol': 'B01J2219/00056', 'titleFull': 'Controlling or regulating the heat exchange system involving measured parameters'}, {'symbol': 'B01J2219/00058', 'titleFull': 'Temperature measurement'}, {'symbol': 'B01J2219/0006', 'titleFull': 'Temperature measurement of the heat exchange medium'}, {'symbol': 'B01J2219/00063', 'titleFull': 'Temperature measurement of the reactants'}, {'symbol': 'B01J2219/00065', 'titleFull': 'Pressure measurement'}, {'symbol': 'B01J2219/00067', 'titleFull': 'Liquid level measurement'}, {'symbol': 'B01J2219/00069', 'titleFull': 'Flow rate measurement'}, {'symbol': 'B01J2219/00072', 'titleFull': 'Mathematical modelling'}, {'symbol': 'B01J2219/00074', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids'}, {'symbol': 'B01J2219/00076', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements inside the reactor'}, {'symbol': 'B01J2219/00078', 'titleFull': 'Fingers'}, {'symbol': 'B01J2219/00081', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00083', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00085', 'titleFull': 'Plates; Jackets; Cylinders'}, {'symbol': 'B01J2219/00087', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor'}, {'symbol': 'B01J2219/0009', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00092', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00094', 'titleFull': 'Jackets'}, {'symbol': 'B01J2219/00096', 'titleFull': 'Plates'}, {'symbol': 'B01J2219/00099', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor the reactor being immersed in the heat exchange medium'}, {'symbol': 'B01J2219/00101', 'titleFull': 'Reflux columns'}, {'symbol': 'B01J2219/00103', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor in a heat exchanger separate from the reactor'}, {'symbol': 'B01J2219/00105', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling'}, {'symbol': 'B01J2219/00108', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant vapours'}, {'symbol': 'B01J2219/0011', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant liquids'}], 'var_functions.query_db:42': []}

exec(code, env_args)
