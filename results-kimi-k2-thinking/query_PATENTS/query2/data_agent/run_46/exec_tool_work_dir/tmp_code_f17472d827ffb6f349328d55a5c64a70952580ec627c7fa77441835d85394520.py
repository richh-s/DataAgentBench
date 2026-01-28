code = """import json

print('Loading data...')

# Load German patents data
german_file = var_functions.execute_python:10
print('German file path:', german_file)

with open(german_file, 'r') as f:
    german_data = json.load(f)

print('German patents loaded:', len(german_data['all_data']))
print('Top groups:', german_data['top_groups'])

# Load CPC definitions
cpc_file = var_functions.query_db:18
print('CPC file path:', cpc_file)

with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

print('CPC definitions loaded:', len(cpc_definitions))

# Get all CPC groups and their counts from German patents
all_groups = {}
for patent in german_data['all_data']:
    group = patent['cpc_group_4']
    all_groups[group] = all_groups.get(group, 0) + 1

print('Unique CPC groups:', len(all_groups))

# Find level 4 definitions for these groups
level_4_titles = {}
for def_item in cpc_definitions:
    symbol = def_item.get('symbol', '')
    level = def_item.get('level', '')
    title = def_item.get('titleFull', '')
    
    try:
        level_num = int(float(level))
        if level_num == 4 and symbol in all_groups:
            level_4_titles[symbol] = title
    except:
        pass

print('Level 4 titles found:', len(level_4_titles))

# Calculate monthly counts for each group
group_monthly = {}
for patent in german_data['all_data']:
    group = patent['cpc_group_4']
    month = patent['month']
    
    if group not in group_monthly:
        group_monthly[group] = {}
    
    group_monthly[group][month] = group_monthly[group].get(month, 0) + 1

# Calculate EMA for each group
alpha = 0.1
results = []

for group in all_groups:
    if group not in group_monthly:
        continue
    
    monthly_counts = group_monthly[group]
    
    # Calculate EMA for months 7-12
    ema_prev = 0
    best_month = None
    best_ema = 0
    
    for month in range(7, 13):
        current = monthly_counts.get(month, 0)
        ema_current = alpha * current + (1 - alpha) * ema_prev
        
        if ema_current > best_ema:
            best_ema = ema_current
            best_month = month
        
        ema_prev = ema_current
    
    title = level_4_titles.get(group, 'Title not found')
    
    results.append({
        'cpc_group_code': group,
        'title_full': title,
        'total_patents': all_groups[group],
        'best_month': best_month,
        'best_ema': round(best_ema, 2),
        'monthly_counts': monthly_counts
    })

# Sort by best EMA
results.sort(key=lambda x: x['best_ema'], reverse=True)

print('Top 10 groups by EMA:')
for i, r in enumerate(results[:10]):
    print(i+1, r['cpc_group_code'], 'EMA:', r['best_ema'], 'Month:', r['best_month'])

# Create final summary
summary = {
    'total_patents': len(german_data['all_data']),
    'total_groups': len(all_groups),
    'top_groups': results[:10]
}

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'symbol': 'C04B20/0012', 'level': '9.0', 'titleFull': 'Irregular shaped fillers'}, {'symbol': 'C04B20/0044', 'level': '9.0', 'titleFull': 'Granular materials, e.g. microballoons obtained from irregularly shaped particles'}, {'symbol': 'C04B20/002', 'level': '9.0', 'titleFull': 'Hollow or porous granular materials'}, {'symbol': 'C04B20/0052', 'level': '9.0', 'titleFull': 'Mixtures of fibres of different physical characteristics, e.g. different lengths'}, {'symbol': 'C04B20/0072', 'level': '9.0', 'titleFull': 'Continuous fibres'}, {'symbol': 'C04B20/0056', 'level': '9.0', 'titleFull': 'Hollow or porous fibres'}, {'symbol': 'C04B20/006', 'level': '9.0', 'titleFull': 'Microfibres; Nanofibres'}, {'symbol': 'C04B20/0064', 'level': '9.0', 'titleFull': 'Ground fibres'}, {'symbol': 'C04B20/0068', 'level': '9.0', 'titleFull': 'Composite fibres, e.g. fibres with a core and sheath of different material'}, {'symbol': 'C04B20/0088', 'level': '9.0', 'titleFull': 'Fillers with mono- or narrow grain size distribution'}, {'symbol': 'C04B20/008', 'level': '9.0', 'titleFull': 'Micro- or nanosized fillers, e.g. micronised fillers with particle size smaller than that of the hydraulic binder'}, {'symbol': 'C04B20/0096', 'level': '9.0', 'titleFull': 'Fillers with bimodal grain size distribution'}, {'symbol': 'C04B2103/105', 'level': '9.0', 'titleFull': 'Accelerators; Activators for reactions involving organo-silicon compounds'}, {'symbol': 'C04B2103/14', 'level': '9.0', 'titleFull': 'Hardening accelerators'}, {'symbol': 'C04B2103/12', 'level': '9.0', 'titleFull': 'Set accelerators'}, {'symbol': 'C04B2103/22', 'level': '9.0', 'titleFull': 'Set retarders'}, {'symbol': 'C04B2103/24', 'level': '9.0', 'titleFull': 'Hardening retarders'}, {'symbol': 'C04B2103/302', 'level': '9.0', 'titleFull': 'Water reducers'}, {'symbol': 'C04B2103/34', 'level': '9.0', 'titleFull': 'Flow improvers'}, {'symbol': 'C04B2103/306', 'level': '9.0', 'titleFull': 'Fluidisers with reduced air-entraning effect'}], 'var_functions.query_db:24': [{'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'E02F', 'titleFull': 'DREDGING; SOIL-SHIFTING'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'F02N', 'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01J', 'titleFull': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}]}

exec(code, env_args)
