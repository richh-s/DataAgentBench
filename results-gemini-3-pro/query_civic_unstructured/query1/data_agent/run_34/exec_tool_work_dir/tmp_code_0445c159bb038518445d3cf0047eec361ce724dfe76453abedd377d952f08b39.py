code = """import pandas as pd
import json

# Load data
funding_path = locals()['var_function-call-16409169562152250528']
docs_path = locals()['var_function-call-16409169562152248833']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# 1. Process Funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
# Filter > 50000
funding_df = funding_df[funding_df['Amount'] > 50000]

# Filter out Disaster suffixes
def is_disaster(name):
    # Check for disaster suffixes or keywords in name
    # Hints: "(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)"
    keywords = ['(FEMA', '(CalOES', '(CalJPIA']
    return any(k in name for k in keywords)

funding_df['is_disaster'] = funding_df['Project_Name'].apply(is_disaster)
capital_funding = funding_df[~funding_df['is_disaster']].copy()

# 2. Process Docs
design_projects = set()

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    in_design_section = False
    
    # Iterate lines
    for i, line in enumerate(lines):
        clean_line = line.strip()
        
        # Check section headers
        if "Capital Improvement Projects (Design)" in clean_line:
            in_design_section = True
            continue
        # Stop conditions
        if "Capital Improvement Projects (Construction)" in clean_line or \
           "Capital Improvement Projects (Not Started)" in clean_line or \
           "Disaster Recovery Projects" in clean_line:
            in_design_section = False
            continue
        
        if in_design_section:
            # Look for Updates marker or bullet point that starts a section
            if "Updates:" in clean_line or "(cid:190)" in clean_line:
                 # Look back for name
                 k = i - 1
                 while k >= 0:
                     prev_line = lines[k].strip()
                     # Skip junk
                     if not prev_line or "Page" in prev_line or "Agenda Item" in prev_line or prev_line.isdigit():
                         k -= 1
                         continue
                     # Skip section header if we hit it going back
                     if "Capital Improvement Projects (Design)" in prev_line:
                         break 
                     
                     # Found candidate
                     design_projects.add(prev_line)
                     break

# 3. Matching
matches = []
count = 0
matched_projects = set()

doc_names = list(design_projects)

for idx, row in capital_funding.iterrows():
    f_name = row['Project_Name'].strip()
    
    found = False
    for d_name in doc_names:
        d_name_clean = d_name.strip()
        
        # Matching Logic
        fn_lower = f_name.lower()
        dn_lower = d_name_clean.lower()
        
        # Exact match or substring
        if fn_lower == dn_lower or fn_lower in dn_lower or dn_lower in fn_lower:
            found = True
            
        if found:
            matches.append((f_name, d_name))
            matched_projects.add(f_name)
            break

print("Matches found:", len(matched_projects))
print("Matched Project Names:", list(matched_projects))

print("__RESULT__:")
print(json.dumps(len(matched_projects)))"""

env_args = {'var_function-call-16409169562152250528': 'file_storage/function-call-16409169562152250528.json', 'var_function-call-16409169562152248833': 'file_storage/function-call-16409169562152248833.json'}

exec(code, env_args)
