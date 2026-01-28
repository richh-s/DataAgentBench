code = """import json
import re

# Load data
with open(locals()['var_function-call-9219159829113401472'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15784328976379923357'], 'r') as f:
    civic_docs = json.load(f)

# Combine text from all docs
full_text = "\n".join([d.get('text', '') for d in civic_docs])

# Define project name list from funding
project_list = funding_data

# Function to check relevance
def is_relevant(text):
    return re.search(r'emergency|fema', text, re.IGNORECASE) is not None

# Prepare results
results = []

# Helper to find project in text and get status/context
# We'll split text by lines and look for project names
# But first, let's identify sections in the text
# Sections: Design, Construction, Not Started
# We can use regex to find start of these sections
section_map = {}
# Find headers
headers = [
    ("Capital Improvement Projects (Design)", "Design"),
    ("Capital Improvement Projects (Construction)", "Construction"),
    ("Capital Improvement Projects (Not Started)", "Not Started")
]

# We need to locate these headers in the text to define ranges
# Since text is unstructured, we find the index of each header
sorted_headers = []
for h_text, status in headers:
    matches = list(re.finditer(re.escape(h_text), full_text, re.IGNORECASE))
    for m in matches:
        sorted_headers.append((m.start(), status))

sorted_headers.sort(key=lambda x: x[0])

# Map text ranges to status
# range i to i+1 has status of i
# Last range goes to end
text_ranges = []
for i in range(len(sorted_headers)):
    start = sorted_headers[i][0]
    status = sorted_headers[i][1]
    end = sorted_headers[i+1][0] if i+1 < len(sorted_headers) else len(full_text)
    text_ranges.append({'status': status, 'text': full_text[start:end]})

# For each project in funding
for proj in project_list:
    p_name = proj['Project_Name']
    p_source = proj['Funding_Source']
    p_amount = proj['Amount']
    
    # Check relevance by name
    name_relevant = is_relevant(p_name)
    
    # Check text for this project
    # We look for the project name in the text ranges
    # Use simple string match or regex with word boundaries
    # Project names can be long, so exact substring match is best, maybe ignore case
    found_status = "Not Found"
    context_relevant = False
    
    # We iterate through ranges to find the project
    # If found, we extract the text block for this project to check context relevance
    # The text block for a project starts at its name and ends at the next project name or end of section
    
    for r in text_ranges:
        # Check if project name is in this range
        # Use simple find
        idx = r['text'].find(p_name) # simple match
        if idx != -1:
            # Found in this section
            # Check for specific "Completed" status if in Construction
            # Extract text block: from idx to next double newline or next project name?
            # The structure is Name \n Updates ...
            # Let's verify if it's a real header or just mention.
            # Assuming it's the header.
            
            # Refined Status Logic
            raw_status = r['status']
            
            # Extract block
            # Start at idx
            # End at ? The next project in the list? Hard to know which one comes next.
            # We can try to find the next occurrence of ANY known project name in this range?
            # Or use "(cid:190)" markers if consistent.
            # Text uses (cid:190) for bullets.
            # Let's grab, say, 1000 chars or until next double newline gap?
            # Let's just grab a chunk
            chunk = r['text'][idx:idx+2000]
            
            # Check relevance in chunk
            if is_relevant(chunk):
                context_relevant = True
            
            # Check for "completed" in chunk if status is Construction
            if raw_status == "Construction":
                if "completed" in chunk.lower() and "construction was completed" in chunk.lower():
                    found_status = "Completed"
                else:
                    found_status = "Construction"
            else:
                found_status = raw_status
            
            break # Stop after finding first occurrence (assuming one report)
    
    if name_relevant or context_relevant:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": p_source,
            "Amount": p_amount,
            "Status": found_status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9219159829113404279': 'file_storage/function-call-9219159829113404279.json', 'var_function-call-9219159829113401472': 'file_storage/function-call-9219159829113401472.json', 'var_function-call-15784328976379923357': 'file_storage/function-call-15784328976379923357.json'}

exec(code, env_args)
