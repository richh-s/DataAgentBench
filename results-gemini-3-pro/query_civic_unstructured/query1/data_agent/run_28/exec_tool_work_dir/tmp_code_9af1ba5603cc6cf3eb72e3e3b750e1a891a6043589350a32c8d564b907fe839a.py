code = """import json

funding_path = locals()['var_function-call-7838865705427955035']
civic_path = locals()['var_function-call-5237099237942450066']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_projects = set()
funding_full = []
for row in funding_data:
    try:
        amt = float(row['Amount'])
        name = row['Project_Name'].strip()
        funding_full.append((name, amt))
        if amt > 50000:
            funding_projects.add(name)
    except:
        pass

extracted_projects = set()
for doc in civic_data:
    text = doc.get('text', '')
    lines = text.splitlines()
    in_design = False
    buffer_line = None
    for line in lines:
        line = line.strip()
        if not line: continue
        if "Capital Improvement Projects (Design)" in line:
            in_design = True
            buffer_line = None
            continue
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design = False
            continue
        if in_design:
            if "(cid:190)" in line or "Updates:" in line or "Project Description:" in line:
                if buffer_line:
                    extracted_projects.add(buffer_line)
                    buffer_line = None
            else:
                if line.startswith("(cid:131)") or line.startswith("Page") or "Agenda Item" in line: continue
                if line.startswith("Date prepared:") or line.startswith("Meeting date:"): continue
                buffer_line = line

# Check for near matches
keywords = ["Morning", "Clover", "Trancas", "Westward", "Civic", "Latigo"]
potential_matches = []
for name, amt in funding_full:
    for k in keywords:
        if k in name:
            potential_matches.append(f"{name} (${amt})")

print("__RESULT__:")
print(json.dumps({
    "extracted_projects": list(extracted_projects),
    "funding_samples": potential_matches[:20]
}))"""

env_args = {'var_function-call-13459136201759015403': ['Funding'], 'var_function-call-13459136201759017542': ['civic_docs'], 'var_function-call-7838865705427955035': 'file_storage/function-call-7838865705427955035.json', 'var_function-call-7838865705427954030': 'file_storage/function-call-7838865705427954030.json', 'var_function-call-5237099237942450066': 'file_storage/function-call-5237099237942450066.json', 'var_function-call-15210746741909145379': {'matches': 10, 'projects': ['Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan', 'Permanent Skate Park', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Outdoor Warning Signs', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'PCH at Trancas Canyon Road Right Turn Lane']}}

exec(code, env_args)
