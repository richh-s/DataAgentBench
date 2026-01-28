code = """import json

funding_key = 'var_function-call-8835626806368298115'
docs_key = 'var_function-call-9685015997201823152'

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

funding_names = [item['Project_Name'] for item in funding_data]

with open(locals()[docs_key], 'r') as f:
    civic_docs = json.load(f)

# Concatenate text
full_text = ""
for d in civic_docs:
    full_text += d['text'] + "\n"

# Check existence
found = []
missing = []
for name in funding_names:
    if name in full_text:
        found.append(name)
    else:
        missing.append(name)

# focus on disaster
disaster_found = [n for n in found if "FEMA" in n or "CalOES" in n]
disaster_missing = [n for n in missing if "FEMA" in n or "CalOES" in n]

print("__RESULT__:")
print(json.dumps({
    "disaster_found": disaster_found,
    "disaster_missing_count": len(disaster_missing),
    "disaster_missing_sample": disaster_missing[:5]
}))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json'}

exec(code, env_args)
