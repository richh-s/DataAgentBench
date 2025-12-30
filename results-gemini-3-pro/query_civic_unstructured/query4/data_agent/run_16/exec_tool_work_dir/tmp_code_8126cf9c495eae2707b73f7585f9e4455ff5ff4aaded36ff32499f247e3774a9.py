code = """import json
import re

with open(locals()['var_function-call-11024242700101333530'], 'r') as f:
    civic_docs = json.load(f)

spring_pattern = r"(Spring 2022|March 2022|April 2022|May 2022)"

results = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_name = "Unknown"
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Look ahead for "Updates:"
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
            
        if j < len(lines):
            next_l = lines[j].strip()
            if "Updates:" in next_l:
                current_name = line
        
        # Check for date match
        match = re.search(spring_pattern, line, re.IGNORECASE)
        if match:
            results.append({
                "name": current_name,
                "context": line,
                "date": match.group(0)
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5331130674983609150': 'file_storage/function-call-5331130674983609150.json', 'var_function-call-5331130674983611055': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11024242700101333530': 'file_storage/function-call-11024242700101333530.json', 'var_function-call-4323330023283925201': 'file_storage/function-call-4323330023283925201.json'}

exec(code, env_args)
