code = """import json
import re
import pandas as pd

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

# Load funding data
funding_df = pd.DataFrame(json.load(open(locals()['var_function-call-4052442815910590834'])))

projects = []

for doc in docs:
    text = doc['text']
    # Simplified Regex: 
    # Capture a line (Name), then newlines, then anything (bullet) followed by "Updates:"
    pattern = r'([^\n]+)\n+.*Updates:'
    
    matches = list(re.finditer(pattern, text))
    
    for i in range(len(matches)):
        name = matches[i].group(1).strip()
        # Filter out if name is too long (likely not a title)
        if len(name) > 100: 
            continue
            
        # content range
        content_start = matches[i].end()
        if i < len(matches) - 1:
            content_end = matches[i+1].start()
        else:
            content_end = len(text)
            
        content = text[content_start:content_end]
        
        # Start Date
        st = None
        # Begin Construction
        m_st = re.search(r'Begin Construction:?\s*([^\n]*)', content, re.IGNORECASE)
        if m_st:
            st = m_st.group(1).strip()
        
        # Is Disaster?
        is_disaster = False
        upper_content = content.upper()
        upper_name = name.upper()
        
        # Keywords check
        if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
            is_disaster = True
        
        # Add to list
        projects.append({
            "extracted_name": name,
            "st": st,
            "is_disaster": is_disaster
        })

# Filter projects
# Started in 2022 -> st contains "2022"
# Disaster related -> is_disaster is True
target_projects = []
for p in projects:
    if p['is_disaster'] and p['st'] and '2022' in p['st']:
        target_projects.append(p)

# Now join with Funding
total_funding = 0
matched_funding_records = []

for p in target_projects:
    p_name = p['extracted_name']
    
    # Check for funding
    # Match exact or "Name (..."
    matches = funding_df[
        (funding_df['Project_Name'] == p_name) | 
        (funding_df['Project_Name'].str.startswith(p_name + " ("))
    ]
    
    amount_sum = pd.to_numeric(matches['Amount']).sum()
    
    if amount_sum > 0:
        total_funding += amount_sum
        matched_funding_records.append({
            "extracted_name": p_name,
            "st": p['st'],
            "matched_rows": len(matches),
            "amount": amount_sum
        })

result = {
    "total_funding": total_funding,
    "projects": matched_funding_records
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
