code = """import json
import re

with open(locals()['var_function-call-11024242700101333530'], 'r') as f:
    civic_docs = json.load(f)

# Use simple strings
spring_regex = re.compile(r"(Spring 2022|March 2022|April 2022|May 2022)", re.IGNORECASE)

results = []

for doc in civic_docs:
    text = doc['text']
    # Split generally by double newline
    chunks = text.split('\n\n')
    
    # Iterate chunks to find project names and data
    # This is hard because names are headers.
    
    # Alternative: iterate all lines
    lines = text.split('\n')
    
    current_name = "Unknown"
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Heuristic: A line that is not a known header, 
        # doesn't start with "Updates:", "Project Schedule:", "Subject:", etc.
        # might be a project name.
        # But this is too noisy.
        
        # Let's rely on the structure:
        # NAME
        # (cid:190) Updates:
        
        # Check if next line (or next non-empty line) starts with "(cid:190) Updates:"
        # Avoid literal parens in string
        
        # Look ahead
        is_name = False
        # Find next non-empty line
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        
        if j < len(lines):
            next_line = lines[j].strip()
            # Check if next line contains "Updates:"
            if "Updates:" in next_line:
                current_name = line
                
        # Check for Spring 2022 in the current line
        if spring_regex.search(line):
            results.append({
                "name": current_name,
                "context": line,
                "date": spring_regex.search(line).group(0)
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5331130674983609150': 'file_storage/function-call-5331130674983609150.json', 'var_function-call-5331130674983611055': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11024242700101333530': 'file_storage/function-call-11024242700101333530.json', 'var_function-call-4323330023283925201': 'file_storage/function-call-4323330023283925201.json'}

exec(code, env_args)
