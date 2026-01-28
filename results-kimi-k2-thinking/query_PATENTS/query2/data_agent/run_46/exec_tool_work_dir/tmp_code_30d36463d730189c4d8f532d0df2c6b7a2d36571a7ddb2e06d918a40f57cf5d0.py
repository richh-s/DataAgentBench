code = """import json

# Access stored data
german_file = locals()['var_functions.execute_python:10']
cpc_file = locals()['var_functions.query_db:18']

with open(german_file, 'r') as f:
    german_data = json.load(f)

with open(cpc_file, 'r') as f:
    cpc_defs = json.load(f)

# Count patents per CPC group level 4
group_counts = {}
for patent in german_data['all_data']:
    group = patent['cpc_group_4']
    group_counts[group] = group_counts.get(group, 0) + 1

# Find level 4 titles
titles = {}
for item in cpc_defs:
    symbol = item.get('symbol', '')
    level = item.get('level', '')
    title = item.get('titleFull', '')
    
    try:
        if int(float(level)) == 4 and symbol in group_counts:
            titles[symbol] = title
    except:
        pass

# Calculate EMA for top groups
alpha = 0.1
results = []

for group_code in list(group_counts.keys())[:15]:
    # Get monthly counts
    monthly = {}
    for patent in german_data['all_data']:
        if patent['cpc_group_4'] == group_code:
            month = patent['month']
            monthly[month] = monthly.get(month, 0) + 1
    
    # Calculate EMA
    ema = 0
    best_month = 0
    best_ema = 0
    
    for month in range(7, 13):
        current = monthly.get(month, 0)
        ema = alpha * current + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_month = month
    
    results.append({
        'cpc_group_code': group_code,
        'title_full': titles.get(group_code, 'Not found'),
        'total_patents': group_counts[group_code],
        'best_month': best_month,
        'ema_value': round(best_ema, 2)
    })

# Sort by EMA
results.sort(key=lambda x: x['ema_value'], reverse=True)

# Create final output
output = {
    'summary': {
        'total_patents': len(german_data['all_data']),
        'total_groups': len(group_counts),
        'analysis_period': 'H2 2019'
    },
    'top_groups': results[:10]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'symbol': 'C04B20/0012', 'level': '9.0', 'titleFull': 'Irregular shaped fillers'}, {'symbol': 'C04B20/0044', 'level': '9.0', 'titleFull': 'Granular materials, e.g. microballoons obtained from irregularly shaped particles'}, {'symbol': 'C04B20/002', 'level': '9.0', 'titleFull': 'Hollow or porous granular materials'}, {'symbol': 'C04B20/0052', 'level': '9.0', 'titleFull': 'Mixtures of fibres of different physical characteristics, e.g. different lengths'}, {'symbol': 'C04B20/0072', 'level': '9.0', 'titleFull': 'Continuous fibres'}, {'symbol': 'C04B20/0056', 'level': '9.0', 'titleFull': 'Hollow or porous fibres'}, {'symbol': 'C04B20/006', 'level': '9.0', 'titleFull': 'Microfibres; Nanofibres'}, {'symbol': 'C04B20/0064', 'level': '9.0', 'titleFull': 'Ground fibres'}, {'symbol': 'C04B20/0068', 'level': '9.0', 'titleFull': 'Composite fibres, e.g. fibres with a core and sheath of different material'}, {'symbol': 'C04B20/0088', 'level': '9.0', 'titleFull': 'Fillers with mono- or narrow grain size distribution'}, {'symbol': 'C04B20/008', 'level': '9.0', 'titleFull': 'Micro- or nanosized fillers, e.g. micronised fillers with particle size smaller than that of the hydraulic binder'}, {'symbol': 'C04B20/0096', 'level': '9.0', 'titleFull': 'Fillers with bimodal grain size distribution'}, {'symbol': 'C04B2103/105', 'level': '9.0', 'titleFull': 'Accelerators; Activators for reactions involving organo-silicon compounds'}, {'symbol': 'C04B2103/14', 'level': '9.0', 'titleFull': 'Hardening accelerators'}, {'symbol': 'C04B2103/12', 'level': '9.0', 'titleFull': 'Set accelerators'}, {'symbol': 'C04B2103/22', 'level': '9.0', 'titleFull': 'Set retarders'}, {'symbol': 'C04B2103/24', 'level': '9.0', 'titleFull': 'Hardening retarders'}, {'symbol': 'C04B2103/302', 'level': '9.0', 'titleFull': 'Water reducers'}, {'symbol': 'C04B2103/34', 'level': '9.0', 'titleFull': 'Flow improvers'}, {'symbol': 'C04B2103/306', 'level': '9.0', 'titleFull': 'Fluidisers with reduced air-entraning effect'}], 'var_functions.query_db:24': [{'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'E02F', 'titleFull': 'DREDGING; SOIL-SHIFTING'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'F02N', 'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01J', 'titleFull': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}]}

exec(code, env_args)
