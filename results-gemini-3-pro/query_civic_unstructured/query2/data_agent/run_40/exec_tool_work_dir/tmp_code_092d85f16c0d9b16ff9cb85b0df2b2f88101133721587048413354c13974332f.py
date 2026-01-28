code = """import json
import re

# Load data
with open(locals()['var_function-call-13888598528909911574'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-13888598528909910147'], 'r') as f:
    funding_data = json.load(f)

# Funding lookup
funding_map = {} # Name -> Amount (or list of amounts if duplicates)
for item in funding_data:
    name = item['Project_Name'].strip().lower()
    amount = int(item['Amount'])
    if name in funding_map:
        funding_map[name] += amount
    else:
        funding_map[name] = amount

projects_found = []

def clean_text(text):
    return text.replace('\n', ' ').strip()

# Regex to find project blocks
# Strategy: Split by the bullet point pattern that starts a section
# Looking at the text, projects seem to start with a Name line, then "(cid:190) Updates:"
# So we iterate through the text.

for doc in civic_docs:
    text = doc['text']
    # Normalize bullet points? The text has (cid:190) and (cid:131).
    # Let's split by regex that finds the "Updates" or "Project Description" line.
    # Pattern: \n(cid:190) (Updates|Project Description|Project Updates):
    
    # We want to capture the Project Name which is the text before this pattern, 
    # going back to the previous double newline or just the line before.
    
    # Let's try splitting the text into "segments" based on the project marker.
    # But splitting removes the delimiter.
    # We can use finditer.
    
    marker_pattern = re.compile(r'\n\n\(cid:190\) (?:Updates|Project Description|Project Updates).*?:')
    
    # This might be tricky because the name is before the match.
    # Let's iterate line by line?
    # Or, let's identify the start of updates, then look backwards for the name.
    
    lines = text.split('\n')
    
    current_project = {}
    buffer_project_text = []
    
    # Better approach:
    # 1. Find all start indices of "(cid:190) Updates:" or similar.
    # 2. Extract the lines immediately preceding as the Name.
    # 3. Extract the lines following (until next project) as the Description/Status.
    
    # Find all matches
    matches = list(re.finditer(r'(?:\(cid:190\)|•)\s*(?:Updates|Project Description|Project Updates)', text))
    
    project_indices = []
    for m in matches:
        project_indices.append(m.start())
        
    for i, start_idx in enumerate(project_indices):
        # Determine end of this block
        end_idx = project_indices[i+1] if i+1 < len(project_indices) else len(text)
        
        # Text block for this project
        block = text[start_idx:end_idx]
        
        # Project Name is strictly BEFORE the start_idx.
        # Let's look at text[prev_end:start_idx].
        # But we need to define "prev_end".
        # For the first one, it's the beginning of text.
        # But the text before might contain the previous project's block.
        # Wait, the structure is: Name \n Marker ... Name \n Marker ...
        # So the text between Marker(i) and Marker(i+1) contains:
        # [Body of Project i] [Name of Project i+1]
        
        # So:
        # 1. Body of Project i starts at start_idx.
        # 2. Ends before Name of Project i+1.
        # 3. Name of Project i+1 is immediately before start_idx(i+1).
        
        # Let's try to extract the name for the CURRENT marker.
        # Look backwards from start_idx.
        # Skip empty lines.
        # The line(s) before that are the name.
        
        # Get text before this marker
        pre_text = text[:start_idx].rstrip()
        # Find the last newline
        last_newline = pre_text.rfind('\n')
        if last_newline == -1:
            name_start = 0
        else:
            # Check if the line before is part of the name (multi-line name?)
            # Usually names are 1-2 lines.
            # Let's take the last non-empty line.
            lines_pre = pre_text.split('\n')
            # Filter empty
            lines_pre = [l.strip() for l in lines_pre if l.strip()]
            if lines_pre:
                name = lines_pre[-1]
                # Sometimes name is split?
                # "2022 Morning View Resurfacing & Storm Drain Improvements"
                # might be on multiple lines?
                # For now, assume 1 line or take last 2 if the second to last is short?
                # Let's stick to last line for now.
            else:
                name = "Unknown"
        
        # Now analyze the block (which contains status and dates)
        # Check for completion in 2022
        is_completed_2022 = False
        
        # Normalize block text
        block_lower = block.lower()
        
        # Check for completion statements
        # "construction was completed [month] 2022"
        # "complete construction: [month] 2022"
        # "construction was completed, [month] 2022"
        
        if '2022' in block_lower:
            # Check context
            # Regex for completed
            if re.search(r'construction (was )?completed.*?2022', block_lower):
                is_completed_2022 = True
            elif re.search(r'complete construction.*?2022', block_lower):
                is_completed_2022 = True
            elif re.search(r'completed.*?2022', block_lower) and 'construction' in block_lower:
                # Fallback
                 is_completed_2022 = True
        
        # Check topic
        topic_park = False
        # Check name and block for keywords
        keywords = ['park', 'playground', 'recreation', 'open space']
        full_content = (name + " " + block).lower()
        if any(kw in full_content for kw in keywords):
            topic_park = True
            
        if topic_park and is_completed_2022:
            projects_found.append(name)

# Normalize and deduplicate found projects
unique_projects = list(set([p.strip() for p in projects_found]))

# Match with funding
total_funding = 0
matched_projects = []

print("Found Projects matching criteria:")
for p in unique_projects:
    print(f"- {p}")
    # Fuzzy match with funding
    # Simple check: is p in funding_map?
    p_lower = p.lower()
    
    # Try exact match first
    if p_lower in funding_map:
        total_funding += funding_map[p_lower]
        matched_projects.append((p, funding_map[p_lower]))
    else:
        # Try finding the name within the funding key or vice versa
        # or common substring
        found = False
        for fname, amount in funding_map.items():
            if p_lower == fname or p_lower in fname or fname in p_lower:
                # Ensure it's a good match (e.g. > 80% overlap?)
                # "Bluffs Park Shade Structure" matches "Bluffs Park Shade Structure"
                # "Trancas Canyon Park Playground" matches "Trancas Canyon Park Playground"
                total_funding += amount
                matched_projects.append((p, amount))
                found = True
                break
        if not found:
            print(f"  No funding match for: {p}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-18388695237617749918': ['civic_docs'], 'var_function-call-18388695237617747301': ['Funding'], 'var_function-call-18388695237617748780': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18388695237617746163': 'file_storage/function-call-18388695237617746163.json', 'var_function-call-13888598528909911574': 'file_storage/function-call-13888598528909911574.json', 'var_function-call-13888598528909910147': 'file_storage/function-call-13888598528909910147.json'}

exec(code, env_args)
