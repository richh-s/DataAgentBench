code = """import json

# Access stored results
german_data_key = 'var_functions.execute_python:10'
cpc_data_key = 'var_functions.query_db:18'

print('German data file:', locals().get(german_data_key))
print('CPC data file:', locals().get(cpc_data_key))

# Load German patents from file
with open(locals()[german_data_key], 'r') as f:
    german_result = json.load(f)

# Load CPC definitions from file  
with open(locals()[cpc_data_key], 'r') as f:
    cpc_definitions = json.load(f)

print('German patents count:', len(german_result['all_data']))
print('CPC definitions count:', len(cpc_definitions))

# Count patents per CPC group (level 4)
group_counts = {}
for patent in german_result['all_data']:
    group = patent['cpc_group_4']
    group_counts[group] = group_counts.get(group, 0) + 1

# Find titles for level 4 CPC groups
level4_titles = {}
for cpc_item in cpc_definitions:
    symbol = cpc_item.get('symbol', '')
    level = cpc_item.get('level', '')
    title = cpc_item.get('titleFull', '')
    
    # Check if this is a level 4 symbol
    try:
        level_num = int(float(level))
        if level_num == 4:
            # Store the title for level 4 groups
            base_class = symbol[:4] if len(symbol) >= 4 else symbol
            # Only store if exactly level 4, not deeper levels
            if symbol in group_counts and len(symbol) == 4:
                level4_titles[symbol] = title
    except:
        continue

# Create results with titles for level 4 groups
results = []
for group, count in group_counts.items():
    title = level4_titles.get(group, 'Title information not found')
    results.append({
        'cpc_group_code': group,
        'title_full': title,
        'patent_count': count
    })

# Sort by patent count (since all in same year)
sorted_results = sorted(results, key=lambda x: x['patent_count'], reverse=True)

print('Top 10 CPC groups in Germany H2 2019:')
for i, item in enumerate(sorted_results[:10], 1):
    print(f"{i}. {item['cpc_group_code']}: {item['patent_count']} patents - {item['title_full'][:60]}...")

# Calculate EMA (exponential moving average)
# For single year data, use monthly distribution
alpha = 0.1
group_ema_results = []

for result_item in sorted_results[:10]:
    group = result_item['cpc_group_code']
    title = result_item['title_full']
    total_patents = result_item['patent_count']
    
    # Get monthly data for this group
    monthly_counts = {}
    for patent in german_result['all_data']:
        if patent['cpc_group_4'] == group:
            month = patent['month']
            monthly_counts[month] = monthly_counts.get(month, 0) + 1
    
    # Calculate EMA for months 7-12 (H2 2019)
    ema = 0
    best_month = None
    best_ema = 0
    
    for month in range(7, 13):  # July to December
        current_value = monthly_counts.get(month, 0)
        ema = alpha * current_value + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_month = month
    
    group_ema_results.append({
        'cpc_group_code': group,
        'title_full': title,
        'total_patents': total_patents,
        'best_month': best_month,
        'ema_value': round(best_ema, 2)
    })

print('\nTop groups with EMA:')
for item in group_ema_results:
    month_name = {
        7: 'July', 8: 'August', 9: 'September',
        10: 'October', 11: 'November', 12: 'December'
    }.get(item['best_month'], 'Unknown')
    print(f"{item['cpc_group_code']}: EMA={item['ema_value']} (peak in {month_name})")

# Final result
final_output = {
    'analysis_summary': {
        'total_german_patents_h2_2019': len(german_result['all_data']),
        'total_cpc_groups': len(group_counts),
        'smoothing_factor': alpha
    },
    'top_groups': group_ema_results
}

# Print final result in required format
print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'symbol': 'C04B20/0012', 'level': '9.0', 'titleFull': 'Irregular shaped fillers'}, {'symbol': 'C04B20/0044', 'level': '9.0', 'titleFull': 'Granular materials, e.g. microballoons obtained from irregularly shaped particles'}, {'symbol': 'C04B20/002', 'level': '9.0', 'titleFull': 'Hollow or porous granular materials'}, {'symbol': 'C04B20/0052', 'level': '9.0', 'titleFull': 'Mixtures of fibres of different physical characteristics, e.g. different lengths'}, {'symbol': 'C04B20/0072', 'level': '9.0', 'titleFull': 'Continuous fibres'}, {'symbol': 'C04B20/0056', 'level': '9.0', 'titleFull': 'Hollow or porous fibres'}, {'symbol': 'C04B20/006', 'level': '9.0', 'titleFull': 'Microfibres; Nanofibres'}, {'symbol': 'C04B20/0064', 'level': '9.0', 'titleFull': 'Ground fibres'}, {'symbol': 'C04B20/0068', 'level': '9.0', 'titleFull': 'Composite fibres, e.g. fibres with a core and sheath of different material'}, {'symbol': 'C04B20/0088', 'level': '9.0', 'titleFull': 'Fillers with mono- or narrow grain size distribution'}, {'symbol': 'C04B20/008', 'level': '9.0', 'titleFull': 'Micro- or nanosized fillers, e.g. micronised fillers with particle size smaller than that of the hydraulic binder'}, {'symbol': 'C04B20/0096', 'level': '9.0', 'titleFull': 'Fillers with bimodal grain size distribution'}, {'symbol': 'C04B2103/105', 'level': '9.0', 'titleFull': 'Accelerators; Activators for reactions involving organo-silicon compounds'}, {'symbol': 'C04B2103/14', 'level': '9.0', 'titleFull': 'Hardening accelerators'}, {'symbol': 'C04B2103/12', 'level': '9.0', 'titleFull': 'Set accelerators'}, {'symbol': 'C04B2103/22', 'level': '9.0', 'titleFull': 'Set retarders'}, {'symbol': 'C04B2103/24', 'level': '9.0', 'titleFull': 'Hardening retarders'}, {'symbol': 'C04B2103/302', 'level': '9.0', 'titleFull': 'Water reducers'}, {'symbol': 'C04B2103/34', 'level': '9.0', 'titleFull': 'Flow improvers'}, {'symbol': 'C04B2103/306', 'level': '9.0', 'titleFull': 'Fluidisers with reduced air-entraning effect'}], 'var_functions.query_db:24': [{'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'E02F', 'titleFull': 'DREDGING; SOIL-SHIFTING'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'F02N', 'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01J', 'titleFull': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}]}

exec(code, env_args)
