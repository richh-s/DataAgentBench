code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-6623226614519656190'])

# Filter for German patents and grant date in the second half of 2019
def is_german_patent(patents_info):
    return 'DE,' in patents_info

def is_second_half_2019(grant_date):
    try:
        if isinstance(grant_date, str):
            grant_date_str = grant_date.lower()
            if 'jul' in grant_date_str or 'aug' in grant_date_str or 'sep' in grant_date_str or \
               'oct' in grant_date_str or 'nov' in grant_date_str or 'dec' in grant_date_str:
                return True
        return False
    except:
        return False

filtered_patents = data[data['Patents_info'].apply(is_german_patent) &
                        data['grant_date'].apply(is_second_half_2019)].copy()

# Extract CPC codes and filing year
cpc_filing_data = []
for index, row in filtered_patents.iterrows():
    cpc_list = json.loads(row['cpc'])
    filing_date_str = row['filing_date']
    filing_year = None
    if isinstance(filing_date_str, str):
        for part in filing_date_str.split():
            if part.isdigit() and len(part) == 4:
                filing_year = int(part)
                break
    
    for cpc_item in cpc_list:
        cpc_code = cpc_item['code']
        if len(cpc_code) >= 5 and filing_year: # Ensure it's at least level 4
            cpc_group = cpc_code[:4] # Get level 4 CPC group
            cpc_filing_data.append({'cpc_group': cpc_group, 'filing_year': filing_year})

cpc_filing_df = pd.DataFrame(cpc_filing_data)

# Group by CPC group and filing year, then count filings
filings_by_cpc_year = cpc_filing_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings_count')

# Calculate EMA
alpha = 0.1
ema_results = []
for cpc_group in filings_by_cpc_year['cpc_group'].unique():
    cpc_group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group'] == cpc_group].sort_values(by='filing_year')
    
    # Initialize EMA for the first year
    if not cpc_group_df.empty:
        ema = 0
        if not cpc_group_df.empty:
            ema = cpc_group_df.iloc[0]['filings_count']
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[0]['filing_year'],
                'ema': ema
            })
        
        # Calculate EMA for subsequent years
        for i in range(1, len(cpc_group_df)):
            ema = alpha * cpc_group_df.iloc[i]['filings_count'] + (1 - alpha) * ema
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[i]['filing_year'],
                'ema': ema
            })

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Get unique CPC groups for querying titles
unique_cpc_groups = best_years['cpc_group'].unique().tolist()

print("__RESULT__:")
print(json.dumps(unique_cpc_groups)))"""

env_args = {'var_function-call-6623226614519656190': 'file_storage/function-call-6623226614519656190.json'}

exec(code, env_args)
