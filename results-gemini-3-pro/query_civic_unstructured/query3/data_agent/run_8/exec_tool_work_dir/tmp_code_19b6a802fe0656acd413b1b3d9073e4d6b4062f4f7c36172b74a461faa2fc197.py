code = """import json
import pandas as pd

# Files
f_civic = locals()['var_function-call-2910026112661516748']
f_funding = locals()['var_function-call-10585127880706054254']

with open(f_civic, 'r') as f:
    civic = json.load(f)
with open(f_funding, 'r') as f:
    funding = json.load(f)

df_funding = pd.DataFrame(funding)
projects = []

for doc in civic:
    text = doc['text']
    lines = [x.strip() for x in text.split('\n') if x.strip()]
    
    # Simple state machine
    status = "unknown"
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headers
        if "Capital Improvement Projects (Design)" in line:
            status = "design"
            i += 1; continue
        if "Capital Improvement Projects (Construction)" in line:
            status = "construction"
            i += 1; continue
        if "Capital Improvement Projects (Not Started)" in line:
            status = "not started"
            i += 1; continue
            
        # Project detection
        # Look for line with "Updates:" or "Project Description:"
        # The line BEFORE it is likely the Project Name (if it's not a header)
        
        if "Updates:" in line or "Project Description:" in line:
            # Found a description block start.
            # The previous line (i-1) should be the name.
            if i > 0:
                name = lines[i-1]
                # Check if name is a header?
                if "Capital Improvement Projects" in name:
                    i += 1; continue
                
                # Extract full text for this project
                # From name (i-1) until next name/header
                # We need to look ahead to find the next project start or header
                # This is tricky without knowing where the next one is.
                # But we can just iterate forward until we see a header or a new "Updates:"/"Description:" line
                
                p_text_lines = [name, line]
                j = i + 1
                while j < len(lines):
                    l2 = lines[j]
                    if "Capital Improvement Projects" in l2:
                        break
                    if "Updates:" in l2 or "Project Description:" in l2:
                        # Found next project's description start. 
                        # So l2 is the start of next project description.
                        # The line before l2 (lines[j-1]) is the next project's name.
                        # So we should stop BEFORE lines[j-1].
                        # But wait, lines[j-1] is part of the current project text? No, it's the name of the next one.
                        # So we stop at j-1.
                        # However, we must be careful if j-1 == i (immediate next).
                        # Usually there is text between.
                        # If j == i + 1, then lines[j] is Updates, lines[j-1] is lines[i].
                        # So we look ahead.
                        break
                    p_text_lines.append(l2)
                    j += 1
                
                # Note: if we broke because of next "Updates:", the loop ended at j.
                # lines[j] is the next Updates line. lines[j-1] is the next Name.
                # So we should exclude lines[j-1] from current text.
                if j < len(lines) and ("Updates:" in lines[j] or "Project Description:" in lines[j]):
                     # Remove the last line if it's the name of the next project
                     # Check if p_text_lines has more than 2 lines (Name, Updates...)
                     if len(p_text_lines) > 1:
                         p_text_lines.pop()
                
                full_text = " ".join(p_text_lines)
                
                # Check completion
                p_status = status
                if status == "construction" and "completed" in full_text.lower():
                    p_status = "completed"
                
                projects.append({"Project_Name": name, "Status": p_status, "Full_Text": full_text})
                
                # Continue loop?
                # We handled lines up to j (exclusive of j and j-1).
                # Actually, we should let the main loop handle the next project.
                # So we just increment i. But we already processed the block.
                # It's safer to just increment i normally, but then we re-process lines?
                # No, we only trigger on "Updates:".
                # So just i += 1 is fine.
        i += 1

# Filter
filtered = []
kws = ['emergency', 'fema']
for p in projects:
    # Check text
    if any(k in p['Full_Text'].lower() for k in kws):
        filtered.append(p)

df_p = pd.DataFrame(filtered)

# Join
if not df_p.empty:
    merged = pd.merge(df_funding, df_p, on='Project_Name', how='inner')
    res = merged[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')
else:
    res = []

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-9102831309616723132': ['civic_docs'], 'var_function-call-9102831309616723245': ['Funding'], 'var_function-call-12492854141756139028': 'file_storage/function-call-12492854141756139028.json', 'var_function-call-7907601960746092281': 'file_storage/function-call-7907601960746092281.json', 'var_function-call-10585127880706054254': 'file_storage/function-call-10585127880706054254.json', 'var_function-call-2910026112661516748': 'file_storage/function-call-2910026112661516748.json'}

exec(code, env_args)
