code = """import json
import os

# Check if var_functions.query_db:2 is a string (file path) and read the file
if isinstance(var_functions.query_db:2, str):
    with open(var_functions.query_db:2, 'r') as f:
        data = json.load(f)
else:
    data = var_functions.query_db:2

# Convert to DataFrame
df = pd.DataFrame(data)

# Show basic info about the data
print(f"Total records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("Sample grant_date values:")
print(df['grant_date'].head(10).tolist())

# Check for Germany-related records
print("\nContains DE records:")
print(df['Patents_info'].str.contains('DE-').sum())

# Check grant date format in 2019
print("\nGrant dates in 2019:")
df_2019 = df[df['grant_date'].str.contains('2019')]
print(f"Total 2019 records: {len(df_2019)}")
print(df_2019['grant_date'].head(15).tolist())

# Filter for Germany patents
print("\nGermany patents in 2019:")
de_2019 = df[(df['Patents_info'].str.contains('DE-')) & (df['grant_date'].str.contains('2019'))]
print(f"Total DE 2019 records: {len(de_2019)}")
print(de_2019['grant_date'].head(15).tolist())

result_str = json.dumps({
    "total_records": len(df),
    "germany_2019_records": len(de_2019),
    "sample_grant_dates": de_2019['grant_date'].head(5).tolist() if len(de_2019) > 0 else []
})
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
