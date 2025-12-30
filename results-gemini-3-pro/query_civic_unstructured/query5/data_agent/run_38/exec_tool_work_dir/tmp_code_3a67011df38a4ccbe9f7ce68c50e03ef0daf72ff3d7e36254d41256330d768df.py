code = """import json
import sqlite3

# Load Funding Data
with open(locals()['var_function-call-8835626806368298115'], 'r') as f:
    funding_data = json.load(f)

funding_names = set(item['Project_Name'] for item in funding_data)

# Load Civic Docs
with open(locals()['var_function-call-9685015997201823152'], 'r') as f:
    civic_docs = json.load(f)

all_text = "\n".join([doc['text'] for doc in civic_docs])

# Check for presence
found_names = []
missing_names = []
for name in funding_names:
    if name in all_text:
        found_names.append(name)
    else:
        missing_names.append(name)

print(f"Total Funding Names: {len(funding_names)}")
print(f"Found in Text: {len(found_names)}")
print(f"Missing from Text: {len(missing_names)}")

# Sample findings
print("__RESULT__:")
print(json.dumps({
    "found_sample": found_names[:10],
    "missing_sample": missing_names[:10],
    "text_sample": all_text[:2000]
}))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json'}

exec(code, env_args)
