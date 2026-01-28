code = """import json

# Load Funding Data
with open(locals()['var_function-call-3926390822647844774'], 'r') as f:
    funding_data = json.load(f)

# Filter candidate projects (Park related)
candidates = {}
keywords = ["park", "playground", "recreation"]
for record in funding_data:
    name = record['Project_Name']
    # Check keywords
    if any(k in name.lower() for k in keywords):
        # Store amount. Note: duplicate names?
        # The table has Funding_ID, so multiple records might exist for one project?
        # The schema says "Funding table contains funding records... Project names can be joined".
        # So one project name might have multiple funding sources.
        # I should sum them up for each project.
        amount = record['Amount']
        if name not in candidates:
            candidates[name] = 0
        candidates[name] += amount

# Load Text Data
with open(locals()['var_function-call-18190371962378278332'], 'r') as f:
    civic_data = json.load(f)

# We only have one document in the sample, but let's iterate.
# We will search for each candidate project name in the text.
# If found, check for "Completed ... 2022" in its section.

completed_projects = []

for doc in civic_data:
    text = doc['text']
    # Normalize text to lower case for searching (optional, but finding sections relies on case usually)
    # The sections seem to be "Project Name" then details.
    
    # Let's locate each candidate in the text
    # Since text is unstructured, we find the position of the name.
    # Then we look at the text immediately following it until the next candidate or known header.
    
    # We can create a list of all project names (candidates + others) to use as delimiters,
    # but we don't know the others.
    # However, we know the structure: Name followed by "(cid:190)" or headers.
    
    # Simplified approach:
    # For each candidate name, if it exists in text:
    #   Extract a window of text after it (e.g., 500 chars).
    #   Check if "completed" and "2022" appear in that window.
    #   Check if "construction" is involved to be sure.
    
    for proj_name in candidates.keys():
        if proj_name in text:
            # Find index
            start_idx = text.find(proj_name)
            # Take a slice. Be careful not to overlap too much or miss info.
            # Usually updates are short. 1000 chars should be enough.
            snippet = text[start_idx:start_idx+1000].lower()
            
            # Check for completion in 2022
            # Patterns:
            # "construction was completed november 2022"
            # "complete construction: ... 2022"
            # "completed, ... 2022"
            
            # Avoid "design"
            
            if "2022" in snippet:
                is_completed = False
                
                # Check for "completed" or "complete construction"
                if "completed" in snippet or "complete construction" in snippet:
                    # Check if "design" is NOT the object of completion
                    # e.g. "complete design: spring 2022" -> NO
                    # "construction was completed" -> YES
                    
                    # Split snippet into lines to be more precise
                    lines = snippet.split('\n')
                    for line in lines:
                        if "2022" in line:
                            if "design" in line:
                                continue
                            if "completed" in line or "complete construction" in line:
                                # Ensure it's not "not started" or future tense (usually headers)
                                # The text says "Construction was completed..."
                                is_completed = True
                                break
                
                if is_completed:
                    if proj_name not in completed_projects:
                        completed_projects.append(proj_name)

# Calculate total funding
total_funding = 0
for proj in completed_projects:
    total_funding += candidates[proj]

result = {
    "projects": completed_projects,
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json'}

exec(code, env_args)
