code = """import json
import pandas as pd

funding_path = locals()['var_function-call-12949068118131678804']
docs_path = locals()['var_function-call-12949068118131677021']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Funding Map
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_map = funding_df.groupby('Project_Name')['Amount'].sum().to_dict()

extracted_projects = []
current_section = "Unknown"

for doc in civic_docs:
    # Escape check: using double backslash for newline
    lines = doc['text'].split('\n')
    current_proj_name = None
    current_proj_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if current_proj_name:
                extracted_projects.append({"name": current_proj_name, "section": current_section, "full_text": " ".join(current_proj_text)})
            current_section = line
            current_proj_name = None
            current_proj_text = []
            continue

        is_new = False
        if i + 1 < len(lines):
            next_l = lines[i+1].strip()
            if "Updates:" in next_l or "Project Description:" in next_l:
                is_new = True
        
        if is_new:
            if current_proj_name:
                extracted_projects.append({"name": current_proj_name, "section": current_section, "full_text": " ".join(current_proj_text)})
            current_proj_name = line
            current_proj_text = []
        else:
            if current_proj_name:
                current_proj_text.append(line)

    if current_proj_name:
        extracted_projects.append({"name": current_proj_name, "section": current_section, "full_text": " ".join(current_proj_text)})

total_funding = 0
matched_projects = []

for p in extracted_projects:
    p_name = p['name']
    p_text = p['full_text']
    p_section = p['section']
    
    # Check Disaster
    is_disaster = False
    if "Disaster" in p_section:
        is_disaster = True
    # Check keywords in name or text
    # Hint: "The topic field contains comma-separated keywords... Common topics include: 'park', 'road', 'FEMA'..."
    # The prompt implies I should extract 'topic' field.
    # In my text parsing, I didn't explicitly extract 'topic' field, but I have the full text block.
    # I can search for "FEMA", "CalOES", "Woolsey", "Disaster" in the text block.
    if "FEMA" in p_text or "CalOES" in p_text or "Woolsey" in p_text or "Disaster" in p_text:
        is_disaster = True
    if "FEMA" in p_name or "CalOES" in p_name:
        is_disaster = True
        
    # Check Start Date 2022
    started_2022 = False
    # Look for "Begin Construction" with "2022"
    # Case insensitive for "Begin Construction"
    lower_text = p_text.lower()
    if "begin construction" in lower_text:
        # Find index
        idx = lower_text.find("begin construction")
        # Check substring
        snippet = lower_text[idx:idx+60] # Capture date
        if "2022" in snippet:
            started_2022 = True
            
    # Also check "Start Construction"
    if "start construction" in lower_text:
        idx = lower_text.find("start construction")
        snippet = lower_text[idx:idx+60]
        if "2022" in snippet:
            started_2022 = True

    if is_disaster and started_2022:
        amount = funding_map.get(p_name, 0)
        # Handle exact name mismatch?
        # If amount is 0, check if p_name is contained in a funding key or vice versa?
        # The prompt says "Project_Name ... matches ... extracted".
        # But extracted might have spaces.
        if amount == 0:
            # Try stripping
            amount = funding_map.get(p_name.strip(), 0)
            
        if amount > 0:
            total_funding += amount
            matched_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json', 'var_function-call-18218646092846697457': 'Done'}

exec(code, env_args)
