code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-8110328958345281458'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open(locals()['var_function-call-13323334654076855934'], 'r') as f:
    civic_docs = json.load(f)

def clean_name(name):
    # Regex with double backslashes for JSON safety
    name = re.sub(r'\s*\(FEMA(?:/CalOES)?(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA(?: Project)?\)\s*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(FEMA\)\s*', '', name, flags=re.IGNORECASE)
    name = name.replace("Warningn", "Warning")
    return name.strip().lower()

doc_projects = {}
current_status = "Unknown"

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Status Headers
        if "Capital Improvement Projects (" in line:
            if "Design" in line:
                current_status = "Design"
            elif "Construction" in line:
                current_status = "Construction"
            elif "Not Started" in line:
                current_status = "Not Started"
            i += 1
            continue
        
        # Check for Project Name candidate
        # Heuristic: Valid name followed by Updates/Description
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for bullet points or keywords often starting the block
            # (cid:190) is distinct.
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                p_name = line
                # Basic validation
                if len(p_name) > 3 and "Page" not in p_name:
                    # Extract text block
                    p_text = ""
                    j = i + 1
                    while j < len(lines):
                        l = lines[j].strip()
                        if "Capital Improvement Projects (" in l:
                            break
                        # Check start of next project
                        if j + 1 < len(lines):
                            nl = lines[j+1].strip()
                            if ("(cid:190)" in nl or "Updates:" in nl or "Project Description:" in nl) and len(l) > 3 and "Page" not in l:
                                break
                        p_text += l + " "
                        j += 1
                    
                    # Determine Status
                    final_status = current_status
                    lower_text = p_text.lower()
                    if "construction was completed" in lower_text or "notice of completion" in lower_text:
                        final_status = "Completed"
                    
                    # Determine Relevance
                    is_related = False
                    if "fema" in lower_text or "emergency" in lower_text or "caloes" in lower_text:
                        is_related = True
                    
                    c_name = clean_name(p_name)
                    doc_projects[c_name] = {
                        "status": final_status,
                        "is_related": is_related,
                        "text": p_text
                    }
                    
                    i = j
                    continue
        i += 1

final_results = []
for rec in funding_data:
    fname = rec['Project_Name']
    fsource = rec['Funding_Source']
    amount = rec['Amount']
    
    c_fname = clean_name(fname)
    
    # Check if related by funding info
    f_related = False
    lower_fname = fname.lower()
    lower_fsource = fsource.lower()
    if "fema" in lower_fname or "emergency" in lower_fname or "fema" in lower_fsource or "emergency" in lower_fsource:
        f_related = True
        
    # Match
    match = doc_projects.get(c_fname)
    
    doc_related = False
    status = "Unknown"
    if match:
        doc_related = match['is_related']
        status = match['status']
        
    if f_related or doc_related:
        final_results.append({
            "Project_Name": fname,
            "Funding_Source": fsource,
            "Amount": amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-8110328958345281458': 'file_storage/function-call-8110328958345281458.json', 'var_function-call-13323334654076855934': 'file_storage/function-call-13323334654076855934.json'}

exec(code, env_args)
