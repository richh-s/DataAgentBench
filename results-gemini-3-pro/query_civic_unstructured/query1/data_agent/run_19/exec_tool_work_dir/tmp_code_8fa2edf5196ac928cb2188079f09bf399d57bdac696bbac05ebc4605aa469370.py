code = """import json

# Load funding
with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
    funding_data = json.load(f)

# Get high value projects
high_funding_projects = []
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            high_funding_projects.append(item['Project_Name'])
    except:
        pass

# Load text
with open(locals()['var_function-call-9654609134184919281'], 'r') as f:
    civic_docs = json.load(f)

# Extract relevant text sections
relevant_texts = []
for doc in civic_docs:
    text = doc['text']
    # Find start
    start_idx = text.find("Capital Improvement Projects (Design)")
    if start_idx == -1: continue
    
    # Find end
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    relevant_texts.append(text[start_idx:end_idx])

# Check for matches
matches = set()
for p_name in high_funding_projects:
    for section in relevant_texts:
        # Check if project name is in section
        # We need to be careful about partial matches, e.g. "Park" matching "Park Improvements"
        # But Project Names are usually full specific names.
        # Let's check if the name appears as a line or substring.
        # Given the prompt "matches the project names that can be extracted", exact substring match is likely intended.
        if p_name in section:
            matches.add(p_name)
            break 

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": list(matches)}))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json'}

exec(code, env_args)
