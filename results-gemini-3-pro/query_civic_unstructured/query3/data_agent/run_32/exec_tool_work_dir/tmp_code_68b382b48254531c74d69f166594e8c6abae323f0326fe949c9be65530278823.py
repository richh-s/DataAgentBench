code = """import json
import sqlite3
import pandas as pd

# Load previous results
funding_file = locals()['var_function-call-5036986330958495032']
civic_docs_file = locals()['var_function-call-5036986330958492415']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Combine text from all civic docs (if multiple)
full_text = "\n".join([doc['text'] for doc in civic_docs_data])

# Normalize text for easier searching
# However, for extraction, we need the original structure. 
# We'll work with the full text string.

funding_df = pd.DataFrame(funding_data)

results = []

# Define keywords
keywords = ['emergency', 'FEMA']

# Helper to find status and text block
# We will iterate through the text to find project names.
# But searching for names in text is better if we iterate through funding names.

# Pre-identify section positions to help with status
# Sections:
# Capital Improvement Projects (Design)
# Capital Improvement Projects (Construction)
# Capital Improvement Projects (Not Started)

# We'll split the text into lines
lines = full_text.split('\n')

# Identify section boundaries
sections = []
current_section = None
for i, line in enumerate(lines):
    line = line.strip()
    if "Capital Improvement Projects (Design)" in line:
        current_section = "design"
    elif "Capital Improvement Projects (Construction)" in line:
        current_section = "construction"
    elif "Capital Improvement Projects (Not Started)" in line:
        current_section = "not started"
    
    # Store line index and section
    sections.append(current_section)

# Now, for each project in Funding, find its location in text
# We assume project name matches a line in the text or is contained in a line
# The project names in text seem to be exact or close. 
# Funding DB: "2022 Morning View Resurfacing & Storm Drain Improvements"
# Text: "2022 Morning View Resurfacing & Storm Drain Improvements" (Exact match)

# Funding DB: "PCH Median Improvements Project"
# Text: "PCH Median Improvements Project"

for index, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    
    # Simple search
    # We need to find the line number where the project name appears as a header.
    # It seems project names appear on their own lines or start of lines.
    
    found_idx = -1
    for i, line in enumerate(lines):
        # Check for exact match or close match (e.g. stripping whitespace)
        # Also, the text might have suffixes like "(FEMA Project)" which might not be in the text header
        # or vice versa.
        # Funding DB has suffixes "(FEMA Project)". Text might not.
        # Let's clean the Funding Name for searching: remove (...) suffixes?
        # But wait, "Latigo Canyon Road Culvert Repairs (FEMA Project)" might be the name.
        # Let's try finding the exact string first.
        
        if proj_name.lower() in line.lower():
            # Potential match. Check if it's a "header" line (e.g. not part of a sentence).
            # In the agenda, project names are usually short lines.
            if len(line) < len(proj_name) + 20: 
                found_idx = i
                break
    
    # If not found, try stripping suffixes in Funding DB name
    if found_idx == -1:
        # Remove parens
        import re
        clean_name = re.sub(r'\s*\(.*?\)', '', proj_name)
        if clean_name and len(clean_name) > 5:
            for i, line in enumerate(lines):
                if clean_name.lower() in line.lower():
                    if len(line) < len(clean_name) + 20:
                        found_idx = i
                        break

    if found_idx != -1:
        # Found the project in text.
        # 1. Determine Section/Status
        section_status = sections[found_idx]
        
        # 2. Extract text block
        # Block ends at next project (which we don't know easily) or double newline or next bullet list start?
        # Looking at text, projects are separated by blank lines and new headers.
        # The next project usually starts with a line that doesn't start with (cid:190) or (cid:131).
        # We'll read lines until we hit a likely new project header or end of section.
        
        block_text = []
        for j in range(found_idx, len(lines)):
            l = lines[j].strip()
            # If we hit a new section header, stop
            if "Capital Improvement Projects (" in l and j != found_idx:
                break
            
            # If we hit a line that looks like a new project name?
            # It's hard to distinguish a project name from other text without a list of names.
            # But the structure is Name -> Updates -> Schedule.
            # If we see a line that is NOT Updates/Schedule/Bullets and is not empty, it might be next project.
            # But "Page x of y" is also there.
            
            # Heuristic: If we have collected some text (Updates/Schedule), and we hit a line that 
            # does not start with special chars and is not page info, it's likely next project.
            if j > found_idx and len(block_text) > 0:
                is_bullet = l.startswith('(cid:') or l.startswith('Updates:') or l.startswith('Project Schedule:')
                is_page = "Page " in l or "Agenda Item" in l or l == ""
                # If it's a plain text line, check if it's a known header or potential project
                if not is_bullet and not is_page:
                    # Could be next project.
                    # Let's assume the block ends here.
                    break
            
            block_text.append(lines[j])
        
        full_block = "\n".join(block_text)
        
        # 3. Check for keywords in Name or Block
        is_relevant = False
        for kw in keywords:
            if kw.lower() in proj_name.lower() or kw.lower() in full_block.lower():
                is_relevant = True
                break
        
        if is_relevant:
            # Determine specific status from text if in "construction" section
            final_status = section_status
            if section_status == 'construction':
                if 'completed' in full_block.lower():
                    final_status = 'completed'
                elif 'under construction' in full_block.lower():
                    final_status = 'in construction' # or 'design' if we want to force fit, but let's keep it descriptive
                else:
                    final_status = 'construction'
            
            # Add to results
            results.append({
                "Project_Name": proj_name,
                "Funding_Source": row['Funding_Source'],
                "Amount": row['Amount'],
                "Status": final_status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11141337925117404384': ['civic_docs'], 'var_function-call-11141337925117405097': ['Funding'], 'var_function-call-3665847163097728255': 'file_storage/function-call-3665847163097728255.json', 'var_function-call-3665847163097727678': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-5036986330958495032': 'file_storage/function-call-5036986330958495032.json', 'var_function-call-5036986330958492415': 'file_storage/function-call-5036986330958492415.json'}

exec(code, env_args)
