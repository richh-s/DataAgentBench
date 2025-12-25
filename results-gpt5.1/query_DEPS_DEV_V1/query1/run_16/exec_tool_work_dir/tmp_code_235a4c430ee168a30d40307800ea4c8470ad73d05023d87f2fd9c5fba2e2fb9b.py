code = """import json, pandas as pd
path = var_call_oI2fxO2SVgLQek4BLqrCane5
with open(path) as f:
    data = json.load(f)
# keep only distinct name+version
pdf = pd.DataFrame(data)[['Name','Version']].drop_duplicates()
# we'll join via SQL later, so just output list
result = pdf.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_oI2fxO2SVgLQek4BLqrCane5': 'file_storage/call_oI2fxO2SVgLQek4BLqrCane5.json', 'var_call_73ET6tvJslEdK0g8sLNlfPhw': ['project_info', 'project_packageversion'], 'var_call_sTcoScalzsWttHqq4nlNf1zW': 'file_storage/call_sTcoScalzsWttHqq4nlNf1zW.json'}

exec(code, env_args)
