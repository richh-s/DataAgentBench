code = """import json
import re
import pandas as pd

# Load the full data from the file
with open(locals()['var_function-call-12991419556258878018'], 'r') as f:
    publication_data = json.load(f)

# Filter patents granted in the second half of 2019 and filed in Germany
germany_patents = []
for record in publication_data:
    patent_info = record['Patents_info']
    grant_date_str = record['grant_date']
    cpc_codes_str = record['cpc']
    filing_date_str = record['filing_date']

    # Extract country code
    country_code = None
    country_matches = re.findall(r'(?:from|in|The|application.*?from)\s([A-Z]{2})', patent_info, re.IGNORECASE)
    if country_matches:
        country_code = country_matches[0]
    
    if country_code == 'DE':
        # Parse grant date
        year_match = re.search(r'\d{4}', grant_date_str)
        month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)

        if year_match and month_match:
            year = int(year_match.group(0))
            month_abbr = month_match.group(0)[:3].capitalize()
            month_map = {
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            month = month_map.get(month_abbr)

            if year == 2019 and month and month >= 7:
                # Extract filing year
                filing_year_match = re.search(r'\d{4}', filing_date_str)
                filing_year = int(filing_year_match.group(0)) if filing_year_match else None

                if filing_year:
                    # Parse CPC codes
                    try:
                        cpc_list = json.loads(cpc_codes_str)
                        for cpc_item in cpc_list:
                            code = cpc_item.get('code')
                            if code and len(code.replace('/', '')) >= 4:  # Ensure it's at least level 4
                                germany_patents.append({
                                    'cpc_group': code[:4],  # Level 4 CPC group
                                    'filing_year': filing_year
                                })
                    except json.JSONDecodeError:
                        pass # Handle cases where cpc_codes_str is not valid JSON

# Create a DataFrame
df = pd.DataFrame(germany_patents)

# Calculate yearly patent filings for each CPC group
yearly_filings = df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='patent_count')

# Sort by CPC group and filing year
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year']).reset_index(drop=True)

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.1
ema_results = []

for cpc_group in yearly_filings['cpc_group'].unique():
    cpc_group_df = yearly_filings[yearly_filings['cpc_group'] == cpc_group].copy()
    cpc_group_df['ema'] = cpc_group_df['patent_count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    
    # Find the year with the highest EMA for this CPC group
    best_year_row = cpc_group_df.loc[cpc_group_df['ema'].idxmax()]
    ema_results.append({
        'cpc_group': cpc_group,
        'best_year': int(best_year_row['filing_year']),
        'highest_ema': best_year_row['ema']
    })

ema_df = pd.DataFrame(ema_results)

# Now, get the full titles for these CPC groups
cpc_symbols = ema_df['cpc_group'].unique().tolist()

__RESULT__:
print(json.dumps(cpc_symbols))"""

env_args = {'var_function-call-12991419556258878018': 'file_storage/function-call-12991419556258878018.json'}

exec(code, env_args)
