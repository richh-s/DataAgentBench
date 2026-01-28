code = """import re, json, pandas as pd

# Load funding data from storage (SQLite query)
funding_records = var_call_yuoy9hbfBjCrDt7ti3DdiGLc

# Load civic documents data from storage (MongoDB query)
# If the result is a file path (string), load the JSON content from that file
civic_docs_data = var_call_GbNYPqDAV7wTvW9baLvNyqVZ
if isinstance(civic_docs_data, str):
    import os, json as json_lib
    if os.path.isfile(civic_docs_data):
        with open(civic_docs_data, 'r') as f:
            civic_docs_data = json_lib.load(f)

texts = [doc.get('text', '') for doc in civic_docs_data]
full_text = '\n'.join(texts)

# Parse capital projects and their statuses using simple heuristics from the text
projects = []

# Look for sections that indicate project status groups
# We'll specifically look for lines under "Capital Improvement Projects (Design)" and capture project names
pattern = r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)"
match = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
if match:
    design_section = match.group(1)
    # Project names appear as standalone lines with no leading bullet characters
    for line in design_section.split('\n'):
        line = line.strip('\r\n ')
        if not line:
            continue
        # Skip obvious non-project lines
        if any(kw in line for kw in ["Updates", "Project Schedule", "Estimated Schedule", "Agenda", "Page "]):
            continue
        # Heuristic: project lines often have title case and no colon
        if ':' in line:
            continue
        # Exclude very short lines
        if len(line.split()) < 3:
            continue
        projects.append({"Project_Name": line, "type": "capital", "status": "design"})

# Create DataFrame for projects
projects_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Create DataFrame for funding records
funding_df = pd.DataFrame(funding_records)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Filter funding > 50000
funding_df = funding_df[funding_df['Amount'] > 50000]

# Join on Project_Name
merged = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')

# Count capital projects with design status and funding > 50000
count = int(len(merged))

result = json.dumps({"count": count})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_yuoy9hbfBjCrDt7ti3DdiGLc': 'file_storage/call_yuoy9hbfBjCrDt7ti3DdiGLc.json', 'var_call_GbNYPqDAV7wTvW9baLvNyqVZ': 'file_storage/call_GbNYPqDAV7wTvW9baLvNyqVZ.json'}

exec(code, env_args)
