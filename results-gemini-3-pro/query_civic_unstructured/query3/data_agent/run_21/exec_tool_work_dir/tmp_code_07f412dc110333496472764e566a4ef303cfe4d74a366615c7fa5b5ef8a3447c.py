code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-13907770032762226910'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-12554270162172100471'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize project names for matching
def normalize_name(name):
    # Remove common suffixes found in Funding for matching with Docs
    name = re.sub(r'\s*\(FEMA.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Parse Civic Docs
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_status = None
    # We will iterate lines and look for headers or project names
    # Headers: "Capital Improvement Projects (Design)", "(Construction)", "(Not Started)"
    
    # A simple state machine or chunking
    # Let's clean empty lines first
    lines = [line.strip() for line in lines if line.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for status headers
        if "Capital Improvement Projects" in line:
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction" # Will refine later
            elif "(Not Started)" in line:
                current_status = "not started"
            i += 1
            continue
            
        # Heuristic for Project Name:
        # It's a line that doesn't start with special chars, and is followed by "(cid:190)" lines (Updates/Description)
        # Note: In the preview, bullet points are `(cid:190)` or `(cid:131)`.
        if current_status and not line.startswith('(') and not line.startswith('Page'):
            # Look ahead to see if next lines are updates
            # Find next line that is not empty (we already filtered empty)
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if next_line.startswith('(cid:190)') or next_line.startswith('Updates:') or next_line.startswith('Project Description:'):
                    # Found a project
                    p_name = line
                    # Extract details until next project or section
                    p_text = ""
                    j = i + 1
                    p_status_refined = current_status
                    
                    while j < len(lines):
                        sub_line = lines[j]
                        if "Capital Improvement Projects" in sub_line:
                            break
                        # Check if this looks like a new project start?
                        # A new project start would be a line not starting with bullets, followed by bullets.
                        # But we need to be careful not to trigger on "Page 1 of 6" or similar.
                        if not sub_line.startswith('(') and not sub_line.startswith('Page') and not sub_line.startswith('Agenda Item'):
                            # Check next for bullet
                            if j + 1 < len(lines):
                                next_sub = lines[j+1]
                                if next_sub.startswith('(cid:190)') or next_sub.startswith('Updates:') or next_sub.startswith('Project Description:'):
                                    # Yep, it's a new project
                                    break
                        
                        p_text += sub_line + " "
                        
                        # Refine status for construction
                        if current_status == "construction":
                            if "Construction was completed" in sub_line or "Notice of completion" in sub_line:
                                p_status_refined = "completed"
                        
                        j += 1
                    
                    extracted_projects.append({
                        "Project_Name": p_name,
                        "Status": p_status_refined,
                        "Full_Text": p_text,
                        "Raw_Status_Section": current_status
                    })
                    
                    i = j - 1 # process loop will increment i
        i += 1

df_extracted = pd.DataFrame(extracted_projects)

# Identify Relevant Projects
# 1. Projects in Docs with "emergency" or "FEMA" in Name or Text
relevant_docs = []
if not df_extracted.empty:
    for idx, row in df_extracted.iterrows():
        is_relevant = False
        if "emergency" in row['Project_Name'].lower() or "fema" in row['Project_Name'].lower():
            is_relevant = True
        elif "emergency" in row['Full_Text'].lower() or "fema" in row['Full_Text'].lower():
            is_relevant = True
        
        if is_relevant:
            relevant_docs.append(row)

df_relevant_docs = pd.DataFrame(relevant_docs)

# 2. Funding projects with "emergency" or "FEMA" in Name
relevant_funding = df_funding[df_funding['Project_Name'].str.contains('emergency|FEMA', case=False, regex=True)].copy()

# We need to output: Name, Funding Source, Amount, Status.
# We will base our final list on the union of relevant projects found.

final_results = []

# Strategy:
# Iterate through ALL funding records.
# If a funding record is relevant (has keyword) OR matches a relevant doc project -> Include it.
# If included, try to find Status from Docs.

# Create a lookup for Doc Status by Normalized Name
doc_lookup = {}
if not df_extracted.empty:
    for idx, row in df_extracted.iterrows():
        norm_name = normalize_name(row['Project_Name'])
        # Store dict, handle duplicates if any (overwrite or list?)
        doc_lookup[norm_name] = row['Status']
        # Also store exact name
        doc_lookup[row['Project_Name'].lower()] = row['Status']

# Also keep track of relevant doc names to ensure we don't miss projects mentioned in docs but maybe having generic names in funding?
# Actually, if it's in docs as relevant, we want to find its funding.
relevant_doc_names = set()
if not df_relevant_docs.empty:
    relevant_doc_names = set(df_relevant_docs['Project_Name'].apply(normalize_name))

processed_funding_ids = set()

# Pass 1: Check all funding records
for idx, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_source = row['Funding_Source']
    f_amount = row['Amount']
    
    is_f_relevant = "emergency" in f_name.lower() or "fema" in f_name.lower()
    
    # Check match with relevant docs
    norm_f_name = normalize_name(f_name)
    matched_doc_status = doc_lookup.get(norm_f_name) or doc_lookup.get(f_name.lower())
    
    # Is this funding record for a project that was identified as relevant in docs?
    # We check if the normalized name matches any relevant doc name
    is_doc_relevant_match = norm_f_name in relevant_doc_names
    
    if is_f_relevant or is_doc_relevant_match:
        # Include this record
        status = matched_doc_status if matched_doc_status else "Unknown" # Or "not found in docs"
        
        final_results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })
        processed_funding_ids.add(row['Funding_ID'])

# Pass 2: Are there relevant projects in docs that we missed because we didn't find a funding record?
# The user asks for "project names, funding sources, amounts...". If no funding, maybe we shouldn't list it?
# Or maybe we should list with "None"?
# Usually "What are the ... funding sources..." implies we need the funding info.
# If a project is in docs but not in funding table, we can't provide amount.
# However, let's check if we missed any funding matches.
# My logic above covers: Relevant Funding -> Output. Relevant Doc -> matched with Funding -> Output.
# What if Relevant Doc exists, but Funding Record does NOT match?
# e.g. Doc: "Emergency Road Repair". Funding: No entry.
# Should I list it?
# The prompt asks "What are the project names, funding sources, amounts...".
# I'll stick to those where I can find funding, or at least where I checked.
# If I can't find funding, I might skip or list as "N/A".
# Given the DB description "Funding table contains funding records... Project names can be joined...", it implies the join is the key.
# I will output the matches found.

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-17503695109884766973': ['civic_docs'], 'var_function-call-17503695109884764492': ['Funding'], 'var_function-call-17012209582147726936': 'file_storage/function-call-17012209582147726936.json', 'var_function-call-13907770032762226910': 'file_storage/function-call-13907770032762226910.json', 'var_function-call-12554270162172100471': 'file_storage/function-call-12554270162172100471.json'}

exec(code, env_args)
