code = """import pandas as pd
import json

# Load patent data from the stored file
patent_data = pd.read_json(locals()['var_function-call-12286119263325599604'])

# Load all CPC definitions from the stored file
with open(locals()['var_function-call-2445608865627351311'], 'r') as f:
    cpc_definitions_list = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_list)

# Create a set of all valid level 4 CPC symbols for efficient lookup
level4_symbols_df = cpc_definitions_df[cpc_definitions_df['level'] == 4.0]
level4_symbols_set = set(level4_symbols_df['symbol'].tolist())

# Create a dictionary to map level 4 symbols to their full titles
level4_titles = level4_symbols_df.set_index('symbol')['titleFull'].to_dict()

def parse_date(date_str):
    if isinstance(date_str, str):
        date_str = date_str.replace("th", "").replace("rd", "").replace("nd", "").replace("st", "").replace("on ", "").replace(",", "")
        try:
            return pd.to_datetime(date_str, format="%B %d %Y", errors='coerce')
        except ValueError:
            try:
                return pd.to_datetime(date_str, format="%d %B %Y", errors='coerce')
            except ValueError:
                try:
                    return pd.to_datetime(date_str, format="%Y %B %d", errors='coerce')
                except ValueError:
                    return pd.to_datetime(date_str, errors='coerce')
    return pd.NaT

patent_data['parsed_grant_date'] = patent_data['grant_date'].apply(parse_date)
patent_data['parsed_filing_date'] = patent_data['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019 and from Germany
filtered_data = patent_data[
    (patent_data['parsed_grant_date'].dt.year == 2019) &
    (patent_data['parsed_grant_date'].dt.month >= 7) &
    (patent_data['Patents_info'].str.contains('from DE', na=False))
]

cpc_filings = []
for _, row in filtered_data.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            level4_cpc_found = None
            # Iterate from the full code down to its shortest possible prefix (length 1),
            # checking if any prefix is an exact match for a level 4 CPC symbol.
            # This ensures we capture the most specific level 4 ancestor if it exists as a prefix.
            for i in range(len(code), 0, -1):
                prefix = code[:i]
                if prefix in level4_symbols_set:
                    level4_cpc_found = prefix
                    break # Found the longest matching prefix that is a level 4 symbol
            
            if level4_cpc_found and not pd.isna(row['parsed_filing_date'].year):
                filing_year = int(row['parsed_filing_date'].year)
                cpc_filings.append({'cpc_group': level4_cpc_found, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

# If no valid CPC filings were found after all the filtering and processing
if not cpc_filings:
    print("__RESULT__:")
    print(json.dumps([])) # Return an empty JSON array
else:
    filings_df = pd.DataFrame(cpc_filings)

    # Group by CPC group and filing year to count patents
    yearly_filings = filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='count')

    # Pivot to have years as columns for easier EMA calculation
    pivot_df = yearly_filings.pivot(index='cpc_group', columns='filing_year', values='count').fillna(0)

    alpha = 0.1
    ema_results = []

    for cpc_group in pivot_df.index:
        current_ema = 0
        best_year_for_group = None
        highest_ema_for_group = -1

        years_for_group = sorted(pivot_df.columns.intersection(pivot_df.loc[cpc_group].dropna().index).tolist())
        
        if not years_for_group:
            continue

        first_year_value = pivot_df.loc[cpc_group, years_for_group[0]]
        current_ema = first_year_value
        highest_ema_for_group = current_ema
        best_year_for_group = years_for_group[0]

        for year in years_for_group[1:]:
            value = pivot_df.loc[cpc_group, year]
            current_ema = alpha * value + (1 - alpha) * current_ema
            if current_ema > highest_ema_for_group:
                highest_ema_for_group = current_ema
                best_year_for_group = year
        
        if best_year_for_group is not None:
            ema_results.append({
                'cpc_group': cpc_group,
                'best_year': int(best_year_for_group),
                'highest_ema': highest_ema_for_group
            })

    best_cpc_ema_df = pd.DataFrame(ema_results).sort_values(by='highest_ema', ascending=False)

    # Add the full title using the pre-created dictionary
    # Use .get() with a default value to avoid KeyError if a cpc_group is not found in the dictionary
    best_cpc_ema_df['full_title'] = best_cpc_ema_df['cpc_group'].apply(lambda x: level4_titles.get(x))

    # Select and format the final columns, filtering out any rows where full_title might not be found
    final_output_df = best_cpc_ema_df[best_cpc_ema_df['full_title'].notna()][['full_title', 'cpc_group', 'best_year']]
    final_result = final_output_df.to_json(orient='records')

    print("__RESULT__:")
    print(final_result)"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json', 'var_function-call-12997310755155396542': 'file_storage/function-call-12997310755155396542.json', 'var_function-call-2925605632421467179': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 5}], 'var_function-call-14461189417186399412': "'A61F', 'A43B'", 'var_function-call-1776554272434386262': [], 'var_function-call-14901571610843142513': [{'titleFull': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR', 'symbol': 'A43B', 'level': '5.0'}, {'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS', 'symbol': 'A61F', 'level': '5.0'}], 'var_function-call-2445608865627351311': 'file_storage/function-call-2445608865627351311.json', 'var_function-call-15580338092589924739': 'file_storage/function-call-15580338092589924739.json'}

exec(code, env_args)
