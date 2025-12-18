code = """import pandas as pd
import json
import io

# Load the full publication data
with open(locals()['var_function-call-9247441433640274170'], 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Convert date columns to datetime objects, coercing errors
df['grant_date_parsed'] = pd.to_datetime(df['grant_date'].str.replace('st|nd|rd|th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')
df['filing_date_parsed'] = pd.to_datetime(df['filing_date'].str.replace('st|nd|rd|th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')

# Filter for patents granted in Germany and in the second half of 2019
germany_patents_2019 = df[
    df['Patents_info'].str.contains('Germany|DE', na=False) &
    (df['grant_date_parsed'] >= '2019-07-01') &
    (df['grant_date_parsed'] <= '2019-12-31')
].copy()

# Load CPC definition data
with open(locals()['var_function-call-1756360509441851569'], 'r') as f:
    cpc_definition_raw = json.load(f)
cpc_definition_df = pd.DataFrame(cpc_definition_raw)

# Filter CPC definitions for level 4
cpc_definition_level_4 = cpc_definition_df[cpc_definition_df['level'] == 4.0].copy()

# Create a set of valid level 4 CPC symbols for efficient lookup
level_4_symbols = set(cpc_definition_level_4['symbol'].unique())

# Function to extract the level 4 CPC group
def get_level_4_cpc_group(cpc_code, level_4_symbols_set):
    # A level 4 CPC code typically has the format XNNXN/XX
    # Iterate through prefixes to find the longest matching level 4 symbol
    current_best_match = None
    for symbol in level_4_symbols_set:
        if cpc_code.startswith(symbol):
            if current_best_match is None or len(symbol) > len(current_best_match):
                current_best_match = symbol
    return current_best_match

# Extract CPC codes and filing year, then map to level 4 CPC groups
cpc_filings = []
for _, row in germany_patents_2019.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date_parsed'].year
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code:
                level_4_group = get_level_4_cpc_group(code, level_4_symbols)
                if level_4_group:
                    cpc_filings.append({'cpc_group': level_4_group, 'filing_year': filing_year})
    except (json.JSONDecodeError, AttributeError):
        continue

cpc_filings_df = pd.DataFrame(cpc_filings)
cpc_filings_df = cpc_filings_df.dropna(subset=['filing_year'])
cpc_filings_df['filing_year'] = cpc_filings_df['filing_year'].astype(int)

# Group by CPC group and filing year, then count filings
yearly_filings = cpc_filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []
for cpc_group in yearly_filings['cpc_group'].unique():
    group_data = yearly_filings[yearly_filings['cpc_group'] == cpc_group].sort_values(by='filing_year')
    if not group_data.empty:
        group_data['ema'] = group_data['filings'].ewm(alpha=alpha, adjust=False).mean()
        ema_results.append(group_data)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group based on the highest EMA
best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Merge with CPC definition to get full title
final_result = pd.merge(
    best_year_per_cpc,
    cpc_definition_level_4,
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
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json', 'var_function-call-1584174934876347345': [{'cpc_group': 'A01H5', 'filing_year': 2017}, {'cpc_group': 'A01H6', 'filing_year': 2017}, {'cpc_group': 'A23L1', 'filing_year': 2017}, {'cpc_group': 'A47C1', 'filing_year': 2016}, {'cpc_group': 'A47C7', 'filing_year': 2016}, {'cpc_group': 'A61B1', 'filing_year': 2018}, {'cpc_group': 'A61B2', 'filing_year': 2016}, {'cpc_group': 'A61B9', 'filing_year': 2016}, {'cpc_group': 'A61G5', 'filing_year': 2016}, {'cpc_group': 'A61K3', 'filing_year': 2018}, {'cpc_group': 'A61K4', 'filing_year': 2018}, {'cpc_group': 'A61K8', 'filing_year': 2018}, {'cpc_group': 'A61K9', 'filing_year': 2018}, {'cpc_group': 'A61L2', 'filing_year': 2016}, {'cpc_group': 'A61M1', 'filing_year': 2015}, {'cpc_group': 'A61M2', 'filing_year': 2015}, {'cpc_group': 'A61P1', 'filing_year': 2018}, {'cpc_group': 'B23Q1', 'filing_year': 2018}, {'cpc_group': 'B29C3', 'filing_year': 2018}, {'cpc_group': 'B33Y8', 'filing_year': 2018}, {'cpc_group': 'B42D2', 'filing_year': 2017}, {'cpc_group': 'B60K2', 'filing_year': 2017}, {'cpc_group': 'B60K3', 'filing_year': 2017}, {'cpc_group': 'B60N2', 'filing_year': 2009}, {'cpc_group': 'B60R1', 'filing_year': 2017}, {'cpc_group': 'B60R2', 'filing_year': 2018}, {'cpc_group': 'B60Y2', 'filing_year': 2018}, {'cpc_group': 'B62B1', 'filing_year': 2018}, {'cpc_group': 'B62B3', 'filing_year': 2018}, {'cpc_group': 'B62B5', 'filing_year': 2018}, {'cpc_group': 'B64D1', 'filing_year': 2018}, {'cpc_group': 'C09K5', 'filing_year': 2014}, {'cpc_group': 'C12Q1', 'filing_year': 2017}, {'cpc_group': 'C12Q2', 'filing_year': 2017}, {'cpc_group': 'C23F1', 'filing_year': 2014}, {'cpc_group': 'E05F1', 'filing_year': 2018}, {'cpc_group': 'E05Y2', 'filing_year': 2018}, {'cpc_group': 'F02D2', 'filing_year': 2017}, {'cpc_group': 'F02D3', 'filing_year': 2017}, {'cpc_group': 'F02D4', 'filing_year': 2010}, {'cpc_group': 'F02M6', 'filing_year': 2010}, {'cpc_group': 'F16K1', 'filing_year': 2017}, {'cpc_group': 'F16K3', 'filing_year': 2017}, {'cpc_group': 'F17C1', 'filing_year': 2017}, {'cpc_group': 'F17C2', 'filing_year': 2017}, {'cpc_group': 'F21S8', 'filing_year': 2018}, {'cpc_group': 'F21V1', 'filing_year': 2018}, {'cpc_group': 'F21Y2', 'filing_year': 2018}, {'cpc_group': 'F41G3', 'filing_year': 2018}, {'cpc_group': 'F41H1', 'filing_year': 2018}, {'cpc_group': 'G01F2', 'filing_year': 2008}, {'cpc_group': 'G01L2', 'filing_year': 2017}, {'cpc_group': 'G01N2', 'filing_year': 2016}, {'cpc_group': 'G01S1', 'filing_year': 2018}, {'cpc_group': 'G01S5', 'filing_year': 2018}, {'cpc_group': 'G02B2', 'filing_year': 2018}, {'cpc_group': 'G02B5', 'filing_year': 2018}, {'cpc_group': 'G05D7', 'filing_year': 2017}, {'cpc_group': 'G06F2', 'filing_year': 2017}, {'cpc_group': 'G06F3', 'filing_year': 2017}, {'cpc_group': 'G06F8', 'filing_year': 2017}, {'cpc_group': 'G06F9', 'filing_year': 2017}, {'cpc_group': 'G06T1', 'filing_year': 2017}, {'cpc_group': 'H01R1', 'filing_year': 2018}, {'cpc_group': 'H01R2', 'filing_year': 2018}, {'cpc_group': 'H01R3', 'filing_year': 2018}, {'cpc_group': 'H02J1', 'filing_year': 2009}, {'cpc_group': 'H02J7', 'filing_year': 2009}, {'cpc_group': 'Y02B7', 'filing_year': 2019}, {'cpc_group': 'Y02B9', 'filing_year': 2019}, {'cpc_group': 'Y02E6', 'filing_year': 2018}, {'cpc_group': 'Y02P2', 'filing_year': 2019}, {'cpc_group': 'Y02T1', 'filing_year': 2017}, {'cpc_group': 'Y04S2', 'filing_year': 2019}, {'cpc_group': 'Y04S4', 'filing_year': 2019}], 'var_function-call-1756360509441851569': 'file_storage/function-call-1756360509441851569.json', 'var_function-call-14836008448129627989': []}

exec(code, env_args)
