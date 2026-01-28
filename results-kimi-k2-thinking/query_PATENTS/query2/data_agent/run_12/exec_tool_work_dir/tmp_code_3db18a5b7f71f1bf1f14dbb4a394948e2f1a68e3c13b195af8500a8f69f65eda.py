code = """import json
import re
from collections import defaultdict

# Load German patent data with historical data
result_path = locals()['var_functions.query_db:62']
if isinstance(result_path, str) and result_path.endswith('.json'):
    with open(result_path, 'r') as f:
        patents = json.load(f)
else:
    patents = result_path

print('Total German patents loaded:', len(patents))

# Function to extract year from grant_date
def extract_year(date_str):
    match = re.search(r'(\d{4})', date_str)
    return int(match.group(1)) if match else None

# Function to extract level 4 CPC codes
def get_cpc_level4(cpc_str):
    try:
        cpc_list = json.loads(cpc_str)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                codes.add(code[:4])
        return list(codes)
    except:
        return []

# Build yearly counts for each CPC code
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
years_found = set()

for rec in patents:
    year = extract_year(rec.get('grant_date', ''))
    if year:
        years_found.add(year)
        cpc_codes = get_cpc_level4(rec.get('cpc', '[]'))
        for cpc in cpc_codes:
            cpc_yearly_counts[cpc][year] += 1

# Sort years
sorted_years = sorted(list(years_found))
print('Year range:', sorted_years)
print('Total CPC level 4 codes:', len(cpc_yearly_counts))

# Calculate Exponential Moving Average (EMA) for each CPC code
# Smoothing factor alpha = 0.1
alpha = 0.1
cpc_ema_results = {}

for cpc in cpc_yearly_counts:
    ema_values = {}
    ema = None
    
    for year in sorted_years:
        count = cpc_yearly_counts[cpc].get(year, 0)
        if ema is None:
            # Initialize with first value
            ema = count
        else:
            # EMA formula: EMA_t = alpha * value_t + (1 - alpha) * EMA_{t-1}
            ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    if ema_values:
        # Find year with highest EMA
        best_year = max(ema_values.items(), key=lambda x: x[1])
        cpc_ema_results[cpc] = {
            'best_year': best_year[0],
            'best_ema': best_year[1],
            'ema_values': ema_values
        }

# Sort by best EMA value
top_cpc_by_ema = sorted(cpc_ema_results.items(), key=lambda x: x[1]['best_ema'], reverse=True)

print('\nTop 15 CPC codes by highest EMA:')
for i, (cpc, data) in enumerate(top_cpc_by_ema[:15]):
    print(f"{i+1}. {cpc}: Best EMA={data['best_ema']:.2f} in year {data['best_year']}")

# Store results for getting titles
results_to_query = {
    'top_cpc_codes': [(cpc, data['best_year'], data['best_ema']) for cpc, data in top_cpc_by_ema[:10]],
    'all_cpc_data': cpc_ema_results
}

print('\n__RESULT__:')
print(json.dumps(results_to_query))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': [{'total': '216'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:56': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.execute_python:58': {'cpc_codes': ['A61K', 'H05K', 'A43B', 'F41H', 'B23Q', 'H03L', 'H01L', 'C08G', 'B02C', 'G01D', 'H04W', 'E02F', 'E21D', 'B62D', 'E05Y', 'G01F', 'F02D', 'F01C', 'H02K', 'Y02W', 'A45D', 'A23L', 'C07D', 'F01N', 'B60R', 'F16K', 'B63B', 'H01F', 'C22C', 'F05D', 'F02M', 'F04C', 'F16F', 'G08B', 'C07C', 'B22F', 'F23L', 'B60K', 'B01D', 'G01L', 'Y02A', 'Y02B', 'H04L', 'A24C', 'A61C', 'A61F', 'C09K', 'F42B', 'G01B', 'F24B', 'B41F', 'B60S', 'Y10T', 'E21B', 'H01J', 'C07K', 'B01J', 'E21C', 'Y02E', 'F02N', 'G08C', 'F16H', 'B60W', 'G05D', 'F04D', 'F16C', 'B64D', 'Y04S', 'G01N', 'F23B', 'G01R', 'F04B', 'A47C', 'E21F', 'F01D', 'G01M', 'C04B', 'H01H', 'B60Y', 'A61P', 'F21S', 'G06T', 'G07C', 'F21Y', 'F17C', 'A61M', 'A47J', 'C25D', 'G01J', 'B82Y', 'B62B', 'C22F', 'Y02C', 'H04J', 'G02B', 'B33Y', 'B60N', 'B66C', 'G01S', 'E05F', 'H01Q', 'F21V', 'E01F', 'B81B', 'F41G', 'B23K', 'A21C', 'F23N', 'Y02D', 'G06E', 'B81C', 'Y02T', 'B29K', 'A01H', 'A61L', 'H04N', 'B01L', 'B42D', 'H02J', 'G06N', 'B29C', 'A61B', 'F24F', 'C23F', 'C07F', 'B29L', 'C12Q', 'A61G', 'G06F', 'E05B', 'B29D', 'F02P', 'B27L', 'Y02P', 'F16D', 'B30B', 'C08L', 'H01R'], 'top_cpcs': [['Y02E', 9], ['A61B', 8], ['Y02P', 8], ['G06F', 7], ['Y02A', 6], ['H04L', 5], ['B29C', 5], ['G01N', 5], ['Y02B', 5], ['G02B', 4], ['B60R', 4], ['B60K', 4], ['A61M', 3], ['F02D', 3], ['H04W', 3]], 'counts': {'F41H': 2, 'G01S': 1, 'F41G': 1, 'A61M': 3, 'F04C': 1, 'F01C': 1, 'E21B': 1, 'G01B': 1, 'G02B': 4, 'G01R': 2, 'G01J': 1, 'G01D': 2, 'F04D': 2, 'H02K': 1, 'G08C': 1, 'G07C': 2, 'E05B': 2, 'B60R': 4, 'B41F': 1, 'F02D': 3, 'F02M': 2, 'F04B': 1, 'B23K': 2, 'B63B': 1, 'Y02D': 2, 'H04W': 3, 'H04L': 5, 'E02F': 2, 'B66C': 1, 'B60S': 1, 'G06E': 1, 'G06N': 1, 'A61P': 2, 'A61K': 2, 'H05K': 1, 'C08L': 1, 'C25D': 1, 'H01L': 2, 'C08G': 1, 'H04N': 2, 'G06F': 7, 'B60K': 4, 'G06T': 2, 'B30B': 1, 'G01L': 2, 'H04J': 1, 'Y02T': 3, 'F16C': 1, 'A21C': 1, 'A47J': 1, 'A61F': 2, 'A43B': 1, 'E21F': 1, 'E21C': 1, 'E21D': 1, 'F23B': 1, 'F24B': 1, 'F23L': 1, 'F23N': 1, 'Y02E': 9, 'H01J': 1, 'F16F': 1, 'F01D': 1, 'G01M': 1, 'F05D': 1, 'B64D': 1, 'H01R': 2, 'B62D': 1, 'F02N': 1, 'B60W': 1, 'C04B': 2, 'C09K': 2, 'B29C': 5, 'G01N': 5, 'A61L': 1, 'A61B': 8, 'F21V': 2, 'Y02P': 8, 'A45D': 1, 'Y02B': 5, 'Y02A': 6, 'H01F': 1, 'F02P': 1, 'B01L': 2, 'B81C': 1, 'B81B': 1, 'B01J': 2, 'B23Q': 1, 'B33Y': 1, 'H01H': 1, 'Y10T': 2, 'B29D': 1, 'A47C': 1, 'A61G': 1, 'B29K': 2, 'E01F': 1, 'C07K': 1, 'C22C': 2, 'B22F': 2, 'Y02W': 2, 'F21Y': 1, 'F21S': 1, 'B27L': 1, 'C22F': 1, 'F24F': 1, 'B42D': 1, 'B60Y': 1, 'E05F': 1, 'E05Y': 1, 'A61C': 1, 'C23F': 1, 'G01F': 1, 'F16H': 1, 'F16D': 1, 'A24C': 1, 'B82Y': 1, 'B62B': 1, 'Y04S': 1, 'C07D': 1, 'C07F': 1, 'B29L': 1, 'B60N': 2, 'B01D': 1, 'F01N': 1, 'C07C': 1, 'Y02C': 1, 'H02J': 1, 'H03L': 1, 'F42B': 1, 'G08B': 1, 'H01Q': 1, 'B02C': 1, 'F16K': 1, 'F17C': 1, 'G05D': 1, 'A23L': 1, 'C12Q': 1, 'A01H': 1}}, 'var_functions.query_db:60': [{'symbol': 'A61B', 'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION'}, {'symbol': 'Y02E', 'titleFull': 'REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION'}, {'symbol': 'Y02A', 'titleFull': 'TECHNOLOGIES FOR ADAPTATION TO CLIMATE CHANGE'}, {'symbol': 'Y02B', 'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES RELATED TO BUILDINGS, e.g. HOUSING, HOUSE APPLIANCES OR RELATED END-USER APPLICATIONS'}, {'symbol': 'Y02P', 'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN THE PRODUCTION OR PROCESSING OF GOODS'}, {'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'G01N', 'titleFull': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
