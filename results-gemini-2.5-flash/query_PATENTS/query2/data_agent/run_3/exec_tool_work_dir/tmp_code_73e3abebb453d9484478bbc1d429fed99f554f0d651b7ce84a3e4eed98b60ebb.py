code = """import json
import re
import pandas as pd

# Load the data from the storage
with open(locals()['var_function-call-14083591909542804425'], 'r') as f:
    data = json.load(f)

# Filter for Germany and second half of 2019
filtered_data = []
for record in data:
    patents_info = record.get('Patents_info', '')
    country_code = None
    if isinstance(patents_info, str):
        country_code_match = re.search(r'"country_code": "([A-Z]{2})"' , patents_info)
        if country_code_match:
            country_code = country_code_match.group(1)

    if country_code == 'DE':
        grant_date_str = record.get('grant_date', '')
        grant_year = None
        grant_month = None

        # Robustly parse grant_date
        year_match = re.search(r'(\d{4})', grant_date_str)
        if year_match:
            grant_year = int(year_match.group(1))

        # Month parsing
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
        if month_match:
            grant_month = month_map[month_match.group(1).lower()]

        if grant_year == 2019 and grant_month is not None and grant_month >= 7:
            filtered_data.append(record)

# Process CPC codes, filing dates, and titles
processed_patents = []
for record in filtered_data:
    cpc_codes_raw = record.get('cpc', '[]')
    cpc_codes = []
    try:
        cpc_codes = json.loads(cpc_codes_raw)
    except json.JSONDecodeError:
        # Handle cases where cpc is not valid JSON
        pass

    filing_date_str = record.get('filing_date', '')
    filing_year = None
    filing_year_match = re.search(r'(\d{4})', filing_date_str)
    if filing_year_match:
        filing_year = int(filing_year_match.group(1))

    title_localized_raw = record.get('title_localized', '[]')
    title = None
    try:
        title_localized = json.loads(title_localized_raw)
        title = next((t['text'] for t in title_localized if t['language'] == 'en'), None)
        if not title and title_localized:
            title = title_localized[0]['text'] # Take first available if no English
    except json.JSONDecodeError:
        # Handle cases where title_localized is not valid JSON
        pass


    for cpc_item in cpc_codes:
        cpc_code = cpc_item.get('code')
        if cpc_code and filing_year is not None:
            # Extract CPC group at level 4
            if len(cpc_code) >= 4:
                cpc_group_4 = cpc_code[:4]
            else:
                # If CPC code is shorter than 4 characters, use the whole code
                cpc_group_4 = cpc_code

            processed_patents.append({
                'cpc_group_4': cpc_group_4,
                'filing_year': filing_year,
                'title_localized': title # Store the title for later lookup
            })

df = pd.DataFrame(processed_patents)

# Calculate patent filings per year for each CPC group
# Filter out rows where cpc_group_4 or filing_year is None
yearly_filings = df.dropna(subset=['cpc_group_4', 'filing_year']).groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

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
        # Handle cases where multiple years have the same highest EMA, pick the earliest
        best_year_row = cpc_group_df.loc[cpc_group_df['ema'].idxmax()]
        ema_results.append({
            'cpc_group_4': best_year_row['cpc_group_4'],
            'best_year': int(best_year_row['filing_year']),
            'ema_value': best_year_row['ema']
        })

ema_df = pd.DataFrame(ema_results)

# Get unique titles for each CPC group
# Group by cpc_group_4 and get the first non-null title_localized
cpc_titles = df.groupby('cpc_group_4')['title_localized'].apply(lambda x: x.dropna().iloc[0] if not x.dropna().empty else None).reset_index()
cpc_titles.rename(columns={'title_localized': 'full_title'}, inplace=True)

merged_results = pd.merge(ema_df, cpc_titles, on='cpc_group_4', how='left')

# Sort by EMA value and prepare final results
final_results = merged_results.sort_values(by='ema_value', ascending=False)

# Reformat for output: CPC group code, full title, best year
final_output = final_results[['cpc_group_4', 'full_title', 'best_year']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_function-call-5163890687866059467': [], 'var_function-call-9707076876655068919': 'file_storage/function-call-9707076876655068919.json', 'var_function-call-5683745495324308164': 'file_storage/function-call-5683745495324308164.json', 'var_function-call-18435751526660848933': 'file_storage/function-call-18435751526660848933.json', 'var_function-call-5982256915993768463': [], 'var_function-call-3426062924692431328': 'file_storage/function-call-3426062924692431328.json', 'var_function-call-1288847198007481625': 'file_storage/function-call-1288847198007481625.json', 'var_function-call-16310302289237273939': 'file_storage/function-call-16310302289237273939.json', 'var_function-call-14861526276822314506': 'file_storage/function-call-14861526276822314506.json', 'var_function-call-14083591909542804425': 'file_storage/function-call-14083591909542804425.json'}

exec(code, env_args)
