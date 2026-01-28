code = """import json
import pandas as pd
import re

# Load data
funding_path = locals()['var_function-call-12949068118131678804']
docs_path = locals()['var_function-call-12949068118131677021']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
# Dict: {Name: Amount}
funding_map = funding_df.groupby('Project_Name')['Amount'].sum().to_dict()

extracted_projects = []
current_section = "Unknown"

# Parsing logic
for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_proj_name = None
    current_proj_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check header
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # Save previous
            if current_proj_name:
                extracted_projects.append({
                    "name": current_proj_name,
                    "section": current_section,
                    "full_text": " ".join(current_proj_text)
                })
            current_section = line
            current_proj_name = None
            current_proj_text = []
            continue

        # Check for new project start
        # Look for pattern: Line followed by "Updates:" or "Project Description:"
        is_new = False
        if i + 1 < len(lines):
            next_l = lines[i+1].strip()
            # The bullet characters might vary, so check substring
            if "Updates:" in next_l or "Project Description:" in next_l:
                is_new = True
        
        if is_new:
            if current_proj_name:
                extracted_projects.append({
                    "name": current_proj_name,
                    "section": current_section,
                    "full_text": " ".join(current_proj_text)
                })
            current_proj_name = line
            current_proj_text = []
        else:
            if current_proj_name:
                current_proj_text.append(line)

    # Save last
    if current_proj_name:
        extracted_projects.append({
            "name": current_proj_name,
            "section": current_section,
            "full_text": " ".join(current_proj_text)
        })

# Analyze projects
total_funding = 0
matched_projects = []

for p in extracted_projects:
    p_name = p['name']
    p_text = p['full_text']
    p_section = p['section']
    
    # 1. Determine if Disaster Related
    is_disaster = False
    # Check section
    if "Disaster" in p_section:
        is_disaster = True
    # Check name keywords
    if any(k in p_name for k in ["FEMA", "CalOES", "Woolsey", "Disaster"]):
        is_disaster = True
    # Check text keywords (optional, based on hints "topic field contains... keywords")
    # Hint: "Projects have two types: 'capital' and 'disaster' ... The topic field contains comma-separated keywords."
    # The text parsing I did aggregates lines. I should check for topic keywords in the text.
    # Common topics: "FEMA", "fire", etc.
    if "FEMA" in p_text or "CalOES" in p_text or "Woolsey" in p_text:
        is_disaster = True
        
    # 2. Determine Start Date
    # Look for "Begin Construction: <Date>"
    # Or "Start Date"
    # Need to handle flexible formats.
    # Hint: "Dates (st, et fields) use flexible formats... Use substring matching... for year-based queries."
    # I will look for "Begin Construction" and check if it has "2022"
    
    started_2022 = False
    # Regex for Begin Construction
    # Matches "Begin Construction: <text>"
    match = re.search(r"Begin [Cc]onstruction:?\s*([A-Za-z0-9\s]+)", p_text)
    if match:
        date_str = match.group(1)
        if "2022" in date_str:
            started_2022 = True
    else:
        # Fallback: Check if "Advertise" date is 2022? Or "Start"?
        # "started in 2022" usually implies construction start.
        # Let's check for "Start: ... 2022" just in case.
        if "Start:" in p_text and "2022" in p_text.split("Start:")[1].split("\n")[0]:
             started_2022 = True

    # 3. Join Funding
    if is_disaster and started_2022:
        # Match name to funding DB
        # Exact match first
        amount = 0
        if p_name in funding_map:
            amount = funding_map[p_name]
        else:
            # Try fuzzy or clean?
            # Maybe the extracted name has extra spaces?
            clean_name = p_name.strip()
            if clean_name in funding_map:
                amount = funding_map[clean_name]
        
        if amount > 0:
            total_funding += amount
            matched_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-12949068118131678804': 'file_storage/function-call-12949068118131678804.json', 'var_function-call-12949068118131677021': 'file_storage/function-call-12949068118131677021.json'}

exec(code, env_args)
