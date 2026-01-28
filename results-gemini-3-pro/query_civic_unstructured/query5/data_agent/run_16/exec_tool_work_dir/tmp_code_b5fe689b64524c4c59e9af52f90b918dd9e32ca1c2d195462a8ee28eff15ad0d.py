code = """import json
import pandas as pd

funding_path = locals()['var_function-call-12949068118131678804']
docs_path = locals()['var_function-call-12949068118131677021']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_map = funding_df.groupby('Project_Name')['Amount'].sum().to_dict()

extracted_projects = []
current_section = "Unknown"

for doc in civic_docs:
    # Use splitlines to avoid newline escaping issues
    lines = doc['text'].splitlines()
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
    
    # Disaster check
    is_disaster = False
    # Check section
    if "Disaster" in p_section:
        is_disaster = True
    # Check text/name keywords
    keywords = ["FEMA", "CalOES", "Woolsey", "Disaster"]
    if any(k in p_name for k in keywords):
        is_disaster = True
    if any(k in p_text for k in keywords):
        is_disaster = True
        
    # Start Date 2022 check
    started_2022 = False
    lower_text = p_text.lower()
    
    # Check Begin Construction or Construction Start
    targets = ["begin construction", "start construction", "construction start"]
    for t in targets:
        idx = lower_text.find(t)
        if idx != -1:
            snippet = lower_text[idx:idx+60]
            if "2022" in snippet:
                started_2022 = True
                break
    
    if is_disaster and started_2022:
        amount = funding_map.get(p_name, 0)
        # Try stripping
        if amount == 0:
            amount = funding_map.get(p_name.strip(), 0)
        
        # If still 0, check for fuzzy match in funding keys?
        # e.g. text: "Project A" -> Funding: "Project A (FEMA)"
        # Or text: "Project A (FEMA)" -> Funding: "Project A"
        # The prompt says Funding Name matches Extracted Name.
        # But maybe extracted name is "Project A" and funding name is "Project A (FEMA Project)"?
        # Let's check for containment match if exact fails.
        if amount == 0:
            for fname in funding_map:
                # Check if fname starts with p_name or p_name starts with fname
                if p_name in fname or fname in p_name:
                    # Only map if close enough (avoid mapping "Project" to "Project 1")
                    # If extraction is "Clover Heights Storm Drainage Improvements" and funding is "Clover Heights Storm Drain", containment might fail or be tricky.
                    # But if extraction is "Clover Heights Storm Drain" and funding is "Clover Heights Storm Drain (FEMA Project)", p_name in fname works.
                    # Let's try simple containment.
                    if p_name.strip() == fname.strip(): # Should be covered
                        amount = funding_map[fname]
                        break
                    # Be careful with short names.
                    
                    # Given the prompt, let's rely on exact match first.
                    pass
        
        if amount > 0:
            # Check for duplicates? If multiple projects match?
            # Assuming names are unique in text.
            total_funding += amount
            matched_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json', 'var_function-call-18218646092846697457': 'Done'}

exec(code, env_args)
