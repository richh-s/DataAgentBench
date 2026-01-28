code = """import json, re
from collections import defaultdict

# Get the file path safely
patents_data_path = locals()['var_functions.query_db:26']

# Load patent data  
with open(patents_data_path, 'r') as f:
    patents = json.load(f)

print(f'Loaded {len(patents)} patents')

# Process patents to extract CPC level 4 codes and count filings
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

cpc_counts = defaultdict(int)
for patent in patents:
    grant_date = patent['grant_date'].lower()
    if '2019' not in grant_date:
        continue
        
    month_found = False
    for month_name, month_num in month_map.items():
        if month_name in grant_date and month_num >= 7:
            month_found = True
            break
    
    if not month_found:
        continue
    
    if isinstance(patent['cpc'], str) and patent['cpc'].strip().startswith('['):
        try:
            cpc_list = json.loads(patent['cpc'])
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:
                    parts = code.split('/')
                    if len(parts) == 2 and len(parts[0]) >= 3 and len(parts[1]) >= 4:
                        section = parts[0][0]
                        class_num = parts[0][1:3]
                        subclass = parts[0][3:] if len(parts[0]) > 3 else ''
                        main_group = parts[1][:4]
                        level4 = f"{section}{class_num}{subclass}/{main_group}"
                        cpc_counts[level4] += 1
        except:
            pass

# Sort by count
top_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print('Top 10 CPC Level 4 groups:')
for code, count in top_cpc:
    print(f'  {code}: {count}')

result = {
    'total_patents': len(patents),
    'unique_cpc_level4': len(cpc_counts),
    'top_groups': [{'code': code, 'count': count} for code, count in top_cpc]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:18': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 3, 'var_functions.execute_python:36': {'total_patents_analyzed': 66, 'total_cpc_combinations': 860, 'unique_cpc_level4': 432, 'top_cpc_groups': [{'cpc_level4': 'B01L3/5027', 'filings_2019': 16, 'ema_2019': 16}, {'cpc_level4': 'B01J2219/0086', 'filings_2019': 8, 'ema_2019': 8}, {'cpc_level4': 'B01J2219/0098', 'filings_2019': 7, 'ema_2019': 7}, {'cpc_level4': 'H04W52/0251', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'G01N27/622', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2869', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2806', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2821', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2872', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2812', 'filings_2019': 5, 'ema_2019': 5}]}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'symbol': 'B01J2219/00', 'titleFull': 'Chemical, physical or physico-chemical processes in general; Their relevant apparatus'}, {'symbol': 'B01J2219/00002', 'titleFull': 'Chemical plants'}, {'symbol': 'B01J2219/00004', 'titleFull': 'Scale aspects'}, {'symbol': 'B01J2219/00006', 'titleFull': 'Large-scale industrial plants'}, {'symbol': 'B01J2219/00009', 'titleFull': 'Pilot-scale plants'}, {'symbol': 'B01J2219/00011', 'titleFull': 'Laboratory-scale plants'}, {'symbol': 'B01J2219/00013', 'titleFull': 'Miniplants'}, {'symbol': 'B01J2219/00015', 'titleFull': 'Scale-up'}, {'symbol': 'B01J2219/00018', 'titleFull': 'Construction aspects'}, {'symbol': 'B01J2219/0002', 'titleFull': 'Plants assembled from modules joined together'}, {'symbol': 'B01J2219/00022', 'titleFull': 'Plants mounted on pallets or skids'}, {'symbol': 'B01J2219/00024', 'titleFull': 'Revamping, retrofitting or modernisation of existing plants'}, {'symbol': 'B01J2219/00027', 'titleFull': 'Process aspects'}, {'symbol': 'B01J2219/00029', 'titleFull': 'Batch processes'}, {'symbol': 'B01J2219/00031', 'titleFull': 'Semi-batch or fed-batch processes'}, {'symbol': 'B01J2219/00033', 'titleFull': 'Continuous processes'}, {'symbol': 'B01J2219/00036', 'titleFull': 'Intermittent processes'}, {'symbol': 'B01J2219/00038', 'titleFull': 'Processes in parallel'}, {'symbol': 'B01J2219/0004', 'titleFull': 'Processes in series'}, {'symbol': 'B01J2219/00042', 'titleFull': 'Features relating to reactants and process fluids'}, {'symbol': 'B01J2219/00045', 'titleFull': 'Green chemistry'}, {'symbol': 'B01J2219/00047', 'titleFull': 'Ionic liquids'}, {'symbol': 'B01J2219/00049', 'titleFull': 'Controlling or regulating processes'}, {'symbol': 'B01J2219/00051', 'titleFull': 'Controlling the temperature'}, {'symbol': 'B01J2219/00054', 'titleFull': 'Controlling or regulating the heat exchange system'}, {'symbol': 'B01J2219/00056', 'titleFull': 'Controlling or regulating the heat exchange system involving measured parameters'}, {'symbol': 'B01J2219/00058', 'titleFull': 'Temperature measurement'}, {'symbol': 'B01J2219/0006', 'titleFull': 'Temperature measurement of the heat exchange medium'}, {'symbol': 'B01J2219/00063', 'titleFull': 'Temperature measurement of the reactants'}, {'symbol': 'B01J2219/00065', 'titleFull': 'Pressure measurement'}, {'symbol': 'B01J2219/00067', 'titleFull': 'Liquid level measurement'}, {'symbol': 'B01J2219/00069', 'titleFull': 'Flow rate measurement'}, {'symbol': 'B01J2219/00072', 'titleFull': 'Mathematical modelling'}, {'symbol': 'B01J2219/00074', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids'}, {'symbol': 'B01J2219/00076', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements inside the reactor'}, {'symbol': 'B01J2219/00078', 'titleFull': 'Fingers'}, {'symbol': 'B01J2219/00081', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00083', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00085', 'titleFull': 'Plates; Jackets; Cylinders'}, {'symbol': 'B01J2219/00087', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor'}, {'symbol': 'B01J2219/0009', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00092', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00094', 'titleFull': 'Jackets'}, {'symbol': 'B01J2219/00096', 'titleFull': 'Plates'}, {'symbol': 'B01J2219/00099', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor the reactor being immersed in the heat exchange medium'}, {'symbol': 'B01J2219/00101', 'titleFull': 'Reflux columns'}, {'symbol': 'B01J2219/00103', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor in a heat exchanger separate from the reactor'}, {'symbol': 'B01J2219/00105', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling'}, {'symbol': 'B01J2219/00108', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant vapours'}, {'symbol': 'B01J2219/0011', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant liquids'}], 'var_functions.query_db:42': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
