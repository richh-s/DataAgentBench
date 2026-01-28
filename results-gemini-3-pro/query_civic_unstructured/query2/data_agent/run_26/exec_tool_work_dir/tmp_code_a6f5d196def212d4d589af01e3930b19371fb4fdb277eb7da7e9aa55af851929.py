code = """import json

# Fetch file paths
d_key = "var_function-call-14510963906005286500"
f_key = "var_function-call-14510963906005285081"
d_path = locals()[d_key]
f_path = locals()[f_key]

# Load data
with open(d_path, "r") as f:
    docs = json.load(f)
with open(f_path, "r") as f:
    funds = json.load(f)

# Build known names set
known_names = set()
for item in funds:
    name = item.get("Project_Name", "").strip()
    if name:
        known_names.add(name)

found_projects = []

for doc in docs:
    # Use splitlines for safety
    lines = doc.get("text", "").splitlines()
    current_project = None
    buffer = []
    
    for line in lines:
        stripped = line.strip()
        if stripped in known_names:
            # Process the previous project block
            if current_project:
                block_text = " ".join(buffer).lower()
                
                # Check for "park"
                is_park = False
                if "park" in current_project.lower():
                    is_park = True
                elif "park" in block_text:
                    is_park = True
                
                # Check for completion in 2022
                is_complete = False
                if "completed" in block_text and "2022" in block_text:
                    if "was completed" in block_text:
                        is_complete = True
                    elif "completed," in block_text:
                        is_complete = True
                
                if is_park and is_complete:
                    found_projects.append(current_project)
            
            # Start new block
            current_project = stripped
            buffer = []
        else:
            if current_project:
                buffer.append(stripped)
    
    # Process the last block
    if current_project:
        block_text = " ".join(buffer).lower()
        is_park = False
        if "park" in current_project.lower():
            is_park = True
        elif "park" in block_text:
            is_park = True
            
        is_complete = False
        if "completed" in block_text and "2022" in block_text:
            if "was completed" in block_text:
                is_complete = True
            elif "completed," in block_text:
                is_complete = True
        
        if is_park and is_complete:
            found_projects.append(current_project)

# Deduplicate found projects
unique_projects = list(set(found_projects))

# Calculate total funding
total_funding = 0
for item in funds:
    name = item.get("Project_Name", "").strip()
    if name in unique_projects:
        amount_str = item.get("Amount", "0")
        try:
            total_funding += int(amount_str)
        except:
            pass

print("__RESULT__:")
print(json.dumps({"projects": unique_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json', 'var_function-call-13072667451122930611': 500}

exec(code, env_args)
