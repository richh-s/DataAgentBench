code = """import json

# Load data
civic_docs_path = locals()['var_function-call-7662231611514557955']
funding_path = locals()['var_function-call-16376562458933732175']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Funding lookup
funding_map = {}
all_funding_names = set()
for f in funding:
    name = f['Project_Name']
    all_funding_names.add(name)
    if name not in funding_map:
        funding_map[name] = []
    funding_map[name].append(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    
    # Temporary storage for current parsing project
    curr_proj_name = None
    curr_proj_desc = []
    
    def save_project():
        nonlocal curr_proj_name, curr_proj_desc, current_status
        if curr_proj_name:
            full_desc = "\n".join(curr_proj_desc).lower()
            proj_name_lower = curr_proj_name.lower()
            
            # Determine Status
            final_status = current_status
            if current_status == "Construction":
                # Check for completion
                if "completed" in full_desc and ("notice of completion" in full_desc or "construction was completed" in full_desc):
                     final_status = "Completed"
                # Else stays Construction
            
            # Filter by topic/relevance
            # "projects related to 'emergency' or 'FEMA'"
            # Check keywords in name or description
            keywords = ['emergency', 'fema']
            is_relevant = False
            for kw in keywords:
                if kw in full_desc or kw in proj_name_lower:
                    is_relevant = True
                    break
            
            if is_relevant:
                extracted_projects.append({
                    "name": curr_proj_name,
                    "status": final_status,
                    "description": full_desc
                })
        
        curr_proj_name = None
        curr_proj_desc = []

    for line in lines:
        line_clean = line.strip()
        if not line_clean: continue
        
        # Check for Section Headers
        if "Capital Improvement Projects (Design)" in line_clean:
            save_project()
            current_status = "Design"
            continue
        elif "Capital Improvement Projects (Construction)" in line_clean:
            save_project()
            current_status = "Construction"
            continue
        elif "Capital Improvement Projects (Not Started)" in line_clean:
            save_project()
            current_status = "Not Started"
            continue
        elif "Disaster Recovery Projects" in line_clean:
            save_project()
            current_status = "Design" # Assumption for Disaster section unless specified otherwise
            continue
        
        # Check for Project Name
        # We match against known funding names
        # Check exact match first
        match = None
        if line_clean in funding_map:
            match = line_clean
        else:
            # Check if stripped of " Project" matches
            if line_clean.endswith(" Project"):
                 stripped = line_clean[:-8]
                 if stripped in funding_map:
                     match = stripped
        
        if match:
            save_project()
            curr_proj_name = match
            # If we found a match but didn't have a header status yet, what do we do?
            # The snippet starts with a header. Assuming headers come first.
            if current_status is None:
                current_status = "Design" # Fallback? Or 'Unknown'
        else:
            # Accumulate description
            if curr_proj_name:
                curr_proj_desc.append(line_clean)
    
    save_project()

# Join with Funding
results = []
# We need to handle duplicates if the same project is in multiple docs?
# The prompt implies querying the database.
# I'll deduplicate by (Project_Name, Funding_ID).
seen_funding_ids = set()

for p in extracted_projects:
    p_name = p['name']
    p_status = p['status']
    
    # Get direct matches
    f_recs = list(funding_map.get(p_name, []))
    
    # Get suffix matches (e.g. FEMA projects)
    # Check for names that start with p_name and contain 'FEMA' or 'CalOES'
    # Be careful not to match completely different projects.
    # e.g. "Road" vs "Road Repair". "Road" is prefix of "Road Repair".
    # We should look for " (FEMA" or " (CalOES" or similar?
    # Or just startswith and contains FEMA.
    
    for fname in all_funding_names:
        if fname == p_name: continue
        if fname.startswith(p_name):
             # Ensure the suffix part is parenthetical or distinct
             remainder = fname[len(p_name):]
             if "FEMA" in remainder or "CalOES" in remainder:
                 f_recs.extend(funding_map[fname])
    
    for fr in f_recs:
        fid = fr['Funding_ID']
        # We might have the same project extracted from multiple docs or multiple times.
        # But here we are iterating extracted projects.
        # If we want to return unique funding records per project?
        # The user asks "What are the project names...".
        # I'll create a composite key of project name (from funding) + ID to ensure uniqueness in output list?
        # Or just append.
        # If I have duplicates in 'results', I should remove them.
        
        # Key for dedup: (Project_Name, Funding_Source, Amount, Status)
        # But 'Status' comes from the doc. 'Project_Name' from Funding.
        # If a project is in multiple docs with same status, we get duplicates.
        # I'll dedup based on funding ID and Status?
        # Actually, status might change over time?
        # Assuming one "current" status.
        # I will dedup by Funding_ID.
        if fid not in seen_funding_ids:
            seen_funding_ids.add(fid)
            results.append({
                "Project_Name": fr['Project_Name'],
                "Funding_Source": fr['Funding_Source'],
                "Amount": fr['Amount'],
                "Status": p_status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7451868806044347925': 'file_storage/function-call-7451868806044347925.json', 'var_function-call-16376562458933732175': 'file_storage/function-call-16376562458933732175.json', 'var_function-call-7662231611514557955': 'file_storage/function-call-7662231611514557955.json'}

exec(code, env_args)
