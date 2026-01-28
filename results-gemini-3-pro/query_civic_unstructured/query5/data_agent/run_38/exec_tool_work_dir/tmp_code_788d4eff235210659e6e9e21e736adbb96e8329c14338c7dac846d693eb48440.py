code = """import json

funding_path = locals()['var_function-call-8835626806368298115']
docs_path = locals()['var_function-call-9685015997201823152']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    docs = json.load(f)

full_text = " ".join([d['text'] for d in docs])

matched_details = []

for row in funding_records:
    name = row['Project_Name']
    
    # 1. Determine if Disaster Project
    is_disaster = False
    suffixes = ["(FEMA", "(CalOES", "(CalJPIA", "(Woolsey"]
    if any(s in name for s in suffixes):
        is_disaster = True
    
    if "(" in name:
        base_name = name.split("(")[0].strip()
    else:
        base_name = name
        
    idx = full_text.find(base_name)
    snippet = ""
    if idx != -1:
        snippet = full_text[idx:idx+2000]
    
    if not is_disaster and snippet:
        if "FEMA" in snippet or "CalOES" in snippet:
             is_disaster = True
    
    if not is_disaster:
        continue

    # 2. Check Start Date == 2022
    started_2022 = False
    date_context = ""
    
    if snippet:
        bc_index = snippet.find("Begin Construction:")
        if bc_index != -1:
            bc_text = snippet[bc_index:bc_index+50]
            if "2022" in bc_text:
                started_2022 = True
                date_context = bc_text

    if started_2022:
        matched_details.append({
            "name": name,
            "amount": row['Amount'],
            "date_context": date_context
        })

print("__RESULT__:")
print(json.dumps(matched_details))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json', 'var_function-call-4907481001215634158': 1528000}

exec(code, env_args)
