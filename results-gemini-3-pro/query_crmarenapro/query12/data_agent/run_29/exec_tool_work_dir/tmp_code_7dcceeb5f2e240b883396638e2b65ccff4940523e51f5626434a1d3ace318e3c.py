code = """import pandas as pd
import json

# Get file paths from storage
path_opp = locals()['var_function-call-8541669410738994321']
path_cont = locals()['var_function-call-8541669410738991182']

# Load data
with open(path_opp, 'r') as f:
    opps = json.load(f)
with open(path_cont, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

df_opp['ContractID__c_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

# Filter Contracts for April 2023
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
df_cont_april = df_cont[
    (df_cont['CompanySignedDate'] >= '2023-04-01') & 
    (df_cont['CompanySignedDate'] <= '2023-04-30')
]

# Join
merged = pd.merge(df_opp, df_cont_april, left_on='ContractID__c_clean', right_on='Id_clean', how='inner')

# Calculate cycle
# CreatedDate format like "2023-08-14T10:30:00.000+0000"
# We need to make it tz-naive or tz-aware matching CompanySignedDate (which is naive usually at 00:00)
# It's better to convert CreatedDate to naive date or datetime
merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')
# Use only date part for day calculation if policy implies full days?
# "number of days between an opportunity's creation date and the company signed date"
# Usually: (SignedDate - CreatedDate).days
# But CreatedDate has time. If created on April 1st 10am and Signed April 2nd, is it 1 day or 0.something?
# Usually "number of days" in business context implies Difference in Days (integer) or float days. 
# Given "quickest average turnaround", float precision is better.
# However, CompanySignedDate is just a date (00:00:00).
# CreatedDate is 2023-08-14 10:30:00.
# If I substract: 2023-04-10 - 2023-04-09 10:00:00 = 0 days 14 hours = 0.58 days.
# If I just use date: 2023-04-10 - 2023-04-09 = 1 day.
# Let's assume precise calculation is safer, or date-based if specified. 
# Policy: "measured as the number of days between...".
# I'll calculate as `(SignedDate - CreatedDate).total_seconds() / 86400`.
# Note: Since SignedDate has no time, it defaults to midnight.
# If SignedDate is the *end* of the process, maybe it should be considered end of that day?
# But usually standard subtraction is fine. If Created is 2023-04-01 23:59 and Signed is 2023-04-02, delta is small.
# But if Created is 2023-04-01 00:01 and Signed is 2023-04-02, delta is larger.
# Let's stick to float days.
# But wait, `CompanySignedDate` is just Date. `CreatedDate` is timestamp.
# I need to handle timezone. CreatedDate has `+0000`.
# I will convert CreatedDate to timezone-naive UTC (strip tz).

merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce').dt.tz_convert(None)
merged['cycle_days'] = (merged['CompanySignedDate'] - merged['CreatedDate_dt']).dt.total_seconds() / (24 * 3600)

# Group by Agent (OwnerId)
avg_cycle = merged.groupby('OwnerId_clean')['cycle_days'].mean().reset_index()

# Find minimum
min_avg = avg_cycle.sort_values('cycle_days').head(1)

print("__RESULT__:")
print(min_avg.to_json(orient='records'))"""

env_args = {'var_function-call-7295838422035824403': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-8541669410738994321': 'file_storage/function-call-8541669410738994321.json', 'var_function-call-8541669410738991182': 'file_storage/function-call-8541669410738991182.json'}

exec(code, env_args)
