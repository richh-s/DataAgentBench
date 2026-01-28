code = """import json
import pandas as pd
import re

# Load funding data
funding_data = json.load(open(locals()['var_function-call-10596372274131677177']))
funding_df = pd.DataFrame(funding_data)

# Load civic docs
docs = json.load(open(locals()['var_function-call-10596372274131674166']))

projects_found = []

for doc in docs:
    text = doc['text']
    # Split lines
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Identify projects
    # A project starts with a line that is NOT a bullet, followed by a line that IS a bullet.
    # The bullet in the text seems to be "(cid:190)".
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line is potentially a project title
        # It shouldn't start with the bullet marker
        if not line.startswith('(cid:190)') and not line.startswith('Updates:') and not line.startswith('Project Description:'):
            # Look ahead
            if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
                project_name = line
                # Collect text
                project_text = ""
                i += 1
                while i < len(lines):
                    # Check if we hit the start of a NEW project
                    # Which is a line not starting with bullet, followed by one that does.
                    if not lines[i].startswith('(cid:190)') and \
                       (i + 1 < len(lines) and lines[i+1].startswith('(cid:190)')):
                        break
                    
                    # Also check for section headers like "Capital Improvement Projects (Construction)"
                    # These headers might be captured as project names if we are not careful.
                    # But section headers usually don't have "(cid:190)" immediately after.
                    # Let's check the preview:
                    # "Capital Improvement Projects (Design)" -> followed by "2022 Morning View..."
                    # So section headers are NOT followed by (cid:190).
                    # "2022 Morning View..." -> followed by "(cid:190) Updates:"
                    # So our logic holds.
                    
                    project_text += lines[i] + " "
                    i += 1
                
                projects_found.append({
                    'Project_Name': project_name,
                    'text': project_text
                })
                continue
        i += 1

# Filter projects
matched_projects = []

for p in projects_found:
    name = p['Project_Name']
    text = p['text']
    
    # Check for Park related
    # Keywords: park, playground, recreation
    is_park = False
    if re.search(r'\bpark\b', name, re.IGNORECASE) or \
       re.search(r'\bplayground\b', name, re.IGNORECASE) or \
       re.search(r'\brecreation\b', name, re.IGNORECASE):
        is_park = True
    
    # Check for Completed in 2022
    # Phrases: "Construction was completed[,] <Month> 2022" or "Complete Construction: <Month> 2022"
    # Also "Construction completed: <Month> 2022"
    
    # Regex to capture date associated with completion
    # We look for "completed" or "complete construction" followed by a date
    # Note: text has (cid:190) bullets.
    
    completed_2022 = False
    
    # Pattern 1: Construction was completed[,] [Month] [Year]
    m1 = re.search(r'Construction was completed,?\s+([A-Za-z]+)\s+(\d{4})', text, re.IGNORECASE)
    if m1:
        if m1.group(2) == '2022':
            completed_2022 = True
            
    # Pattern 2: Complete Construction: [Month] [Year] or [Season] [Year]
    if not completed_2022:
        m2 = re.search(r'Complete Construction:\s+([A-Za-z]+)\s+(\d{4})', text, re.IGNORECASE)
        if m2:
            if m2.group(2) == '2022':
                completed_2022 = True

    # Pattern 3: Construction completed [Month] [Year]
    if not completed_2022:
        m3 = re.search(r'Construction completed\s+([A-Za-z]+)\s+(\d{4})', text, re.IGNORECASE)
        if m3:
            if m3.group(2) == '2022':
                completed_2022 = True

    if is_park and completed_2022:
        matched_projects.append(name)

# Join with Funding
total_funding = 0
funded_projects = []

for pname in matched_projects:
    # Find in funding_df
    # Try exact match first
    match = funding_df[funding_df['Project_Name'] == pname]
    if match.empty:
        # Try stripping whitespace
        match = funding_df[funding_df['Project_Name'] == pname.strip()]
    
    if not match.empty:
        amount = pd.to_numeric(match['Amount']).sum()
        total_funding += amount
        funded_projects.append({'name': pname, 'amount': amount})
    else:
        # Fuzzy match or check partial?
        # The prompt says names match. Let's assume they match closely.
        # Maybe handle case sensitivity?
        match = funding_df[funding_df['Project_Name'].str.lower() == pname.lower()]
        if not match.empty:
            amount = pd.to_numeric(match['Amount']).sum()
            total_funding += amount
            funded_projects.append({'name': pname, 'amount': amount})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'projects': funded_projects}))"""

env_args = {'var_function-call-15461874300401161107': ['civic_docs'], 'var_function-call-15461874300401161542': ['Funding'], 'var_function-call-10596372274131677177': 'file_storage/function-call-10596372274131677177.json', 'var_function-call-10596372274131674166': 'file_storage/function-call-10596372274131674166.json'}

exec(code, env_args)
