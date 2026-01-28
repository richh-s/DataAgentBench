code = """import json
import re
import pandas as pd

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

projects = []

for doc in docs:
    text = doc['text']
    # Regex to find project headers.
    # We look for a line (Project Name) followed by "Updates:" with optional bullet
    # Bullet can be (cid:190) or special chars. We escape parenthesis.
    pattern = r'([^\n]+)\n+(?:(?:\(cid:190\)|\u00be|¾|●|•)\s*)?Updates:'
    
    matches = list(re.finditer(pattern, text))
    
    if not matches:
        # Fallback for simple "Updates:"
        matches = list(re.finditer(r'([^\n]+)\n+Updates:', text))

    for i in range(len(matches)):
        start_idx = matches[i].start()
        # The project name is captured in group 1
        name = matches[i].group(1).strip()
        
        # content range
        content_start = matches[i].end()
        if i < len(matches) - 1:
            content_end = matches[i+1].start()
        else:
            content_end = len(text)
            
        content = text[content_start:content_end]
        
        # Extract dates
        st = None
        # Try to find "Begin Construction: <date>"
        m_st = re.search(r'Begin Construction:\s*([^\n]*)', content, re.IGNORECASE)
        if m_st:
            st = m_st.group(1).strip()
        else:
            # Try "Construction was completed <date>"
            m_comp = re.search(r'Construction was completed\D*(\w+\s+\d{4})', content, re.IGNORECASE)
            if m_comp:
                # If completed in 2022, we might count it? 
                # But query asks "started in 2022".
                # If completed in Nov 2022, it started earlier.
                # I'll stick to explicit start dates or "Begin Construction".
                # Or maybe "Construction Start: ..."
                pass
        
        # If no construction start, maybe "Advertise" is the start of the project execution phase?
        # But usually "started" = broke ground.
        # Let's collect "Advertise" just in case.
        m_adv = re.search(r'Advertise:\s*([^\n]*)', content, re.IGNORECASE)
        adv_date = m_adv.group(1).strip() if m_adv else None
        
        # Extract Type/Topics
        keywords = []
        is_disaster = False
        
        content_upper = content.upper()
        name_upper = name.upper()
        
        if "FEMA" in name_upper or "FEMA" in content_upper:
            is_disaster = True
        if "CALOES" in name_upper or "CALOES" in content_upper:
            is_disaster = True
        if "DISASTER" in name_upper or "DISASTER" in content_upper:
            is_disaster = True
        # CalJPIA
        if "CALJPIA" in name_upper or "CALJPIA" in content_upper:
            is_disaster = True
            
        # Check specific suffixes in name (extracted name usually doesn't have them in the text, but check)
        
        projects.append({
            "Project_Name": name,
            "st": st,
            "adv_date": adv_date,
            "is_disaster": is_disaster,
            "filename": doc['filename']
        })

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
