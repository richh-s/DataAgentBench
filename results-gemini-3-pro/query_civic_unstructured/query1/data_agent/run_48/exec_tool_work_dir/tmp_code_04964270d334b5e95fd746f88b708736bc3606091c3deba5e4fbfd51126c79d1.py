code = """import json
import pandas as pd

# Load funding data
funding_file = locals()['var_function-call-1527972859100208008']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Convert funding to DataFrame
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Filter funding > 50000
df_funding_high = df_funding[df_funding['Amount'] > 50000].copy()
df_funding_high['Project_Name'] = df_funding_high['Project_Name'].str.strip()
high_funding_names = set(df_funding_high['Project_Name'].unique())

# Load civic docs
docs_file = locals()['var_function-call-9348591525037587814']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

capital_design_projects = []

for doc in docs_data:
    text = doc['text']
    
    # Locate "Capital Improvement Projects (Design)"
    start_marker = "Capital Improvement Projects (Design)"
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
    start_idx += len(start_marker)
    
    # Identify end markers
    possible_end_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects"
    ]
    
    end_idx = len(text)
    for marker in possible_end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    lines = section_text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    
    for i, line in enumerate(cleaned_lines):
        # Check if this line is a project name
        # A project name is followed by a line containing "Updates:"
        if i + 1 < len(cleaned_lines):
            next_line = cleaned_lines[i+1]
            if "Updates:" in next_line:
                capital_design_projects.append(line)

# Dedup
capital_design_projects = list(set(capital_design_projects))
print(f"Extracted: {capital_design_projects}")

# Join
count = 0
matched_projects = []
for p in capital_design_projects:
    if p in high_funding_names:
        count += 1
        matched_projects.append(p)

print(f"Matched: {matched_projects}")

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-1527972859100208008': 'file_storage/function-call-1527972859100208008.json', 'var_function-call-9348591525037587814': 'file_storage/function-call-9348591525037587814.json'}

exec(code, env_args)
