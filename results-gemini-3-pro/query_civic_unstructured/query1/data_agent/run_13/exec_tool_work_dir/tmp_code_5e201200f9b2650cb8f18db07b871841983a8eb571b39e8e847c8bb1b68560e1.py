code = """import json

# Load Funding Data
with open('var_function-call-2725984221883882111.json', 'r') as f:
    funding_data = json.load(f)

# Filter Funding Data > 50000
# Ensure Amount is converted to int/float
funded_projects = {}
for item in funding_data:
    try:
        amt = float(item['Amount'])
        if amt > 50000:
            funded_projects[item['Project_Name']] = amt
    except ValueError:
        continue

# Load Civic Docs Data
with open('var_function-call-2725984221883882726.json', 'r') as f:
    docs_data = json.load(f)

# We assume the list contains the latest document as checked previously
text = docs_data[0]['text']

# Extract Capital Projects (Design)
# Find the section
start_marker = "Capital Improvement Projects (Design)"
end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

start_idx = text.find(start_marker)
if start_idx == -1:
    print("__RESULT__:")
    print(json.dumps("Error: Section not found"))
    exit()

# Find the nearest end marker
end_idx = len(text)
for marker in end_markers:
    idx = text.find(marker, start_idx + len(start_marker))
    if idx != -1 and idx < end_idx:
        end_idx = idx

section_text = text[start_idx + len(start_marker):end_idx]

# Parse lines
lines = section_text.split('\n')
candidate_projects = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    # Filter junk
    if "Updates:" in line or "(cid:" in line or "Project Schedule:" in line or "Agenda Item" in line or "Page " in line:
        continue
    if line.startswith("Complete Design") or line.startswith("Advertise") or line.startswith("Begin Construction"):
        continue
    if line.startswith("Approved by") or line.startswith("Date prepared"):
        continue
    
    # Heuristic: Project names in this doc seem to be capitalized and standalone.
    # The filtering above removes most details.
    candidate_projects.append(line)

# Clean up candidates
# Some lines might be parts of a header or noise.
# In the sample, project names are "2022 Morning View..."
# "Public Works Commission" etc might be at the top if I parsed wrong, but I used markers.

# Let's verify candidates by checking if they look like project names or are in funding list.
# The hint says names match.
confirmed_projects = []
for proj in candidate_projects:
    # Exact match check
    if proj in funded_projects:
        confirmed_projects.append(proj)
    else:
        # Check if stripping special chars helps or partial match?
        # For now, stick to exact match as per hint.
        pass

# Count unique projects
unique_projects = list(set(confirmed_projects))

print("__RESULT__:")
print(json.dumps({"count": len(unique_projects), "projects": unique_projects, "candidates": candidate_projects}))"""

env_args = {'var_function-call-2725984221883880881': ['Funding'], 'var_function-call-2725984221883881496': ['civic_docs'], 'var_function-call-2725984221883882111': 'file_storage/function-call-2725984221883882111.json', 'var_function-call-2725984221883882726': 'file_storage/function-call-2725984221883882726.json', 'var_function-call-1453355728292058709': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
