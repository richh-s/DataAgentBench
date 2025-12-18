code = """import json
import re
import pandas as pd

# Load the data from the storage
with open(locals()['var_function-call-18038317103130586081'], 'r') as f:
    data = json.load(f)

# Filter for Germany and second half of 2019
filtered_data = []
for record in data:
    patents_info_str = record.get('Patents_info', '')
    country_code = None
    
    # Attempt to parse Patents_info as JSON first
    try:
        patents_info_json = json.loads(patents_info_str)
        country_code = patents_info_json.get('country_code')
    except json.JSONDecodeError:
        # If not a valid JSON string, try regex matching for country code
        country_code_match = re.search(r'"country_code":\s*"([A-Z]{2})"' , patents_info_str)
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

        # Extract month (handling various formats like 'July', 'Jul', '07')
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month_match_text = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
        if month_match_text:
            grant_month = month_map[month_match_text.group(1).lower()]
        else:
            # Try to find month as a number if not found as text (e.g., '2019-07-01')
            month_num_match = re.search(r'-\d{2}-|' + r'^\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(January|February|March|April|May|June|July|August|September|October|November|December)', grant_date_str, re.IGNORECASE)
            if month_num_match:
                # This regex is a bit complex for different numerical patterns.
                # A simpler approach for numeric month in 'YYYY-MM-DD' or 'DD-MM-YYYY' like format would be:
                # For 'YYYY-MM-DD'
                if re.search(r'\d{4}-\d{2}-\d{2}', grant_date_str):
                    grant_month = int(grant_date_str[5:7])
                # For 'DD-MM-YYYY'
                elif re.search(r'\d{2}-\d{2}-\d{4}', grant_date_str):
                    grant_month = int(grant_date_str[3:5])


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
            # Try to get any text if English is not available, ensuring it's a dict and has 'text'
            if isinstance(title_localized[0], dict) and 'text' in title_localized[0]:
                title = title_localized[0].get('text')
            else:
                title = str(title_localized[0]) # Fallback to string conversion if not a dict with 'text'
    except json.JSONDecodeError:
        pass # title remains None

    for cpc_item in cpc_codes:
        cpc_code = cpc_item.get('code')
        if cpc_code and filing_year is not None:
            # Extract CPC group at level 4 (first 4 characters)
            if len(cpc_code) >= 4:
                cpc_group_4 = cpc_code[:4]
            else:
                cpc_group_4 = cpc_code # Use whole code if shorter than 4 characters
            processed_patents.append({
                'cpc_group_4': cpc_group_4,
                'filing_year': filing_year,
                'full_title': title # Store the title for later lookup
            })

df = pd.DataFrame(processed_patents)

# Ensure DataFrame is not empty before proceeding
if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
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
            # Handle cases where multiple years have the same highest EMA, pick the earliest
            best_year_row = cpc_group_df.loc[cpc_group_df['ema'].idxmax()]
            ema_results.append({
                'cpc_group_4': best_year_row['cpc_group_4'],
                'best_year': int(best_year_row['filing_year']),
                'ema_value': best_year_row['ema']
            })

    ema_df = pd.DataFrame(ema_results)

    # Get unique titles for each CPC group, ensure it handles potential None titles
    # We need to consider that the 'full_title' might be None or a string, or even a list of dicts if the parsing failed somehow
    # Group by cpc_group_4 and get the first non-null title from the original records (or the pre-processed 'full_title')
    # To ensure we get a single title per CPC group, let's create a mapping from df for cpc_group_4 to a single title
    title_map = df.drop_duplicates(subset=['cpc_group_4']).set_index('cpc_group_4')['full_title'].to_dict()
    ema_df['full_title'] = ema_df['cpc_group_4'].map(title_map)

    merged_results = ema_df # Since we added title to ema_df directly

    # Sort by EMA value and prepare final results
    final_results = merged_results.sort_values(by='ema_value', ascending=False)

    # Reformat for output: CPC group code, full title, best year
    final_output = final_results[['cpc_group_4', 'full_title', 'best_year']].to_dict(orient='records')

    print('__RESULT__:')
    print(json.dumps(final_output))"""

env_args = {'var_function-call-5163890687866059467': [], 'var_function-call-9707076876655068919': 'file_storage/function-call-9707076876655068919.json', 'var_function-call-5683745495324308164': 'file_storage/function-call-5683745495324308164.json', 'var_function-call-18435751526660848933': 'file_storage/function-call-18435751526660848933.json', 'var_function-call-5982256915993768463': [], 'var_function-call-3426062924692431328': 'file_storage/function-call-3426062924692431328.json', 'var_function-call-1288847198007481625': 'file_storage/function-call-1288847198007481625.json', 'var_function-call-16310302289237273939': 'file_storage/function-call-16310302289237273939.json', 'var_function-call-14861526276822314506': 'file_storage/function-call-14861526276822314506.json', 'var_function-call-14083591909542804425': 'file_storage/function-call-14083591909542804425.json', 'var_function-call-983563472515922662': [], 'var_function-call-18038317103130586081': 'file_storage/function-call-18038317103130586081.json'}

exec(code, env_args)
