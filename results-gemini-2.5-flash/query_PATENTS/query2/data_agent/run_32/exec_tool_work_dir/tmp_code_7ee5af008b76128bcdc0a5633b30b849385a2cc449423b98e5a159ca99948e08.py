code = """import pandas as pd
import json
import io

# The result from var_function-call-1584174934876347345 is a list of dictionaries.
# It needs to be converted to a JSON string before passing to pd.read_json.
best_year_cpc_data_str = json.dumps(locals()['var_function-call-1584174934876347345'])
best_year_cpc_df = pd.read_json(io.StringIO(best_year_cpc_data_str))

# Load the CPC definition data from the file path
with open(locals()['var_function-call-1756360509441851569'], 'r') as f:
    cpc_definition_raw = json.load(f)
cpc_definition_df = pd.DataFrame(cpc_definition_raw)

# Filter CPC definitions for level 4
cpc_definition_level_4 = cpc_definition_df[cpc_definition_df['level'] == 4.0].copy()

# Merge the dataframes to get the full title
merged_df = pd.merge(
    best_year_cpc_df,
    cpc_definition_level_4,
    left_on='cpc_group',
    right_on='symbol',
    how='inner'
)

# Select and rename columns for final output
final_result = merged_df[['titleFull', 'cpc_group', 'filing_year']].rename(columns={
    'titleFull': 'Full Title',
    'cpc_group': 'CPC Group Code',
    'filing_year': 'Best Year'
})

# Convert to JSON and print
print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json', 'var_function-call-1584174934876347345': [{'cpc_group': 'A01H5', 'filing_year': 2017}, {'cpc_group': 'A01H6', 'filing_year': 2017}, {'cpc_group': 'A23L1', 'filing_year': 2017}, {'cpc_group': 'A47C1', 'filing_year': 2016}, {'cpc_group': 'A47C7', 'filing_year': 2016}, {'cpc_group': 'A61B1', 'filing_year': 2018}, {'cpc_group': 'A61B2', 'filing_year': 2016}, {'cpc_group': 'A61B9', 'filing_year': 2016}, {'cpc_group': 'A61G5', 'filing_year': 2016}, {'cpc_group': 'A61K3', 'filing_year': 2018}, {'cpc_group': 'A61K4', 'filing_year': 2018}, {'cpc_group': 'A61K8', 'filing_year': 2018}, {'cpc_group': 'A61K9', 'filing_year': 2018}, {'cpc_group': 'A61L2', 'filing_year': 2016}, {'cpc_group': 'A61M1', 'filing_year': 2015}, {'cpc_group': 'A61M2', 'filing_year': 2015}, {'cpc_group': 'A61P1', 'filing_year': 2018}, {'cpc_group': 'B23Q1', 'filing_year': 2018}, {'cpc_group': 'B29C3', 'filing_year': 2018}, {'cpc_group': 'B33Y8', 'filing_year': 2018}, {'cpc_group': 'B42D2', 'filing_year': 2017}, {'cpc_group': 'B60K2', 'filing_year': 2017}, {'cpc_group': 'B60K3', 'filing_year': 2017}, {'cpc_group': 'B60N2', 'filing_year': 2009}, {'cpc_group': 'B60R1', 'filing_year': 2017}, {'cpc_group': 'B60R2', 'filing_year': 2018}, {'cpc_group': 'B60Y2', 'filing_year': 2018}, {'cpc_group': 'B62B1', 'filing_year': 2018}, {'cpc_group': 'B62B3', 'filing_year': 2018}, {'cpc_group': 'B62B5', 'filing_year': 2018}, {'cpc_group': 'B64D1', 'filing_year': 2018}, {'cpc_group': 'C09K5', 'filing_year': 2014}, {'cpc_group': 'C12Q1', 'filing_year': 2017}, {'cpc_group': 'C12Q2', 'filing_year': 2017}, {'cpc_group': 'C23F1', 'filing_year': 2014}, {'cpc_group': 'E05F1', 'filing_year': 2018}, {'cpc_group': 'E05Y2', 'filing_year': 2018}, {'cpc_group': 'F02D2', 'filing_year': 2017}, {'cpc_group': 'F02D3', 'filing_year': 2017}, {'cpc_group': 'F02D4', 'filing_year': 2010}, {'cpc_group': 'F02M6', 'filing_year': 2010}, {'cpc_group': 'F16K1', 'filing_year': 2017}, {'cpc_group': 'F16K3', 'filing_year': 2017}, {'cpc_group': 'F17C1', 'filing_year': 2017}, {'cpc_group': 'F17C2', 'filing_year': 2017}, {'cpc_group': 'F21S8', 'filing_year': 2018}, {'cpc_group': 'F21V1', 'filing_year': 2018}, {'cpc_group': 'F21Y2', 'filing_year': 2018}, {'cpc_group': 'F41G3', 'filing_year': 2018}, {'cpc_group': 'F41H1', 'filing_year': 2018}, {'cpc_group': 'G01F2', 'filing_year': 2008}, {'cpc_group': 'G01L2', 'filing_year': 2017}, {'cpc_group': 'G01N2', 'filing_year': 2016}, {'cpc_group': 'G01S1', 'filing_year': 2018}, {'cpc_group': 'G01S5', 'filing_year': 2018}, {'cpc_group': 'G02B2', 'filing_year': 2018}, {'cpc_group': 'G02B5', 'filing_year': 2018}, {'cpc_group': 'G05D7', 'filing_year': 2017}, {'cpc_group': 'G06F2', 'filing_year': 2017}, {'cpc_group': 'G06F3', 'filing_year': 2017}, {'cpc_group': 'G06F8', 'filing_year': 2017}, {'cpc_group': 'G06F9', 'filing_year': 2017}, {'cpc_group': 'G06T1', 'filing_year': 2017}, {'cpc_group': 'H01R1', 'filing_year': 2018}, {'cpc_group': 'H01R2', 'filing_year': 2018}, {'cpc_group': 'H01R3', 'filing_year': 2018}, {'cpc_group': 'H02J1', 'filing_year': 2009}, {'cpc_group': 'H02J7', 'filing_year': 2009}, {'cpc_group': 'Y02B7', 'filing_year': 2019}, {'cpc_group': 'Y02B9', 'filing_year': 2019}, {'cpc_group': 'Y02E6', 'filing_year': 2018}, {'cpc_group': 'Y02P2', 'filing_year': 2019}, {'cpc_group': 'Y02T1', 'filing_year': 2017}, {'cpc_group': 'Y04S2', 'filing_year': 2019}, {'cpc_group': 'Y04S4', 'filing_year': 2019}], 'var_function-call-1756360509441851569': 'file_storage/function-call-1756360509441851569.json'}

exec(code, env_args)
