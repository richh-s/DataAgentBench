code = """import json
import re

# Load data
with open(locals()['var_function-call-10469334728230477233'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2938925832300121320'], 'r') as f:
    civic_docs = json.load(f)

# Combine text from all docs
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Simple parser to find project blocks
# Assumptions: Project titles are lines that are not indented/bulleted and are followed by updates/bullets.
# We'll also look for "Capital Improvement Projects" headers to ignore or categorize.

lines = full_text.split('\n')
projects = {}
current_project = None
current_info = {"text": []}

skip_phrases = ["Page ", "Agenda Item", "Prepared by", "Approved by", "Date prepared", "Meeting date", "Subject:", "RECOMMENDED ACTION", "DISCUSSION", "Public Works", "Commission Meeting"]
headers = ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Check if line is a known header
    if any(h.lower() in line.lower() for h in headers):
        continue
        
    if any(s in line for s in skip_phrases):
        continue

    # Identify potential project title
    # It shouldn't start with (cid:190) or (cid:131) or be a bullet
    if not line.startswith("(cid:") and not line.startswith("•") and len(line) > 5:
        # Save previous
        if current_project:
            projects[current_project] = "\n".join(current_info["text"])
        
        current_project = line
        current_info = {"text": []}
    else:
        if current_project:
            current_info["text"].append(line)

# Save last
if current_project:
    projects[current_project] = "\n".join(current_info["text"])

# Extract details
parsed_projects = {}
for name, text in projects.items():
    # Look for dates
    # Patterns: "Begin Construction: <Date>", "Advertise: <Date>", "Construction was completed <Date>"
    # We want "started in 2022".
    # If "Begin Construction" is 2022 -> Yes.
    # If "Construction was completed" is 2022 -> Maybe, but assume yes if no other date? No, completed means it started earlier. 
    # But usually short projects start and end same year.
    # Let's collect all year mentions in context.
    
    start_year = None
    
    # Check "Begin Construction"
    match = re.search(r"Begin [Cc]onstruction:?\s*([A-Za-z0-9\s]+)", text)
    if match:
        date_str = match.group(1)
        if "2022" in date_str:
            start_year = 2022
        elif "2023" in date_str:
            start_year = 2023
        elif "2021" in date_str:
            start_year = 2021
            
    # If not found, check "Construction was completed"
    if start_year is None:
        match = re.search(r"Construction was completed,?\s*([A-Za-z0-9\s]+)", text)
        if match:
             # If completed in 2022, we are unsure if started in 2022. 
             # But prompt says "started in 2022". 
             # I should look for start. 
             pass
    
    # Check for "2022" in Project Name
    if "2022" in name:
        # "2022 Annual Street Maintenance" -> Started 2022.
        start_year = 2022
        
    parsed_projects[name] = {
        "text": text,
        "start_year": start_year
    }

print("__RESULT__:")
print(json.dumps(list(parsed_projects.keys())[:20])) # Print first 20 names to check parsing"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json'}

exec(code, env_args)
