code = """import json

# Load Funding Data
with open(locals()['var_function-call-8835626806368298115'], 'r') as f:
    funding_data = json.load(f)

funding_names = set(item['Project_Name'] for item in funding_data)

# Load Civic Docs
with open(locals()['var_function-call-9685015997201823152'], 'r') as f:
    civic_docs = json.load(f)

# Combine text
all_text = ""
for doc in civic_docs:
    all_text += doc['text'] + "\n"

# Check for presence
found_names = []
missing_names = []
# Focus on names that look like disaster projects
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey"]
potential_disaster_names = [n for n in funding_names if any(k in n for k in disaster_keywords)]

for name in potential_disaster_names:
    if name in all_text:
        found_names.append(name)
    else:
        missing_names.append(name)

print(f"Total Potential Disaster Names: {len(potential_disaster_names)}")
print(f"Found in Text: {len(found_names)}")
print(f"Missing from Text: {len(missing_names)}")

print("__RESULT__:")
print(json.dumps({
    "found_sample": found_names[:5],
    "missing_sample": missing_names[:5]
}))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json'}

exec(code, env_args)
