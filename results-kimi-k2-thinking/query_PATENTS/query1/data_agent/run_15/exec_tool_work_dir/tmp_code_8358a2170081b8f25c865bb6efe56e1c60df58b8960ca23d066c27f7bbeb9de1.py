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

print('Processing ' + str(len(publications)) + ' publications...')

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

# Convert to DataFrame
df = pd.DataFrame(cpc_year_data)

# Extract group codes (before the slash)
df['group_code'] = df['full_code'].apply(lambda x: x.split('/')[0] if '/' in x else x)

# Load CPC level 5 symbols
result_key = 'var_functions.query_db:32'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        cpc_level5_data = json.load(f)
else:
    cpc_level5_data = result_file

cpc_level5_symbols = sorted([item['symbol'] for item in cpc_level5_data])
print('Loaded ' + str(len(cpc_level5_symbols)) + ' level 5 symbols')

# For group codes in patent data, extract the first 4 characters to match level 5
# e.g., "C01B33" -> "C01B", "H01M10" -> "H01M"
df['level5_match'] = df['group_code'].apply(lambda x: x[:4] if len(x) >= 4 else x)

# Filter to only include level 5 CPC groups
df_level5 = df[df['level5_match'].isin(cpc_level5_symbols)].copy()

print('Level 5 patent entries: ' + str(len(df_level5)))
print('Unique level 5 groups in patents: ' + str(len(df_level5['level5_match'].unique())))

# Count filings per level 5 group per year
yearly_counts = df_level5.groupby(['level5_match', 'year']).size().reset_index(name='count')

# Get all years and level5 groups
all_years = sorted(yearly_counts['year'].unique())
all_groups = sorted(yearly_counts['level5_match'].unique())

print('Year range: ' + str(all_years[0]) + ' to ' + str(all_years[-1]))
print('Total years: ' + str(len(all_years)))
print('Total level 5 groups: ' + str(len(all_groups)))

# Create complete matrix with all combinations
complete_matrix = []
for group in all_groups:
    for year in all_years:
        complete_matrix.append({'level5_match': group, 'year': year, 'count': 0})

complete_df = pd.DataFrame(complete_matrix)

# Merge with actual counts
merged_counts = pd.merge(complete_df, yearly_counts, on=['level5_match', 'year'], how='left', suffixes=('_default', '_actual'))
merged_counts['final_count'] = merged_counts['count_actual'].fillna(0)

# Calculate exponential moving average for each group
smoothing_factor = 0.2

def calculate_ema(group_data):
    group_data = group_data.sort_values('year')
    ema_values = []
    ema_prev = None
    
    for _, row in group_data.iterrows():
        count = row['final_count']
        if ema_prev is None:
            ema = count
        else:
            ema = smoothing_factor * count + (1 - smoothing_factor) * ema_prev
        
        ema_values.append(ema)
        ema_prev = ema
    
    group_data = group_data.copy()
    group_data['ema'] = ema_values
    return group_data

# Apply EMA calculation to each group
ema_results = []
for group in all_groups:
    group_data = merged_counts[merged_counts['level5_match'] == group]
    group_ema = calculate_ema(group_data)
    ema_results.append(group_ema)

ema_df = pd.concat(ema_results, ignore_index=True)

# Find best year for each group (year with highest EMA)
best_years = ema_df.loc[ema_df.groupby('level5_match')['ema'].idxmax()][['level5_match', 'year', 'ema']]

# Filter groups whose best year is 2022
groups_best_2022 = best_years[best_years['year'] == 2022]['level5_match'].tolist()

print('Groups with best year 2022: ' + str(len(groups_best_2022)))

# Format final result
final_result = {
    'level5_groups_best_2022': groups_best_2022,
    'count': len(groups_best_2022)
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'cpc_entries': 1333969, 'dataframe_shape': [1333969, 5], 'columns': ['full_code', 'group_code', 'year', 'inventive', 'first']}, 'var_functions.execute_python:20': {'total_level5_entries': 0, 'unique_level5_groups': 0, 'year_range': 'No data', 'years_available': []}, 'var_functions.query_db:24': [{'symbol': 'A62B', 'level': '5.0', 'titleFull': 'DEVICES, APPARATUS OR METHODS FOR LIFE-SAVING'}, {'symbol': 'A63G', 'level': '5.0', 'titleFull': 'MERRY-GO-ROUNDS; SWINGS; ROCKING-HORSES; CHUTES; SWITCHBACKS; SIMILAR DEVICES FOR PUBLIC AMUSEMENT'}, {'symbol': 'A63K', 'level': '5.0', 'titleFull': 'RACING; RIDING SPORTS; EQUIPMENT OR ACCESSORIES THEREFOR'}, {'symbol': 'A63B', 'level': '5.0', 'titleFull': 'APPARATUS FOR PHYSICAL TRAINING, GYMNASTICS, SWIMMING, CLIMBING, OR FENCING; BALL GAMES; TRAINING EQUIPMENT'}, {'symbol': 'A63J', 'level': '5.0', 'titleFull': 'DEVICES FOR THEATRES, CIRCUSES, OR THE LIKE; CONJURING APPLIANCES OR THE LIKE'}, {'symbol': 'A63C', 'level': '5.0', 'titleFull': 'SKATES; SKIS; ROLLER SKATES; DESIGN OR LAYOUT OF COURTS, RINKS OR THE LIKE'}, {'symbol': 'A63D', 'level': '5.0', 'titleFull': 'BOWLING GAMES, e.g. SKITTLES, BOCCE OR BOWLS; INSTALLATIONS THEREFOR; BAGATELLE OR SIMILAR GAMES; BILLIARDS'}, {'symbol': 'A63F', 'level': '5.0', 'titleFull': 'CARD, BOARD, OR ROULETTE GAMES; INDOOR GAMES USING SMALL MOVING PLAYING BODIES; VIDEO GAMES; GAMES NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'C25D', 'level': '5.0', 'titleFull': 'PROCESSES FOR THE ELECTROLYTIC OR ELECTROPHORETIC PRODUCTION OF COATINGS; ELECTROFORMING; APPARATUS THEREFOR'}, {'symbol': 'A63H', 'level': '5.0', 'titleFull': 'TOYS, e.g. TOPS, DOLLS, HOOPS OR BUILDING BLOCKS'}, {'symbol': 'A99Z', 'level': '5.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B01J', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS'}, {'symbol': 'B01B', 'level': '5.0', 'titleFull': 'BOILING; BOILING APPARATUS ; EVAPORATION; EVAPORATION APPARATUS'}, {'symbol': 'B01D', 'level': '5.0', 'titleFull': 'SEPARATION'}, {'symbol': 'B01L', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE'}, {'symbol': 'B01F', 'level': '5.0', 'titleFull': 'MIXING, e.g. DISSOLVING, EMULSIFYING OR DISPERSING'}, {'symbol': 'B02C', 'level': '5.0', 'titleFull': 'CRUSHING, PULVERISING, OR DISINTEGRATING IN GENERAL; MILLING GRAIN'}, {'symbol': 'B02B', 'level': '5.0', 'titleFull': 'PREPARING GRAIN FOR MILLING; REFINING GRANULAR FRUIT TO COMMERCIAL PRODUCTS BY WORKING THE SURFACE'}, {'symbol': 'B03B', 'level': '5.0', 'titleFull': 'SEPARATING SOLID MATERIALS USING LIQUIDS OR USING PNEUMATIC TABLES OR JIGS'}, {'symbol': 'B03D', 'level': '5.0', 'titleFull': 'FLOTATION; DIFFERENTIAL SEDIMENTATION'}], 'var_functions.execute_python:28': {'total_entries': 1333969, 'unique_groups': 9368, 'level5_symbols': 20, 'exact_matches': 0, 'partial_matches': 19, 'reverse_matches': 0, 'char4_matches': 19, 'year_range': '1837 to 2024', 'years_available': [1837, 1839, 1841, 1842, 1844, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
