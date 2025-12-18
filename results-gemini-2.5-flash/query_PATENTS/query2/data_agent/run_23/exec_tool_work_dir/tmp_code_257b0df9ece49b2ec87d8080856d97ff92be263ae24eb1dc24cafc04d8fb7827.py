code = """import json
import pandas as pd

with open(locals()['var_function-call-4759286018936783178'], 'r') as f:
    publication_data = json.load(f)

parsed_data = []
for record in publication_data:
    grant_date_str = record.get('grant_date')
    filing_date_str = record.get('filing_date')
    cpc_json_str = record.get('cpc')
    patents_info_str = record.get('Patents_info')

    grant_year = None
    if grant_date_str:
        try:
            # Extract year and month for grant_date
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
            else: grant_month = None

            if grant_month:
                words = grant_date_str.replace(",", "").replace(".", "").split()
                for word in words:
                    if word.isdigit() and len(word) == 4:
                        grant_year = int(word)
                        break
        except:
            grant_year = None
    
    filing_year = None
    if filing_date_str:
        try:
            # Extract year for filing_date
            words = filing_date_str.replace(",", "").replace(".", "").split()
            for word in words:
                if word.isdigit() and len(word) == 4:
                    filing_year = int(word)
                    break
        except:
            filing_year = None
            
    country_code = None
    if patents_info_str and "country_code" in patents_info_str:
        try:
            country_code_start = patents_info_str.find("country_code") + len("country_code") + 2  # +2 for ': "'
            country_code_end = patents_info_str.find("'", country_code_start)
            if country_code_end == -1: # if single quote not found try double quote
                country_code_end = patents_info_str.find('"', country_code_start)
            country_code = patents_info_str[country_code_start:country_code_end]
        except:
            country_code = None

    cpc_codes = []
    if cpc_json_str:
        try:
            cpc_data = json.loads(cpc_json_str)
            for cpc_item in cpc_data:
                code = cpc_item.get('code')
                if code:
                    cpc_codes.append(code)
        except json.JSONDecodeError:
            pass

    parsed_data.append({
        'grant_year': grant_year,
        'grant_month': grant_month,
        'filing_year': filing_year,
        'cpc_codes': cpc_codes,
        'country_code': country_code
    })

df = pd.DataFrame(parsed_data)

filtered_df = df[(df['grant_year'] == 2019) & (df['grant_month'].isin([7, 8, 9, 10, 11, 12])) & (df['country_code'] == 'DE')]

cpc_filings = []
for index, row in filtered_df.iterrows():
    for cpc_code in row['cpc_codes']:
        if len(cpc_code) >= 7:  # CPC group at level 4 example: A61K 31/00, so at least 7 characters
            cpc_group_level4 = cpc_code[:4] + '/' + cpc_code[4:7]
            cpc_filings.append({
                'cpc_group_level4': cpc_group_level4,
                'filing_year': row['filing_year']
            })

cpc_filings_df = pd.DataFrame(cpc_filings)

# Calculate yearly patent filings for each CPC group
yearly_filings = cpc_filings_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='patent_count')

# Sort by CPC group and filing year
yearly_filings = yearly_filings.sort_values(by=['cpc_group_level4', 'filing_year'])

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []

for cpc_group in yearly_filings['cpc_group_level4'].unique():
    cpc_group_df = yearly_filings[yearly_filings['cpc_group_level4'] == cpc_group].copy()
    cpc_group_df['ema'] = cpc_group_df['patent_count'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(cpc_group_df)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group based on the highest EMA
best_years = ema_df.loc[ema_df.groupby('cpc_group_level4')['ema'].idxmax()]
result = best_years[['cpc_group_level4', 'ema', 'filing_year']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2381264414405672356': ['publicationinfo'], 'var_function-call-4759286018936783178': 'file_storage/function-call-4759286018936783178.json'}

exec(code, env_args)
