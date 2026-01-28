code = """import json
import pandas as pd

# Load Funding data
with open(locals()['var_function-call-12574336957284000911'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Convert Amount to numeric just in case
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Load Civic Docs data
with open(locals()['var_function-call-12574336957284002122'], 'r') as f:
    civic_docs = json.load(f)

# Extract projects in 'design' status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Identify the section
    start_marker = "Capital Improvement Projects (Design)"
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"]
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    # Find the earliest end marker after start_idx
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_marker):end_idx]
    
    # Split into lines
    lines = section_text.split('\n')
    
    # Strategy: Look for lines that look like project headers.
    # Based on preview: Project Name is followed by "(cid:190) Updates:" or "(cid:190) Project Description:" or similar.
    # The bullet points seem to start with (cid:190) or (cid:131).
    # Project names do not start with these.
    # We can iterate and find lines that are followed by a line starting with a bullet or "Updates".
    
    # Let's clean lines first
    clean_lines = [line.strip() for line in lines if line.strip()]
    
    for i, line in enumerate(clean_lines):
        # Heuristic: A project name is a line that is NOT a bullet point, 
        # and is followed by a line that IS a bullet point or starts with "Updates" or "Project Description".
        # Bullet chars in preview: (cid:190), (cid:131). 
        # Or just checking if the next line indicates start of details.
        
        # Check if current line is likely a header
        if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda Item"):
            continue
            
        if i + 1 < len(clean_lines):
            next_line = clean_lines[i+1]
            # Check if next line starts with a bullet or key phrase
            if next_line.startswith("(cid:190)") or "Updates:" in next_line or "Project Description:" in next_line:
                # Likely a project name
                # Clean up the name?
                name = line.strip()
                # Check if it is a noise line (like a date or "Item 4.B.")
                if len(name) < 3 or "Item" in name or "Meeting" in name:
                    continue
                design_projects.append(name)

# Remove duplicates if any
design_projects = list(set(design_projects))

print(f"Identified Design Projects: {design_projects}")

# Join with funding
# We need to match names.
# "How many capital projects with a 'design' status have funding greater than $50,000?"

matched_projects = []
for proj in design_projects:
    # Find in funding
    # Exact match?
    funding_records = df_funding[df_funding['Project_Name'] == proj]
    
    if not funding_records.empty:
        total_amount = funding_records['Amount'].sum() # Assuming one project has one record, but if multiple, maybe sum or check each?
        # The query asks "have funding greater than $50,000". Usually implies the project's funding.
        # If there are multiple records for one project, sum them? Or is it one record per project?
        # Database description says: "Funding_ID ... Project_Name ... Amount". A project *could* have multiple sources.
        # "Amount (int): Funding amount in dollars".
        # I will sum the amount for the project.
        
        if total_amount > 50000:
            matched_projects.append({'name': proj, 'amount': total_amount})
    else:
        # Try fuzzy match or stripping?
        # The hint says "The Project_Name in the Funding SQLite table matches the project names that can be extracted".
        # So exact match should work if extracted correctly.
        pass

print(f"Matched Projects (>50k): {matched_projects}")
print("__RESULT__:")
print(len(matched_projects))"""

env_args = {'var_function-call-16012235446979576453': ['civic_docs'], 'var_function-call-16012235446979577650': ['Funding'], 'var_function-call-12574336957284000911': 'file_storage/function-call-12574336957284000911.json', 'var_function-call-12574336957284002122': 'file_storage/function-call-12574336957284002122.json'}

exec(code, env_args)
