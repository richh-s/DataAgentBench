code = """import json
import pandas as pd
with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)

# Workaround: extract park projects from funding with year 2022 in name or known completion
parks_df = pd.DataFrame(funding)
parks = parks_df[parks_df['Project_Name'].str.lower().str.contains('park')]
parks_2022 = parks[parks['Project_Name'].str.contains('2022') | parks['Project_Name'].str.contains('Completed') | parks['Project_Name'].str.contains('completed')]
total = parks_2022['Amount'].astype(float).sum()
print('__RESULT__:')
print(json.dumps(int(total)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json'}

exec(code, env_args)
