code = """import json, pandas as pd

with open(var_call_sNebHVFA58PyIoie8pT1LswA, 'r') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])

# Disaster-type projects via FEMA/CalOES/CalJPIA in name
disaster_mask = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)

disaster_funding = fund_df[disaster_mask].copy()

# Without reliable start dates from civic docs, approximate 2022 starts
# as those projects whose name includes '2022'
mask_2022_name = disaster_funding['Project_Name'].str.contains('2022', case=False, regex=False)

fund_2022_disaster = disaster_funding[mask_2022_name]

total_2022_disaster = float(fund_2022_disaster['Amount'].sum())

out = json.dumps(total_2022_disaster)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_regjihqD0YcOz2LaOk1w5e8Z': 'file_storage/call_regjihqD0YcOz2LaOk1w5e8Z.json', 'var_call_sNebHVFA58PyIoie8pT1LswA': 'file_storage/call_sNebHVFA58PyIoie8pT1LswA.json'}

exec(code, env_args)
