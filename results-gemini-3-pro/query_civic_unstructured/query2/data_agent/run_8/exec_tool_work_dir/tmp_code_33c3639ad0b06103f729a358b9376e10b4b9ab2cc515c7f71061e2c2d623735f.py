code = """import json
import re

# Load data
funding_path = locals()['var_function-call-13109238308160603251']
docs_path = locals()['var_function-call-13109238308160604256']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([d['text'] for d in civic_docs])
lines = full_text.split('\n')

# Identify projects
projects_found = []
current_name = None
current_text = ""

# Heuristic: 
# Look for lines that look like titles.
# A title is followed eventually by a line containing "(cid:190)" or "(cid:131)".
# But to be robust: iterate lines.
# If line has "(cid:190)", it belongs to the current project.
# The line BEFORE the FIRST "(cid:190)" of a block is the Title.

block_started = False
for i, line in enumerate(lines):
    line = line.strip()
    if not line: continue
    
    if "(cid:190)" in line:
        if not block_started:
            # This is the start of a new block.
            # The previous non-empty line should be the title.
            # Look back
            k = i - 1
            title_candidate = None
            while k >= 0:
                prev = lines[k].strip()
                if prev:
                    # Check if prev is a marker or header
                    if "(cid:190)" in prev or "(cid:131)" in prev:
                        break # No title found, maybe continuation
                    if prev.lower().startswith("agenda"): break
                    if prev.lower().startswith("page"): break
                    title_candidate = prev
                    break
                k -= 1
            
            if title_candidate:
                # Save previous project if exists
                if current_name:
                    projects_found.append({"name": current_name, "text": current_text})
                
                current_name = title_candidate
                current_text = line
                block_started = True
            else:
                # Continuation or title not found
                if current_name:
                    current_text += "\n" + line
        else:
            # Already in a block, append
            current_text += "\n" + line
    else:
        # Normal text line.
        # If it starts with "(cid:131)", it's part of the block.
        if "(cid:131)" in line:
            if current_name:
                current_text += "\n" + line
        else:
            # If we encounter a line that is NOT a marker, it *might* be a new title.
            # But we don't know until we see the NEXT marker.
            # So we effectively end the current block if we see a non-marker line?
            # No, descriptions can have multiple lines.
            # But Titles usually separate blocks.
            # We'll buffer it.
            # Actually, the 'look back' logic at the next "(cid:190)" handles the title identification.
            # So here we just append to text?
            # If it's a new Title, it will be captured by the next "(cid:190)" lookback.
            # So we can append it to the current text for now. If it turns out to be a title later, 
            # we will switch projects then.
            # But the title shouldn't be part of the *previous* project's text.
            # This is a bit messy.
            
            # Alternative: Just collect all (Title, Text) pairs.
            # If a line becomes a title for the next project, it doesn't matter if it was in the text of the previous one
            # as long as we extract the metadata correctly.
            # But ideally we want clean text.
            if current_name:
                current_text += "\n" + line

# Add last project
if current_name:
    projects_found.append({"name": current_name, "text": current_text})

# Filter and Sum
total_funding = 0
matched_projects = []

for p in projects_found:
    name = p['name']
    text = p['text'].lower()
    
    # Park Check
    park_keywords = ['park', 'playground', 'recreation', 'walkway', 'trail', 'beach']
    is_park = False
    if any(k in name.lower() for k in park_keywords):
        is_park = True
    elif "park" in text: # strict "park" in text
         if re.search(r'\\bpark\\b', text): # escaped backslash
             is_park = True
    
    # Completed 2022 Check
    # Look for "completed" and "2022" near each other?
    # Or just both present.
    # Text says "Construction was completed November 2022".
    is_completed_2022 = False
    if "2022" in text and ("completed" in text or "complete construction" in text):
        # Verify strict pattern
        if re.search(r'(completed|complete construction).*?2022', text, re.DOTALL):
            is_completed_2022 = True
    
    if is_park and is_completed_2022:
        # Find Funding
        # Look for funding records where Project_Name matches p['name']
        # Match Logic: Funding Name starts with p['name']
        # Clean p['name']
        clean_name = name.strip()
        
        # We need to find the funding records
        # There might be multiple funding records (different sources) for the same project
        # We sum them.
        
        # Check for duplicates?
        # If we have "Project A" and "Project A (FEMA)", and we matched "Project A", we sum both.
        
        current_project_funding = 0
        found_match = False
        
        for f in funding_data:
            f_name = f['Project_Name']
            f_amt = int(f['Amount'])
            
            # Exact match or prefix match with suffix
            if f_name == clean_name or f_name.startswith(clean_name + " ("):
                current_project_funding += f_amt
                found_match = True
        
        if found_match:
            matched_projects.append({"name": clean_name, "amount": current_project_funding})
            total_funding += current_project_funding

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-4994192944937523556': ['civic_docs'], 'var_function-call-4994192944937523005': ['Funding'], 'var_function-call-4994192944937522454': 'file_storage/function-call-4994192944937522454.json', 'var_function-call-4994192944937521903': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13109238308160603251': 'file_storage/function-call-13109238308160603251.json', 'var_function-call-13109238308160604256': 'file_storage/function-call-13109238308160604256.json'}

exec(code, env_args)
