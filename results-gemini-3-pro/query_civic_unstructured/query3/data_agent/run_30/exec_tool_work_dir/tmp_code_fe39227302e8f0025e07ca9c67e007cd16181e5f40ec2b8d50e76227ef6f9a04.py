code = """import json
import re
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-8110328958345281458'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open(locals()['var_function-call-13323334654076855934'], 'r') as f:
    civic_docs = json.load(f)

# Helper function to clean project names for matching
def clean_name(name):
    # Remove common suffixes found in Funding table
    name = re.sub(r'\s*\(FEMA(?:/CalOES)?(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(FEMA\)\s*', '', name, flags=re.IGNORECASE)
    # Also handle typo "Warningn" -> "Warning"
    name = name.replace("Warningn", "Warning")
    return name.strip().lower()

# Parse Civic Docs
doc_projects = {}

status_map = {
    "Capital Improvement Projects (Design)": "Design",
    "Capital Improvement Projects (Construction)": "Construction", # Map to 'Completed' if constructed? Or just 'Construction'. Hint says: 'design', 'completed', 'not started'. 'Construction' usually means active. But let's see headers.
    # The hint says: "Projects have three statuses: 'design', 'completed', and 'not started'".
    # In the doc: "Capital Improvement Projects (Construction)" -> Wait, is "Construction" a status? 
    # The hint lists: "design", "completed", "not started".
    # "Construction" is likely "design" (in progress?) or its own.
    # Actually, if it's under construction, it's not "completed" and not "not started". Maybe I should output "Construction" or map to "Design" (as "in progress")?
    # Let's look at the doc content:
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    # And updates say "Construction was completed..." -> Status "Completed".
    # I will stick to the headers first, but if update says "Completed", I'll use that.
}

# Regex for headers
header_re = re.compile(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_status = None
    
    # Simple line-based parser
    # We look for headers to set status
    # We look for project names. Project names seem to be lines that are not empty, not headers, and followed by "Updates:" or "Project Description:" blocks.
    
    # Iterate lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for status header
        # The header in doc: "Capital Improvement Projects (Design)"
        # Note: the doc might have "Capital Improvement Projects and Disaster Recovery Projects Status Report" at top.
        
        if "Capital Improvement Projects (" in line:
            if "Design" in line:
                current_status = "Design"
            elif "Construction" in line:
                current_status = "Construction" # Will refine later
            elif "Not Started" in line:
                current_status = "Not Started"
            i += 1
            continue
            
        # Check for potential project name
        # A project name is usually followed by "(cid:190) Updates:" or "(cid:190) Project Description:" or similar markers in the text.
        # In the preview: "(cid:190)" is likely a bullet point character.
        # Let's look ahead.
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check if next line starts with update marker
            if next_line.startswith("(cid:190)") or "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line:
                project_name = line
                # Skip invalid names (like "Updates:", page numbers, etc)
                if len(project_name) < 3 or "Page" in project_name:
                    i += 1
                    continue
                
                # Extract description/text for this project
                # Read until next project or end of section
                # (Simple heuristic: read until next line that looks like a project name or header, or big gap)
                # Actually, reading until next "(cid:190)" block start for a *different* project is hard.
                # Let's just grab a chunk of lines or look for the next project start.
                
                # Identifying the end of a project block:
                # The next project starts with a Name line followed by `(cid:190)`.
                # So we can scan ahead.
                
                project_text = ""
                j = i + 1
                while j < len(lines):
                    l = lines[j].strip()
                    if "Capital Improvement Projects (" in l:
                        break
                    # Check if this line is a start of a new project
                    # New project name line (l) followed by marker (lines[j+1])
                    if j + 1 < len(lines):
                        nl = lines[j+1].strip()
                        if (nl.startswith("(cid:190)") or "Updates:" in nl or "Project Description:" in nl) and len(l) > 3 and "Page" not in l and "Agenda Item" not in l:
                            # Found new project start
                            break
                    project_text += l + " "
                    j += 1
                
                # Refine Status based on text
                # If text says "Construction was completed", status = "Completed"
                p_status = current_status
                if "Construction was completed" in project_text or "Notice of completion filed" in project_text:
                    p_status = "Completed"
                elif p_status == "Construction":
                    # If under construction and not completed, maybe "Under Construction"? 
                    # Hint: "Projects have three statuses: 'design', 'completed', and 'not started'".
                    # "Construction" phase projects are likely considered "Active" or just "Capital" type.
                    # But the hint statuses are specific. 
                    # Maybe "Construction" -> "Design" (as in 'Active')? No, 'Design' is 'Design'.
                    # Let's look at hint again. "Projects have three statuses: 'design', 'completed', and 'not started'."
                    # Maybe "Construction" is mapped to one of these?
                    # Or maybe the hint is non-exhaustive or I should output "Construction" if that's what it is.
                    # I will output "Construction" if not completed, or maybe "Design" is the wrong label for construction. 
                    # Wait, the user wants "statuses". I should provide the most accurate status. "Construction" is a valid status in the real world. I will use "Construction".
                    pass

                # Check keywords in project_text + name
                topics = []
                text_lower = (project_name + " " + project_text).lower()
                keywords = ["park", "road", "fema", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
                for kw in keywords:
                    if kw in text_lower:
                        topics.append(kw)
                
                # Special check for FEMA/Emergency relevance
                is_related = False
                if "fema" in text_lower or "emergency" in text_lower or "caloes" in text_lower:
                    is_related = True
                
                # Store
                c_name = clean_name(project_name)
                # If duplicate, keep latest?
                doc_projects[c_name] = {
                    "original_name": project_name,
                    "status": p_status,
                    "topics": topics,
                    "is_related_doc": is_related,
                    "full_text": project_text
                }
                
                i = j
                continue
        i += 1

# Join with Funding
results = []
seen_funding_ids = set()

for rec in funding_data:
    fid = rec['Funding_ID']
    f_name = rec['Project_Name']
    f_source = rec['Funding_Source']
    amount = rec['Amount']
    
    # Determine relevance from Funding record
    f_related = False
    if "fema" in f_name.lower() or "emergency" in f_name.lower() or "fema" in f_source.lower() or "emergency" in f_source.lower():
        f_related = True
        
    c_fname = clean_name(f_name)
    
    # Match with docs
    match = doc_projects.get(c_fname)
    
    # Determine final relevance
    is_relevant = f_related
    if match and match['is_related_doc']:
        is_relevant = True
    
    # Filter
    if is_relevant:
        status = "Unknown"
        if match:
            status = match['status']
        else:
            # Try partial match if exact match failed?
            # Or assume if it's in funding with "FEMA", it's relevant, but status is unknown.
            status = "Not Found in Docs" 

        # If status is "Not Found in Docs", and user wants statuses, maybe I should try harder to find it?
        # Maybe the name clean function wasn't enough.
        # But for now, let's list it.
        
        results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8110328958345281458': 'file_storage/function-call-8110328958345281458.json', 'var_function-call-13323334654076855934': 'file_storage/function-call-13323334654076855934.json'}

exec(code, env_args)
