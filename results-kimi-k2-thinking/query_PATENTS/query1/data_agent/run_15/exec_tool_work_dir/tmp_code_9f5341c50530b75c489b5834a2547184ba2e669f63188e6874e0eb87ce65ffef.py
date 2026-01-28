code = """import json
import pandas as pd
import re

# Load the publication data
result_key = 'var_functions.query_db:6'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        publications = json.load(f)
else:
    publications = result_file

print('Loading ' + str(len(publications)) + ' publications...')

# Parse CPC codes and extract years
cpc_year_data = []
for pub in publications:
    cpc_str = pub.get('cpc', '').strip()
    pub_date_str = pub.get('publication_date', '').strip()
    
    if not cpc_str or not pub_date_str:
        continue
    
    # Extract year from publication date
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Parse CPC JSON string
    try:
        if cpc_str.startswith('['):
            cpc_list = json.loads(cpc_str)
        else:
            continue
    except:
        continue
    
    if not isinstance(cpc_list, list):
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            code = cpc_item['code']
            cpc_year_data.append({
                'full_code': code,
                'year': year
            })

print('Extracted ' + str(len(cpc_year_data)) + ' CPC entries')

# Convert to DataFrame
df = pd.DataFrame(cpc_year_data)

# Extract group codes (before the slash)
df['group_code'] = df['full_code'].apply(lambda x: x.split('/')[0] if '/' in x else x)

# Get unique group codes
unique_groups = sorted(df['group_code'].unique())
print('Total unique group codes: ' + str(len(unique_groups)))

# Load CPC level 5 definitions
cpc_level5_key = 'var_functions.query_db:24'
cpc_level5_data = locals()[cpc_level5_key]
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

print('Level 5 symbols loaded: ' + str(len(cpc_level5_symbols)))

# Find exact matches between our data and level 5 symbols
matching_groups = set(unique_groups) & set(cpc_level5_symbols)
print('Exact matches found: ' + str(len(matching_groups)))

# Check for partial matches (data groups that start with level 5 symbols)
partial_matches = []
for level5_symbol in cpc_level5_symbols:
    for data_group in unique_groups:
        if data_group.startswith(level5_symbol):
            partial_matches.append(level5_symbol)
            break

print('Partial matches (data starts with level5): ' + str(len(partial_matches)))

# Also check for reverse (level5 starts with data group)
reverse_matches = []
for data_group in unique_groups:
    for level5_symbol in cpc_level5_symbols:
        if level5_symbol.startswith(data_group):
            reverse_matches.append(data_group)
            break

print('Reverse matches (level5 starts with data): ' + str(len(reverse_matches)))

# Let's sample the data to understand patterns
sample_groups = unique_groups[:50]
sample_level5 = cpc_level5_symbols[:50]

# Let's also check if we can match by taking first 4 characters
data_4char = set([g[:4] if len(g) >= 4 else g for g in unique_groups])
level5_4char = set([g[:4] if len(g) >= 4 else g for g in cpc_level5_symbols])
char4_matches = data_4char & level5_4char

print('4-character prefix matches: ' + str(len(char4_matches)))

# Store the results for next steps - convert numpy types to Python types
years_available = sorted(df['year'].unique()) if len(df) > 0 else []
years_range = str(int(df['year'].min())) + ' to ' + str(int(df['year'].max())) if len(df) > 0 else 'No data'

result = {
    'total_entries': int(len(df)),
    'unique_groups': int(len(unique_groups)),
    'level5_symbols': int(len(cpc_level5_symbols)),
    'exact_matches': int(len(matching_groups)),
    'partial_matches': int(len(partial_matches)),
    'reverse_matches': int(len(reverse_matches)),
    'char4_matches': int(len(char4_matches)),
    'year_range': years_range,
    'years_available': [int(y) for y in years_available]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'cpc_entries': 1333969, 'dataframe_shape': [1333969, 5], 'columns': ['full_code', 'group_code', 'year', 'inventive', 'first']}, 'var_functions.execute_python:20': {'total_level5_entries': 0, 'unique_level5_groups': 0, 'year_range': 'No data', 'years_available': []}, 'var_functions.query_db:24': [{'symbol': 'A62B', 'level': '5.0', 'titleFull': 'DEVICES, APPARATUS OR METHODS FOR LIFE-SAVING'}, {'symbol': 'A63G', 'level': '5.0', 'titleFull': 'MERRY-GO-ROUNDS; SWINGS; ROCKING-HORSES; CHUTES; SWITCHBACKS; SIMILAR DEVICES FOR PUBLIC AMUSEMENT'}, {'symbol': 'A63K', 'level': '5.0', 'titleFull': 'RACING; RIDING SPORTS; EQUIPMENT OR ACCESSORIES THEREFOR'}, {'symbol': 'A63B', 'level': '5.0', 'titleFull': 'APPARATUS FOR PHYSICAL TRAINING, GYMNASTICS, SWIMMING, CLIMBING, OR FENCING; BALL GAMES; TRAINING EQUIPMENT'}, {'symbol': 'A63J', 'level': '5.0', 'titleFull': 'DEVICES FOR THEATRES, CIRCUSES, OR THE LIKE; CONJURING APPLIANCES OR THE LIKE'}, {'symbol': 'A63C', 'level': '5.0', 'titleFull': 'SKATES; SKIS; ROLLER SKATES; DESIGN OR LAYOUT OF COURTS, RINKS OR THE LIKE'}, {'symbol': 'A63D', 'level': '5.0', 'titleFull': 'BOWLING GAMES, e.g. SKITTLES, BOCCE OR BOWLS; INSTALLATIONS THEREFOR; BAGATELLE OR SIMILAR GAMES; BILLIARDS'}, {'symbol': 'A63F', 'level': '5.0', 'titleFull': 'CARD, BOARD, OR ROULETTE GAMES; INDOOR GAMES USING SMALL MOVING PLAYING BODIES; VIDEO GAMES; GAMES NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'C25D', 'level': '5.0', 'titleFull': 'PROCESSES FOR THE ELECTROLYTIC OR ELECTROPHORETIC PRODUCTION OF COATINGS; ELECTROFORMING; APPARATUS THEREFOR'}, {'symbol': 'A63H', 'level': '5.0', 'titleFull': 'TOYS, e.g. TOPS, DOLLS, HOOPS OR BUILDING BLOCKS'}, {'symbol': 'A99Z', 'level': '5.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B01J', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS'}, {'symbol': 'B01B', 'level': '5.0', 'titleFull': 'BOILING; BOILING APPARATUS ; EVAPORATION; EVAPORATION APPARATUS'}, {'symbol': 'B01D', 'level': '5.0', 'titleFull': 'SEPARATION'}, {'symbol': 'B01L', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE'}, {'symbol': 'B01F', 'level': '5.0', 'titleFull': 'MIXING, e.g. DISSOLVING, EMULSIFYING OR DISPERSING'}, {'symbol': 'B02C', 'level': '5.0', 'titleFull': 'CRUSHING, PULVERISING, OR DISINTEGRATING IN GENERAL; MILLING GRAIN'}, {'symbol': 'B02B', 'level': '5.0', 'titleFull': 'PREPARING GRAIN FOR MILLING; REFINING GRANULAR FRUIT TO COMMERCIAL PRODUCTS BY WORKING THE SURFACE'}, {'symbol': 'B03B', 'level': '5.0', 'titleFull': 'SEPARATING SOLID MATERIALS USING LIQUIDS OR USING PNEUMATIC TABLES OR JIGS'}, {'symbol': 'B03D', 'level': '5.0', 'titleFull': 'FLOTATION; DIFFERENTIAL SEDIMENTATION'}]}

exec(code, env_args)
