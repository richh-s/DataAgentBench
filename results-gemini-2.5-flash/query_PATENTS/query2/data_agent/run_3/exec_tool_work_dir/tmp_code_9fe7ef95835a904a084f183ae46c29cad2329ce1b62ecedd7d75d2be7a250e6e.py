code = """import json
import re
import pandas as pd

# Load the data from the storage
with open(locals()['var_function-call-14083591909542804425'], 'r') as f:
    data = json.load(f)

# Filter for Germany and second half of 2019
filtered_data = []
for record in data:
    patents_info = record.get('Patents_info', '{}')
    if isinstance(patents_info, str):
        country_code_match = re.search(r'"country_code": "(\w+)"', patents_info)
        country_code = country_code_match.group(1) if country_code_match else None
    else:
        country_code = None

    if country_code == 'DE':
        grant_date = record.get('grant_date', '')
        # Check for various date formats
        if re.search(r'(July|Aug|September|Oct|Nov|Dec)[a-zA-Z]*( |\.,|\'s|\d{1,2})? *(2019)', grant_date, re.IGNORECASE):
            filtered_data.append(record)

# Process CPC codes, filing dates, and titles
processed_patents = []
for record in filtered_data:
    cpc_codes = json.loads(record.get('cpc', '[]'))
    filing_date_str = record.get('filing_date', '')
    
    # Extract year from filing_date
    filing_year_match = re.search(r'(\d{4})', filing_date_str)
    filing_year = int(filing_year_match.group(1)) if filing_year_match else None

    title_localized = json.loads(record.get('title_localized', '[]'))
    title = next((t['text'] for t in title_localized if t['language'] == 'en'), None)
    if not title and title_localized:
        title = title_localized[0]['text'] # Take first available if no English

    for cpc_item in cpc_codes:
        cpc_code = cpc_item.get('code')
        if cpc_code and len(cpc_code) >= 4:
            cpc_group_4 = cpc_code[:4]
            processed_patents.append({
                'cpc_group_4': cpc_group_4,
                'filing_year': filing_year,
                'title_localized': title
            })

df = pd.DataFrame(processed_patents)

# Calculate patent filings per year for each CPC group
yearly_filings = df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []
for cpc_group in yearly_filings['cpc_group_4'].unique():
    cpc_group_df = yearly_filings[yearly_filings['cpc_group_4'] == cpc_group].sort_values(by='filing_year')
    ema = []
    if not cpc_group_df.empty:
        ema.append(cpc_group_df.iloc[0]['filings'])  # Initialize EMA with the first value
        for i in range(1, len(cpc_group_df)):
            ema.append(alpha * cpc_group_df.iloc[i]['filings'] + (1 - alpha) * ema[-1])
        cpc_group_df['ema'] = ema
        
        # Find the best year for each CPC group (highest EMA)
        best_year_row = cpc_group_df.loc[cpc_group_df['ema'].idxmax()]
        ema_results.append({
            'cpc_group_4': cpc_group,
            'best_year': int(best_year_row['filing_year']),
            'ema_value': best_year_row['ema']
        })

ema_df = pd.DataFrame(ema_results)

# Get unique titles for each CPC group
cpc_titles = df[['cpc_group_4', 'title_localized']].drop_duplicates(subset='cpc_group_4')
merged_results = pd.merge(ema_df, cpc_titles, on='cpc_group_4', how='left')

# Sort by EMA value and get the top results (not specified how many, so return all)
final_results = merged_results.sort_values(by='ema_value', ascending=False)
final_results = final_results.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_function-call-5163890687866059467': [], 'var_function-call-9707076876655068919': 'file_storage/function-call-9707076876655068919.json', 'var_function-call-5683745495324308164': 'file_storage/function-call-5683745495324308164.json', 'var_function-call-18435751526660848933': 'file_storage/function-call-18435751526660848933.json', 'var_function-call-5982256915993768463': [], 'var_function-call-3426062924692431328': 'file_storage/function-call-3426062924692431328.json', 'var_function-call-1288847198007481625': 'file_storage/function-call-1288847198007481625.json', 'var_function-call-16310302289237273939': 'file_storage/function-call-16310302289237273939.json', 'var_function-call-14861526276822314506': 'file_storage/function-call-14861526276822314506.json', 'var_function-call-14083591909542804425': 'file_storage/function-call-14083591909542804425.json'}

exec(code, env_args)
