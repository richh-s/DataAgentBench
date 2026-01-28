code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the publication data
pub_file = var_functions.query_db:0
if isinstance(pub_file, str) and pub_file.endswith('.json'):
    with open(pub_file, 'r') as f:
        publications = json.load(f)
else:
    publications = var_functions.query_db:0

# Load the level 5 CPC symbols
cpc_file = var_functions.query_db:2
if isinstance(cpc_file, str) and cpc_file.endswith('.json'):
    with open(cpc_file, 'r') as f:
        level5_symbols = json.load(f)
else:
    level5_symbols = var_functions.query_db:2

# Create a set of level 5 symbols for quick lookup
level5_set = set([item['symbol'] for item in level5_symbols])

# Process publications to extract year and CPC codes
processed_data = []
for pub in publications:
    if pub['cpc'] is None or pub['publication_date'] is None:
        continue
    
    # Parse publication date
    date_str = pub['publication_date']
    # Extract year using regex
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC field (it's a string that looks like JSON)
    cpc_str = pub['cpc']
    try:
        # Sometimes it's a string representation of a list, sometimes it might already be parsed
        if isinstance(cpc_str, str):
            cpc_list = json.loads(cpc_str)
        else:
            cpc_list = cpc_str
        
        # Extract CPC codes
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                # Extract base symbol (e.g., "C01B33/00" -> "C01B")
                if code:
                    # Split by various delimiters to get the main group
                    # CPC codes can be like "C01B33/00" or "C01B" or "C01B33"
                    base_symbol = code.split('/')[0]
                    # Remove numeric parts to get the level 5 symbol
                    # e.g., "C01B33" -> "C01B" (but "C01B" stays "C01B")
                    # We want to match against our level5_set
                    
                    # Try to find the matching level 5 symbol
                    # Start with the full code and progressively shorten
                    test_symbol = base_symbol
                    while len(test_symbol) > 2:
                        if test_symbol in level5_set:
                            processed_data.append({
                                'year': year,
                                'cpc_symbol': test_symbol,
                                'full_code': code
                            })
                            break
                        # Remove last character and try again
                        test_symbol = test_symbol[:-1]
    except:
        # Skip malformed entries
        continue

print(f"Processed {len(processed_data)} CPC entries")

# Create DataFrame
df = pd.DataFrame(processed_data)

# Count filings per CPC symbol per year
counts = df.groupby(['cpc_symbol', 'year']).size().reset_index(name='count')

# Get all years and symbols
years = sorted(counts['year'].unique())
symbols = sorted(counts['cpc_symbol'].unique())

print(f"Years: {min(years)} to {max(years)}")
print(f"Number of level 5 CPC symbols with data: {len(symbols)}")

# Create a pivot table for easier EMA calculation
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
    max_year = max(zip(years, ema_values), key=lambda x: x[1])[0]
    best_years[symbol] = max_year

# Filter symbols where best year is 2022
symbols_2022 = [symbol for symbol, year in best_years.items() if year == 2022]

print(f"\nNumber of CPC symbols with best year 2022: {len(symbols_2022)}")

if symbols_2022:
    # Print details
    print("\nCPC symbols with best year 2022:")
    for symbol in sorted(symbols_2022):
        print(f"  {symbol}")
    
    # Prepare final result
    result = sorted(symbols_2022)
else:
    result = []

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
