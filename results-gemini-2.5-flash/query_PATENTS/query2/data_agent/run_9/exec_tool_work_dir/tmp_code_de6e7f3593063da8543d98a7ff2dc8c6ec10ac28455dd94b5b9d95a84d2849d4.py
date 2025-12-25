code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-10273422858072318649'])
filtered_data = []

for _, row in data.iterrows():
    grant_date_str = str(row['grant_date']).lower()
    filing_date_str = str(row['filing_date']).lower()
    patents_info_str = str(row['Patents_info'])

    is_germany = 'from de' in patents_info_str.lower() or 'in de' in patents_info_str.lower()

    grant_date_parts = grant_date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').split(' ')
    grant_year = None
    grant_month = None

    for part in grant_date_parts:
        if part.isdigit() and len(part) == 4:
            grant_year = int(part)
        elif part in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec',
                      'january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
            month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
                         'january': 1, 'february': 2, 'march': 3, 'april': 4, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
            grant_month = month_map.get(part[:3], None)

    is_second_half_2019 = (grant_year == 2019 and grant_month is not None and grant_month >= 7)

    if is_germany and is_second_half_2019:
        try:
            cpc_codes = json.loads(row['cpc'])
        except (json.JSONDecodeError, TypeError):
            cpc_codes = []

        filing_year = None
        filing_date_parts = filing_date_str.split(' ')
        for part in filing_date_parts:
            if part.isdigit() and len(part) == 4:
                filing_year = int(part)
                break

        if filing_year:
            for cpc_item in cpc_codes:
                cpc_code = cpc_item.get('code')
                if cpc_code and len(cpc_code) >= 4:
                    filtered_data.append({'cpc_group_level_4': cpc_code[:4], 'filing_year': filing_year})

df_filtered = pd.DataFrame(filtered_data)

if not df_filtered.empty:
    # Calculate annual patent filings for each CPC group
    filings_by_cpc_year = df_filtered.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='filings')

    # Ensure all years are present for each CPC group for EMA calculation
    all_years = pd.MultiIndex.from_product([filings_by_cpc_year['cpc_group_level_4'].unique(),
                                            range(filings_by_cpc_year['filing_year'].min(), filings_by_cpc_year['filing_year'].max() + 1)],
                                           names=['cpc_group_level_4', 'filing_year'])
    filings_by_cpc_year = filings_by_cpc_year.set_index(['cpc_group_level_4', 'filing_year']).reindex(all_years, fill_value=0).reset_index()

    # Calculate EMA
    smoothing_factor = 0.1
    filings_by_cpc_year['ema'] = filings_by_cpc_year.groupby('cpc_group_level_4')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

    # Find the best year (highest EMA) for each CPC group
    best_year_ema = filings_by_cpc_year.loc[filings_by_cpc_year.groupby('cpc_group_level_4')['ema'].idxmax()]
    result = best_year_ema[['cpc_group_level_4', 'filing_year', 'ema']].to_json(orient='records')
else:
    result = "[]"

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10273422858072318649': 'file_storage/function-call-10273422858072318649.json'}

exec(code, env_args)
