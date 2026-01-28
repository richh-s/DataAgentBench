code = """import json

funding_key = "var_function-call-14956260562366733902"
docs_key = "var_function-call-4179271317217180395"

with open(locals()[funding_key], "r") as f:
    funding = json.load(f)

with open(locals()[docs_key], "r") as f:
    docs = json.load(f)

funded_names = []
for x in funding:
    try:
        if float(x["Amount"]) > 50000:
            funded_names.append(x["Project_Name"].strip())
    except:
        pass

extracted_lines = set()
for doc in docs:
    text = doc.get("text", "")
    lines = text.split('\n')
    active = False
    for line in lines:
        line = line.strip()
        if not line: continue
        
        if "Capital Improvement Projects (Design)" in line:
            active = True
            continue
        
        if "Capital Improvement Projects (Construction)" in line:
            active = False
            continue
        if "Capital Improvement Projects (Not Started)" in line:
            active = False
            continue
        if "Disaster Recovery Projects" in line:
            active = False
            continue
            
        if active:
            if line.startswith("(") or "Updates:" in line or "Schedule:" in line or "Page " in line or "Agenda Item" in line:
                continue
            if "Prepared by" in line or "Approved by" in line or "Subject:" in line:
                continue
            # Also exclude lines that look like sentences?
            # Project names are usually Title Case.
            if len(line) < 5:
                continue
            extracted_lines.add(line)

matched_projects = []
for line in extracted_lines:
    line_lower = line.lower()
    for fname in funded_names:
        # Check strict substring
        if fname.lower() in line_lower:
            matched_projects.append(line)
            break

print("__RESULT__:")
print(json.dumps({"count": len(matched_projects), "matches": matched_projects}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json', 'var_function-call-16896789202292209147': {'count': 12, 'matches': ['Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Canyon Road Traffic Study', 'Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Permanent Skate Park']}}

exec(code, env_args)
