code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-4759286018936783178'], 'r') as f:
    publication_data = json.load(f)

parsed_data = []
for record in publication_data:
    grant_date_str = record.get('grant_date')
    filing_date_str = record.get('filing_date')
    cpc_json_str = record.get('cpc')
    patents_info_str = record.get('Patents_info')

    grant_year = None
    grant_month = None
    if grant_date_str:
        try:
            words = grant_date_str.replace(",", "").replace(".", "").split()
            for word in words:
                if word.isdigit() and len(word) == 4:
                    grant_year = int(word)
                    break

            if "January" in grant_date_str: grant_month = 1
            elif "February" in grant_date_str: grant_month = 2
            elif "March" in grant_date_str: grant_month = 3
            elif "April" in grant_date_str: grant_month = 4
            elif "May" in grant_date_str: grant_month = 5
            elif "June" in grant_date_str: grant_month = 6
            elif "July" in grant_date_str: grant_month = 7
            elif "August" in grant_date_str: grant_month = 8
            elif "September" in grant_date_str: grant_month = 9
            elif "October" in grant_date_str: grant_month = 10
            elif "November" in grant_date_str: grant_month = 11
            elif "December" in grant_date_str: grant_month = 12
        except:
            pass
    
    filing_year = None
    if filing_date_str:
        try:
            words = filing_date_str.replace(",", "").replace(".", "").split()
            for word in words:
                if word.isdigit() and len(word) == 4:
                    filing_year = int(word)
                    break
        except:
            pass
            
    country_code = None
    if patents_info_str:
        match = re.search(r'\b([A-Z]{2})-\d', patents_info_str)
        if match:
            country_code = match.group(1)

    cpc_codes_raw = []
    if cpc_json_str:
        try:
            cpc_data = json.loads(cpc_json_str)
            for cpc_item in cpc_data:
                code = cpc_item.get('code')
                if code:
                    cpc_codes_raw.append(code)
        except json.JSONDecodeError:
            pass

    parsed_data.append({
        'grant_year': grant_year,
        'grant_month': grant_month,
        'filing_year': filing_year,
        'cpc_codes_raw': cpc_codes_raw,
        'country_code': country_code
    })

df = pd.DataFrame(parsed_data)

filtered_df = df[(df['grant_year'] == 2019) & (df['grant_month'].isin([7, 8, 9, 10, 11, 12])) & (df['country_code'] == 'DE')]

cpc_filings = []
for index, row in filtered_df.iterrows():
    if pd.notna(row['filing_year']): # Ensure filing_year is not NaN
        for cpc_code in row['cpc_codes_raw']:
            cpc_group_level4 = None
            if '/' in cpc_code:
                prefix = cpc_code.split('/')[0]
                cpc_group_level4 = prefix + '/00'
            
            if cpc_group_level4:
                cpc_filings.append({
                    'cpc_group_level4': cpc_group_level4,
                    'filing_year': row['filing_year']
                })

cpc_filings_df = pd.DataFrame(cpc_filings)

if not cpc_filings_df.empty:
    yearly_filings = cpc_filings_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='patent_count')
    yearly_filings = yearly_filings.sort_values(by=['cpc_group_level4', 'filing_year'])

    alpha = 0.1
    ema_results = []

    for cpc_group in yearly_filings['cpc_group_level4'].unique():
        cpc_group_df = yearly_filings[yearly_filings['cpc_group_level4'] == cpc_group].copy()
        cpc_group_df['ema'] = cpc_group_df['patent_count'].ewm(alpha=alpha, adjust=False).mean()
        ema_results.append(cpc_group_df)

    ema_df = pd.concat(ema_results)
    best_years = ema_df.loc[ema_df.groupby('cpc_group_level4')['ema'].idxmax()]
    final_result_df = best_years[['cpc_group_level4', 'filing_year']]
    result_json = final_result_df.to_json(orient='records')
else:
    result_json = json.dumps([]) # Return empty if no filings found

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-2381264414405672356': ['publicationinfo'], 'var_function-call-4759286018936783178': 'file_storage/function-call-4759286018936783178.json', 'var_function-call-17180731294119715552': ['cpc_definition'], 'var_function-call-412462610012970301': 'file_storage/function-call-412462610012970301.json'}

exec(code, env_args)
