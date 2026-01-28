code = """import json
import re

# Load funding data
with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-9654609134184919281'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding > 50000
high_funding_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            high_funding_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        continue

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Locate Capital Design section
    start_match = re.search(r'Capital Improvement Projects\s*\(\s*Design\s*\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_idx = start_match.end()
    
    # Locate end of section
    next_headers = [
        r'Capital Improvement Projects\s*\(\s*Construction\s*\)',
        r'Capital Improvement Projects\s*\(\s*Not Started\s*\)',
        r'Disaster Recovery Projects'
    ]
    
    end_idx = len(text)
    for header in next_headers:
        match = re.search(header, text[start_idx:], re.IGNORECASE)
        if match:
            current_end = start_idx + match.start()
            if current_end < end_idx:
                end_idx = current_end
                
    section_text = text[start_idx:end_idx]
    
    # Split by (cid:190) which is likely the bullet point in the text representation
    segments = section_text.split('(cid:190)')
    
    # Function to clean and get the project name from the end of a segment
    def get_project_name(segment):
        lines = [line.strip() for line in segment.split('\n') if line.strip()]
        if not lines:
            return None
        # Iterate backwards to find the first likely project name
        for line in reversed(lines):
            # Ignore page numbers/headers that might have been caught
            if "Page" in line and "of" in line: continue
            if "Agenda Item" in line: continue
            # Ignore lines that are part of the previous item's details if strictness needed
            # But usually the details are indented or specific keywords.
            # The project name stands out.
            return line
        return None

    # Segment 0 ends with first project name
    p1 = get_project_name(segments[0])
    if p1: capital_design_projects.add(p1)
    
    # Segments 1 to N-1 end with subsequent project names
    for seg in segments[1:-1]:
        p = get_project_name(seg)
        if p: capital_design_projects.add(p)

# Matching
count = 0
matches = []
# Create a set of normalized funding names for easier matching
funding_names = set(high_funding_projects.keys())

for proj in capital_design_projects:
    # Exact match
    if proj in funding_names:
        count += 1
        matches.append(proj)
    else:
        # Try some basic normalization
        # e.g. "Project" suffix optional?
        # Check if proj is a substring of any funding name or vice versa?
        # The prompt says names match.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted": list(capital_design_projects), "funding_candidates": list(funding_names)[:10]}))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json'}

exec(code, env_args)
