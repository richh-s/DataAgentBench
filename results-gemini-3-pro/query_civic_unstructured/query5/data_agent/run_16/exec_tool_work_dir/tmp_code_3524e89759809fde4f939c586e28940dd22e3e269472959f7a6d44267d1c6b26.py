code = """import json
import pandas as pd

# Load data
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
    
    # 1. Check Disaster
    is_disaster = False
    if "Disaster" in p_section:
        is_disaster = True
    if any(k in p_name for k in ["FEMA", "CalOES", "Woolsey", "Disaster"]):
        is_disaster = True
    if "FEMA" in p_text or "CalOES" in p_text:
        is_disaster = True
        
    # 2. Check Start Date (2022)
    started_2022 = False
    
    # Check for "Begin Construction: ... 2022"
    # Find "Begin Construction"
    idx = p_text.find("Begin Construction")
    if idx == -1:
        idx = p_text.find("Begin construction")
    
    if idx != -1:
        # Extract next 50 chars
        snippet = p_text[idx:idx+50]
        if "2022" in snippet:
            started_2022 = True
    
    # If not found, maybe check "Start Construction" or just "Construction: ... 2022" if appropriate?
    # Or "Advertize"? No, stick to Construction or strict start.
    # What if "Construction was completed November 2022"? That means it started before or in 2022.
    # But prompt says "started in 2022". Completed in 2022 might mean started in 2021.
    # However, "Bluffs Park Shade Structure ... Construction was completed November 2022".
    # Did it start in 2022? Maybe.
    # "Broad Beach Road Water Quality Repair ... Construction was completed, November 2022".
    # If I only look for "Begin Construction ... 2022", I might miss these?
    # But usually "Status Report" lists "Updates: Construction was completed...".
    # It doesn't explicitly state start date in that summary sometimes.
    # But if "Begin Construction: Fall 2023", it's future.
    # If "Updates: Construction was completed November 2022", can I infer start?
    # Maybe I shouldn't unless explicitly stated.
    # The prompt says "For each project mentioned, you may need to extract... st: Start time/date".
    # This implies there is a field or text indicating start.
    # I will stick to "Begin Construction" containing "2022".

    # 3. Join
    if is_disaster and started_2022:
        amount = funding_map.get(p_name, 0)
        # Try finding suffix versions in funding map if amount is 0?
        # Or finding base name in funding map if p_name has suffix?
        if amount == 0:
            # Try to see if p_name is in Funding DB with a suffix
            # e.g. p_name="Birdview Avenue Improvements" -> Funding has "Birdview Avenue Improvements (CalOES Project)"
            # Iterate funding keys?
            # Or assume the text name matches one of them exactly?
            # If the text name is "Birdview Avenue Improvements" and it is NOT in funding map, that's a problem.
            # But the Funding DB has "Birdview Avenue Improvements" ($79000). So it matches.
            pass
        
        if amount > 0:
            total_funding += amount
            matched_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json'}

exec(code, env_args)
