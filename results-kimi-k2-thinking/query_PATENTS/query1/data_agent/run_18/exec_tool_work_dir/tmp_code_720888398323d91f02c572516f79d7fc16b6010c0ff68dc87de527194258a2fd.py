code = """import json
import pandas as pd
import re

# Load CPC level 5 symbols
cpc_file = locals()['var_functions.query_db:36']
cpc_symbols = json.load(open(cpc_file))
level5_symbols = set(item['symbol'] for item in cpc_symbols)

# Load publication data
pub_file = locals()['var_functions.query_db:10']
publications = json.load(open(pub_file))

print(f'CPC Level 5 symbols loaded: {len(level5_symbols)}')
print(f'Publications loaded: {len(publications)}')
print(f'Sample CPC symbols: {list(level5_symbols)[:10]}')

# Process publication data: extract CPC codes and years
patent_counts = {}
valid_years = set()

for i, record in enumerate(publications):
    if i % 50000 == 0:
        print(f'Processing record {i}...')
    
    # Extract year from publication_date
    pub_date = record.get('publication_date', '')
    year_match = re.search(r'(\d{4})', str(pub_date))
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Skip years outside reasonable range
    if year < 2010 or year > 2023:
        continue
        
    valid_years.add(year)
    
    # Parse CPC codes
    cpc_str = record.get('cpc', '[]')
    try:
        if isinstance(cpc_str, str):
            cpc_list = json.loads(cpc_str)
        else:
            cpc_list = cpc_str
    except:
        continue
    
    if not isinstance(cpc_list, list):
        continue
    
    for cpc_item in cpc_list:
        if not isinstance(cpc_item, dict):
            continue
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        # Extract group code (first 4 characters before any slash)
        group_code = code.split('/')[0][:4]
        
        # Check if this is a level 5 group
        if group_code in level5_symbols:
            key = (group_code, year)
            patent_counts[key] = patent_counts.get(key, 0) + 1

print(f'Processed {len(patent_counts)} CPC group-year combinations')
print(f'Valid years range: {min(valid_years) if valid_years else "None"} to {max(valid_years) if valid_years else "None"}')

# Convert to DataFrame
if patent_counts:
    df = pd.DataFrame(
        [(group, year, count) for (group, year), count in patent_counts.items()],
        columns=['cpc_group', 'year', 'count']
    )
    
    # Create pivot table: CPC groups as rows, years as columns
    pivot = df.pivot(index='cpc_group', columns='year', values='count').fillna(0)
    
    # Calculate EMA for each group
    alpha = 0.2
    results = []
    
    years_sorted = sorted(pivot.columns)
    print(f'Years in data: {years_sorted}')
    
    for cpc_group in pivot.index:
        values = [pivot.loc[cpc_group, year] for year in years_sorted]
        
        # Calculate EMA
        ema_values = []
        ema_prev = values[0]
        
        for i, val in enumerate(values):
            if i == 0:
                ema = val
            else:
                ema = alpha * val + (1 - alpha) * ema_prev
            ema_values.append(ema)
            ema_prev = ema
        
        # Find year with max EMA
        max_ema = max(ema_values)
        best_year = years_sorted[ema_values.index(max_ema)]
        
        results.append({
            'cpc_group': cpc_group,
            'best_year': int(best_year),
            'max_ema': max_ema
        })
    
    df_results = pd.DataFrame(results)
    
    # Filter for best year = 2022
    groups_2022 = df_results[df_results['best_year'] == 2022]['cpc_group'].tolist()
    
    # Get top 10 for verification
    top_10 = df_results.sort_values('max_ema', ascending=False).head(10)
    
    output = {
        'total_level5_groups': len(level5_symbols),
        'groups_with_patents': len(pivot),
        'groups_best_year_2022': groups_2022,
        'count_best_year_2022': len(groups_2022),
        'top_groups': top_10.to_dict('records')
    }
else:
    output = {
        'total_level5_groups': len(level5_symbols),
        'groups_with_patents': 0,
        'groups_best_year_2022': [],
        'count_best_year_2022': 0,
        'top_groups': []
    }

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:32': [{'symbol': 'A01H', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES', 'level': '5.0'}, {'symbol': 'A01F', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE', 'level': '5.0'}, {'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING', 'level': '5.0'}, {'symbol': 'A01G', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING', 'level': '5.0'}, {'symbol': 'A23J', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS', 'level': '5.0'}, {'symbol': 'A01N', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS', 'level': '5.0'}, {'symbol': 'A01P', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS', 'level': '5.0'}, {'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING', 'level': '5.0'}, {'symbol': 'A01L', 'titleFull': 'SHOEING OF ANIMALS', 'level': '5.0'}, {'symbol': 'A01K', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS', 'level': '5.0'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
