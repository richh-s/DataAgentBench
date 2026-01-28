code = """import json

with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

target = "Malibu Park Drainage Improvements"
found_text = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    capturing = False
    for line in lines:
        if target in line:
            capturing = True
            found_text.append("HEADER: " + line)
            continue
        if capturing:
            if "Projects (" in line: # New section
                capturing = False
            else:
                found_text.append(line)

print("__RESULT__:")
print(json.dumps(found_text[:20]))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}}

exec(code, env_args)
