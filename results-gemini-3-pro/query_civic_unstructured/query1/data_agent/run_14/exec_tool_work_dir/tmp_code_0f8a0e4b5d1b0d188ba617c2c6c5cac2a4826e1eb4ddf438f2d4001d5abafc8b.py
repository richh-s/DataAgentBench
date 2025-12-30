code = """import json
import re

# Load funding data
with open(locals()['var_function-call-14769478683806682002'], 'r') as f:
    funding_data = json.load(f)

# Load civic doc data
with open(locals()['var_function-call-14769478683806682871'], 'r') as f:
    civic_data = json.load(f)

# Get the text of the relevant document (latest one)
# We know the latest is 03222023 based on previous step, which is the first one in the sample list if the sample was just one doc.
# But the sample query was limit 1. The result is a list containing one dict.
text = civic_data[0]['text']

# Extract the "Capital Improvement Projects (Design)" section
start_marker = "Capital Improvement Projects (Design)"
end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

start_idx = text.find(start_marker)
if start_idx == -1:
    print("Error: Start marker not found")
    section_text = ""
else:
    start_idx += len(start_marker)
    # Find the nearest end marker
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    section_text = text[start_idx:end_idx]

# Extract project names
# Pattern: looks for lines followed by "(cid:190) Updates:"
# The text has "(cid:190) Updates:" (symbol might be unicode)
# Let's inspect the unicode char. In the output it showed (cid:190). 
# Using regex to find the line before "Updates:"
# Note: The text output had "(cid:190) Updates:".
# We can try to match "Updates:" directly.

project_names = []
lines = section_text.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    if "Updates:" in line or "Project Description:" in line:
        # The project name should be the previous non-empty line(s)
        # Scan backwards
        j = i - 1
        while j >= 0:
            prev_line = lines[j].strip()
            if prev_line:
                # This is likely the project name
                # Sometimes project name is split across lines? 
                # In the sample: "2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:"
                # So it's the line immediately before (ignoring empty lines).
                project_names.append(prev_line)
                break
            j -= 1

# Normalize names and filter
# Funding data is a list of dicts: {"Project_Name": "...", "Amount": "..."}
# Amount is string in the preview, need to convert to float/int.
funding_dict = {}
for item in funding_data:
    try:
        amt = float(item['Amount'])
        funding_dict[item['Project_Name']] = amt
    except:
        pass

# Check matches
matches = []
for name in project_names:
    # Try exact match
    if name in funding_dict:
        if funding_dict[name] > 50000:
            matches.append(name)
    else:
        # Try stripping special chars or handling minor diffs?
        # Let's just print the found names and matches for debugging
        pass

print("__RESULT__:")
print(json.dumps({"matches": matches, "found_names_in_text": project_names, "count": len(matches)}))"""

env_args = {'var_function-call-14769478683806682002': 'file_storage/function-call-14769478683806682002.json', 'var_function-call-14769478683806682871': 'file_storage/function-call-14769478683806682871.json', 'var_function-call-602477253164993976': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
