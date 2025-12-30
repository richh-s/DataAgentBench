code = """import json
import re

# Load data
with open(locals()['var_function-call-2334395091731140458'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2334395091731137035'], 'r') as f:
    funding_data = json.load(f)

# Create Funding Lookup
# Map Project_Name to Amount. There might be multiple entries (suffixes).
# I will create a dictionary where key = Cleaned Project Name, value = list of amounts (or objects)
# To handle the suffix issue, I'll store all and decide later.
funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

# Parse Documents
projects_found = []

# Regex patterns
# Pattern to find project block: Look for the marker (cid:190) followed by Updates or Project Description
# Capture the line before it as the Project Name.
# Note: The text has newlines.
# Example: "Project Name\n\n(cid:190) Updates:"
# We'll regex over the full text.
project_header_pattern = re.compile(r'\n([^\n]+)\n+(?:\(cid:190\)|[vV]i\.|-)\s*(?:Updates|Project Description|Project Updates|Status):', re.MULTILINE)

# Date patterns for Spring 2022
# Spring 2022 = March, April, May 2022 or "Spring 2022"
spring_2022_regex = re.compile(r'(?:Spring|March|April|May)[, ]+2022', re.IGNORECASE)

# Pattern for Start Date
# Look for "Begin Construction:" or "Start:"
start_date_pattern = re.compile(r'Begin [Cc]onstruction:?\s*([^\n]+)', re.IGNORECASE)
start_date_pattern_2 = re.compile(r'Construction [Ss]tart:?\s*([^\n]+)', re.IGNORECASE)

# Helper to checking if date string is Spring 2022
def is_spring_2022(date_str):
    if not date_str: return False
    # Check explicitly for Spring 2022 or the months
    if re.search(r'Spring[, ]+2022', date_str, re.IGNORECASE):
        return True
    if re.search(r'(?:March|April|May)[, ]+2022', date_str, re.IGNORECASE):
        return True
    return False

# Function to extract projects from text
for doc in civic_docs:
    text = doc['text']
    # Split text into chunks based on project headers?
    # Or find all matches and their indices
    matches = list(project_header_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.end()
        # End index is the start of the next match or end of text
        end_index = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        block = text[start_index:end_index]
        
        # Extract Start Date
        st_match = start_date_pattern.search(block)
        if not st_match:
            st_match = start_date_pattern_2.search(block)
            
        st_date = st_match.group(1).strip() if st_match else None
        
        # Check if st_date is Spring 2022
        if is_spring_2022(st_date):
            projects_found.append({
                "Project_Name": project_name,
                "st": st_date,
                "filename": doc['filename']
            })

# Deduplicate projects (same project might be in multiple agendas)
# We should probably take the most recent one? Or if any mention it started in Spring 2022?
# The question asks "How many projects started in Spring 2022".
# If a project is listed in multiple docs, it's the same project.
unique_projects = {}
for p in projects_found:
    name = p['Project_Name']
    # Clean name: remove extra spaces, maybe trailing chars
    # Sometimes header has "Project" at the end, sometimes not?
    # Use the name as key
    if name not in unique_projects:
        unique_projects[name] = p

print("__RESULT__:")
print(json.dumps(list(unique_projects.values())))"""

env_args = {'var_function-call-3266784049698579057': 'file_storage/function-call-3266784049698579057.json', 'var_function-call-3266784049698579578': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2334395091731140458': 'file_storage/function-call-2334395091731140458.json', 'var_function-call-2334395091731137035': 'file_storage/function-call-2334395091731137035.json'}

exec(code, env_args)
