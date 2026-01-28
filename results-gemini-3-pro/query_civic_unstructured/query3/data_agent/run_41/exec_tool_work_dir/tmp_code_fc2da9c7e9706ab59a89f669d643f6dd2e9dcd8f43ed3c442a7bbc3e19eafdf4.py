code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-12443390616213881639'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-13902106228594848871'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

projects = []

# Keywords
topic_keywords = ["park", "road", "fema", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "emergency"]

def extract_dates(text):
    st = None
    et = None
    # Flexible date patterns
    # Begin Construction: Fall 2023
    # Advertise: Summer 2023
    # Complete Construction: Summer 2025
    
    begin_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9\s]+)', text)
    if begin_match:
        st = begin_match.group(1).strip()
    else:
        # Fallback to Advertise
        adv_match = re.search(r'Advertise:?\s*([A-Za-z0-9\s]+)', text)
        if adv_match:
            st = adv_match.group(1).strip()
            
    comp_match = re.search(r'Complete [Cc]onstruction:?\s*([A-Za-z0-9\s]+)', text)
    if comp_match:
        et = comp_match.group(1).strip()
    
    return st, et

def get_status(section_status, text):
    if section_status == "design":
        return "design"
    elif section_status == "not_started":
        return "not started"
    elif section_status == "construction":
        if "completed" in text.lower() and "notice of completion" in text.lower():
             return "completed"
        if "construction was completed" in text.lower():
            return "completed"
        return "design" # Default for active construction if not completed? Or maybe "design" as "in progress".
        # Based on hint: "design" (in planning/design phase). But construction is later.
        # However, the hint only gives 3 statuses. "Completed" is finished. "Not started" is not started.
        # "Design" is the only active one. So I'll map active construction to "design".
    return "design" # Default

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_type = None
    current_section_status = None
    
    # Buffer to hold potential project name
    name_buffer = []
    
    # Store parsed projects to associate details
    # We need to process line by line.
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check headers
        if "Capital Improvement Projects" in line:
            current_type = "capital"
            if "(Design)" in line:
                current_section_status = "design"
            elif "(Construction)" in line:
                current_section_status = "construction"
            elif "(Not Started)" in line:
                current_section_status = "not_started"
            i += 1
            continue
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            if "(Design)" in line:
                current_section_status = "design"
            elif "(Construction)" in line:
                current_section_status = "construction"
            elif "(Not Started)" in line:
                current_section_status = "not_started"
            i += 1
            continue
            
        # Check for project block start marker (cid:190) which often appears as special char or text
        # In the provided text representation it shows as "(cid:190)" or maybe a bullet point.
        # The preview showed "(cid:190)".
        
        if line.startswith("(cid:190)") or line.startswith("¾"): # encoding
            # The lines before this (in name_buffer) are the project name.
            # Clean up name buffer
            proj_name = " ".join([n for n in name_buffer if n]).strip()
            
            # Now extract details from this block until next project
            # Block ends at next project name (which is hard to detect without lookahead) or next header.
            # Actually, the structure seems to be: Name -> Updates -> Schedule -> Next Name
            # The Next Name is detected because it's followed by (cid:190) eventually.
            # So we capture everything from here until next (cid:190) or Header.
            
            block_lines = []
            block_lines.append(line)
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if "Capital Improvement Projects" in next_line or "Disaster Recovery Projects" in next_line:
                    break
                if next_line.startswith("(cid:190)") or next_line.startswith("¾"):
                    # This indicates start of another block?
                    # Wait, a project has "(cid:190) Updates" AND "(cid:190) Project Schedule".
                    # So multiple (cid:190) per project.
                    # We need to distinguish between a new project and a subsection.
                    # Project names don't start with (cid:190).
                    # Subsections do.
                    # So if we hit a line that is NOT starting with (cid:190) and looks like a project name?
                    # How to tell a project name from regular text?
                    # Project names are usually capitalized, short, and distinct.
                    # But the surest way is that they are followed by (cid:190) block.
                    # But we are currently IN a block.
                    # If we see a line that is followed by (cid:190) later, it's a new project name.
                    pass
                
                # Let's collect all lines until we see a line that is likely a new project name.
                # A new project name is followed by (cid:190) on the next non-empty line.
                
                # Peek ahead to check if next_line is a name
                # find next non-empty line after next_line
                k = j + 1
                found_next_marker = False
                while k < len(lines):
                    if lines[k].strip():
                        if lines[k].strip().startswith("(cid:190)") or lines[k].strip().startswith("¾"):
                            found_next_marker = True
                        break
                    k += 1
                
                if found_next_marker and not (next_line.startswith("(cid:190)") or next_line.startswith("¾")):
                    # next_line is likely a new project name
                    break
                
                block_lines.append(next_line)
                j += 1
            
            # Process the block
            block_text = "\n".join(block_lines)
            
            # Extract info
            topics = []
            for kw in topic_keywords:
                if kw.lower() in proj_name.lower() or kw.lower() in block_text.lower():
                    topics.append(kw)
            
            # Status
            status = get_status(current_section_status, block_text)
            
            # Dates
            st, et = extract_dates(block_text)
            
            # Store
            if proj_name:
                projects.append({
                    "Project_Name": proj_name,
                    "topics": topics,
                    "type": current_type,
                    "status": status,
                    "st": st,
                    "et": et,
                    "full_text": block_text # for debugging or further search
                })
            
            # Reset buffer
            name_buffer = []
            i = j
            continue
            
        else:
            if line:
                name_buffer.append(line)
            i += 1

# Filter projects
relevant_projects = []
for p in projects:
    is_related = False
    # Check topics
    if "emergency" in p['topics'] or "fema" in p['topics']:
        is_related = True
    # Check name
    if "emergency" in p['Project_Name'].lower() or "fema" in p['Project_Name'].lower():
        is_related = True
        
    if is_related:
        relevant_projects.append(p)

# Join with Funding
final_results = []
for p in relevant_projects:
    p_name = p['Project_Name']
    
    # Find matching funding
    # Match criteria: Funding Project Name starts with p_name (to handle suffixes)
    # or p_name starts with Funding Project Name (unlikely given suffixes in funding)
    # Also ignore case
    
    matches = df_funding[df_funding['Project_Name'].apply(lambda x: x.lower().startswith(p_name.lower()) or p_name.lower().startswith(x.lower()))]
    
    if not matches.empty:
        for _, row in matches.iterrows():
            final_results.append({
                "Project_Name": p['Project_Name'], # or row['Project_Name']? User asked for "project names". I'll provide the one from document usually as it's the "entity". Or the one from funding. Let's use funding name to be precise about source? 
                # Actually, if I match "Project X" to "Project X (FEMA)", the name "Project X (FEMA)" is more descriptive.
                # But the status comes from "Project X".
                # I'll output the Funding Project Name if available, else Document name.
                # But wait, one doc project might match multiple funding records.
                "Project_Name": row['Project_Name'],
                "Funding_Source": row['Funding_Source'],
                "Amount": row['Amount'],
                "Status": p['status']
            })
    else:
        # If no funding found, should I include it? The user asks for "funding sources, amounts".
        # If no funding, maybe "None"?
        # But usually in SQL questions, inner join is implied.
        # "What are the project names, funding sources, amounts..."
        # I will include only those with funding info found.
        pass

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-6697639078713076568': ['civic_docs'], 'var_function-call-6697639078713075367': ['Funding'], 'var_function-call-4303639865338753386': 'file_storage/function-call-4303639865338753386.json', 'var_function-call-13902106228594848871': 'file_storage/function-call-13902106228594848871.json', 'var_function-call-12443390616213881639': 'file_storage/function-call-12443390616213881639.json'}

exec(code, env_args)
