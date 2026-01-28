code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the publication data
pub_file = locals()['var_functions.query_db:0']
if isinstance(pub_file, str) and pub_file.endswith('.json'):
    with open(pub_file, 'r') as f:
        publications = json.load(f)
else:
    publications = pub_file

print(f"Total publications: {len(publications)}")
print(f"Sample publication: {publications[0] if publications else 'None'}")

# Load the level 5 CPC symbols
cpc_file = locals()['var_functions.query_db:2']
if isinstance(cpc_file, str) and cpc_file.endswith('.json'):
    with open(cpc_file, 'r') as f:
        level5_symbols = json.load(f)
else:
    level5_symbols = cpc_file

print(f"Total level 5 symbols: {len(level5_symbols)}")
print(f"Sample symbol: {level5_symbols[0] if level5_symbols else 'None'}")

# Create a set of level 5 symbols for quick lookup
level5_set = set()
for item in level5_symbols:
    symbol = item.get('symbol', '')
    level = item.get('level', '')
    # Convert level to int/float and compare
    try:
        level_num = float(level) if level else 0
        if level_num == 5:
            level5_set.add(symbol)
    except:
        continue

print(f"Level 5 symbols count: {len(level5_set)}")
print(f"Sample level 5 symbols: {list(level5_set)[:10]}")

# Process publications to extract year and CPC codes
processed_data = []
for pub in publications:
    if pub.get('cpc') is None or pub.get('publication_date') is None:
        continue
    
    # Parse publication date
    date_str = pub['publication_date']
    # Extract year using regex
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC field
    cpc_str = pub['cpc']
    try:
        if isinstance(cpc_str, str):
            cpc_list = json.loads(cpc_str)
        else:
            cpc_list = cpc_str
        
        # Extract CPC codes and match to level 5
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                if not code:
                    continue
                
                # Try to find the matching level 5 symbol
                # Start with the full code and progressively shorten
                test_symbol = code
                found = False
                
                while len(test_symbol) >= 1 and not found:
                    if test_symbol in level5_set:
                        processed_data.append({
                            'year': year,
                            'cpc_symbol': test_symbol,
                            'full_code': code
                        })
                        found = True
                    else:
                        # Remove last character and try again
                        test_symbol = test_symbol[:-1]
    except:
        continue

print(f"Processed {len(processed_data)} CPC entries")

# Create DataFrame if we have data
if len(processed_data) > 0:
    df = pd.DataFrame(processed_data)
    
    # Count filings per CPC symbol per year
    counts = df.groupby(['cpc_symbol', 'year']).size().reset_index(name='count')
    
    # Get all years and symbols
    years = sorted(counts['year'].unique())
    symbols = sorted(counts['cpc_symbol'].unique())
    
    print(f"Years: {min(years)} to {max(years)}")
    print(f"Number of level 5 CPC symbols with data: {len(symbols)}")
    
    # Create a pivot table
    pivot = counts.pivot(index='year', columns='cpc_symbol', values='count').fillna(0)
    
    # Calculate EMA for each symbol (smoothing factor 0.2 means alpha=0.2)
    alpha = 0.2
    
    ema_results = {}
    best_years = {}
    
    for symbol in symbols:
        if symbol not in pivot.columns:
            continue
        
        values = pivot[symbol].values
        ema_values = []
        
        # Calculate EMA
        ema = None
        for i, value in enumerate(values):
            if ema is None:
                ema = value
            else:
                ema = alpha * value + (1 - alpha) * ema
            ema_values.append(ema)
        
        ema_results[symbol] = dict(zip(years, ema_values))
        
        # Find year with max EMA
        if ema_values:
            max_year = max(zip(years, ema_values), key=lambda x: x[1])[0]
            best_years[symbol] = max_year
    
    # Filter symbols where best year is 2022
    symbols_2022 = [symbol for symbol, year in best_years.items() if year == 2022]
    
    print(f"Number of CPC symbols with best year 2022: {len(symbols_2022)}")
    
    if symbols_2022:
        result = sorted(symbols_2022)
    else:
        result = []
else:
    print("No processed data found")
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
