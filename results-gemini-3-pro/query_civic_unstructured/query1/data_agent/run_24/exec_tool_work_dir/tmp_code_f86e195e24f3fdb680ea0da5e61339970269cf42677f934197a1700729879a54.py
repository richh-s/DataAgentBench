code = """import json
import re

# Load funding results
with open(locals()['var_function-call-2470903467818453572'], 'r') as f:
    funding_data = json.load(f)

# Create a set of high-funding project names for fast lookup
# Normalize names (strip, lower?) - DB usually matches exactly or close. 
# The hint says "Project_Name in the Funding SQLite table matches the project names that can be extracted".
# So I will trust exact match or simple strip.
high_funding_projects = set(item['Project_Name'].strip() for item in funding_data)

# Load civic docs
with open(locals()['var_function-call-1752816955858049091'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Locate the "Capital Improvement Projects (Design)" section
    # The text might have different whitespace or newlines, so use flexible regex
    # Pattern: Capital Improvement Projects (Design) ... until ... Capital Improvement Projects (Construction) 
    # or similar headers.
    
    # Let's find the start index
    start_match = re.search(r'Capital Improvement Projects\s*\(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_index = start_match.end()
    
    # Find the end index (Next major section)
    # Possible next sections based on preview: "(Construction)", "(Not Started)", "Disaster Recovery"
    end_match = re.search(r'Capital Improvement Projects\s*\((?:Construction|Not Started)\)|Disaster Recovery Projects', text[start_index:], re.IGNORECASE)
    
    if end_match:
        end_index = start_index + end_match.start()
        section_text = text[start_index:end_index]
    else:
        # If no next section found, take the rest of the text (risky but better than nothing)
        section_text = text[start_index:]
        
    # Now parse project names from section_text
    # Project names seem to be lines followed by a line starting with (cid:190) or similar marker
    # In the preview: 
    # "2022 Morning View Resurfacing & Storm Drain Improvements"
    # "(cid:190) Updates:"
    
    # Let's clean the lines
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    for i in range(len(lines) - 1):
        current_line = lines[i]
        next_line = lines[i+1]
        
        # Heuristic: A project name is a line that does not look like a bullet or metadata, 
        # and is followed by a line that starts with a bullet marker or "Updates" or "Project Description"
        # The markers in the preview were "(cid:190)" and "(cid:131)". 
        # Note: (cid:190) might be represented differently in string, likely unicode.
        # But usually raw text shows as "(cid:190)". 
        # Also check for "Updates:" or "Project Description:" in next line.
        
        # Check if next line looks like a start of details
        is_detail_start = next_line.startswith('(cid:') or \
                          next_line.startswith('Updates:') or \
                          next_line.startswith('Project Description:') or \
                          next_line.startswith('Project Schedule:') or \
                          'Updates:' in next_line or \
                          '(cid:190)' in next_line
                          
        # Check if current line is not a noise line
        is_noise = current_line.startswith('Page ') or \
                   current_line.startswith('Agenda Item') or \
                   current_line.startswith('(cid:')
                   
        if is_detail_start and not is_noise:
            # Potentially a project name
            # Remove any trailing colons or noise
            p_name = current_line.strip()
            capital_design_projects.add(p_name)

# Filter by high funding
# Using the set for intersection
# We need to handle potential slight mismatches or case, but let's try exact match first
matched_projects = []
for p in capital_design_projects:
    if p in high_funding_projects:
        matched_projects.append(p)
    else:
        # try checking without case?
        # or checking if p is substring?
        pass

result = {
    "extracted_capital_design_projects": list(capital_design_projects),
    "high_funding_projects_count": len(high_funding_projects),
    "matched_projects": matched_projects,
    "count": len(matched_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2470903467818453572': 'file_storage/function-call-2470903467818453572.json', 'var_function-call-1752816955858049091': 'file_storage/function-call-1752816955858049091.json'}

exec(code, env_args)
