code = """import json

key_funding = "var_function-call-14384747128822080394"
key_docs = "var_function-call-12725139888695263289"

with open(locals()[key_funding], "r") as f:
    funding_data = json.load(f)

with open(locals()[key_docs], "r") as f:
    civic_docs = json.load(f)

funding_map = {item["Project_Name"].strip(): float(item["Amount"]) for item in funding_data}

extracted_candidates = []

for doc in civic_docs:
    text = doc["text"]
    # Use splitlines to avoid backslash issues
    lines = text.splitlines()
    in_design = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_design = True
            continue
            
        if "Capital Improvement Projects" in line and "(Design)" not in line:
            in_design = False
        if "Disaster Recovery Projects" in line:
            in_design = False
            
        if in_design:
            if line.startswith("(cid:") or line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Estimated Schedule:"):
                continue
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            if line.endswith(":"):
                continue
            
            lower_line = line.lower()
            if "complete design" in lower_line or "begin construction" in lower_line or "advertise" in lower_line:
                continue
                
            extracted_candidates.append(line)

unique_candidates = set(extracted_candidates)
matches = []
count = 0

for cand in unique_candidates:
    if cand in funding_map:
        if funding_map[cand] > 50000:
            count += 1
            matches.append(cand)

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "candidates": list(unique_candidates)}))"""

env_args = {'var_function-call-14384747128822080394': 'file_storage/function-call-14384747128822080394.json', 'var_function-call-12725139888695263289': 'file_storage/function-call-12725139888695263289.json'}

exec(code, env_args)
