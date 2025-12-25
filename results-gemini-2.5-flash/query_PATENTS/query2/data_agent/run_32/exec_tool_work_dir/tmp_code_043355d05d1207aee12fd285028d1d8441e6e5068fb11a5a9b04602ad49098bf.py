code = """import pandas as pd
import json
import re

# Load the full publication data
with open(locals()['var_function-call-9247441433640274170'], 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Convert date columns to datetime objects, coercing errors
df['grant_date_parsed'] = pd.to_datetime(df['grant_date'].str.replace('st|nd|rd|th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')
df['filing_date_parsed'] = pd.to_datetime(df['filing_date'].str.replace('st|nd|rd|th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')

# Filter for patents granted in Germany and in the second half of 2019
germany_patents_2019 = df[
    df['Patents_info'].str.contains(r'\bDE\b|Germany', na=False, flags=re.IGNORECASE) &
    (df['grant_date_parsed'] >= '2019-07-01') &
    (df['grant_date_parsed'] <= '2019-12-31')
].copy()

# Load CPC definition data (all levels) to get titles later
with open(locals()['var_function-call-1756360509441851569'], 'r') as f:
    cpc_definition_raw = json.load(f)
cpc_definition_all_df = pd.DataFrame(cpc_definition_raw)

# Load level 4 CPC symbols (only symbols at level 4)
level_4_symbols_data = locals()['var_function-call-10295012344133101524']
level_4_symbols_df = pd.DataFrame(level_4_symbols_data)
level_4_symbols_set = set(level_4_symbols_df['symbol'].unique())

# Function to get the most specific level 4 parent for a given CPC code
def get_most_specific_level_4_parent(cpc_code, level_4_symbols_set):
    if not cpc_code:
        return None

    longest_match = None
    for l4_symbol in level_4_symbols_set:
        if cpc_code.startswith(l4_symbol):
            if longest_match is None or len(l4_symbol) > len(longest_match):
                longest_match = l4_symbol
    return longest_match

# Extract CPC codes and filing year, then map to actual level 4 CPC groups
cpc_filings = []
for _, row in germany_patents_2019.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date_parsed'].year
        if pd.isna(filing_year):
            continue

        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code:
                level_4_group = get_most_specific_level_4_parent(code, level_4_symbols_set)
                if level_4_group:
                    cpc_filings.append({'cpc_group': level_4_group, 'filing_year': int(filing_year)})
    except (json.JSONDecodeError, AttributeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(cpc_filings)

# Check if cpc_filings_df is empty before further processing
if cpc_filings_df.empty:
    print('__RESULT__:')
    print(json.dumps("No CPC filings found for the specified criteria."))
else:
    # Group by CPC group and filing year, then count filings
    yearly_filings = cpc_filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings')

    # Calculate Exponential Moving Average (EMA)
    alpha = 0.1
    ema_results = []
    for cpc_group in yearly_filings['cpc_group'].unique():
        group_data = yearly_filings[yearly_filings['cpc_group'] == cpc_group].sort_values(by='filing_year')
        if not group_data.empty:
            # If there's only one data point for a group, EMA will be equal to the filing count for that year.
            # The concept of 'highest exponential moving average each year' is tricky with sparse data.
            # For simplicity, if only one year exists, that year is considered the 'best'.
            group_data['ema'] = group_data['filings'].ewm(alpha=alpha, adjust=False).mean()
            ema_results.append(group_data)

    if not ema_results:
        print('__RESULT__:')
        print(json.dumps("No EMA results could be calculated."))
    else:
        ema_df = pd.concat(ema_results)

        # Find the best year for each CPC group based on the highest EMA
        if not ema_df.empty and 'cpc_group' in ema_df.columns and 'ema' in ema_df.columns:
            # Handle cases where multiple years have the same max EMA, picking the earliest year for consistency
            best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]
            
            # Merge with CPC definition (all levels) to get full title
            cpc_definition_level_4_filtered = cpc_definition_all_df[cpc_definition_all_df['level'] == 4.0]
            
            final_result = pd.merge(
                best_year_per_cpc,
                cpc_definition_level_4_filtered,
                left_on='cpc_group',
                right_on='symbol',
                how='inner'
            )

            # Select and rename columns for final output
            final_result = final_result[['titleFull', 'cpc_group', 'filing_year']].rename(columns={
                'titleFull': 'Full Title',
                'cpc_group': 'CPC Group Code',
                'filing_year': 'Best Year'
            })

            # Convert to JSON and print
            print('__RESULT__:')
            print(final_result.to_json(orient='records'))
        else:
            print('__RESULT__:')
            print(json.dumps("Could not determine best year per CPC group."))"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json', 'var_function-call-1584174934876347345': [{'cpc_group': 'A01H5', 'filing_year': 2017}, {'cpc_group': 'A01H6', 'filing_year': 2017}, {'cpc_group': 'A23L1', 'filing_year': 2017}, {'cpc_group': 'A47C1', 'filing_year': 2016}, {'cpc_group': 'A47C7', 'filing_year': 2016}, {'cpc_group': 'A61B1', 'filing_year': 2018}, {'cpc_group': 'A61B2', 'filing_year': 2016}, {'cpc_group': 'A61B9', 'filing_year': 2016}, {'cpc_group': 'A61G5', 'filing_year': 2016}, {'cpc_group': 'A61K3', 'filing_year': 2018}, {'cpc_group': 'A61K4', 'filing_year': 2018}, {'cpc_group': 'A61K8', 'filing_year': 2018}, {'cpc_group': 'A61K9', 'filing_year': 2018}, {'cpc_group': 'A61L2', 'filing_year': 2016}, {'cpc_group': 'A61M1', 'filing_year': 2015}, {'cpc_group': 'A61M2', 'filing_year': 2015}, {'cpc_group': 'A61P1', 'filing_year': 2018}, {'cpc_group': 'B23Q1', 'filing_year': 2018}, {'cpc_group': 'B29C3', 'filing_year': 2018}, {'cpc_group': 'B33Y8', 'filing_year': 2018}, {'cpc_group': 'B42D2', 'filing_year': 2017}, {'cpc_group': 'B60K2', 'filing_year': 2017}, {'cpc_group': 'B60K3', 'filing_year': 2017}, {'cpc_group': 'B60N2', 'filing_year': 2009}, {'cpc_group': 'B60R1', 'filing_year': 2017}, {'cpc_group': 'B60R2', 'filing_year': 2018}, {'cpc_group': 'B60Y2', 'filing_year': 2018}, {'cpc_group': 'B62B1', 'filing_year': 2018}, {'cpc_group': 'B62B3', 'filing_year': 2018}, {'cpc_group': 'B62B5', 'filing_year': 2018}, {'cpc_group': 'B64D1', 'filing_year': 2018}, {'cpc_group': 'C09K5', 'filing_year': 2014}, {'cpc_group': 'C12Q1', 'filing_year': 2017}, {'cpc_group': 'C12Q2', 'filing_year': 2017}, {'cpc_group': 'C23F1', 'filing_year': 2014}, {'cpc_group': 'E05F1', 'filing_year': 2018}, {'cpc_group': 'E05Y2', 'filing_year': 2018}, {'cpc_group': 'F02D2', 'filing_year': 2017}, {'cpc_group': 'F02D3', 'filing_year': 2017}, {'cpc_group': 'F02D4', 'filing_year': 2010}, {'cpc_group': 'F02M6', 'filing_year': 2010}, {'cpc_group': 'F16K1', 'filing_year': 2017}, {'cpc_group': 'F16K3', 'filing_year': 2017}, {'cpc_group': 'F17C1', 'filing_year': 2017}, {'cpc_group': 'F17C2', 'filing_year': 2017}, {'cpc_group': 'F21S8', 'filing_year': 2018}, {'cpc_group': 'F21V1', 'filing_year': 2018}, {'cpc_group': 'F21Y2', 'filing_year': 2018}, {'cpc_group': 'F41G3', 'filing_year': 2018}, {'cpc_group': 'F41H1', 'filing_year': 2018}, {'cpc_group': 'G01F2', 'filing_year': 2008}, {'cpc_group': 'G01L2', 'filing_year': 2017}, {'cpc_group': 'G01N2', 'filing_year': 2016}, {'cpc_group': 'G01S1', 'filing_year': 2018}, {'cpc_group': 'G01S5', 'filing_year': 2018}, {'cpc_group': 'G02B2', 'filing_year': 2018}, {'cpc_group': 'G02B5', 'filing_year': 2018}, {'cpc_group': 'G05D7', 'filing_year': 2017}, {'cpc_group': 'G06F2', 'filing_year': 2017}, {'cpc_group': 'G06F3', 'filing_year': 2017}, {'cpc_group': 'G06F8', 'filing_year': 2017}, {'cpc_group': 'G06F9', 'filing_year': 2017}, {'cpc_group': 'G06T1', 'filing_year': 2017}, {'cpc_group': 'H01R1', 'filing_year': 2018}, {'cpc_group': 'H01R2', 'filing_year': 2018}, {'cpc_group': 'H01R3', 'filing_year': 2018}, {'cpc_group': 'H02J1', 'filing_year': 2009}, {'cpc_group': 'H02J7', 'filing_year': 2009}, {'cpc_group': 'Y02B7', 'filing_year': 2019}, {'cpc_group': 'Y02B9', 'filing_year': 2019}, {'cpc_group': 'Y02E6', 'filing_year': 2018}, {'cpc_group': 'Y02P2', 'filing_year': 2019}, {'cpc_group': 'Y02T1', 'filing_year': 2017}, {'cpc_group': 'Y04S2', 'filing_year': 2019}, {'cpc_group': 'Y04S4', 'filing_year': 2019}], 'var_function-call-1756360509441851569': 'file_storage/function-call-1756360509441851569.json', 'var_function-call-14836008448129627989': [], 'var_function-call-10295012344133101524': [{'symbol': 'B04', 'level': '4.0'}, {'symbol': 'B23', 'level': '4.0'}, {'symbol': 'B30', 'level': '4.0'}, {'symbol': 'B99', 'level': '4.0'}, {'symbol': 'B29', 'level': '4.0'}, {'symbol': 'B33', 'level': '4.0'}, {'symbol': 'F28', 'level': '4.0'}, {'symbol': 'F25', 'level': '4.0'}, {'symbol': 'G05', 'level': '4.0'}, {'symbol': 'G12', 'level': '4.0'}, {'symbol': 'G21', 'level': '4.0'}, {'symbol': 'G09', 'level': '4.0'}, {'symbol': 'G04', 'level': '4.0'}, {'symbol': 'G11', 'level': '4.0'}, {'symbol': 'G06', 'level': '4.0'}, {'symbol': 'G03', 'level': '4.0'}, {'symbol': 'G08', 'level': '4.0'}, {'symbol': 'G99', 'level': '4.0'}, {'symbol': 'G16', 'level': '4.0'}, {'symbol': 'G10', 'level': '4.0'}, {'symbol': 'G02', 'level': '4.0'}, {'symbol': 'G01', 'level': '4.0'}, {'symbol': 'G07', 'level': '4.0'}, {'symbol': 'H03', 'level': '4.0'}, {'symbol': 'H05', 'level': '4.0'}, {'symbol': 'H04', 'level': '4.0'}, {'symbol': 'H01', 'level': '4.0'}, {'symbol': 'H02', 'level': '4.0'}, {'symbol': 'H10', 'level': '4.0'}, {'symbol': 'H99', 'level': '4.0'}, {'symbol': 'Y02', 'level': '4.0'}, {'symbol': 'Y10', 'level': '4.0'}, {'symbol': 'Y04', 'level': '4.0'}, {'symbol': 'B21', 'level': '4.0'}, {'symbol': 'B25', 'level': '4.0'}, {'symbol': 'C22', 'level': '4.0'}, {'symbol': 'D99', 'level': '4.0'}, {'symbol': 'A45', 'level': '4.0'}, {'symbol': 'A24', 'level': '4.0'}, {'symbol': 'A61', 'level': '4.0'}, {'symbol': 'A63', 'level': '4.0'}, {'symbol': 'A22', 'level': '4.0'}, {'symbol': 'A42', 'level': '4.0'}, {'symbol': 'A99', 'level': '4.0'}, {'symbol': 'A43', 'level': '4.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A62', 'level': '4.0'}, {'symbol': 'A23', 'level': '4.0'}, {'symbol': 'A47', 'level': '4.0'}, {'symbol': 'A46', 'level': '4.0'}, {'symbol': 'A44', 'level': '4.0'}, {'symbol': 'A21', 'level': '4.0'}, {'symbol': 'A41', 'level': '4.0'}, {'symbol': 'B27', 'level': '4.0'}, {'symbol': 'B68', 'level': '4.0'}, {'symbol': 'B31', 'level': '4.0'}, {'symbol': 'B26', 'level': '4.0'}, {'symbol': 'B66', 'level': '4.0'}, {'symbol': 'B02', 'level': '4.0'}, {'symbol': 'B65', 'level': '4.0'}, {'symbol': 'B61', 'level': '4.0'}, {'symbol': 'B24', 'level': '4.0'}, {'symbol': 'B06', 'level': '4.0'}, {'symbol': 'B43', 'level': '4.0'}, {'symbol': 'B62', 'level': '4.0'}, {'symbol': 'B64', 'level': '4.0'}, {'symbol': 'B22', 'level': '4.0'}, {'symbol': 'B28', 'level': '4.0'}, {'symbol': 'B09', 'level': '4.0'}, {'symbol': 'B01', 'level': '4.0'}, {'symbol': 'B63', 'level': '4.0'}, {'symbol': 'B60', 'level': '4.0'}, {'symbol': 'B44', 'level': '4.0'}, {'symbol': 'B07', 'level': '4.0'}, {'symbol': 'B08', 'level': '4.0'}, {'symbol': 'B82', 'level': '4.0'}, {'symbol': 'B42', 'level': '4.0'}, {'symbol': 'B32', 'level': '4.0'}, {'symbol': 'B81', 'level': '4.0'}, {'symbol': 'B05', 'level': '4.0'}, {'symbol': 'B41', 'level': '4.0'}, {'symbol': 'B03', 'level': '4.0'}, {'symbol': 'B67', 'level': '4.0'}, {'symbol': 'C23', 'level': '4.0'}, {'symbol': 'C06', 'level': '4.0'}, {'symbol': 'C02', 'level': '4.0'}, {'symbol': 'C07', 'level': '4.0'}, {'symbol': 'C25', 'level': '4.0'}, {'symbol': 'C30', 'level': '4.0'}, {'symbol': 'C12', 'level': '4.0'}, {'symbol': 'C99', 'level': '4.0'}, {'symbol': 'C05', 'level': '4.0'}, {'symbol': 'C40', 'level': '4.0'}, {'symbol': 'C11', 'level': '4.0'}, {'symbol': 'C08', 'level': '4.0'}, {'symbol': 'C10', 'level': '4.0'}, {'symbol': 'C21', 'level': '4.0'}, {'symbol': 'C04', 'level': '4.0'}, {'symbol': 'C09', 'level': '4.0'}, {'symbol': 'C03', 'level': '4.0'}, {'symbol': 'C13', 'level': '4.0'}, {'symbol': 'C14', 'level': '4.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'D02', 'level': '4.0'}, {'symbol': 'D21', 'level': '4.0'}, {'symbol': 'D04', 'level': '4.0'}, {'symbol': 'D07', 'level': '4.0'}, {'symbol': 'D01', 'level': '4.0'}, {'symbol': 'D10', 'level': '4.0'}, {'symbol': 'D06', 'level': '4.0'}, {'symbol': 'D03', 'level': '4.0'}, {'symbol': 'D05', 'level': '4.0'}, {'symbol': 'E05', 'level': '4.0'}, {'symbol': 'E21', 'level': '4.0'}, {'symbol': 'E04', 'level': '4.0'}, {'symbol': 'E99', 'level': '4.0'}, {'symbol': 'E06', 'level': '4.0'}, {'symbol': 'E02', 'level': '4.0'}, {'symbol': 'E01', 'level': '4.0'}, {'symbol': 'E03', 'level': '4.0'}, {'symbol': 'F41', 'level': '4.0'}, {'symbol': 'F01', 'level': '4.0'}, {'symbol': 'F22', 'level': '4.0'}, {'symbol': 'F26', 'level': '4.0'}, {'symbol': 'F04', 'level': '4.0'}, {'symbol': 'F16', 'level': '4.0'}, {'symbol': 'F05', 'level': '4.0'}, {'symbol': 'F42', 'level': '4.0'}, {'symbol': 'F03', 'level': '4.0'}, {'symbol': 'F02', 'level': '4.0'}, {'symbol': 'F23', 'level': '4.0'}, {'symbol': 'F27', 'level': '4.0'}, {'symbol': 'F24', 'level': '4.0'}, {'symbol': 'F21', 'level': '4.0'}, {'symbol': 'F99', 'level': '4.0'}, {'symbol': 'F15', 'level': '4.0'}, {'symbol': 'F17', 'level': '4.0'}], 'var_function-call-5514630318995129550': [], 'var_function-call-6093804149096176201': [], 'var_function-call-17240091598940257019': [], 'var_function-call-11612361122900825043': {'num_germany_patents_2019': 2}}

exec(code, env_args)
