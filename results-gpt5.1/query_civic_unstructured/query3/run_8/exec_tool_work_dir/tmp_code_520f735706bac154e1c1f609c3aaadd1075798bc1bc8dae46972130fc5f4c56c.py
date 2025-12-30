code = """import re, json
from pathlib import Path

# Load full funding data
path_funding = Path(var_call_LKQAIvBa9vRkHFMGJ6ebMkVD)
import pandas as pd
funding_df = pd.read_json(path_funding)

# Filter projects with 'FEMA' or 'emergency' in the project name (case-insensitive)
mask = funding_df['Project_Name'].str.contains('FEMA', case=False, na=False) | funding_df['Project_Name'].str.contains('emergency', case=False, na=False)
rel_funding = funding_df[mask][['Project_Name','Funding_Source','Amount']]

result = rel_funding.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LKQAIvBa9vRkHFMGJ6ebMkVD': 'file_storage/call_LKQAIvBa9vRkHFMGJ6ebMkVD.json', 'var_call_YQXd9vbJuoT2RIvG4K2Ls4iP': 'file_storage/call_YQXd9vbJuoT2RIvG4K2Ls4iP.json'}

exec(code, env_args)
