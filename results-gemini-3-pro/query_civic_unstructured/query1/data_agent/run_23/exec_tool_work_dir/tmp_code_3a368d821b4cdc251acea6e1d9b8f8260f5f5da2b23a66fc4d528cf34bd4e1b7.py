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

project_lines = set()
for doc in docs:
    text = doc.get("text", "")
    start_marker = "Capital Improvement Projects (Design)"
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = -1
    for em in end_markers:
        idx = text.find(em, start_idx)
        if idx != -1:
            if end_idx == -1 or idx < end_idx:
                end_idx = idx
    
    if end_idx == -1:
        section = text[start_idx:]
    else:
        section = text[start_idx:end_idx]
        
    lines = section.split(chr(10))
    for line in lines:
        line = line.strip()
        if not line: continue
        if "Capital Improvement Projects" in line: continue
        if line.startswith("(") or "Updates:" in line or "Schedule:" in line or "Page " in line or "Agenda Item" in line:
            continue
        if "Prepared by" in line or "Approved by" in line:
            continue
        
        if not line[0].isupper(): continue 
        if line.endswith("."): continue 
        if len(line) > 100: continue
        if len(line) < 5: continue
        
        project_lines.add(line)

count = 0
matches = []
for line in project_lines:
    line_lower = line.lower()
    for fname in funded_names:
        fname_lower = fname.lower()
        # Check bidirectional substring
        if fname_lower in line_lower or line_lower in fname_lower:
            count += 1
            matches.append(line)
            break 

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json', 'var_function-call-16896789202292209147': {'count': 12, 'matches': ['Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Canyon Road Traffic Study', 'Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Permanent Skate Park']}, 'var_function-call-17244096442756523597': {'count': 12, 'matches': ['Westward Beach Road Drainage Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Canyon Road Traffic Study', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'PCH Median Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Permanent Skate Park']}, 'var_function-call-9482907091417017496': {'count': 11, 'matches': ['Storm Drain Master Plan', 'PCH Median Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Drainage Improvements Project', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', 'Clover Heights Storm Drainage Improvements', 'PCH at Trancas Canyon Road Right Turn Lane']}}

exec(code, env_args)
