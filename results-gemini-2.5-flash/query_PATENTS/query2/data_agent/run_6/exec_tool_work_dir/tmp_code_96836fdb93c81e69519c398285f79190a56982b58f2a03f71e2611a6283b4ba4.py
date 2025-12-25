code = """import pandas as pd
import json
import re

raw_data = pd.read_json(locals()['var_function-call-15167329076479841775'])

def parse_date(date_str):
    if not isinstance(date_str, str):
        return None, None
    
    year = None
    month = None
    month_str = None

    # Pattern to capture month string or numerical month (if any) and year
    # This regex is more comprehensive and attempts to capture various date formats
    match_full_date = re.search(r'(?:(\d{1,2})(?:st|nd|rd|th)?)?\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*(?:(\d{1,2})(?:st|nd|rd|th)?,)?\s*(\d{4})'  # Day Month Year (e.g., 14th Mar 2019)
                                r'|\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*(?:(\d{1,2})(?:st|nd|rd|th)?,)?\s*(\d{4})' # Month Day Year (e.g., Mar 14th, 2019)
                                r'|(\d{4}),\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*(?:(\d{1,2})(?:st|nd|rd|th)?)?' # Year, Month Day (e.g., 2019, July 12th)
                                r'|\b(\d{4})\b', date_str, re.IGNORECASE) # Year only

    if match_full_date:
        if match_full_date.group(4): # Day Month Year
            month_str = match_full_date.group(2)
            year = int(match_full_date.group(4))
        elif match_full_date.group(7): # Month Day Year
            month_str = match_full_date.group(5)
            year = int(match_full_date.group(7))
        elif match_full_date.group(8): # Year, Month Day
            year = int(match_full_date.group(8))
            month_str = match_full_date.group(9)
        elif match_full_date.group(11): # Year only
            year = int(match_full_date.group(11))

    month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    if month_str:
        month = month_map.get(month_str.lower(), None)
    
    return year, month

def get_country_code(patents_info_str):
    if not isinstance(patents_info_str, str): 
        return None
    match = re.search(r'"country_code":\s*"([A-Z]{2})"', patents_info_str)
    return match.group(1) if match else None

# Filter for patents granted in Germany in the second half of 2019
filtered_patents = []
for _, row in raw_data.iterrows():
    grant_year, grant_month = parse_date(row['grant_date'])
    country_code = get_country_code(row['Patents_info'])
    
    if grant_year == 2019 and grant_month and grant_month >= 7 and country_code == 'DE':
        filing_year, _ = parse_date(row['filing_date'])
        if filing_year is not None:
            # Extract CPC codes at level 4
            cpc_codes = []
            try:
                cpc_data = json.loads(row['cpc'])
                if isinstance(cpc_data, list):
                    for cpc_entry in cpc_data:
                        code = cpc_entry.get('code')
                        if code and len(code) >= 4:  # CPC group at level 4
                            cpc_codes.append(code[:4])
            except json.JSONDecodeError:
                pass # Handle cases where CPC is not valid JSON
            
            for cpc_code in set(cpc_codes):
                filtered_patents.append({'cpc_group': cpc_code, 'filing_year': filing_year})


# Create a DataFrame for EMA calculation
pdf_filtered = pd.DataFrame(filtered_patents)

# Calculate yearly filings for each CPC group
if not pdf_filtered.empty:
    yearly_filings = pdf_filtered.groupby(['cpc_group', 'filing_year']).size().unstack(fill_value=0)

    # Calculate EMA for each CPC group
    smoothing_factor = 0.1
    ema_results = []
    for cpc_group, filings in yearly_filings.iterrows():
        ema = pd.Series(filings).ewm(alpha=smoothing_factor, adjust=False).mean()
        if not ema.empty:
            best_year = ema.idxmax()
            highest_ema = ema.max()
            ema_results.append({'cpc_group': cpc_group, 'best_year': int(best_year), 'highest_ema': highest_ema})

    # Sort by highest EMA
    ema_df = pd.DataFrame(ema_results).sort_values(by='highest_ema', ascending=False)
    result_df_json = ema_df.to_json(orient='records')
else:
    result_df_json = "[]"

print("__RESULT__:")
print(result_df_json)"""

env_args = {'var_function-call-4974102629247983957': ['publicationinfo'], 'var_function-call-15607172090208474855': [], 'var_function-call-9272648693801938418': 'file_storage/function-call-9272648693801938418.json', 'var_function-call-13744357239052805177': ['cpc_definition'], 'var_function-call-14994806578432216053': 'file_storage/function-call-14994806578432216053.json', 'var_function-call-13549183485278852171': [], 'var_function-call-5665014815337330465': [], 'var_function-call-14965831809541476123': 'file_storage/function-call-14965831809541476123.json', 'var_function-call-10478981295189184130': [], 'var_function-call-12302277692986144323': 'file_storage/function-call-12302277692986144323.json', 'var_function-call-542895921075829997': [], 'var_function-call-8695021391172718570': 'file_storage/function-call-8695021391172718570.json', 'var_function-call-10646157812208479788': [], 'var_function-call-1056033459753607260': 'file_storage/function-call-1056033459753607260.json', 'var_function-call-11911875829396121333': [], 'var_function-call-12083259259987615714': 'file_storage/function-call-12083259259987615714.json', 'var_function-call-10721318483349681273': 'file_storage/function-call-10721318483349681273.json', 'var_function-call-6442685032807394280': 'file_storage/function-call-6442685032807394280.json', 'var_function-call-15167329076479841775': 'file_storage/function-call-15167329076479841775.json'}

exec(code, env_args)
