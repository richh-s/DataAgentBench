code = """import json
import re

# Load data
with open(locals()['var_function-call-2334395091731140458'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2334395091731137035'], 'r') as f:
    funding_data = json.load(f)

projects_found = []

# Regex patterns with double escaping
# looking for newline, capture line, newline, (cid:190)
project_header_pattern = re.compile(r'\\n([^\\n]+)\\n+(?:\\(cid:190\\)|[vV]i\\.|-)\\s*(?:Updates|Project Description|Project Updates|Status):', re.MULTILINE)

start_date_pattern = re.compile(r'Begin [Cc]onstruction:?\\s*([^\\n]+)', re.IGNORECASE)
start_date_pattern_2 = re.compile(r'Construction [Ss]tart:?\\s*([^\\n]+)', re.IGNORECASE)

def is_spring_2022(date_str):
    if not date_str: return False
    if re.search(r'Spring[, ]+2022', date_str, re.IGNORECASE):
        return True
    if re.search(r'(?:March|April|May)[, ]+2022', date_str, re.IGNORECASE):
        return True
    return False

for doc in civic_docs:
    text = doc['text']
    matches = list(project_header_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.end()
        end_index = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        block = text[start_index:end_index]
        
        st_match = start_date_pattern.search(block)
        if not st_match:
            st_match = start_date_pattern_2.search(block)
            
        st_date = st_match.group(1).strip() if st_match else None
        
        if is_spring_2022(st_date):
            projects_found.append({
                "Project_Name": project_name,
                "st": st_date
            })

# Deduplicate
unique_projects = {}
for p in projects_found:
    name = p['Project_Name']
    # Removing trailing colons or spaces if any
    name = name.rstrip(': ')
    if name not in unique_projects:
        unique_projects[name] = p

print("__RESULT__:")
print(json.dumps(list(unique_projects.values())))"""

env_args = {'var_function-call-3266784049698579057': 'file_storage/function-call-3266784049698579057.json', 'var_function-call-3266784049698579578': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2334395091731140458': 'file_storage/function-call-2334395091731140458.json', 'var_function-call-2334395091731137035': 'file_storage/function-call-2334395091731137035.json'}

exec(code, env_args)
