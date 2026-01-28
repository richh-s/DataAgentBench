code = """import json

# Load data
with open(locals()['var_function-call-14769478683806682002'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-14769478683806682871'], 'r') as f:
    civic_data = json.load(f)

text = civic_data[0]['text']

# Extract Section
start_marker = "Capital Improvement Projects (Design)"
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

# Extract Names
project_names = []
lines = section_text.splitlines()
for i, line in enumerate(lines):
    line_strip = line.strip()
    # Check for keywords indicating a project block follows
    if "Updates:" in line_strip or "Project Description:" in line_strip:
        j = i - 1
        while j >= 0:
            prev_line = lines[j].strip()
            if prev_line:
                project_names.append(prev_line)
                break
            j -= 1

# Normalize and Match
funding_map = {}
for item in funding_data:
    # Key: normalized name, Value: amount
    funding_map[item['Project_Name'].strip().lower()] = float(item['Amount'])

matches = []
for name in project_names:
    norm_name = name.strip().lower()
    # Exact match check
    if norm_name in funding_map:
        if funding_map[norm_name] > 50000:
            matches.append(name)

print("__RESULT__:")
print(json.dumps({"matches": matches, "extracted_names": project_names, "count": len(matches)}))"""

env_args = {'var_function-call-14769478683806682002': 'file_storage/function-call-14769478683806682002.json', 'var_function-call-14769478683806682871': 'file_storage/function-call-14769478683806682871.json', 'var_function-call-602477253164993976': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
