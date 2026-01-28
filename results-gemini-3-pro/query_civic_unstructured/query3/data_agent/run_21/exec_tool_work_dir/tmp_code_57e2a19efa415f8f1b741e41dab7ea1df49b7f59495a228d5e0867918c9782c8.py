code = """import json
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-13907770032762226910'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-12554270162172100471'], 'r') as f:
    civic_docs = json.load(f)

def normalize_name(name):
    # Simple string manipulation instead of regex
    if "(FEMA" in name:
        name = name.split("(FEMA")[0]
    if "(CalOES" in name:
        name = name.split("(CalOES")[0]
    if "(CalJPIA" in name:
        name = name.split("(CalJPIA")[0]
    return name.strip().lower()

extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Handle messy text
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    
    current_status = None
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if "Capital Improvement Projects" in line:
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction"
            elif "(Not Started)" in line:
                current_status = "not started"
            i += 1
            continue
        
        # Heuristic for Project Name
        if current_status and not line.startswith('(') and not line.startswith('Page') and not line.startswith('Agenda Item'):
            if i + 1 < len(lines):
                next_line = lines[i+1]
                # Check keywords in next line
                if "cid:" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                    p_name = line
                    p_text = ""
                    p_status_refined = current_status
                    j = i + 1
                    
                    while j < len(lines):
                        sub_line = lines[j]
                        if "Capital Improvement Projects" in sub_line:
                            break
                        
                        # Check start of new project
                        if not sub_line.startswith('(') and not sub_line.startswith('Page') and not sub_line.startswith('Agenda Item'):
                            if j + 1 < len(lines):
                                next_sub = lines[j+1]
                                if "cid:" in next_sub or "Updates:" in next_sub or "Project Description:" in next_sub:
                                    break
                        
                        p_text += sub_line + " "
                        
                        if current_status == "construction":
                            if "Construction was completed" in sub_line or "Notice of completion" in sub_line:
                                p_status_refined = "completed"
                        
                        j += 1
                    
                    extracted_projects.append({
                        "Project_Name": p_name,
                        "Status": p_status_refined,
                        "Full_Text": p_text
                    })
                    i = j - 1
        i += 1

df_extracted = pd.DataFrame(extracted_projects)

relevant_doc_names = set()
doc_lookup = {}

if not df_extracted.empty:
    for idx, row in df_extracted.iterrows():
        p_name = row['Project_Name']
        p_text = row['Full_Text']
        
        # Check relevance
        is_relevant = False
        if "emergency" in p_name.lower() or "fema" in p_name.lower():
            is_relevant = True
        elif "emergency" in p_text.lower() or "fema" in p_text.lower():
            is_relevant = True
            
        norm_name = normalize_name(p_name)
        doc_lookup[norm_name] = row['Status']
        doc_lookup[p_name.lower()] = row['Status']
        
        if is_relevant:
            relevant_doc_names.add(norm_name)

final_results = []

for idx, row in df_funding.iterrows():
    f_name = row['Project_Name']
    norm_f_name = normalize_name(f_name)
    
    is_f_relevant = "emergency" in f_name.lower() or "fema" in f_name.lower()
    is_doc_relevant = norm_f_name in relevant_doc_names
    
    if is_f_relevant or is_doc_relevant:
        status = doc_lookup.get(norm_f_name) or doc_lookup.get(f_name.lower()) or "Unknown"
        final_results.append({
            "Project_Name": f_name,
            "Funding_Source": row['Funding_Source'],
            "Amount": row['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-17503695109884766973': ['civic_docs'], 'var_function-call-17503695109884764492': ['Funding'], 'var_function-call-17012209582147726936': 'file_storage/function-call-17012209582147726936.json', 'var_function-call-13907770032762226910': 'file_storage/function-call-13907770032762226910.json', 'var_function-call-12554270162172100471': 'file_storage/function-call-12554270162172100471.json'}

exec(code, env_args)
