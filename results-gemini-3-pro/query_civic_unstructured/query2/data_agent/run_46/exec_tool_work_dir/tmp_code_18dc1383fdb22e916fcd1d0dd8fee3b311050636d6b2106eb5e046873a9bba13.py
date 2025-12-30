code = """import json
import re

# Load data
with open(locals()['var_function-call-14713834321312381364'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-14713834321312381855'], 'r') as f:
    civic_docs = json.load(f)
full_text = " ".join([doc.get('text', '') for doc in civic_docs])

# Candidates
candidates = [
    "Bluffs Park Shade Structure",
    "Point Dume Walkway Repairs",
    "Legacy Park Paver Repair Project",
    "Legacy Park Benches and Arbors Renovation",
    "Malibu Bluffs Park Workout Station",
    "Malibu Bluffs Park Roof Replacement Project",
    "Trancas Canyon Park Planting and Irrigation Repairs",
    "Trancas Canyon Park Playground"
]

project_info = {}

for p in funding_data:
    if p['Project_Name'] in candidates:
        project_info[p['Project_Name']] = {"amount": p['Amount'], "status_found": "No"}

# Check status in text
for name in project_info:
    # Find all mentions
    starts = [m.start() for m in re.finditer(re.escape(name), full_text)]
    for start in starts:
        chunk = full_text[start:start+1000].lower()
        if "completed" in chunk:
            # Check context
            if "2022" in chunk:
                # Check strict proximity
                # Look for "completed ... 2022" pattern
                if re.search(r"completed.{0,100}2022", chunk) or re.search(r"2022.{0,100}completed", chunk):
                    project_info[name]["status_found"] = "Completed 2022 (Maybe)"
                    # Store snippet for verification
                    project_info[name]["snippet"] = full_text[start:start+300]

print("__RESULT__:")
print(json.dumps(project_info))"""

env_args = {'var_function-call-14713834321312381364': 'file_storage/function-call-14713834321312381364.json', 'var_function-call-14713834321312381855': 'file_storage/function-call-14713834321312381855.json', 'var_function-call-14503968957198369253': {'matched_projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}, 'var_function-call-17804470175278883708': 'file_storage/function-call-17804470175278883708.json'}

exec(code, env_args)
