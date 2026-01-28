code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-14523358791805029933'], 'r') as f:
    funding_data = json.load(f)

# Create a lookup for funding info by Project_Name
funding_map = {item['Project_Name']: item for item in funding_data}
funding_project_names = set(funding_map.keys())

# Load Civic Docs
# var_function-call-18295450404769870360 is the key for civic_docs result
with open(locals()['var_function-call-18295450404769870360'], 'r') as f:
    civic_docs = json.load(f)

projects_extracted = []

# Headers mapping to Status
# "Capital Improvement Projects (Design)" -> Design
# "Capital Improvement Projects (Construction)" -> Completed? No, "Construction" is a phase. 
# Prompt says statuses are: "design", "completed", "not started".
# Maybe "Construction" -> "design"? Or is there a "construction" status?
# Prompt says: "Projects have three statuses: 'design', 'completed', and 'not started'".
# Wait, "Construction" is not in the list. 
# Maybe "Construction" falls under "design" (in progress) or I should output "construction" if it's there?
# Actually, the prompt says "design" (in planning/design phase). Construction is later.
# Let's look at the text: "Capital Improvement Projects (Construction)"
# And "Capital Improvement Projects (Not Started)"
# And "Capital Improvement Projects (Design)"
# Maybe "Construction" should be mapped to "design" or "completed"?
# Usually "Construction" is distinct. But if I must choose from the 3, "design" is the closest to "active/in progress" before completion.
# However, usually "Construction" is distinct. I will capture the header text first and decide later or map it if obvious.
# Actually, looking at the hints: "Projects have three statuses: 'design', 'completed', 'not started'".
# Maybe "Construction" is NOT one of the statuses I should output? 
# Or maybe the hint is just examples? "Projects have three statuses: ...". This sounds exhaustive.
# Let's check the text for "Bluffs Park Shade Structure". It says "Construction was completed November 2022".
# And it is listed under "Capital Improvement Projects (Construction)". Wait.
# If it's completed, why is it under Construction?
# Maybe the section is "Projects in Construction phase" or "Recently Completed"?
# The header in the text is "Capital Improvement Projects (Construction)".
# Under it: "Malibu Road Slope Repairs... Updates: Project is currently under construction".
# "Bluffs Park Shade Structure... Updates: Construction was completed November 2022".
# So this section contains both.
# I will extract the status from the text if possible, or use the section as a fallback.
# Actually, the prompt says "extract... status: Current status (e.g., 'design', 'completed', 'not started')".
# I'll try to extract explicit status from "Updates". If "completed" appears in updates, use that.
# If "under construction", maybe I should use "design" or just "construction" (but prompt listed 3).
# I'll output "construction" if that's what it is, but if the prompt strictly enforces 3, I'll have to map.
# Given "Hints: Projects have three statuses...", I should probably stick to those if possible, but "construction" is a very valid status.
# I will just output what I find (e.g. section header or text) and maybe the user can interpret or I map "Construction" to "design" (as "in progress") if needed.
# But for "Bluffs Park Shade Structure", it is "completed".
# Let's extract the raw status first.

regex_header = re.compile(r"Capital Improvement Projects \((.*?)\)", re.IGNORECASE)
regex_project_start = re.compile(r"^\s*(.+?)\s*$", re.MULTILINE) # Too broad
# Better: Look for lines followed by "(cid:190) Updates:" or "(cid:190) Project Description:"

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status_context = "Unknown"
    
    # We will iterate lines and look for patterns
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Headers
        header_match = regex_header.search(line)
        if header_match:
            current_status_context = header_match.group(1).lower() # design, construction, not started
            i += 1
            continue
            
        # Check for Project Name candidates
        # A project name is usually a line that is NOT empty, and the NEXT non-empty line starts with (cid:190) Updates or Project Description
        # We need to look ahead
        
        if not line:
            i += 1
            continue
            
        # Look ahead for marker
        j = i + 1
        found_marker = False
        marker_type = ""
        while j < len(lines):
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                # Found a marker
                # Check if it looks like a marker line
                if "Updates:" in next_line or "Project Description:" in next_line:
                    found_marker = True
                    marker_type = next_line
                break
            else:
                # Next line is text but not a marker.
                # If the project name is multi-line, this might be part of it, 
                # but based on preview, project names are single lines.
                # So if we hit another text line before marker, 'line' is probably not a project name 
                # OR the project name is multiple lines.
                # Let's assume single line project names for now as per preview.
                break
        
        if found_marker:
            # 'line' is likely the project name
            p_name = line
            # Extract description/updates until next project or end
            # The block starts at j (marker)
            # Find end of block (next project start or header)
            
            # To be robust, let's collect text until we hit a known header or a new project start.
            # But "New Project Start" is hard to detect without the lookahead.
            # Simplified approach: Collect text until we hit a line that *could* be a project name (followed by marker) OR a Header.
            
            p_description = []
            k = j
            while k < len(lines):
                l_text = lines[k].strip()
                
                # Check if l_text is a header
                if regex_header.search(l_text):
                    break
                
                # Check if l_text is start of NEXT project
                # We need to look ahead again from k to see if l_text is followed by marker
                # parsing like this is slow/complex.
                # Alternative: identify all start indices first.
                p_description.append(l_text)
                k += 1
            
            full_desc = " ".join(p_description)
            
            # Determine Status
            # Check text for "completed"
            status = current_status_context
            if "completed" in full_desc.lower() and "construction" in full_desc.lower():
                # "Construction was completed"
                status = "completed"
            elif "not started" in full_desc.lower():
                status = "not started"
            elif "design" in full_desc.lower() and status == "construction":
                # unexpected, but keep context
                pass
                
            extracted_projects.append({
                "Project_Name": p_name,
                "Status": status,
                "Description": full_desc,
                "Filename": doc['filename']
            })
            
            # Move i to k
            i = k
        else:
            i += 1

# Normalize Status
# Map "construction" -> "design" ? No, better to keep it or map to 'capital' type logic?
# Prompt says "Projects have three statuses: 'design', 'completed', 'not started'".
# If I have "construction", and it's not "completed", it's effectively "active".
# "design" is also active.
# I will map "construction" to "design" IF strict adherence is needed, but "Construction" is a valid phase.
# However, "design" (in planning/design phase) vs "Construction" (building).
# I'll leave it as "construction" if extracted, or map if I see fit. 
# Wait, let's look at the result I get.

# Filter and Join
final_results = []

for p in extracted_projects:
    name = p['Project_Name']
    desc = p['Description']
    
    # Check relevance
    is_relevant = False
    if "emergency" in name.lower() or "fema" in name.lower():
        is_relevant = True
    if "emergency" in desc.lower() or "fema" in desc.lower():
        is_relevant = True
        
    if is_relevant:
        # Find funding
        # Try exact match
        funding = funding_map.get(name)
        
        # If not found, try stripping non-ascii or extra spaces
        if not funding:
             # Try simple normalization
             norm_name = name.strip()
             funding = funding_map.get(norm_name)
        
        if not funding:
            # Try fuzzy or substring?
            # "Projects have suffixes like (FEMA Project)"
            # Maybe the extracted name doesn't have the suffix, but Funding does?
            # Or extracted name HAS suffix?
            # Let's check if name is substring of any funding key or vice versa
            pass
            
        funding_source = funding['Funding_Source'] if funding else "N/A"
        amount = funding['Amount'] if funding else "N/A"
        
        final_results.append({
            "Project_Name": name,
            "Funding_Source": funding_source,
            "Amount": amount,
            "Status": p['Status']
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-9697041815942477768': 'file_storage/function-call-9697041815942477768.json', 'var_function-call-292566524849709372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18295450404769870360': 'file_storage/function-call-18295450404769870360.json', 'var_function-call-14523358791805029933': 'file_storage/function-call-14523358791805029933.json'}

exec(code, env_args)
