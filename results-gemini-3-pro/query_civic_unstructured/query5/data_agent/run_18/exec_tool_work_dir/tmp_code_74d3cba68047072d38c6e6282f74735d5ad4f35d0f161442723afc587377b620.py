code = """import json

# Load data
with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

projects_to_check = ["2021 Annual Street Maintenance", "Broad Beach Road Water Quality Infrastructure Repairs", "Malibu Park Drainage Improvements"]

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_proj = None
    buffer = []
    
    for line in lines:
        line_clean = line.strip()
        
        # Check if new project
        found = False
        for p in projects_to_check:
            # simple check
            if p in line_clean or line_clean in p:
                if len(line_clean) > 10: # avoid short matches
                     found = p
                     break
        
        if found:
            if current_proj:
                print(f"--- TEXT FOR {current_proj} ---")
                print("\n".join(buffer[:10])) # print first 10 lines
            current_proj = found
            buffer = []
            continue
            
        if current_proj:
            buffer.append(line_clean)

    if current_proj:
        print(f"--- TEXT FOR {current_proj} ---")
        print("\n".join(buffer[:10]))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}}

exec(code, env_args)
