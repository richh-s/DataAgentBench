code = """import json, pandas as pd

funding_records = var_call_TrTbkuE4mQWE5DgrbFTkIZUF

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

result_count = int((funding_df['Amount'] > 50000).sum())

out = json.dumps({'count': result_count})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TrTbkuE4mQWE5DgrbFTkIZUF': 'file_storage/call_TrTbkuE4mQWE5DgrbFTkIZUF.json', 'var_call_LxmJvzaILhIL32F5HGpYfuiz': 'file_storage/call_LxmJvzaILhIL32F5HGpYfuiz.json'}

exec(code, env_args)
