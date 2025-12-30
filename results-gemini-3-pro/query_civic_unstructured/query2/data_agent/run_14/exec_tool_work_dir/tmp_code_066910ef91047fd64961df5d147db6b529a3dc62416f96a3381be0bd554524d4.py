code = """import json
import re

# Load data
funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Combine all text for easier searching (or search per doc to keep context better)
# searching per doc is safer to avoid cross-project pollution if text is concatenated
# But the Funding names are unique enough.

# Let's normalize funding list
projects = []
for item in funding_data:
    projects.append({
        "name": item['Project_Name'],
        "amount": int(item['Amount']),
        "id": item['Funding_ID']
    })

# Define a function to check text for a project
def check_project_status(project_name, text_content):
    # Find the project name in text
    # The name might be slightly different or have extra spaces, so normalize spaces
    normalized_name = re.escape(project_name)
    
    # We look for the project name followed by some text that indicates completion in 2022.
    # We grab a chunk of text after the name.
    # The text structure in the sample: "Project Name\n\n(cid:190) Updates:..."
    
    matches = list(re.finditer(normalized_name, text_content, re.IGNORECASE))
    
    is_completed_2022 = False
    
    for match in matches:
        start_index = match.end()
        # look ahead e.g. 500 chars
        snippet = text_content[start_index:start_index+500]
        
        # Check for completion indicators
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        
        # We need "completed" and "2022" in the snippet.
        if "completed" in snippet.lower() and "2022" in snippet:
            # refine check to ensure it's not "to be completed"
            # Look for past tense or specific phrase
            if re.search(r"was completed.*?2022", snippet, re.IGNORECASE):
                is_completed_2022 = True
            elif re.search(r"completed.*?2022", snippet, re.IGNORECASE):
                 # Check for "scheduled to be" or "will be"
                 if not re.search(r"(will be|scheduled to be|expected to be).*?completed", snippet, re.IGNORECASE):
                     is_completed_2022 = True
    
    return is_completed_2022

# Filter for Park related projects first
park_projects = []
for p in projects:
    name = p['name'].lower()
    # Topic keywords from hints: "park", "playground"
    if "park" in name or "playground" in name:
        park_projects.append(p)

# Now check status in docs
total_funding = 0
confirmed_projects = []

# Concatenate all text from docs? Or check each.
# Checking each is better.
all_text = "\n".join([d['text'] for d in civic_data])

for p in park_projects:
    if check_project_status(p['name'], all_text):
        total_funding += p['amount']
        confirmed_projects.append(p['name'])

print("__RESULT__:")
print(json.dumps({"confirmed_projects": confirmed_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json'}

exec(code, env_args)
