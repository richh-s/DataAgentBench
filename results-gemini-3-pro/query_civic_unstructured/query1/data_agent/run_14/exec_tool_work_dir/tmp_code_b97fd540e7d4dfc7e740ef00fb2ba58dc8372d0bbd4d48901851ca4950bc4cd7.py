code = """import json

# Load funding data
with open(locals()['var_function-call-14769478683806682002'], 'r') as f:
    funding_data = json.load(f)

# Load civic doc data
with open(locals()['var_function-call-14769478683806682871'], 'r') as f:
    civic_data = json.load(f)

text = civic_data[0]['text']

# Extract the "Capital Improvement Projects (Design)" section
start_marker = "Capital Improvement Projects (Design)"
# The end markers based on the document structure
end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"]

start_idx = text.find(start_marker)
section_text = ""
if start_idx != -1:
    start_idx += len(start_marker)
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    section_text = text[start_idx:end_idx]

# Extract project names
# Strategy: Iterate lines. If a line contains "Updates:" or "Project Description:", the previous non-empty line is the Title.
project_names = []
lines = section_text.split('\n')
for i, line in enumerate(lines):
    line_strip = line.strip()
    if "Updates:" in line_strip or "Project Description:" in line_strip:
        # Check previous lines for the title
        j = i - 1
        while j >= 0:
            prev_line = lines[j].strip()
            if prev_line:
                # Found the title line
                project_names.append(prev_line)
                break
            j -= 1

# Normalize and match
# Create a map of normalized funding name to amount
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip().lower()
    try:
        amount = float(item['Amount'])
        funding_map[name] = amount
    except:
        continue

found_matches = []
# Normalize extracted names
for name in project_names:
    norm_name = name.strip().lower()
    # Check for exact match
    if norm_name in funding_map:
        if funding_map[norm_name] > 50000:
            found_matches.append(name)
    else:
        # Try to match with Funding table entries that might contain this name or vice versa
        # Example: "Morning View Resurfacing" vs "2022 Morning View Resurfacing..."
        pass

print("__RESULT__:")
print(json.dumps({"matches": found_matches, "extracted_names": project_names, "count": len(found_matches)}))"""

env_args = {'var_function-call-14769478683806682002': 'file_storage/function-call-14769478683806682002.json', 'var_function-call-14769478683806682871': 'file_storage/function-call-14769478683806682871.json', 'var_function-call-602477253164993976': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
