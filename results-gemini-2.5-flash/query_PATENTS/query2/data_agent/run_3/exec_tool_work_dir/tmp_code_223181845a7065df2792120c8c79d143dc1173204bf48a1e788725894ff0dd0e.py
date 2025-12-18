code = """import json
import re
import pandas as pd

# Load the data from the storage
with open(locals()['var_function-call-16775230555930352805'], 'r') as f:
    data = json.load(f)

# Filter for Germany and second half of 2019
filtered_data = []
for record in data:
    patents_info_str = record.get('Patents_info', '')
    country_code = None
    
    # Try to extract country_code from Patents_info using a more general regex
    country_code_match = re.search(r'(?:country_code":\s*"|from\s)([A-Z]{2})', patents_info_str)
    if country_code_match:
        country_code = country_code_match.group(1)

    if country_code == 'DE':
        grant_date_str = record.get('grant_date', '')
        grant_year = None
        grant_month = None

        # Extract year
        year_match = re.search(r'(\d{4})', grant_date_str)
        if year_match:
            grant_year = int(year_match.group(1))

        # Extract month
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
            'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
            'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
        }
        month_match_text = re.search(r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)', grant_date_str, re.IGNORECASE)
        if month_match_text:
            grant_month = month_map[month_match_text.group(1).lower()]
        
        # Check for numeric month in formats like 'DDth Mon YYYY' or 'Mon DD, YYYY' or 'YYYY-MM-DD'
        if grant_month is None:
            # Try MM/DD/YYYY, MM-DD-YYYY, YYYY/MM/DD, YYYY-MM-DD
            date_parts = re.findall(r'\d{1,2}|\d{4}', grant_date_str)
            if len(date_parts) == 3:
                # Assuming YYYY-MM-DD or MM-DD-YYYY or DD-MM-YYYY possibilities
                if len(date_parts[0]) == 4: # YYYY-MM-DD
                    grant_month = int(date_parts[1])
                elif len(date_parts[2]) == 4: # MM-DD-YYYY or DD-MM-YYYY. Try to infer. Safest to rely on month names.
                    pass # skip for now, as natural language is specified.

        if grant_year == 2019 and grant_month is not None and grant_month >= 7:
            filtered_data.append(record)

processed_patents = []
for record in filtered_data:
    cpc_codes_raw = record.get('cpc', '[]')
    cpc_codes = []
    try:
        cpc_codes = json.loads(cpc_codes_raw)
    except json.JSONDecodeError:
        pass

    filing_date_str = record.get('filing_date', '')
    filing_year = None
    filing_year_match = re.search(r'(\d{4})', filing_date_str)
    if filing_year_match:
        filing_year = int(filing_year_match.group(1))

    title = None
    title_localized_raw = record.get('title_localized', '[]')
    try:
        title_localized = json.loads(title_localized_raw)
        title = next((t['text'] for t in title_localized if t.get('language') == 'en'), None)
        if not title and title_localized and isinstance(title_localized, list) and len(title_localized) > 0:
            if isinstance(title_localized[0], dict) and 'text' in title_localized[0]:
                title = title_localized[0].get('text')
            else:
                title = str(title_localized[0])
    except json.JSONDecodeError:
        pass

    for cpc_item in cpc_codes:
        cpc_code = cpc_item.get('code')
        if cpc_code and filing_year is not None:
            if len(cpc_code) >= 4:
                cpc_group_4 = cpc_code[:4]
            else:
                cpc_group_4 = cpc_code
            processed_patents.append({
                'cpc_group_4': cpc_group_4,
                'filing_year': filing_year,
                'full_title': title
            })

df = pd.DataFrame(processed_patents)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    yearly_filings = df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

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
            
            best_year_row = cpc_group_df.loc[cpc_group_df['ema'].idxmax()]
            ema_results.append({
                'cpc_group_4': best_year_row['cpc_group_4'],
                'best_year': int(best_year_row['filing_year']),
                'ema_value': best_year_row['ema']
            })

    ema_df = pd.DataFrame(ema_results)

    title_map = df.drop_duplicates(subset=['cpc_group_4']).set_index('cpc_group_4')['full_title'].to_dict()
    ema_df['full_title'] = ema_df['cpc_group_4'].map(title_map)

    final_results = ema_df.sort_values(by='ema_value', ascending=False)

    final_output = final_results[['cpc_group_4', 'full_title', 'best_year']].to_dict(orient='records')

    print('__RESULT__:')
    print(json.dumps(final_output))"""

env_args = {'var_function-call-5163890687866059467': [], 'var_function-call-9707076876655068919': 'file_storage/function-call-9707076876655068919.json', 'var_function-call-5683745495324308164': 'file_storage/function-call-5683745495324308164.json', 'var_function-call-18435751526660848933': 'file_storage/function-call-18435751526660848933.json', 'var_function-call-5982256915993768463': [], 'var_function-call-3426062924692431328': 'file_storage/function-call-3426062924692431328.json', 'var_function-call-1288847198007481625': 'file_storage/function-call-1288847198007481625.json', 'var_function-call-16310302289237273939': 'file_storage/function-call-16310302289237273939.json', 'var_function-call-14861526276822314506': 'file_storage/function-call-14861526276822314506.json', 'var_function-call-14083591909542804425': 'file_storage/function-call-14083591909542804425.json', 'var_function-call-983563472515922662': [], 'var_function-call-18038317103130586081': 'file_storage/function-call-18038317103130586081.json', 'var_function-call-2368330865793497200': [], 'var_function-call-16775230555930352805': 'file_storage/function-call-16775230555930352805.json'}

exec(code, env_args)
