code = """import json
import pandas as pd
import re

# Load Funding results
with open(locals()['var_function-call-8710431092191465218'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-268115837659623776'], 'r') as f:
    civic_docs = json.load(f)

# Filter Funding > 50000 (Already done in query, but good to ensure)
# Convert Amount to float/int
funding_projects = []
for item in funding_data:
    try:
        amt = float(item['Amount'])
        if amt > 50000:
            funding_projects.append(item['Project_Name'])
    except:
        pass

# Extract Project Names from Civic Docs in "Capital Improvement Projects (Design)" section
extracted_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Find section
    # Regex to find the content between "Capital Improvement Projects (Design)" and the next section
    # Next section could be "Capital Improvement Projects (Construction)" or "Disaster Recovery..."
    # or just end of file or "Page X of Y"
    
    # Locate start
    start_pattern = r"Capital Improvement Projects \(Design\)"
    match_start = re.search(start_pattern, text, re.IGNORECASE)
    if match_start:
        start_idx = match_start.end()
        # Find end: Look for next header. Common headers in sample:
        # "Capital Improvement Projects (Construction)"
        # "Capital Improvement Projects (Not Started)"
        # "Disaster Recovery Projects"
        # "Agenda Item"
        # "Page"
        
        # We can scan line by line after start_idx
        lines = text[start_idx:].split('\n')
        
        current_project_name = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Check for end of section
            if "Capital Improvement Projects" in line and "(Design)" not in line:
                break
            if "Disaster Recovery Projects" in line:
                break
            if "Agenda Item" in line:
                continue # Footer
            if line.startswith("Page"):
                continue # Footer
                
            # Identify Project Name
            # Pattern: The line is followed by "(cid:190) Updates:" or similar in the next few non-empty lines
            # Look ahead
            is_project = False
            for forward_line in lines[i+1:i+5]:
                fw = forward_line.strip()
                if not fw:
                    continue
                if "Updates:" in fw or "(cid:190)" in fw or "Project Description:" in fw:
                    is_project = True
                    break
                # If we hit another potential project name or header, stop
                break
            
            if is_project:
                # This line is a project name
                # Clean it
                # Remove year prefix if strictly numeric? "2022 Morning View..."
                # But Funding might include it.
                extracted_projects.add(line)

# Matching Logic
matched_projects = []
unmatched_funding = []

# Normalize for comparison
def normalize(s):
    # Remove dates, text in parens?
    # Funding: "Name (Type)". Text: "Name".
    # Text: "Name". Funding: "Name".
    # Strategy: remove (...) from both.
    s = re.sub(r'\(.*?\)', '', s)
    # Remove leading years "2022 "
    s = re.sub(r'^\d{4}\s+', '', s)
    # Lowercase, strip
    return s.lower().strip().replace('  ', ' ')

norm_extracted = {normalize(p): p for p in extracted_projects}

count = 0
for fp in funding_projects:
    norm_fp = normalize(fp)
    
    # Try exact match on normalized
    if norm_fp in norm_extracted:
        matched_projects.append(fp)
        count += 1
    else:
        # Try substring match
        # Check if norm_fp is substring of any norm_extracted
        found = False
        for ne in norm_extracted:
            if norm_fp in ne or ne in norm_fp:
                # Check similarity length?
                # "Storm Drain" in "Storm Drain Master Plan" -> Yes
                # "Storm Drain Master Plan" in "Storm Drain" -> No
                # We want to match the specific project.
                # If Funding is "Storm Drain Master Plan" and Text is "Storm Drain Master Plan", match.
                # If Funding "Clover Heights Storm Drain" and Text "Clover Heights Storm Drainage Improvements",
                # "clover heights storm drain" is not in "clover heights storm drainage improvements" (drain vs drainage)
                # But "clover heights" is.
                # Let's use simple token overlap
                fp_tokens = set(norm_fp.split())
                ne_tokens = set(ne.split())
                common = fp_tokens.intersection(ne_tokens)
                if len(common) >= len(fp_tokens) * 0.7: # 70% of Funding tokens in Text
                     matched_projects.append(fp)
                     found = True
                     count += 1
                     break
        if not found:
            unmatched_funding.append(fp)

result = {
    "count": count,
    "matched_projects": matched_projects,
    "extracted_headers": list(extracted_projects),
    "funding_candidates_sample": funding_projects[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8710431092191465218': 'file_storage/function-call-8710431092191465218.json', 'var_function-call-8710431092191464643': 'file_storage/function-call-8710431092191464643.json', 'var_function-call-268115837659623776': 'file_storage/function-call-268115837659623776.json'}

exec(code, env_args)
