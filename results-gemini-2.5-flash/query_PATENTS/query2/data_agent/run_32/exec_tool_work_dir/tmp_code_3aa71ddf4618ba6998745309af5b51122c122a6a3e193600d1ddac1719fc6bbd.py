code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-9247441433640274170'])

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        # Try another format if the default fails (e.g., 'March the 18th, 2019')
        # This is a more robust way to handle natural language dates
        month_map = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
            'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        parts = date_str.replace('the ', '').replace(',', '').split()
        if len(parts) >= 3:
            day = ''.join(filter(str.isdigit, parts[0]))
            month = month_map.get(parts[1])
            year = parts[2]
            if day and month and year:
                try:
                    return pd.to_datetime(f"{year}-{month}-{day}", errors='coerce')
                except:
                    pass
        return pd.NaT

data['grant_date_parsed'] = data['grant_date'].apply(parse_date)
data['filing_date_parsed'] = data['filing_date'].apply(parse_date)

# Filter for patents granted in Germany and in the second half of 2019
germany_patents = data[data['Patents_info'].str.contains('Germany|DE')].copy()
second_half_2019 = germany_patents[
    (germany_patents['grant_date_parsed'] >= '2019-07-01') &
    (germany_patents['grant_date_parsed'] <= '2019-12-31')
].copy()

# Extract CPC codes and filing year
cpc_filings = []
for index, row in second_half_2019.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date_parsed'].year
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code')
            if cpc_code:
                # Extract CPC group at level 4 (e.g., A61B, A61B5, A61B5/00, A61B5/0001)
                parts = cpc_code.split('/')
                if len(parts) > 0:
                    group_code = parts[0]
                    if len(parts) > 1:
                        group_code += '/' + parts[1]
                        if len(group_code) >= 7 and group_code[4].isalpha(): # Handle A61B5/00 vs A61B5
                           cpc_group_level_4 = cpc_code[:7]
                           cpc_filings.append({'cpc_group': cpc_group_level_4, 'filing_year': filing_year})
                        elif len(group_code) >= 5 and group_code[4].isdigit(): # A61B5
                            cpc_group_level_4 = cpc_code[:5]
                            cpc_filings.append({'cpc_group': cpc_group_level_4, 'filing_year': filing_year})
                        else: # A61B
                            cpc_group_level_4 = cpc_code[:4]
                            cpc_filings.append({'cpc_group': cpc_group_level_4, 'filing_year': filing_year})
                    else: # A61B
                        cpc_group_level_4 = cpc_code[:4]
                        cpc_filings.append({'cpc_group': cpc_group_level_4, 'filing_year': filing_year})
    except json.JSONDecodeError:
        continue
    except AttributeError:
        continue # Handle cases where 'cpc' might be NaN or not a string

cpc_filings_df = pd.DataFrame(cpc_filings)

# Group by CPC group and filing year, then count filings
yearly_filings = cpc_filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []
for cpc_group in yearly_filings['cpc_group'].unique():
    group_data = yearly_filings[yearly_filings['cpc_group'] == cpc_group].sort_values(by='filing_year')
    group_data['ema'] = group_data['filings'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(group_data)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group based on the highest EMA
best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Select relevant columns
result = best_year_per_cpc[['cpc_group', 'filing_year']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json'}

exec(code, env_args)
