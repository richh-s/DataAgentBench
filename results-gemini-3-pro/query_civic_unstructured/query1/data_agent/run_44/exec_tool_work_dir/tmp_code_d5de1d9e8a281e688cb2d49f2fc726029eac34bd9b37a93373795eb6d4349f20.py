code = """import json
import pandas as pd

# Load funding data
funding_file = locals()['var_function-call-6902551004111180448']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)
high_funding_projects = set(df_funding[df_funding['Amount'] > 50000]['Project_Name'].str.strip().tolist())

# Load civic docs
civic_file = locals()['var_function-call-6902551004111182541']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Find the document with the latest date (03222023)
target_doc = None
for doc in civic_data:
    if "03222023" in doc['filename']:
        target_doc = doc
        break
if not target_doc:
    target_doc = civic_data[0]

text = target_doc['text']
lines = text.splitlines()

design_projects = []
in_design_section = False
buffer_line = None

design_header = "Capital Improvement Projects (Design)"
stop_headers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for line in lines:
    line = line.strip()
    if not line:
        continue

    if design_header in line:
        in_design_section = True
        continue

    if in_design_section:
        # Check if we hit a stop header
        is_stop = False
        for sh in stop_headers:
            if sh in line:
                is_stop = True
                break
        if is_stop:
            in_design_section = False
            break
        
        # Check for markers indicating the PREVIOUS line was a project name
        # Markers: "Updates:", "Project Description:", "Project Schedule:"
        # The text has "(cid:190) Updates:", so checking "Updates:" is safe.
        if "Updates:" in line or "Project Description:" in line:
            if buffer_line:
                name = buffer_line.strip()
                # Simple filter to avoid noise
                if len(name) > 3 and "Page " not in name:
                    design_projects.append(name)
                buffer_line = None
        else:
            buffer_line = line

# Deduplicate
design_projects = sorted(list(set(design_projects)))

# Count matches
matches = []
for p in design_projects:
    if p in high_funding_projects:
        matches.append(p)

print("__RESULT__:")
print(json.dumps({
    "extracted": design_projects,
    "matches": matches,
    "count": len(matches)
}))"""

env_args = {'var_function-call-12023591803711719665': ['Funding'], 'var_function-call-12023591803711719498': ['civic_docs'], 'var_function-call-6902551004111180448': 'file_storage/function-call-6902551004111180448.json', 'var_function-call-6902551004111182541': 'file_storage/function-call-6902551004111182541.json', 'var_function-call-17629615109180015549': 'file_storage/function-call-17629615109180015549.json', 'var_function-call-13245772916019581985': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
