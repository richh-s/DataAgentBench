code = """import json
import re

# Load data
with open('var_function-call-3666629617059837292.json', 'r') as f:
    funding_data = json.load(f)

with open('var_function-call-5922907063922145685.json', 'r') as f:
    civic_docs = json.load(f)

# Build a map of Project Name to Funding Info
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = {
        'Funding_Source': item['Funding_Source'],
        'Amount': item['Amount']
    }

# All known project names for parsing boundaries
all_project_names = list(funding_map.keys())
# Sort by length descending to match longest names first to avoid partial matches
all_project_names.sort(key=len, reverse=True)

results = []

for doc in civic_docs:
    text = doc['text']
    # Normalize text to handle newlines and spacing easier
    # We'll keep newlines for structure but clean up excessive ones
    lines = text.split('\n')
    
    current_header_status = "Unknown"
    
    # We'll iterate through lines and try to identify sections and projects
    # This is a simple state machine
    
    # Clean lines
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    # Reconstruct text for searching project names, but keeping track of indices is hard.
    # Alternative: Search for known project names in the text blocks.
    # But we need to know the section header associated with the project.
    
    # Let's try to map each project found to a status based on headers found before it.
    
    # Identify Header positions
    headers = [
        "Capital Improvement Projects (Design)",
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects"
    ]
    
    # We will find the index of these headers in the clean_lines list
    header_indices = []
    for h in headers:
        for i, line in enumerate(clean_lines):
            if h.lower() in line.lower():
                status = "unknown"
                if "design" in h.lower():
                    status = "design"
                elif "construction" in h.lower():
                    status = "construction" # We will refine this later (completed check)
                elif "not started" in h.lower():
                    status = "not started"
                header_indices.append((i, status))
    
    header_indices.sort()
    
    # Now find projects
    # We'll scan the text and find project names.
    # A project name from our list must appear as a distinct line or start of a line.
    
    # To associate with status, we need to know position.
    
    found_projects = []
    
    for proj_name in all_project_names:
        # Simple string search might be too loose, let's match exact lines or near exact
        # But text has artifacts like "2022 Morning View..."
        # We'll search in the full text to get position, then map to headers?
        # Text is unstructured.
        
        # Better: Iterate lines.
        # If a line closely matches a project name.
        pass

    # Let's iterate lines and maintain current status
    current_status = None
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check if line is a header
        is_header = False
        for h in headers:
            if h.lower() in line.lower():
                if "design" in h.lower():
                    current_status = "design"
                elif "construction" in h.lower():
                    current_status = "construction"
                elif "not started" in h.lower():
                    current_status = "not started"
                is_header = True
                break
        
        if is_header:
            i += 1
            continue
            
        # Check if line contains a project name
        # We look for a match in our project list
        # We need to be careful about substrings.
        # Check exact match or "startswith"
        
        matched_proj = None
        for proj in all_project_names:
            # Check if line is roughly equal to project name
            # Remove punctuation/artifacts
            line_clean = re.sub(r'[^\w\s]', '', line).strip()
            proj_clean = re.sub(r'[^\w\s]', '', proj).strip()
            
            if proj_clean and line_clean and (proj_clean == line_clean or line_clean.startswith(proj_clean)):
                 matched_proj = proj
                 break
        
        if matched_proj:
            # Found a project
            # Extract text until next project or end of doc or major header?
            # Actually, just capture a chunk of lines
            project_text = []
            j = i + 1
            while j < len(clean_lines):
                next_line = clean_lines[j]
                # Check if next_line is a header
                is_next_header = False
                for h in headers:
                    if h.lower() in next_line.lower():
                        is_next_header = True
                        break
                if is_next_header:
                    break
                    
                # Check if next_line is another project
                is_next_proj = False
                for proj in all_project_names:
                    nl_clean = re.sub(r'[^\w\s]', '', next_line).strip()
                    p_clean = re.sub(r'[^\w\s]', '', proj).strip()
                    if p_clean and nl_clean and (p_clean == nl_clean or nl_clean.startswith(p_clean)):
                        is_next_proj = True
                        break
                if is_next_proj:
                    break
                
                project_text.append(next_line)
                j += 1
            
            full_proj_text = " ".join(project_text)
            
            # Determine refined status
            final_status = current_status
            if final_status == "construction":
                if "completed" in full_proj_text.lower() or "notice of completion" in full_proj_text.lower():
                    final_status = "completed"
            
            # Check keywords
            keywords = ['emergency', 'fema', 'disaster', 'fire', 'warning']
            is_relevant = False
            
            # Check name
            for kw in keywords:
                if kw.lower() in matched_proj.lower():
                    is_relevant = True
                    break
            
            # Check text
            if not is_relevant:
                for kw in keywords:
                    if kw.lower() in full_proj_text.lower():
                        is_relevant = True
                        break
            
            if is_relevant:
                # Add to results
                # Get funding info
                f_info = funding_map.get(matched_proj, {})
                
                results.append({
                    "Project_Name": matched_proj,
                    "Funding_Source": f_info.get('Funding_Source'),
                    "Amount": f_info.get('Amount'),
                    "Status": final_status
                })
            
            i = j # Skip to where we left off
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8927615700191605796': ['Funding'], 'var_function-call-8927615700191608741': ['civic_docs'], 'var_function-call-3666629617059836093': 'file_storage/function-call-3666629617059836093.json', 'var_function-call-3666629617059837292': 'file_storage/function-call-3666629617059837292.json', 'var_function-call-5922907063922145685': 'file_storage/function-call-5922907063922145685.json'}

exec(code, env_args)
