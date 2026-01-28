code = """import json, re, os

# Load data from file
file_path = '/tmp/tmp6y9g1h9v.json'
print('Loading data from', file_path)

with open(file_path, 'r') as f:
    publications = json.load(f)

print('Loaded', len(publications), 'publications')

# Count patents by CPC group and year
patent_counts = {}
years = set()

for pub in publications:
    date_str = pub.get('publication_date', '')
    if date_str:
        year_match = re.search(r'\d{4}', date_str)
        if year_match:
            year = int(year_match.group())
            years.add(year)
            cpc_str = pub.get('cpc', '')
            if cpc_str:
                try:
                    cpc_list = json.loads(cpc_str)
                    for item in cpc_list:
                        code = item.get('code', '')
                        if code:
                            group = code.split('/')[0].split()[0]
                            if group not in patent_counts:
                                patent_counts[group] = {}
                            patent_counts[group][year] = patent_counts[group].get(year, 0) + 1
                except:
                    pass

print('Found', len(patent_counts), 'CPC groups')
print('Year range:', sorted(years))

# Calculate EMA for each CPC group
alpha = 0.2
cpc_ema_data = {}

for cpc, yearly_counts in patent_counts.items():
    sorted_years = sorted(yearly_counts.keys())
    if len(sorted_years) < 2:
        continue
    
    ema_values = {}
    # First EMA is just the first year's count
    ema_values[sorted_years[0]] = yearly_counts[sorted_years[0]]
    
    # Calculate EMA for subsequent years
    for year in sorted_years[1:]:
        ema_values[year] = alpha * yearly_counts[year] + (1 - alpha) * ema_values[sorted_years[sorted_years.index(year)-1]]
    
    cpc_ema_data[cpc] = ema_values

print('Calculated EMA for', len(cpc_ema_data), 'CPC groups')

# Find CPC groups with best year = 2022
cpc_best_2022 = []
years_test = sorted(years)

if 2022 in years_test:
    for cpc, ema_values in cpc_ema_data.items():
        if 2022 in ema_values:
            # Find year with max EMA
            max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
            if max_year == 2022:
                cpc_best_2022.append(cpc)

print('CPC groups with best year 2022:', len(cpc_best_2022))
print('Sample:', cpc_best_2022[:10])

# Get level 5 CPC codes from CPC definition database
result = {
    'total_cpc_groups': len(cpc_best_2022),
    'cpc_codes': cpc_best_2022,
    'status': 'success'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
