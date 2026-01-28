code = """import json

# Load Data
with open(locals()['var_function-call-8110328958345281458'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-13323334654076855934'], 'r') as f:
    civic_docs = json.load(f)

def clean_name(name):
    # Manual cleanup to avoid regex issues
    n = name.strip()
    suffixes = [
        "(FEMA Project)", "(CalOES Project)", "(FEMA/CalOES Project)", 
        "(CalJPIA Project)", "(FEMA)", "(CalOES)"
    ]
    for s in suffixes:
        if n.endswith(s):
            n = n.replace(s, "").strip()
        # Handle case where it's in the middle? Usually suffix.
        # Try replace anyway
        n = n.replace(s, "").strip()
    
    n = n.replace("Warningn", "Warning")
    return n.lower()

doc_projects = {}
current_status = "Unknown"

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Headers
        if "Capital Improvement Projects (" in line:
            if "Design" in line:
                current_status = "Design"
            elif "Construction" in line:
                current_status = "Construction"
            elif "Not Started" in line:
                current_status = "Not Started"
            i += 1
            continue
            
        # Check Project
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check markers
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                p_name = line
                if len(p_name) > 3 and "Page" not in p_name and "Agenda Item" not in p_name:
                    # Extract Text
                    p_text = ""
                    j = i + 1
                    while j < len(lines):
                        l = lines[j].strip()
                        if "Capital Improvement Projects (" in l:
                            break
                        if j + 1 < len(lines):
                            nl = lines[j+1].strip()
                            if ("(cid:190)" in nl or "Updates:" in nl or "Project Description:" in nl) and len(l) > 3 and "Page" not in l and "Agenda Item" not in l:
                                break
                        p_text += l + " "
                        j += 1
                    
                    # Analyze
                    status = current_status
                    lower_text = p_text.lower()
                    if "construction was completed" in lower_text or "notice of completion" in lower_text:
                        status = "Completed"
                        
                    is_rel = False
                    if "fema" in lower_text or "emergency" in lower_text or "caloes" in lower_text:
                        is_rel = True
                        
                    c_name = clean_name(p_name)
                    doc_projects[c_name] = {"status": status, "is_related": is_rel}
                    
                    i = j
                    continue
        i += 1

results = []
for rec in funding_data:
    fname = rec['Project_Name']
    # Check relevance
    is_f_rel = "fema" in fname.lower() or "emergency" in fname.lower() or "fema" in rec['Funding_Source'].lower()
    
    c_fname = clean_name(fname)
    match = doc_projects.get(c_fname)
    
    is_d_rel = False
    status = "Unknown"
    if match:
        is_d_rel = match['is_related']
        status = match['status']
        
    if is_f_rel or is_d_rel:
        results.append({
            "Project_Name": fname,
            "Funding_Source": rec['Funding_Source'],
            "Amount": rec['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8110328958345281458': 'file_storage/function-call-8110328958345281458.json', 'var_function-call-13323334654076855934': 'file_storage/function-call-13323334654076855934.json'}

exec(code, env_args)
