code = """import re, json

# Load full funding table from file path
import pandas as pd
from pathlib import Path

funding_path = Path(var_call_jZxzEsy3eEdNy5m4EL0AJuxD)
funding_df = pd.read_json(funding_path)

# Filter projects related to 'emergency' or 'FEMA' in the Project_Name (case-insensitive)
mask = funding_df['Project_Name'].str.contains('emergency', case=False, na=False) | funding_df['Project_Name'].str.contains('FEMA', case=False, na=False)
filtered = funding_df.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

result = filtered.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jZxzEsy3eEdNy5m4EL0AJuxD': 'file_storage/call_jZxzEsy3eEdNy5m4EL0AJuxD.json', 'var_call_oHYyDA5Gb8B8Rtgh08LNpiyW': 'file_storage/call_oHYyDA5Gb8B8Rtgh08LNpiyW.json'}

exec(code, env_args)
