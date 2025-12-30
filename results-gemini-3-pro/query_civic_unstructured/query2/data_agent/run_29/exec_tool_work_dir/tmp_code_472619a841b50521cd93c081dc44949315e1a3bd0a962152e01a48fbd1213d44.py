code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-18248731954071622536'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-18328159169731343039'], 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Identify indices of project headers
    # A header is a line before a line containing "Updates:" or "Project Description:"
    
    header_indices = []
    for i in range(1, len(lines)):
        curr = lines[i]
        # Check for markers
        if "Updates:" in curr or "Project Description:" in curr:
            # Candidate header at i-1
            # Check if i-1 is not another marker (unlikely)
            header_indices.append(i-1)
            
    # Sort and unique
    header_indices = sorted(list(set(header_indices)))
    
    for k in range(len(header_indices)):
        start_idx = header_indices[k]
        end_idx = header_indices[k+1] if k+1 < len(header_indices) else len(lines)
        
        # Project Name
        p_name = lines[start_idx]
        
        # Content
        p_text = " ".join(lines[start_idx+1:end_idx])
        
        projects.append({'name': p_name, 'text': p_text})

# Filtering
completed_park_projects = []
df_funding = pd.DataFrame(funding_data)
funding_names = set(df_funding['Project_Name'].unique())

final_names = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Topic "park"
    # Check if "park" is in name or text
    # Hint: "The topic field contains comma-separated keywords. Common topics include: 'park'..."
    # Since we don't have the topic field pre-extracted, we search keywords.
    if "park" not in name.lower() and "park" not in text:
        continue
        
    # Status "completed" in "2022"
    is_completed_2022 = False
    
    # Logic: Look for "completed" and "2022"
    # Also "notice of completion filed ... 2023" might imply 2022 completion but let's stick to explicit completion date.
    # Sample: "Construction was completed November 2022"
    
    if "completed" in text and "2022" in text:
         # simple check: are they close?
         # find index of 'completed' and '2022'
         # This is a heuristic.
         is_completed_2022 = True
    elif "complete construction" in text and "2022" in text:
         is_completed_2022 = True
    
    if is_completed_2022:
        # Resolve name against Funding DB
        clean_name = name
        
        # Exact match
        if clean_name in funding_names:
            final_names.append(clean_name)
        else:
            # Check substrings
            match_found = False
            for fn in funding_names:
                # Check if fn is inside clean_name or clean_name is inside fn
                if fn in clean_name or clean_name in fn:
                    final_names.append(fn)
                    match_found = True
                    # prioritize exact matches or longer matches? 
                    # If we found one, maybe sufficient.
            
            if not match_found:
                # Try checking if lines[start_idx] included the bullet point char
                pass

# Remove duplicates
final_names = list(set(final_names))

# Sum amount
total = df_funding[df_funding['Project_Name'].isin(final_names)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total_funding": float(total), "projects": final_names}))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json'}

exec(code, env_args)
