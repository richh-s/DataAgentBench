code = """import json

# Load Funding Data
with open(locals()['var_function-call-13808490642390448201'], 'r') as f:
    funding_data = json.load(f)

funded_projects = set()
for item in funding_data:
    if float(item['Amount']) > 50000:
        funded_projects.add(item['Project_Name'].strip())

# Load Civic Docs
with open(locals()['var_function-call-4985696884690537041'], 'r') as f:
    civic_docs = json.load(f)

extracted_design_projects = []

for doc in civic_docs:
    text = doc['text']
    # Find the Design section
    start_marker = "Capital Improvement Projects (Design)"
    start_idx = text.find(start_marker)
    
    if start_idx != -1:
        search_start = start_idx + len(start_marker)
        
        end_idx = -1
        next_markers = ["Capital Improvement Projects (Construction)", 
                        "Capital Improvement Projects (Not Started)",
                        "Disaster Recovery Projects"]
        
        for nm in next_markers:
            idx = text.find(nm, search_start)
            if idx != -1:
                if end_idx == -1 or idx < end_idx:
                    end_idx = idx
        
        if end_idx == -1:
            section_text = text[search_start:]
        else:
            section_text = text[search_start:end_idx]
            
        lines = [line.strip() for line in section_text.split('\n') if line.strip()]
        
        # Identify project names
        for i in range(len(lines) - 1):
            current_line = lines[i]
            next_line = lines[i+1]
            
            if "Page " in current_line or "Agenda Item" in current_line:
                continue
            
            # Check markers in next line
            # (cid: markers or "Updates:" or "Project Schedule"
            if "(cid:" in next_line or "Updates:" in next_line or "Project Schedule" in next_line:
                extracted_design_projects.append(current_line)

# Deduplicate
extracted_design_projects = list(set(extracted_design_projects))

matches = []
misses = []

for p in extracted_design_projects:
    if p in funded_projects:
        matches.append(p)
    else:
        misses.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": len(matches),
    "matches": matches,
    "misses": misses
}))"""

env_args = {'var_function-call-13808490642390448090': ['Funding'], 'var_function-call-13808490642390448201': 'file_storage/function-call-13808490642390448201.json', 'var_function-call-13808490642390448312': 'file_storage/function-call-13808490642390448312.json', 'var_function-call-4985696884690537041': 'file_storage/function-call-4985696884690537041.json'}

exec(code, env_args)
