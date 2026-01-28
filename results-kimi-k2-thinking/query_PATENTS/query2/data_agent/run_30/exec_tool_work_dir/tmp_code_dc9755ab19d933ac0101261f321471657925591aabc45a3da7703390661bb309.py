code = """import json
import re
from collections import Counter

# Read the file from previous query
file_path = locals()['var_functions.query_db:15']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Filter for German patents granted in second half of 2019
filtered_patents = []
th_2019_months = ['July', 'August', 'September', 'October', 'November', 'December']

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    
    # Check if German
    if 'DE' not in patents_info:
        continue
    
    # Check if 2019
    if '2019' not in grant_date:
        continue
    
    # Check if second half
    is_second_half = any(month in grant_date for month in th_2019_months)
    if not is_second_half:
        continue
    
    filtered_patents.append(patent)

print('German patents in second half of 2019:', len(filtered_patents))

# Extract CPC codes at level 4 (5 characters: section+class+subclass+group digit)
cpc_level4_data = []

for patent in filtered_patents:
    grant_date = patent.get('grant_date', '')
    cpc_field = patent.get('cpc', '[]')
    
    try:
        cpc_list = json.loads(cpc_field)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        # Split by '/' to get main group
        parts = code.split('/')
        if len(parts) >= 1:
            main_group = parts[0]
            # For level 4, we need format like: A61M1, C04B7, H04L9
            if len(main_group) >= 5:
                level4_code = main_group[:5]
                cpc_level4_data.append({
                    'cpc_code': level4_code,
                    'full_code': code,
                    'patent_info': patent['Patents_info'],
                    'grant_date': grant_date,
                    'year': 2019
                })

print('CPC level 4 entries extracted:', len(cpc_level4_data))

# Count occurrences of each level 4 CPC code
cpc_counts = Counter()
cpc_year_patents = {}

for item in cpc_level4_data:
    code = item['cpc_code']
    cpc_counts[code] += 1
    if code not in cpc_year_patents:
        cpc_year_patents[code] = []
    cpc_year_patents[code].append(item['patent_info'])

print('Unique level 4 CPC codes:', len(cpc_counts))

# Get top CPC codes by count
top_cpc = cpc_counts.most_common(20)
print('Top 20 CPC level 4 codes:')
for code, count in top_cpc:
    print(f'  {code}: {count}')

# Prepare results
result = {
    'german_patents_h2_2019': len(filtered_patents),
    'level4_cpc_entries': len(cpc_level4_data),
    'unique_level4_cpc': len(cpc_counts),
    'top_level4_cpc': top_cpc,
    'all_level4_cpc_codes': list(cpc_counts.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'filtered_patents_count': 72, 'cpc_level4_entries': 878, 'unique_cpc_codes_count': 97, 'top_cpc_codes': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]], 'all_unique_cpc_codes': ['B29L', 'A61K', 'F23L', 'C04B', 'F21V', 'E01F', 'B64D', 'B60Y', 'B01L', 'Y02D', 'C22F', 'B29D', 'F23N', 'G06N', 'G01R', 'A61P', 'G01L', 'H01L', 'F24F', 'G01N', 'B60W', 'B81C', 'Y04S', 'G06E', 'A61C', 'G01J', 'H01H', 'B60R', 'Y02A', 'B41F', 'C09K', 'F02M', 'B23K', 'B30B', 'F02D', 'F24B', 'G06T', 'B81B', 'Y02T', 'F04B', 'B60S', 'G01B', 'B82Y', 'H02K', 'F41H', 'A61F', 'F23B', 'F42B', 'E21B', 'Y02W', 'G02B', 'B01J', 'H04N', 'F04C', 'F02N', 'G05D', 'Y02P', 'E05Y', 'A61M', 'G08C', 'G07C', 'E05F', 'F01C', 'B27L', 'C22C', 'B22F', 'A61G', 'Y02B', 'F17C', 'E05B', 'B02C', 'G08B', 'A24C', 'B62B', 'C23F', 'F16C', 'Y02E', 'Y10T', 'H04W', 'H04L', 'B60K', 'B29K', 'F04D', 'B29C', 'G06F', 'G01D', 'C07K', 'H01R', 'F16H', 'A43B', 'A61B', 'B66C', 'F16K', 'A47C', 'B63B', 'E02F', 'B60N']}, 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:12': {'german_patents_2019_h2': 72, 'cpc_entries': 878, 'unique_cpc_codes': 97, 'cpc_code_list': ['A61M', 'F04C', 'F01C', 'E21B', 'G02B', 'G01J', 'G01B', 'G01D', 'G01R', 'H02K', 'F04D', 'G08C', 'G07C', 'B60R', 'E05B', 'B41F', 'F02D', 'F02M', 'F04B', 'B23K', 'B63B', 'H04W', 'H04L', 'Y02D', 'B66C', 'E02F', 'B60S', 'G06E', 'G06N', 'A61P', 'A61K', 'G06T', 'H04N', 'G06F', 'B60K', 'B30B', 'G01L', 'Y02T', 'F16C', 'A61F', 'A43B', 'F24B', 'F23L', 'F23B', 'F23N', 'Y02E', 'H01R', 'B64D', 'H01L', 'F02N', 'B60W', 'C04B', 'C09K', 'B29C', 'A61B', 'F21V', 'Y02P', 'Y02B', 'G01N', 'B81B', 'B01L', 'B81C', 'B01J', 'Y10T', 'B29D', 'H01H', 'A61G', 'A47C', 'E01F', 'B29K', 'C07K', 'B22F', 'C22C', 'Y02W', 'B27L', 'C22F', 'F24F', 'E05Y', 'B60Y', 'E05F', 'A61C', 'C23F', 'F16H', 'A24C', 'B82Y', 'B62B', 'Y04S', 'Y02A', 'B29L', 'B60N', 'F42B', 'F41H', 'G08B', 'B02C', 'F17C', 'G05D', 'F16K'], 'top_cpc': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]]}, 'var_functions.execute_python:14': {'total_cpc_groups': 97, 'cpc_codes': ['A61M', 'F04C', 'F01C', 'E21B', 'G02B', 'G01J', 'G01B', 'G01D', 'G01R', 'H02K', 'F04D', 'G08C', 'G07C', 'B60R', 'E05B', 'B41F', 'F02D', 'F02M', 'F04B', 'B23K', 'B63B', 'H04W', 'H04L', 'Y02D', 'B66C', 'E02F', 'B60S', 'G06E', 'G06N', 'A61P', 'A61K', 'G06T', 'H04N', 'G06F', 'B60K', 'B30B', 'G01L', 'Y02T', 'F16C', 'A61F', 'A43B', 'F24B', 'F23L', 'F23B', 'F23N', 'Y02E', 'H01R', 'B64D', 'H01L', 'F02N', 'B60W', 'C04B', 'C09K', 'B29C', 'A61B', 'F21V', 'Y02P', 'Y02B', 'G01N', 'B81B', 'B01L', 'B81C', 'B01J', 'Y10T', 'B29D', 'H01H', 'A61G', 'A47C', 'E01F', 'B29K', 'C07K', 'B22F', 'C22C', 'Y02W', 'B27L', 'C22F', 'F24F', 'E05Y', 'B60Y', 'E05F', 'A61C', 'C23F', 'F16H', 'A24C', 'B82Y', 'B62B', 'Y04S', 'Y02A', 'B29L', 'B60N', 'F42B', 'F41H', 'G08B', 'B02C', 'F17C', 'G05D', 'F16K'], 'top_groups': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]]}, 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.query_db:18': [{'symbol': 'A61M', 'titleFull': 'DEVICES FOR INTRODUCING MEDIA INTO, OR ONTO, THE BODY; DEVICES FOR TRANSDUCING BODY MEDIA OR FOR TAKING MEDIA FROM THE BODY; DEVICES FOR PRODUCING OR ENDING SLEEP OR STUPOR', 'level': '5.0'}, {'symbol': 'A61B', 'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'level': '5.0'}, {'symbol': 'B23K', 'titleFull': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM', 'level': '5.0'}, {'symbol': 'B60N', 'titleFull': 'SEATS SPECIALLY ADAPTED FOR VEHICLES; VEHICLE PASSENGER ACCOMMODATION NOT OTHERWISE PROVIDED FOR', 'level': '5.0'}, {'symbol': 'B60K', 'titleFull': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'level': '5.0'}, {'symbol': 'F17C', 'titleFull': 'VESSELS FOR CONTAINING OR STORING COMPRESSED, LIQUEFIED OR SOLIDIFIED GASES; FIXED-CAPACITY GAS-HOLDERS; FILLING VESSELS WITH, OR DISCHARGING FROM VESSELS, COMPRESSED, LIQUEFIED, OR SOLIDIFIED GASES', 'level': '5.0'}, {'symbol': 'H02K', 'titleFull': 'DYNAMO-ELECTRIC MACHINES', 'level': '5.0'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS', 'level': '5.0'}, {'symbol': 'B01J', 'titleFull': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS', 'level': '5.0'}, {'symbol': 'B01L', 'titleFull': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE', 'level': '5.0'}, {'symbol': 'B29K', 'titleFull': 'INDEXING SCHEME ASSOCIATED WITH SUBCLASSES B29B, B29C OR B29D, RELATING TO MOULDING MATERIALS OR TO MATERIALS FOR MOULDS, REINFORCEMENTS, FILLERS OR PREFORMED PARTS, e.g. INSERTS', 'level': '5.0'}, {'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING', 'level': '5.0'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE', 'level': '5.0'}, {'symbol': 'F04C', 'titleFull': 'ROTARY-PISTON, OR OSCILLATING-PISTON, POSITIVE-DISPLACEMENT MACHINES FOR LIQUIDS; ROTARY-PISTON, OR OSCILLATING-PISTON, POSITIVE-DISPLACEMENT PUMPS', 'level': '5.0'}, {'symbol': 'F04D', 'titleFull': 'NON-POSITIVE-DISPLACEMENT PUMPS', 'level': '5.0'}, {'symbol': 'G01R', 'titleFull': 'MEASURING ELECTRIC VARIABLES; MEASURING MAGNETIC VARIABLES', 'level': '5.0'}, {'symbol': 'G01N', 'titleFull': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES', 'level': '5.0'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION', 'level': '5.0'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS', 'level': '5.0'}, {'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING', 'level': '5.0'}]}

exec(code, env_args)
