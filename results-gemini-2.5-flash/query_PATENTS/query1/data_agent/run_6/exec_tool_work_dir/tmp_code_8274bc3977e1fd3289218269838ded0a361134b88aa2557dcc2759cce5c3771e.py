code = """import pandas as pd
import json
import re

# Load the full result from the JSON file for patent publications
with open(locals()['var_function-call-14622800233827138684'], 'r') as f:
    publication_data = json.load(f)

# Load the full result from the JSON file for CPC definitions (level 5)
with open(locals()['var_function-call-3356983374149566720'], 'r') as f:
    cpc_definition_data = json.load(f)

# Extract level 5 CPC symbols
level_5_cpc_symbols = set([entry['symbol'] for entry in cpc_definition_data if entry.get('level') == 5.0])

records = []
for entry in publication_data:
    filing_date_str = entry.get('filing_date')
    cpc_data = entry.get('cpc')

    if filing_date_str and cpc_data:
        # Efficiently extract year using regex
        year_match = re.search(r'\\b(19|20)\\d{2}\\b', filing_date_str)
        if not year_match:
            continue # Skip if year cannot be extracted
        filing_year = int(year_match.group(0))

        try:
            # Parse CPC codes
            cpc_list = json.loads(cpc_data)
            for cpc_item in cpc_list:
                cpc_code_full = cpc_item.get('code')
                if cpc_code_full:
                    # Extract the main group part for comparison with level 5 symbols (e.g., A01B29/041 -> A01B29)
                    # The problem asks for CPC group codes at level 5. The level 5 symbols are typically like 'A01B', 'A01B29', etc. (not full A01B29/041)
                    # Assuming level 5 means the first 4 characters plus 2 digits and a letter, or just the main group without subgroup for now based on the examples in hint
                    # Let's consider a CPC code at level 5 to be 'section + class + subclass + main_group' (e.g., A01B29)
                    # The provided list of level 5 symbols like 'B28D' seems to imply just the group, not the full code. Let's assume we need to extract the relevant part for matching.
                    # For now, let's just take the first part until the '/' if it exists, otherwise the whole code. Then, check if it's in the level_5_cpc_symbols.
                    cpc_group_code = cpc_code_full.split('/')[0]
                    if cpc_group_code in level_5_cpc_symbols:
                        records.append({'cpc_code': cpc_group_code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            continue # Skip if cpc_data is not valid JSON

df = pd.DataFrame(records)

# If df is empty, return an empty list
if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Count patent filings per CPC code per year
    filings_per_year = df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

    # Calculate EMA
    smoothing_factor = 0.2

    # Sort by cpc_code and filing_year for efficient grouped EMA calculation
    filings_per_year = filings_per_year.sort_values(by=['cpc_code', 'filing_year'])

    # Calculate EMA within each cpc_code group using transform
    filings_per_year['ema'] = filings_per_year.groupby('cpc_code')['filings'].transform(
        lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean()
    )

    # Find the year with the highest EMA for each CPC code
    best_ema_year = filings_per_year.loc[filings_per_year.groupby('cpc_code')['ema'].idxmax()]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

    print("__RESULT__:")
    print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-16036621143290588479': ['publicationinfo'], 'var_function-call-17677642065960427698': 'file_storage/function-call-17677642065960427698.json', 'var_function-call-6409921778620027728': ['cpc_definition'], 'var_function-call-14622800233827138684': 'file_storage/function-call-14622800233827138684.json', 'var_function-call-18355725859426800648': 'file_storage/function-call-18355725859426800648.json', 'var_function-call-3356983374149566720': 'file_storage/function-call-3356983374149566720.json'}

exec(code, env_args)
