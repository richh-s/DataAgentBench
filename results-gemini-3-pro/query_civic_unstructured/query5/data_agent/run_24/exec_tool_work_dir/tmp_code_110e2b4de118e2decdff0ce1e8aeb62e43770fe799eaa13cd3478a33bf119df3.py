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
    # Regex: Title line, newlines, optional bullet/junk, "Updates:"
    pattern = r'([^\n]+)\n+(?:(?:\(cid:190\)|[^\w\s])\s*)?Updates:'
    
    matches = list(re.finditer(pattern, text))
    if not matches:
        matches = list(re.finditer(r'([^\n]+)\n+\s*Updates:', text))

    for i in range(len(matches)):
        name = matches[i].group(1).strip()
        
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
    
    # Logic: Find rows in funding_df where Project_Name matches p_name
    # OR Project_Name starts with p_name + " (" (assuming suffix)
    # Be careful of partial matches (e.g. "Park" matches "Park Improvement")
    # So we check for exact match or "Name ("
    
    # We'll normalize names to be safe (strip whitespace)
    matches = funding_df[
        (funding_df['Project_Name'] == p_name) | 
        (funding_df['Project_Name'].str.startswith(p_name + " ("))
    ]
    
    # Sum amount
    # Convert Amount to numeric (it might be string in JSON)
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
    "projects": matched_funding_records,
    "debug_all_extracted": projects[:5] # Debug
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
