code = """import json

# Load funding data
with open(locals()['var_function-call-14384747128822080394'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-12725139888695263289'], 'r') as f:
    civic_docs = json.load(f)

# Create a map for funding lookup
# Normalize names (strip) just in case
funding_map = {item['Project_Name'].strip(): item['Amount'] for item in funding_data}

extracted_candidates = []
matched_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect section start
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
            
        # Detect section end (any other Capital or Disaster header)
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design_section = False
        
        # Another stop condition: specific headers that might appear
        if line.startswith("Capital Improvement Projects") and "(Design)" not in line:
            in_design_section = False

        if in_design_section:
            # Skip bullet points and metadata
            if line.startswith("(cid:") or line.startswith("Updates:") or \
               line.startswith("Project Schedule:") or line.startswith("Estimated Schedule:") or \
               line.startswith("Page") or line.startswith("Agenda Item") or \
               line.endswith(":") or \
               line.lower().startswith("complete design") or \
               line.lower().startswith("advertise") or \
               line.lower().startswith("begin construction"):
                continue
            
            # This line is a candidate project name
            extracted_candidates.append(line)

# Now try to match candidates with funding_map
# We need to filter by Amount > 50000
count = 0
final_list = []

# Use set to deduplicate candidates
unique_candidates = set(extracted_candidates)

for cand in unique_candidates:
    # Exact match check
    if cand in funding_map:
        amount = float(funding_map[cand])
        if amount > 50000:
            count += 1
            final_list.append(cand)
    else:
        # Fallback: check if the candidate is contained in a funding project name or vice versa?
        # The prompt says "matches the project names".
        # Let's try to see if there's a loose match?
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": final_list, "candidates": list(unique_candidates)}))"""

env_args = {'var_function-call-14384747128822080394': 'file_storage/function-call-14384747128822080394.json', 'var_function-call-12725139888695263289': 'file_storage/function-call-12725139888695263289.json'}

exec(code, env_args)
