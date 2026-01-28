code = """import json
import re

# Get the CPC definition results file
cpc_def_file = var_functions.query_db:18
with open(cpc_def_file, 'r') as f:
    cpc_definitions = json.load(f)

# Get the analysis results from previous step
analysis_data = var_functions.execute_python:8
cpc_groups = analysis_data['cpc_groups']

print(f"Found {len(cpc_definitions)} CPC definitions")
print(f"Found {len(cpc_groups)} CPC groups from analysis")

# Create a mapping from the query results
cpc_title_map = {}
for def_item in cpc_definitions:
    symbol = def_item['symbol']
    title = def_item['titleFull']
    
    # Extract level 4 prefix
    match = re.match(r'^([A-Z]\d{2}[A-Z]\d)', symbol)
    if match:
        level4 = match.group(1)
        if level4 not in cpc_title_map:
            cpc_title_map[level4] = title

# Combine with our analysis results
final_results = []
for group in cpc_groups:
    level4_code = group['cpc_level4_code']
    final_results.append({
        'cpc_level4_code': level4_code,
        'full_code': group['full_code'],
        'title': cpc_title_map.get(level4_code, 'Title not found'),
        'best_year': 2019,
        'best_month': group['best_month'],
        'monthly_count': group['best_month_count'],
        'ema_value': round(group['ema'], 2)
    })

# Sort by EMA value in descending order
final_results.sort(key=lambda x: x['ema_value'], reverse=True)

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'cpc_groups': [{'cpc_level4_code': 'C04B2', 'full_code': 'C04B2235/662', 'best_month': 12, 'best_month_count': 32, 'ema': 32}, {'cpc_level4_code': 'H04W5', 'full_code': 'H04W52/0229', 'best_month': 8, 'best_month_count': 12, 'ema': 12}, {'cpc_level4_code': 'C04B3', 'full_code': 'C04B35/6455', 'best_month': 12, 'best_month_count': 12, 'ema': 12}, {'cpc_level4_code': 'F02M5', 'full_code': 'F02M59/06', 'best_month': 8, 'best_month_count': 10, 'ema': 10}, {'cpc_level4_code': 'H04W7', 'full_code': 'H04W76/28', 'best_month': 8, 'best_month_count': 10, 'ema': 10}, {'cpc_level4_code': 'H04L1', 'full_code': 'H04L1/1671', 'best_month': 8, 'best_month_count': 10, 'ema': 10}, {'cpc_level4_code': 'H01J4', 'full_code': 'H01J49/0431', 'best_month': 8, 'best_month_count': 10, 'ema': 10}, {'cpc_level4_code': 'G02B1', 'full_code': 'G02B15/143507', 'best_month': 7, 'best_month_count': 7, 'ema': 7}, {'cpc_level4_code': 'A61F5', 'full_code': 'A61F5/0111', 'best_month': 12, 'best_month_count': 6, 'ema': 6}, {'cpc_level4_code': 'F23L1', 'full_code': 'F23L15/04', 'best_month': 8, 'best_month_count': 6, 'ema': 6}, {'cpc_level4_code': 'H01L2', 'full_code': 'H01L2924/16195', 'best_month': 7, 'best_month_count': 6, 'ema': 6}, {'cpc_level4_code': 'H03L7', 'full_code': 'H03L7/1976', 'best_month': 10, 'best_month_count': 6, 'ema': 6}, {'cpc_level4_code': 'G02B2', 'full_code': 'G02B23/2438', 'best_month': 10, 'best_month_count': 6, 'ema': 5.1}, {'cpc_level4_code': 'H04L5', 'full_code': 'H04L5/0007', 'best_month': 8, 'best_month_count': 4, 'ema': 4}, {'cpc_level4_code': 'G01M1', 'full_code': 'G01M1/24', 'best_month': 11, 'best_month_count': 4, 'ema': 4}, {'cpc_level4_code': 'F02N2', 'full_code': 'F02N2200/023', 'best_month': 10, 'best_month_count': 4, 'ema': 4}, {'cpc_level4_code': 'G01L2', 'full_code': 'G01L23/22', 'best_month': 10, 'best_month_count': 4, 'ema': 4}, {'cpc_level4_code': 'H02J7', 'full_code': 'H02J7/007182', 'best_month': 8, 'best_month_count': 4, 'ema': 4}, {'cpc_level4_code': 'B41F2', 'full_code': 'B41F21/00', 'best_month': 11, 'best_month_count': 3, 'ema': 3}, {'cpc_level4_code': 'F16C3', 'full_code': 'F16C33/4635', 'best_month': 12, 'best_month_count': 3, 'ema': 3}]}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.query_db:14': [{'symbol': 'C04B20/00', 'titleFull': 'Use of materials as fillers for mortars, concrete or artificial stone according to more than one of groups C04B14/00\xa0-\xa0C04B18/00 and characterised by shape or grain distribution; Treatment of materials according to more than one of the groups C04B14/00\xa0-\xa0C04B18/00 specially adapted to enhance their filling properties in mortars, concrete or artificial stone; Expanding or defibrillating materials', 'level': '7.0'}, {'symbol': 'C04B2/00', 'titleFull': 'Lime, magnesia or dolomite', 'level': '7.0'}, {'symbol': 'C04B2290/00', 'titleFull': 'Organisational aspects of production methods, equipment or plants', 'level': '7.0'}, {'symbol': 'C04B2111/00', 'titleFull': 'Mortars, concrete or artificial stone or mixtures to prepare them, characterised by specific function, property or use', 'level': '7.0'}, {'symbol': 'C04B22/00', 'titleFull': 'Use of inorganic materials as active ingredients for mortars, concrete or artificial stone, e.g. accelerators, shrinkage compensating agents', 'level': '7.0'}, {'symbol': 'C04B26/00', 'titleFull': 'Compositions of mortars, concrete or artificial stone, containing only organic binders, e.g. polymer or resin concrete', 'level': '7.0'}, {'symbol': 'C04B24/00', 'titleFull': 'Use of organic materials as active ingredients for mortars, concrete or artificial stone, e.g. plasticisers', 'level': '7.0'}, {'symbol': 'C04B2237/00', 'titleFull': 'Aspects relating to ceramic laminates or to joining of ceramic articles with other articles by heating', 'level': '7.0'}, {'symbol': 'C04B28/00', 'titleFull': 'Compositions of mortars, concrete or artificial stone, containing inorganic binders or the reaction product of an inorganic and an organic binder, e.g. polycarboxylate cements', 'level': '7.0'}, {'symbol': 'C04B2201/00', 'titleFull': 'Mortars, concrete or artificial stone characterised by specific physical values', 'level': '7.0'}], 'var_functions.query_db:16': [{'symbol': 'F02M5/00', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level'}, {'symbol': 'C04B2/10', 'titleFull': 'Preheating, burning calcining or cooling'}, {'symbol': 'C04B2/005', 'titleFull': 'Lime, magnesia or dolomite obtained from an industrial by-product'}, {'symbol': 'C04B2/02', 'titleFull': 'Lime'}, {'symbol': 'F02M5/02', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level with provisions to meet variations in carburettor position, e.g. upside-down position in aircraft'}, {'symbol': 'F02M5/06', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level having adjustable float mechanism, e.g. to meet dissimilarities in specific gravity of different fuels'}, {'symbol': 'F02M5/08', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level having means for venting float chambers'}, {'symbol': 'F02M5/10', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level having means for preventing vapour lock, e.g. insulated float chambers or forced fuel circulation through float chamber with engine stopped'}, {'symbol': 'F02M5/12', 'titleFull': 'Other details, e.g. floats, valves, setting devices or tools'}, {'symbol': 'C04B2/04', 'titleFull': 'Slaking'}, {'symbol': 'C04B2/106', 'titleFull': 'Preheating, burning calcining or cooling in fluidised bed furnaces'}, {'symbol': 'C04B2/104', 'titleFull': 'Ingredients added before or during the burning process'}, {'symbol': 'C04B2/102', 'titleFull': 'Preheating, burning calcining or cooling of magnesia, e.g. dead burning'}, {'symbol': 'C04B2/12', 'titleFull': 'Preheating, burning calcining or cooling in shaft or vertical furnaces'}, {'symbol': 'C04B2/108', 'titleFull': 'Treatment or selection of the fuel therefor'}, {'symbol': 'F02M5/04', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level with provisions to meet variations in carburettor position, e.g. upside-down position in aircraft with pivotally or rotatably mounted float chambers'}, {'symbol': 'F02M5/085', 'titleFull': 'Float-controlled apparatus for maintaining a constant fuel level having means for venting float chambers consisting of an overflow from the float chamber'}, {'symbol': 'F02M5/105', 'titleFull': 'Auxiliary input valve which can be regulated to obtain an increased fuel supply from the float chamber'}, {'symbol': 'F02M5/125', 'titleFull': 'Shape of the jet needle'}, {'symbol': 'F02M5/14', 'titleFull': 'Float chambers, e.g. adjustable in position'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
