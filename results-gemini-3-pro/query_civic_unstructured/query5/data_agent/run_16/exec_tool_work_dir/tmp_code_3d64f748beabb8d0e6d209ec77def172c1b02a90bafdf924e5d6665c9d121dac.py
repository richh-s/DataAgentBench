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
    
    # Check Disaster
    is_disaster = False
    if "Disaster" in p_section:
        is_disaster = True
    keywords = ["FEMA", "CalOES", "Woolsey", "Disaster", "CalJPIA"]
    if any(k in p_name for k in keywords):
        is_disaster = True
    if any(k in p_text for k in keywords):
        is_disaster = True
        
    # Check Start Date 2022
    started_2022 = False
    lower_text = p_text.lower()
    
    targets = [
        "begin construction", "start construction", "construction start",
        "construction began", "construction commenced", "work started",
        "broke ground"
    ]
    
    for t in targets:
        idx = lower_text.find(t)
        if idx != -1:
            snippet = lower_text[idx:idx+60]
            if "2022" in snippet:
                started_2022 = True
                break
    
    if is_disaster and started_2022:
        amount = funding_map.get(p_name, 0)
        if amount == 0:
            amount = funding_map.get(p_name.strip(), 0)
        
        # Try to find matching funding if name is slightly different
        if amount == 0:
            # Check if p_name starts with a known funding name
            # or funding name starts with p_name
            # and verify disaster status of funding name?
            # E.g. p_name = "Corral Canyon Culvert Repairs"
            # funding = "Corral Canyon Culvert Repairs (FEMA Project)"
            # If p_name is contained in funding name, and funding name has extra suffix.
            for fname, amt in funding_map.items():
                if fname.startswith(p_name.strip()) and len(fname) > len(p_name):
                    # Potential match
                    # Only accept if suffix is one of the disaster ones?
                    # Or just assume it's the right project.
                    amount = amt
                    # But wait, funding map has multiple keys for same base?
                    # "Corral Canyon Culvert Repairs" ($54k)
                    # "Corral Canyon Culvert Repairs (FEMA Project)" ($43k)
                    # Which one to pick?
                    # If the text name was "Corral Canyon Culvert Repairs" (no suffix), and I classified it as disaster via text content.
                    # Should I take the base one? Or the FEMA one?
                    # Usually I should take the one matching the name.
                    # If text is "Corral Canyon Culvert Repairs", I take $54k.
                    # If the user wants "total funding for disaster-related projects", and this project is disaster-related.
                    # The funding table splits it. "Corral Canyon Culvert Repairs" might be the City match, "FEMA Project" the grant.
                    # I should probably sum ALL funding for the project if it's the same project.
                    # But the "Project_Name" field is the join key.
                    # If I join on Project_Name, I only get the specific record.
                    # "You will typically need to: ... Join the funding data ... based on Project_Name".
                    # This implies exact match join.
                    # So if extraction yields "Corral Canyon Culvert Repairs", I add $54k.
                    # I don't add the FEMA one unless the extraction matches it.
                    # This seems to be the strict interpretation.
                    amount = funding_map.get(p_name.strip(), 0)
                    break
        
        if amount > 0:
            # Avoid duplicates if p_name matches multiple times? 
            # (Unlikely with loop logic)
            total_funding += amount
            matched_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json', 'var_function-call-18218646092846697457': 'Done', 'var_function-call-17619093976837636519': {'total_funding': 85000, 'matched_projects': [{'name': 'Birdview Avenue Improvements (CalOES Project)', 'amount': 85000}]}}

exec(code, env_args)
