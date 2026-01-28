code = """import json
import pandas as pd
from datetime import datetime
import re

# Access the query results
print("=== Accessing storage keys ===")
all_keys = [k for k in locals().keys() if k.startswith('var_')]
print("All storage keys:", all_keys)

# Let's load the actual JSON file for the CPC data
if isinstance(var_functions.query_db_2, str) and '.json' in var_functions.query_db_2:
    print("Loading CPC data from file:", var_functions.query_db_2)
    with open(var_functions.query_db_2, 'r') as f:
        cpc_data = json.load(f)
else:
    cpc_data = var_functions.query_db_2

# Level 5 codes
level_5_codes = var_functions.query_db_5
print("Level 5 codes (first 5):", level_5_codes[:5] if level_5_codes else "Empty")
print("Total level 5 codes:", len(level_5_codes))

# Debug first few CPC records
if cpc_data:
    print("\nFirst CPC record sample:")
    print(json.dumps(cpc_data[0], indent=2))
else:
    print("No CPC data found")

# Create DataFrame from CPC data
cpc_records = []
for row in cpc_data:
    cpc_codes_str = row.get('cpc', '')
    pub_date_str = row.get('publication_date', '')
    
    # Parse date from formats like "Aug 3rd, 2021" or "Oct 6th, 2020"
    try:
        # Remove ordinal suffixes (st, nd, rd, th)
        clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date_str)
        date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
        year = date_obj.year
    except:
        year = None
    
    # Parse CPC codes JSON
    if cpc_codes_str and cpc_codes_str != '[]':
        try:
            codes_list = json.loads(cpc_codes_str)
            for code_item in codes_list:
                code = code_item.get('code', '')
                if code:
                    cpc_records.append({
                        'code': code,
                        'year': year,
                        'pub_date': pub_date_str
                    })
        except:
            # Manual parsing as fallback
            code_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_codes_str)
            for code in code_matches:
                cpc_records.append({
                    'code': code,
                    'year': year,
                    'pub_date': pub_date_str
                })

print(f"\nParsed {len(cpc_records)} CPC code-year records")

# Create DataFrame
df = pd.DataFrame(cpc_records)
print("DataFrame shape:", df.shape)
print("Year range:", df['year'].min(), "to", df['year'].max())
print("Sample data:")
print(df.head(10))

# Extract level 5 codes from the complete symbols
level_5_symbols = [item['symbol'] for item in level_5_codes]
print(f"\nLevel 5 symbols loaded: {len(level_5_symbols)} codes")
print("Sample level 5 symbols:", level_5_symbols[:10])

# Group by year and code, count filings
code_year_counts = df.groupby(['year', 'code']).size().reset_index(name='count')
print(f"\nTotal year-code combinations: {len(code_year_counts)}")

# Show sample of counts
print("Sample year-code counts:")
print(code_year_counts.head(10))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}]}

exec(code, env_args)
