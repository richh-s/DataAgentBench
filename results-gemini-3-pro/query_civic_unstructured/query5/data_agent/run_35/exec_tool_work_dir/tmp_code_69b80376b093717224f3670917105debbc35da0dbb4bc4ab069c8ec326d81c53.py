code = """import json
import re

# Load the civic docs
with open(locals()['var_function-call-6738799764007294516'], 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
with open(locals()['var_function-call-6738799764007295879'], 'r') as f:
    funding_data = json.load(f)

# Helper to normalize strings
def normalize(text):
    return text.strip()

# Pattern to find project blocks
# Looking for lines that appear to be headers followed by "Updates" or "Project Description"
# We'll split by double newlines or scan line by line
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_text_block = []
    
    # Iterate lines to find project headers
    # A header is usually a non-empty line, not starting with special chars, followed shortly by "Updates:" or "Project Description:"
    # This is a heuristic.
    
    # Let's try splitting by double newlines to get potential blocks
    blocks = re.split(r'\n\s*\n', text)
    
    # But headers might be separated from body by single newline.
    # Let's try identifying project starts.
    # From preview: "Project Name\n\n(cid:190) Updates:"
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project title
        # Look ahead for "(cid:190) Updates:" or "Updates:" or "Project Description:"
        is_title = False
        look_ahead_range = 5 # check next few lines
        for j in range(1, look_ahead_range + 1):
            if i + j < len(lines):
                next_line = lines[i+j].strip()
                if re.search(r'(Updates:|Project Description:|Project Updates:)', next_line):
                    is_title = True
                    break
        
        if is_title:
            # Save previous project if exists
            if current_project:
                extracted_projects.append(current_project)
            
            current_project = {
                'name': line,
                'text_lines': []
            }
        else:
            if current_project:
                current_project['text_lines'].append(line)
    
    # Append last
    if current_project:
        extracted_projects.append(current_project)

# Now process extracted projects to find details
processed_projects = []
for proj in extracted_projects:
    full_text = " ".join(proj['text_lines'])
    
    # Extract Start Date
    # Look for "Begin [cC]onstruction:? (.*)"
    # Or "Start [dD]ate:? (.*)"
    # Note: Text often has "(cid:131)" bullets.
    start_match = re.search(r'Begin [cC]onstruction:?\s*([A-Za-z0-9\s,]+)', full_text, re.IGNORECASE)
    if not start_match:
        start_match = re.search(r'Construction start:?\s*([A-Za-z0-9\s,]+)', full_text, re.IGNORECASE)
    
    start_date_str = start_match.group(1).strip() if start_match else None
    
    # Check for Year 2022
    started_in_2022 = False
    if start_date_str and "2022" in start_date_str:
        started_in_2022 = True
    
    # Check for Disaster related
    # Keywords in name or text
    is_disaster = False
    disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Recovery", "Emergency"]
    
    # Check Name
    if any(k.lower() in proj['name'].lower() for k in disaster_keywords):
        is_disaster = True
    
    # Check Text
    # But topics might be comma separated keywords.
    # If the text mentions FEMA approval, it's likely disaster.
    if any(k in full_text for k in disaster_keywords):
        is_disaster = True
        
    processed_projects.append({
        'name': proj['name'],
        'start_date_raw': start_date_str,
        'started_in_2022': started_in_2022,
        'is_disaster': is_disaster,
        'full_text_preview': full_text[:200]
    })

print("__RESULT__:")
print(json.dumps(processed_projects))"""

env_args = {'var_function-call-6738799764007294516': 'file_storage/function-call-6738799764007294516.json', 'var_function-call-6738799764007295879': 'file_storage/function-call-6738799764007295879.json'}

exec(code, env_args)
