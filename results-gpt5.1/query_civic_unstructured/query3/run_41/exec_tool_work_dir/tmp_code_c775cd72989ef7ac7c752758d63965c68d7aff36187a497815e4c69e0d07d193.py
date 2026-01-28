code = """import json, pandas as pd
from pathlib import Path

funding_records = json.loads(Path(var_call_INJPNSIiOrkvaUryVQc2KpPo).read_text())

funding_df = pd.DataFrame(funding_records)
mask = funding_df['Project_Name'].str.contains('FEMA', case=False) | funding_df['Project_Name'].str.contains('emergency', case=False)
result_df = funding_df.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_INJPNSIiOrkvaUryVQc2KpPo': 'file_storage/call_INJPNSIiOrkvaUryVQc2KpPo.json', 'var_call_dmYcMEoaddRjV82TTDl9Y4Tp': 'file_storage/call_dmYcMEoaddRjV82TTDl9Y4Tp.json'}

exec(code, env_args)
