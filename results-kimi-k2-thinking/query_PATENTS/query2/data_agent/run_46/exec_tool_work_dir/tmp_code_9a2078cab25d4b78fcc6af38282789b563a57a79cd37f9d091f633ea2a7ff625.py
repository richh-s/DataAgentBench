code = """import json

# Load German patents data
german_file = var_functions.execute_python:10
with open(german_file, 'r') as f:
    german_data = json.load(f)

# Get top CPC groups
top_groups = [group for group, count in german_data['top_groups']]
print("Top CPC groups:", top_groups)

# Load CPC definitions
cpc_file = var_functions.query_db:18
with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

print(f"Total CPC definitions loaded: {len(cpc_definitions)}")

# Find level information and symbols
level_stats = {}
symbol_patterns = {}

for def_item in cpc_definitions:
    symbol = def_item.get('symbol', '')
    level = def_item.get('level', '')
    title = def_item.get('titleFull', '')
    
    # Track level statistics
    try:
        level_num = int(float(level))
        level_stats[level_num] = level_stats.get(level_num, 0) + 1
    except:
        pass
    
    # Check if symbol starts with any of our top groups
    for group in top_groups:
        if symbol.startswith(group):
            if group not in symbol_patterns:
                symbol_patterns[group] = []
            symbol_patterns[group].append({
                'symbol': symbol,
                'level': level,
                'title': title
            })

print("Level statistics:", level_stats)
print("\nSymbol patterns for top groups:")
for group, symbols in symbol_patterns.items():
    print(f"\n{group}: {len(symbols)} symbols")
    for sym in symbols[:3]:
        print(f"  Level {sym['level']}: {sym['symbol']} - {sym['title'][:80]}...")

# Find exact level 4 matches for top groups
level_4_matches = []
for def_item in cpc_definitions:
    symbol = def_item.get('symbol', '')
    level = def_item.get('level', '')
    title = def_item.get('titleFull', '')
    
    try:
        level_num = int(float(level))
        if level_num == 4 and symbol in top_groups:
            level_4_matches.append({
                'symbol': symbol,
                'titleFull': title
            })
    except:
        continue

print(f"\nFound {len(level_4_matches)} exact level 4 matches:")
for match in level_4_matches:
    print(f"  {match['symbol']}: {match['titleFull'][:80]}...")

result = {
    'top_groups': top_groups,
    'level_stats': level_stats,
    'level_4_matches': level_4_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'symbol': 'C04B20/0012', 'level': '9.0', 'titleFull': 'Irregular shaped fillers'}, {'symbol': 'C04B20/0044', 'level': '9.0', 'titleFull': 'Granular materials, e.g. microballoons obtained from irregularly shaped particles'}, {'symbol': 'C04B20/002', 'level': '9.0', 'titleFull': 'Hollow or porous granular materials'}, {'symbol': 'C04B20/0052', 'level': '9.0', 'titleFull': 'Mixtures of fibres of different physical characteristics, e.g. different lengths'}, {'symbol': 'C04B20/0072', 'level': '9.0', 'titleFull': 'Continuous fibres'}, {'symbol': 'C04B20/0056', 'level': '9.0', 'titleFull': 'Hollow or porous fibres'}, {'symbol': 'C04B20/006', 'level': '9.0', 'titleFull': 'Microfibres; Nanofibres'}, {'symbol': 'C04B20/0064', 'level': '9.0', 'titleFull': 'Ground fibres'}, {'symbol': 'C04B20/0068', 'level': '9.0', 'titleFull': 'Composite fibres, e.g. fibres with a core and sheath of different material'}, {'symbol': 'C04B20/0088', 'level': '9.0', 'titleFull': 'Fillers with mono- or narrow grain size distribution'}, {'symbol': 'C04B20/008', 'level': '9.0', 'titleFull': 'Micro- or nanosized fillers, e.g. micronised fillers with particle size smaller than that of the hydraulic binder'}, {'symbol': 'C04B20/0096', 'level': '9.0', 'titleFull': 'Fillers with bimodal grain size distribution'}, {'symbol': 'C04B2103/105', 'level': '9.0', 'titleFull': 'Accelerators; Activators for reactions involving organo-silicon compounds'}, {'symbol': 'C04B2103/14', 'level': '9.0', 'titleFull': 'Hardening accelerators'}, {'symbol': 'C04B2103/12', 'level': '9.0', 'titleFull': 'Set accelerators'}, {'symbol': 'C04B2103/22', 'level': '9.0', 'titleFull': 'Set retarders'}, {'symbol': 'C04B2103/24', 'level': '9.0', 'titleFull': 'Hardening retarders'}, {'symbol': 'C04B2103/302', 'level': '9.0', 'titleFull': 'Water reducers'}, {'symbol': 'C04B2103/34', 'level': '9.0', 'titleFull': 'Flow improvers'}, {'symbol': 'C04B2103/306', 'level': '9.0', 'titleFull': 'Fluidisers with reduced air-entraning effect'}], 'var_functions.query_db:24': [{'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'E02F', 'titleFull': 'DREDGING; SOIL-SHIFTING'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'F02N', 'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01J', 'titleFull': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}]}

exec(code, env_args)
