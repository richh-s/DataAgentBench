code = """import json

# Load Funding Data
path_funding = locals()['var_function-call-13808490642390448201']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

funded_projects = set()
for item in funding_data:
    amt = float(item['Amount'])
    if amt > 50000:
        funded_projects.add(item['Project_Name'].strip())

# Load Civic Docs
path_docs = locals()['var_function-call-4985696884690537041']
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

extracted = []

for doc in civic_docs:
    text = doc['text']
    # Start of Design Section
    marker = "Capital Improvement Projects (Design)"
    idx = text.find(marker)
    
    if idx == -1:
        continue
        
    start_search = idx + len(marker)
    
    # End of Design Section
    # Look for next header
    end_idx = -1
    for stop_m in ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]:
        stop_i = text.find(stop_m, start_search)
        if stop_i != -1:
            if end_idx == -1 or stop_i < end_idx:
                end_idx = stop_i
    
    if end_idx == -1:
        subtext = text[start_search:]
    else:
        subtext = text[start_search:end_idx]
        
    lines = [l.strip() for l in subtext.splitlines() if l.strip()]
    
    for i in range(len(lines) - 1):
        curr = lines[i]
        nxt = lines[i+1]
        
        # Skip garbage
        if "Page " in curr or "Agenda Item" in curr:
            continue
            
        # Check next line for indicators
        # Use simple strings
        if "Updates:" in nxt or "Project Schedule" in nxt:
            extracted.append(curr)

extracted = list(set(extracted))

matches = []
misses = []

for p in extracted:
    if p in funded_projects:
        matches.append(p)
    else:
        misses.append(p)

res = {"count": len(matches), "matches": matches, "misses": misses}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-13808490642390448090': ['Funding'], 'var_function-call-13808490642390448201': 'file_storage/function-call-13808490642390448201.json', 'var_function-call-13808490642390448312': 'file_storage/function-call-13808490642390448312.json', 'var_function-call-4985696884690537041': 'file_storage/function-call-4985696884690537041.json'}

exec(code, env_args)
