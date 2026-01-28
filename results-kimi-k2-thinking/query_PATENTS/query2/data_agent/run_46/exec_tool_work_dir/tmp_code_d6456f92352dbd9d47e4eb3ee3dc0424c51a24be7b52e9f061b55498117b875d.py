code = """import json

# Load German patents data
german_file = var_functions.execute_python:10
with open(german_file, 'r') as f:
    german_data = json.load(f)

# Load CPC definitions data
cpc_file = var_functions.query_db:18
with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

print('Loaded', len(german_data['all_data']), 'German patents')
print('Loaded', len(cpc_definitions), 'CPC definitions')

# Get top CPC groups from German patents
top_groups = [group for group, count in german_data['top_groups']]
print('Top groups:', top_groups)

# Find exact level 4 matches in CPC definitions
level_4_info = {}
for def_item in cpc_definitions:
    symbol = def_item.get('symbol', '')
    level = str(def_item.get('level', ''))
    title = def_item.get('titleFull', '')
    
    # Check if level is 4 (handle both int and float)
    try:
        level_num = int(float(level))
        if level_num == 4 and symbol in top_groups:
            level_4_info[symbol] = title
    except:
        continue

print('Level 4 matches found:', len(level_4_info))
for symbol, title in level_4_info.items():
    print('  ', symbol, ':', title[:60])

# Get all CPC groups from German patents (not just top 10)
all_groups = {}
for patent in german_data['all_data']:
    group = patent['cpc_group_4']
    if group not in all_groups:
        all_groups[group] = 0
    all_groups[group] += 1

print('Total unique CPC groups:', len(all_groups))

# Find level 4 titles for all groups
all_level_4_info = {}
for def_item in cpc_definitions:
    symbol = def_item.get('symbol', '')
    level = str(def_item.get('level', ''))
    title = def_item.get('titleFull', '')
    
    try:
        level_num = int(float(level))
        if level_num == 4 and symbol in all_groups:
            all_level_4_info[symbol] = {
                'title': title,
                'count': all_groups[symbol]
            }
    except:
        continue

print('Level 4 info for all groups:', len(all_level_4_info))

# Calculate exponential moving average for each CPC group
# For this dataset (all in 2019), we'll create a simple monthly EMA
import math

# Group patents by CPC group and month
group_monthly = {}
for patent in german_data['all_data']:
    group = patent['cpc_group_4']
    month = patent['month']
    
    if group not in group_monthly:
        group_monthly[group] = {}
    
    if month not in group_monthly[group]:
        group_monthly[group][month] = 0
    
    group_monthly[group][month] += 1

# Calculate EMA for each group (smoothing factor alpha = 0.1)
alpha = 0.1
group_ema = {}

for group, monthly_counts in group_monthly.items():
    # Sort months 7-12 for 2019
    months = sorted(monthly_counts.keys())
    
    ema_values = []
    ema_prev = 0  # Start with 0
    
    for month in range(7, 13):  # July to December
        current_value = monthly_counts.get(month, 0)
        ema_current = alpha * current_value + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find best month (highest EMA)
    if ema_values:
        best_month_idx = ema_values.index(max(ema_values))
        best_month = 7 + best_month_idx
        best_ema = ema_values[best_month_idx]
        
        group_ema[group] = {
            'best_month': best_month,
            'best_ema': best_ema,
            'monthly_counts': monthly_counts,
            'ema_values': ema_values
        }

# Sort by best EMA and get top groups
sorted_groups = sorted(group_ema.items(), key=lambda x: x[1]['best_ema'], reverse=True)

# Combine with title information
result_data = []
for group, ema_data in sorted_groups[:10]:  # Top 10
    title = all_level_4_info.get(group, {}).get('title', 'Title not found')
    count = all_level_4_info.get(group, {}).get('count', 0)
    
    result_data.append({
        'cpc_group_code': group,
        'title_full': title,
        'total_patents': count,
        'best_month': ema_data['best_month'],
        'best_ema': round(ema_data['best_ema'], 2),
        'monthly_breakdown': ema_data['monthly_counts']
    })

print('Top groups by EMA:')
for item in result_data:
    print(f"  {item['cpc_group_code']}: {item['best_ema']} in month {item['best_month']}")

# Create final output
final_result = {
    'analysis_summary': {
        'total_german_patents_h2_2019': len(german_data['all_data']),
        'total_cpc_groups': len(all_groups),
        'analysis_period': 'July-December 2019',
        'smoothing_factor': alpha
    },
    'top_groups_by_ema': result_data
}

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'symbol': 'C04B20/0012', 'level': '9.0', 'titleFull': 'Irregular shaped fillers'}, {'symbol': 'C04B20/0044', 'level': '9.0', 'titleFull': 'Granular materials, e.g. microballoons obtained from irregularly shaped particles'}, {'symbol': 'C04B20/002', 'level': '9.0', 'titleFull': 'Hollow or porous granular materials'}, {'symbol': 'C04B20/0052', 'level': '9.0', 'titleFull': 'Mixtures of fibres of different physical characteristics, e.g. different lengths'}, {'symbol': 'C04B20/0072', 'level': '9.0', 'titleFull': 'Continuous fibres'}, {'symbol': 'C04B20/0056', 'level': '9.0', 'titleFull': 'Hollow or porous fibres'}, {'symbol': 'C04B20/006', 'level': '9.0', 'titleFull': 'Microfibres; Nanofibres'}, {'symbol': 'C04B20/0064', 'level': '9.0', 'titleFull': 'Ground fibres'}, {'symbol': 'C04B20/0068', 'level': '9.0', 'titleFull': 'Composite fibres, e.g. fibres with a core and sheath of different material'}, {'symbol': 'C04B20/0088', 'level': '9.0', 'titleFull': 'Fillers with mono- or narrow grain size distribution'}, {'symbol': 'C04B20/008', 'level': '9.0', 'titleFull': 'Micro- or nanosized fillers, e.g. micronised fillers with particle size smaller than that of the hydraulic binder'}, {'symbol': 'C04B20/0096', 'level': '9.0', 'titleFull': 'Fillers with bimodal grain size distribution'}, {'symbol': 'C04B2103/105', 'level': '9.0', 'titleFull': 'Accelerators; Activators for reactions involving organo-silicon compounds'}, {'symbol': 'C04B2103/14', 'level': '9.0', 'titleFull': 'Hardening accelerators'}, {'symbol': 'C04B2103/12', 'level': '9.0', 'titleFull': 'Set accelerators'}, {'symbol': 'C04B2103/22', 'level': '9.0', 'titleFull': 'Set retarders'}, {'symbol': 'C04B2103/24', 'level': '9.0', 'titleFull': 'Hardening retarders'}, {'symbol': 'C04B2103/302', 'level': '9.0', 'titleFull': 'Water reducers'}, {'symbol': 'C04B2103/34', 'level': '9.0', 'titleFull': 'Flow improvers'}, {'symbol': 'C04B2103/306', 'level': '9.0', 'titleFull': 'Fluidisers with reduced air-entraning effect'}], 'var_functions.query_db:24': [{'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'E02F', 'titleFull': 'DREDGING; SOIL-SHIFTING'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'F02N', 'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01J', 'titleFull': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}]}

exec(code, env_args)
