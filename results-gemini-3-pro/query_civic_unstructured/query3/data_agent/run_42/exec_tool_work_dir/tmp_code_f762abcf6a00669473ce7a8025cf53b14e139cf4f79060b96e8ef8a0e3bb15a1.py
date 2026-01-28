code = """import json
import pandas as pd

# Load the previous results
result_file_path = locals()['var_function-call-1982793532978862857']
with open(result_file_path, 'r') as f:
    raw_results = json.load(f)

df = pd.DataFrame(raw_results)

# Deduplicate
# Logic: If multiple entries for same Project_Name, pick the one with "highest" status?
# Hierarchy: completed > construction > design > not started > unknown
status_rank = {
    'completed': 5,
    'construction': 4,
    'design': 3,
    'not started': 2,
    'unknown': 1
}

def get_rank(status):
    return status_rank.get(status.lower(), 0)

# Sort by Project Name and Rank descending
df['rank'] = df['Status'].apply(get_rank)
df = df.sort_values(by=['Project_Name', 'rank'], ascending=[True, False])

# Drop duplicates, keeping first (highest rank)
df_unique = df.drop_duplicates(subset=['Project_Name'], keep='first')

# Select columns
final_df = df_unique[['Project_Name', 'Funding_Source', 'Amount', 'Status']]

# Convert to list of dicts
final_records = final_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_records, indent=2))"""

env_args = {'var_function-call-7580785904433881642': ['Funding'], 'var_function-call-7580785904433881717': ['civic_docs'], 'var_function-call-15139260812561284578': 'file_storage/function-call-15139260812561284578.json', 'var_function-call-15139260812561285023': 'file_storage/function-call-15139260812561285023.json', 'var_function-call-12991954254927401902': 'file_storage/function-call-12991954254927401902.json', 'var_function-call-1982793532978862857': 'file_storage/function-call-1982793532978862857.json'}

exec(code, env_args)
