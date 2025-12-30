code = """import json

# Load data
with open(locals()['var_function-call-96073466168105581'], 'r') as f:
    civic_docs = json.load(f)

results = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = "Unknown"
    potential_header = "Unknown"
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect Project Name (heuristic)
        # If line contains "Updates:" or "Project Description:", the previous non-marker line was likely the title.
        # But here we just want to see the context of "Spring 2022"
        
        if "(cid:" in line and ("Updates:" in line or "Project Description:" in line):
            current_project = potential_header
        elif not line.startswith("(cid:") and not line.startswith("Page") and "Agenda Item" not in line:
            potential_header = line
            
        if "Spring 2022" in line:
            results.append({
                "project": current_project,
                "line": line
            })

print("__RESULT__:")
print(json.dumps(results[:20], indent=2))"""

env_args = {'var_function-call-9243709298217568361': ['civic_docs'], 'var_function-call-9243709298217569292': ['Funding'], 'var_function-call-1240620947166126016': 'file_storage/function-call-1240620947166126016.json', 'var_function-call-1240620947166124723': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-96073466168105581': 'file_storage/function-call-96073466168105581.json', 'var_function-call-96073466168105534': 'file_storage/function-call-96073466168105534.json'}

exec(code, env_args)
