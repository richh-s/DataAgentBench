code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)

text = docs[0]['text']

# Load funding data
with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
funding_names = set(funding_map.keys())

# Parse text to find projects
# Strategy: Split by "\n\n" and identify blocks that look like project titles followed by updates
# Or better, regex for the pattern
# Pattern: Title \n\n (cid:190) Updates:

# We also need to capture the section (Capital vs Disaster) if possible
# Text contains "Capital Improvement Projects (...)" and possibly "Disaster Recovery Projects"

# Let's clean the text first (remove page numbers etc if needed, but maybe not strictly necessary)
# text = re.sub(r'Page \d+ of \d+.*', '', text)

# Find all indices of project starts
project_matches = list(re.finditer(r'([^\n]+)\n\n\(cid:190\) Updates:', text))

projects_found = []

# Function to check if a project is disaster related
def is_disaster(name, section_header):
    if "FEMA" in name or "CalOES" in name or "CalJPIA" in name:
        return True
    if "Disaster" in section_header:
        return True
    return False

# Iterate through matches
for i in range(len(project_matches)):
    match = project_matches[i]
    name = match.group(1).strip()
    start_index = match.start()
    
    # Determine the end of this project block (start of next match or end of text)
    if i < len(project_matches) - 1:
        end_index = project_matches[i+1].start()
    else:
        end_index = len(text)
        
    block = text[start_index:end_index]
    
    # Find the section header preceding this project
    # Search backwards from start_index for a line containing "Projects (" or similar
    # or just "Capital Improvement Projects" or "Disaster Recovery Projects"
    preceding_text = text[:start_index]
    # Reverse search for header
    header_match = re.search(r'(Capital Improvement Projects|Disaster Recovery Projects)[^\n]*', preceding_text[::-1])
    section_header = ""
    if header_match:
        section_header = header_match.group(0)[::-1]
    
    # Determine if disaster
    # Also check if name is in funding_names to correct loose matches if needed
    # But names should match exactly or closely
    
    project_type = "disaster" if is_disaster(name, section_header) else "capital"
    
    # Extract start date
    # Look for "Begin Construction:" or "Advertise:"
    # Also check "Updates:" for dates
    
    start_date_match = re.search(r'Begin Construction:\s*([^\n]+)', block, re.IGNORECASE)
    advertise_match = re.search(r'Advertise:\s*([^\n]+)', block, re.IGNORECASE)
    
    start_date = None
    if start_date_match:
        start_date = start_date_match.group(1).strip()
    elif advertise_match:
        start_date = advertise_match.group(1).strip() # Fallback?
    
    # Check if started in 2022
    started_in_2022 = False
    if start_date and "2022" in start_date:
        started_in_2022 = True
    
    # Special case: "Construction was completed November 2022" -> might have started in 2022?
    # Or "Updates: ... 2022 ... received bids" -> Started
    if not started_in_2022:
        if "2022" in block:
             # Look for context
             if re.search(r'Begin [cC]onstruction.*2022', block):
                 started_in_2022 = True
             elif re.search(r'Advertise.*2022', block):
                 started_in_2022 = True
             elif re.search(r'Construction was completed.*2022', block):
                 # If completed in 2022, it likely started in 2022 or 2021. 
                 # Given the prompt asks for "started in 2022", I should be careful.
                 # "Westward Beach Road Repair Project" -> Updates: "City working...". Schedule: "Summer 2023" -> Not 2022.
                 # "Bluffs Park Shade Structure" -> "Construction was completed November 2022". 
                 # Did it start in 2022? Small projects likely yes.
                 # I'll flag it for review or include it if the prompt implies simple 2022 matching.
                 # Hint says: "Dates (st, et fields) use flexible formats... Use substring matching".
                 # It doesn't explicitly say "completed in 2022 implies started in 2022".
                 # But if I can't find a start date, and it finished in 2022, maybe. 
                 # However, "Begin Construction" is the most direct map to "st".
                 # Let's stick to "Begin Construction" or explicit start indicators first.
                 pass
             
             # Check for "On [Date] 2022 ... awarded contract" -> Start is close.
             if re.search(r'awarded the contract.*2022', block, re.IGNORECASE):
                 started_in_2022 = True
    
    projects_found.append({
        "name": name,
        "type": project_type,
        "start_date_raw": start_date,
        "block_preview": block[:200], # For debugging
        "started_in_2022": started_in_2022
    })

print("__RESULT__:")
print(json.dumps(projects_found))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json'}

exec(code, env_args)
