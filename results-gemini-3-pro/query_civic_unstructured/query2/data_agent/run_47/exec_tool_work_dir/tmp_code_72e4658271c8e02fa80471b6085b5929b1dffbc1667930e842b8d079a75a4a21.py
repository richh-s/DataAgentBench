code = """import json
import pandas as pd

with open(locals()['var_function-call-14770944468380468337'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-14241512510866870290'], 'r') as f:
    civic_docs = json.load(f)

# Find Point Dume Walkway text
target = "Point Dume Walkway Repairs"
found_text = ""

for doc in civic_docs:
    if target in doc['text']:
        # Extract context
        idx = doc['text'].find(target)
        found_text = doc['text'][idx:idx+500] 

# Find funding
funding_df = pd.DataFrame(funding_data)
row = funding_df[funding_df['Project_Name'] == target]
amount = 0
if not row.empty:
    amount = row.iloc[0]['Amount']

print("__RESULT__:")
print(json.dumps({'text_preview': found_text, 'amount': int(amount)}))"""

env_args = {'var_function-call-18374819534709684417': 'file_storage/function-call-18374819534709684417.json', 'var_function-call-14770944468380468337': 'file_storage/function-call-14770944468380468337.json', 'var_function-call-14241512510866870290': 'file_storage/function-call-14241512510866870290.json', 'var_function-call-13095277623249706244': {'matches': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'shade structures at Malibu Bluffs Park.', 'amount': 0}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}, {'name': 'shade structures at Malibu Bluffs Park.', 'amount': 0}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}], 'total': 195000}}

exec(code, env_args)
