code = """import re, json
from pathlib import Path

# Load full funding data from storage file if needed
funding_path = var_call_Y1PfJXzsOxR9adqmpxF25Rjc if isinstance(var_call_Y1PfJXzsOxR9adqmpxF25Rjc, str) else None
if funding_path and Path(funding_path).is_file():
    import pandas as pd
    funding_df = pd.read_json(funding_path)
else:
    import pandas as pd
    funding_df = pd.DataFrame(var_call_Y1PfJXzsOxR9adqmpxF25Rjc)

# Filter funding projects whose names or types suggest FEMA or emergency relevance
mask = funding_df['Project_Name'].str.contains('FEMA', case=False, na=False) | funding_df['Project_Name'].str.contains('emergency', case=False, na=False)
relevant_funding = funding_df.loc[mask, ['Project_Name','Funding_Source','Amount']]

result = relevant_funding.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Y1PfJXzsOxR9adqmpxF25Rjc': 'file_storage/call_Y1PfJXzsOxR9adqmpxF25Rjc.json', 'var_call_ih8tP0aO7OzqD4m5ZWCh0rfu': 'file_storage/call_ih8tP0aO7OzqD4m5ZWCh0rfu.json'}

exec(code, env_args)
