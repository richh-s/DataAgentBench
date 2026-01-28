code = """import json

# Load the CPC definition query results
cpc_definitions_file = var_functions.query_db:40
with open(cpc_definitions_file, 'r') as f:
    cpc_defs = json.load(f)

print(f'Loaded {len(cpc_defs)} CPC definitions')

# Create a lookup for CPC titles
cpc_title_lookup = {}
for def_item in cpc_defs:
    symbol = def_item['symbol']
    title = def_item['titleFull']
    cpc_title_lookup[symbol] = title

# Load top CPC results from previous analysis
top_results_file = var_functions.execute_python:36
with open(top_results_file, 'r') as f:
    top_results = json.load(f)

top_cpc_groups = top_results['top_cpc_groups']

# Enrich with titles
enriched_results = []
for item in top_cpc_groups:
    cpc_code = item['cpc_level4']
    title = cpc_title_lookup.get(cpc_code, 'Title not found')
    
    # Try to find parent code if not found
    if title == 'Title not found':
        # Try progressively broader codes
        parts = cpc_code.split('/')
        if len(parts) == 2:
            section_class = parts[0]
            group = parts[1]
            
            # Try with just section+class (format: A61M)
            if len(section_class) >= 3:
                parent1 = f"{section_class[:3]}"
                title = cpc_title_lookup.get(parent1, 'Title not found')
                
                # Try section+class+subclass
                if title == 'Title not found' and len(section_class) >= 4:
                    parent2 = section_class
                    title = cpc_title_lookup.get(parent2, 'Title not found')
    
    enriched_results.append({
        'cpc_group_code': cpc_code,
        'titleFull': title,
        'filings_2019': item['filings_2019'],
        'ema_2019': item['ema_2019'],
        'best_year': 2019
    })

# Print results
print('\nTop CPC Technology Areas in Germany (Second Half 2019):')
print('=' * 80)
for i, result in enumerate(enriched_results, 1):
    print(f"{i}. CPC Group: {result['cpc_group_code']}")
    print(f"   Title: {result['titleFull']}")
    print(f"   Patent Filings 2019: {result['filings_2019']}")
    print(f"   EMA (2019): {result['ema_2019']:.1f}")
    print(f"   Best Year: {result['best_year']}")
    print()

# Count titles found
titles_found = sum(1 for r in enriched_results if r['titleFull'] != 'Title not found')
print(f'Titles found: {titles_found}/{len(enriched_results)}')

print('__RESULT__:')
print(json.dumps(enriched_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:18': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 3, 'var_functions.execute_python:36': {'total_patents_analyzed': 66, 'total_cpc_combinations': 860, 'unique_cpc_level4': 432, 'top_cpc_groups': [{'cpc_level4': 'B01L3/5027', 'filings_2019': 16, 'ema_2019': 16}, {'cpc_level4': 'B01J2219/0086', 'filings_2019': 8, 'ema_2019': 8}, {'cpc_level4': 'B01J2219/0098', 'filings_2019': 7, 'ema_2019': 7}, {'cpc_level4': 'H04W52/0251', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'G01N27/622', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2869', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2806', 'filings_2019': 6, 'ema_2019': 6}, {'cpc_level4': 'B60N2/2821', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2872', 'filings_2019': 5, 'ema_2019': 5}, {'cpc_level4': 'B60N2/2812', 'filings_2019': 5, 'ema_2019': 5}]}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'symbol': 'B01J2219/00', 'titleFull': 'Chemical, physical or physico-chemical processes in general; Their relevant apparatus'}, {'symbol': 'B01J2219/00002', 'titleFull': 'Chemical plants'}, {'symbol': 'B01J2219/00004', 'titleFull': 'Scale aspects'}, {'symbol': 'B01J2219/00006', 'titleFull': 'Large-scale industrial plants'}, {'symbol': 'B01J2219/00009', 'titleFull': 'Pilot-scale plants'}, {'symbol': 'B01J2219/00011', 'titleFull': 'Laboratory-scale plants'}, {'symbol': 'B01J2219/00013', 'titleFull': 'Miniplants'}, {'symbol': 'B01J2219/00015', 'titleFull': 'Scale-up'}, {'symbol': 'B01J2219/00018', 'titleFull': 'Construction aspects'}, {'symbol': 'B01J2219/0002', 'titleFull': 'Plants assembled from modules joined together'}, {'symbol': 'B01J2219/00022', 'titleFull': 'Plants mounted on pallets or skids'}, {'symbol': 'B01J2219/00024', 'titleFull': 'Revamping, retrofitting or modernisation of existing plants'}, {'symbol': 'B01J2219/00027', 'titleFull': 'Process aspects'}, {'symbol': 'B01J2219/00029', 'titleFull': 'Batch processes'}, {'symbol': 'B01J2219/00031', 'titleFull': 'Semi-batch or fed-batch processes'}, {'symbol': 'B01J2219/00033', 'titleFull': 'Continuous processes'}, {'symbol': 'B01J2219/00036', 'titleFull': 'Intermittent processes'}, {'symbol': 'B01J2219/00038', 'titleFull': 'Processes in parallel'}, {'symbol': 'B01J2219/0004', 'titleFull': 'Processes in series'}, {'symbol': 'B01J2219/00042', 'titleFull': 'Features relating to reactants and process fluids'}, {'symbol': 'B01J2219/00045', 'titleFull': 'Green chemistry'}, {'symbol': 'B01J2219/00047', 'titleFull': 'Ionic liquids'}, {'symbol': 'B01J2219/00049', 'titleFull': 'Controlling or regulating processes'}, {'symbol': 'B01J2219/00051', 'titleFull': 'Controlling the temperature'}, {'symbol': 'B01J2219/00054', 'titleFull': 'Controlling or regulating the heat exchange system'}, {'symbol': 'B01J2219/00056', 'titleFull': 'Controlling or regulating the heat exchange system involving measured parameters'}, {'symbol': 'B01J2219/00058', 'titleFull': 'Temperature measurement'}, {'symbol': 'B01J2219/0006', 'titleFull': 'Temperature measurement of the heat exchange medium'}, {'symbol': 'B01J2219/00063', 'titleFull': 'Temperature measurement of the reactants'}, {'symbol': 'B01J2219/00065', 'titleFull': 'Pressure measurement'}, {'symbol': 'B01J2219/00067', 'titleFull': 'Liquid level measurement'}, {'symbol': 'B01J2219/00069', 'titleFull': 'Flow rate measurement'}, {'symbol': 'B01J2219/00072', 'titleFull': 'Mathematical modelling'}, {'symbol': 'B01J2219/00074', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids'}, {'symbol': 'B01J2219/00076', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements inside the reactor'}, {'symbol': 'B01J2219/00078', 'titleFull': 'Fingers'}, {'symbol': 'B01J2219/00081', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00083', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00085', 'titleFull': 'Plates; Jackets; Cylinders'}, {'symbol': 'B01J2219/00087', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor'}, {'symbol': 'B01J2219/0009', 'titleFull': 'Coils'}, {'symbol': 'B01J2219/00092', 'titleFull': 'Tubes'}, {'symbol': 'B01J2219/00094', 'titleFull': 'Jackets'}, {'symbol': 'B01J2219/00096', 'titleFull': 'Plates'}, {'symbol': 'B01J2219/00099', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor the reactor being immersed in the heat exchange medium'}, {'symbol': 'B01J2219/00101', 'titleFull': 'Reflux columns'}, {'symbol': 'B01J2219/00103', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids with heat exchange elements outside the reactor in a heat exchanger separate from the reactor'}, {'symbol': 'B01J2219/00105', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling'}, {'symbol': 'B01J2219/00108', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant vapours'}, {'symbol': 'B01J2219/0011', 'titleFull': 'Controlling the temperature by indirect heating or cooling employing heat exchange fluids part or all of the reactants being heated or cooled outside the reactor while recycling involving reactant liquids'}], 'var_functions.query_db:42': []}

exec(code, env_args)
