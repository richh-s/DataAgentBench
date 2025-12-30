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
# Normalize project names (strip)
df_funding_high['Project_Name'] = df_funding_high['Project_Name'].str.strip()

# Load civic docs
docs_file = locals()['var_function-call-9348591525037587814']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

capital_design_projects = []

for doc in docs_data:
    text = doc['text']
    
    # Locate "Capital Improvement Projects (Design)"
    start_marker = "Capital Improvement Projects (Design)"
    
    # Identify end markers
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    # "Disaster Recovery Projects" - The preview showed "Capital Improvement Projects and Disaster Recovery Projects Status Report", so maybe "Disaster Recovery Projects" is a main header.
    # Let's try to find the earliest occurrence of any next section header.
    
    possible_end_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Disaster Recovery Projects (Design)", # Just in case
        "Disaster Recovery Projects (Construction)"
    ]
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    start_idx += len(start_marker)
    
    end_idx = len(text)
    for marker in possible_end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    # Split by (cid:190) Updates:
    # Note: The marker in the text might be encoded or just characters.
    # In the preview: "\n\n(cid:190) Updates:\n\n"
    # I'll try to split by "Updates:" and look around it, or use the specific unicode char if possible, or just "Updates:" if it's unique enough in this context.
    # Actually, the preview shows `(cid:190) Updates:`.
    # Let's try splitting by "Updates:" and assume the line before is the project name.
    
    chunks = section_text.split("Updates:")
    
    # The first chunk contains the first project name at the end.
    # Subsequent chunks (except the last one?) contain project details and then the next project name at the end.
    # The last chunk contains only details for the last project.
    
    # Wait.
    # Chunk 0: "... \n\nProject Name A\n\n(cid:190) " -> (ends with "Updates:" split)
    # The split removes "Updates:".
    # So Chunk 0 ends with "(cid:190) " or similar.
    # I need to clean the end of Chunk 0 to find Project Name A.
    
    # Let's refine:
    # Look for lines that look like project names.
    # They are usually standalone lines.
    # Lines starting with (cid:190) or (cid:131) (bullets) are details.
    # Lines starting with "Complete Design", "Advertise", etc. are details.
    # Empty lines are separators.
    # A project name is a line that doesn't start with these bullets and is not a known keyword.
    
    # Let's try a different approach:
    # Split the section into lines.
    # Iterate through lines.
    # Maintain a state.
    # But filtering out noise is safer.
    
    lines = section_text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    
    # In the preview:
    # Capital Improvement Projects (Design) (we skipped this)
    # 2022 Morning View Resurfacing & Storm Drain Improvements
    # (cid:190) Updates:
    # ...
    # PCH Median Improvements Project
    # (cid:190) Updates:
    
    # So if a line is followed immediately (ignoring empty lines) by a line starting with "(cid:190) Updates" or just containing "Updates:", then it is a project name.
    
    for i, line in enumerate(cleaned_lines):
        # Check if this line is a project name
        # A project name is followed by "Updates:" or "(cid:190) Updates:"
        if i + 1 < len(cleaned_lines):
            next_line = cleaned_lines[i+1]
            if "Updates:" in next_line:
                # Potential project name
                # Clean it up
                p_name = line
                # Sometimes the bullet might be on the same line? No, preview shows newlines.
                capital_design_projects.append(p_name)

# Dedup
capital_design_projects = list(set(capital_design_projects))

print(f"Extracted Capital Design Projects: {capital_design_projects}")

# Join with funding
funded_projects = []
for p in capital_design_projects:
    # Attempt match
    # Exact match first
    match = df_funding_high[df_funding_high['Project_Name'] == p]
    if not match.empty:
        funded_projects.append(p)
    else:
        # Try checking if one is substring of another or normalized
        # The db description says "Project_Name in the Funding ... matches ... extracted".
        # But let's be careful about whitespace or minor diffs.
        pass

print(f"Funded Capital Design Projects (>50k): {funded_projects}")

result_count = len(funded_projects)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_function-call-1527972859100208008': 'file_storage/function-call-1527972859100208008.json', 'var_function-call-9348591525037587814': 'file_storage/function-call-9348591525037587814.json'}

exec(code, env_args)
