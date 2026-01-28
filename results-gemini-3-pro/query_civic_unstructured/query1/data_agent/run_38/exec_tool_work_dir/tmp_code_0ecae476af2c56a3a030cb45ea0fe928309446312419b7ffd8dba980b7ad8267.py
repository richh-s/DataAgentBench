code = """import json
import pandas as pd
import re

# Load funding data
funding_data = pd.read_json('var_function-call-5988651082647865980')

# Filter for funding > 50,000
high_funding_projects = funding_data[funding_data['Amount'] > 50000]['Project_Name'].tolist()

# Load civic docs
with open('var_function-call-9407752625735979853', 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    # We are looking for "Capital Improvement Projects (Design)"
    # It might be split across lines or have slightly different formatting, so we'll search for the phrase.
    
    # Iterate through lines to find projects
    # A simple state machine approach
    capture_mode = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if "Capital Improvement Projects" in line and "Design" in line:
            capture_mode = True
            continue
        elif "Capital Improvement Projects" in line and ("Construction" in line or "Not Started" in line):
            capture_mode = False
            continue
        elif "Disaster Recovery Projects" in line:
            capture_mode = False
            continue
        elif "Agenda Item" in line or "Page" in line and "of" in line:
            continue
            
        if capture_mode:
            # Heuristic to identify project name:
            # It should not be a bullet point or "Updates:" or "Project Schedule:"
            if line.startswith("(cid:") or line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Complete Design:") or line.startswith("Advertise:") or line.startswith("Begin Construction:") or line.startswith("Final Design:"):
                continue
            
            # If it's a date or short generic string, skip
            if len(line) < 5:
                continue
            
            # This line is likely a project name
            # Clean up potential artifacts
            project_name = line
            capital_design_projects.append(project_name)

# Remove duplicates and clean
capital_design_projects = sorted(list(set(capital_design_projects)))

# Now match with high funding projects
# We'll use exact match or basic containment. The database description says names can be joined.
# Let's try exact match first, then normalize if needed.

count = 0
matched_projects = []

for cp in capital_design_projects:
    # Check if this project is in the high funding list
    # The names in text might be slightly different (e.g., extra spaces, casing).
    # Let's try to find a match in high_funding_projects
    
    # Direct match
    if cp in high_funding_projects:
        count += 1
        matched_projects.append(cp)
    else:
        # fuzzy match or substring
        # Check if cp is a substring of any high_funding_project or vice versa
        # But we must be careful not to over-match.
        # Let's normalize both
        cp_norm = cp.lower().replace("  ", " ").strip()
        found = False
        for hfp in high_funding_projects:
            hfp_norm = hfp.lower().replace("  ", " ").strip()
            if cp_norm == hfp_norm:
                count += 1
                matched_projects.append(hfp)
                found = True
                break
        
        if not found:
             # Try partial match if one is contained in another significantly
             # E.g. "PCH Median Improvements" vs "PCH Median Improvements Project"
             for hfp in high_funding_projects:
                hfp_norm = hfp.lower().replace("project", "").strip()
                cp_without_proj = cp.lower().replace("project", "").strip()
                if hfp_norm and cp_without_proj and (hfp_norm == cp_without_proj):
                     count += 1
                     matched_projects.append(hfp)
                     break


print("__RESULT__:")
print(json.dumps({"count": count, "matched_projects": matched_projects, "extracted_capital_design_projects": capital_design_projects}))"""

env_args = {'var_function-call-5988651082647865980': 'file_storage/function-call-5988651082647865980.json', 'var_function-call-9407752625735979853': 'file_storage/function-call-9407752625735979853.json'}

exec(code, env_args)
