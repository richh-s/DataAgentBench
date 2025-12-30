code = """import json
import re

# Load data
with open(locals()['var_function-call-17402731764388360423'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-17402731764388360612'], 'r') as f:
    funding_data = json.load(f)

projects = []

# Keywords
topics = ["park", "road", "FEMA", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]

# Helper to check topic
def get_topics(text):
    found = []
    text_lower = text.lower()
    for t in topics:
        if t in text_lower:
            found.append(t)
    return found

# Parsing logic
# We'll assume a project starts with a line that isn't indented/bulleted and is followed by "Updates" or "Project Description" or "Project Schedule".
# Or more simply, we can split by double newlines or check for the specific structure.

# Let's iterate through lines and try to group them into projects.
# Based on the preview, project titles are on their own lines.
# And are followed by sections starting with bullets (cid:190) or "Updates:".

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_info = []
    
    # Simple state machine
    # We look for a line that looks like a title.
    # A title is usually non-empty, doesn't start with special chars (bullets), and is followed eventually by "Updates:" or "Project Description:"
    
    # Because text is unstructured, let's try a block-based approach.
    # We can identify project blocks by finding the "Updates:" or "Project Description:" lines and looking backwards for the title.
    
    # Actually, let's look for the pattern:
    # Line P (Project Name)
    # [Empty Lines]
    # Line U (starts with bullet or 'Updates' or 'Project Description')
    
    # Regex to find project blocks might be hard due to noise.
    # Let's clean the lines first.
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check if this line is a potential project title
        # It shouldn't be a known header like "Public Works Commission", "Agenda Report", etc.
        # It shouldn't start with (cid:...) or "Page".
        
        is_candidate = True
        if line.startswith('(') or line.startswith('Page') or "Agenda Item" in line:
            is_candidate = False
        if "Capital Improvement Projects" in line: # Section headers
            is_candidate = False
            
        if is_candidate:
            # Look ahead to see if it introduces a project section
            # A project section typically has "Updates:", "Project Description:", "Project Schedule:" in the next few lines.
            j = i + 1
            is_project = False
            found_indicator = False
            while j < len(clean_lines) and j < i + 5: # Look ahead a few lines
                next_line = clean_lines[j]
                if "Updates" in next_line or "Project Description" in next_line or "Project Schedule" in next_line:
                    found_indicator = True
                    break
                j += 1
            
            if found_indicator:
                # We found a project!
                project_name = line
                # Now extract the content until the next project starts
                # How do we know the next project starts?
                # We can search for the next candidate line that is followed by an indicator.
                # Or just grab everything until we hit the next known indicator block?
                # Let's grab lines until the next start-of-project pattern or end of text.
                
                project_content_lines = []
                k = i + 1
                while k < len(clean_lines):
                    # Check if line k is the start of a new project
                    # To be the start of a new project, it must be a candidate AND followed by an indicator.
                    # This check is expensive if done for every line.
                    
                    # Optimization: Just check if line k is a candidate and k+1/2/3 has indicator.
                    
                    sub_line = clean_lines[k]
                    
                    # Check if sub_line is start of new project
                    is_new_proj = False
                    if not (sub_line.startswith('(') or sub_line.startswith('Page') or "Agenda Item" in sub_line or "Capital Improvement Projects" in sub_line):
                        # Look ahead
                        m = k + 1
                        while m < len(clean_lines) and m < k + 5:
                            nl = clean_lines[m]
                            if "Updates" in nl or "Project Description" in nl or "Project Schedule" in nl:
                                is_new_proj = True
                                break
                            m += 1
                    
                    if is_new_proj:
                        break # End of current project
                    
                    project_content_lines.append(sub_line)
                    k += 1
                
                # Analyze the extracted project block
                full_block = " ".join(project_content_lines)
                
                # Extract Status
                # Search for "completed"
                status = "unknown"
                completion_date = None
                
                if "completed" in full_block.lower():
                    status = "completed"
                    # Try to extract date near "completed"
                    # Pattern: "completed [Month] [Year]" or "completed in [Month] [Year]" or "completed [Year]"
                    # Regex for date: (January|February|...)?\s*\d{4}
                    
                    # Be specific: "Construction was completed November 2022"
                    # Find sentences with "completed"
                    # Split by '. ' to get sentences?
                    
                    # Simple regex for finding year 2022 near "completed"
                    # Check if "2022" is in the same sentence or clause as "completed"
                    
                    # Let's capture the date string
                    # Regex: completed.*?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})
                    date_match = re.search(r'completed.*?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\s,]+\d{4})', full_block, re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(1)
                    else:
                        # Maybe just "completed in 2022"
                         date_match_yr = re.search(r'completed.*?(\d{4})', full_block, re.IGNORECASE)
                         if date_match_yr:
                             completion_date = date_match_yr.group(1)

                
                # Extract Topic
                proj_topics = get_topics(project_name + " " + full_block)
                
                extracted_projects.append({
                    "Project_Name": project_name,
                    "topics": proj_topics,
                    "status": status,
                    "completion_date": completion_date
                })
                
                i = k # Advance to next project
                continue

        i += 1

# Now filter and join
total_funding = 0
matched_projects = []

funding_dict = {} # Map Project_Name to Amount (sum if multiple entries, though usually 1)
for f in funding_data:
    nm = f['Project_Name'].strip()
    amt = f['Amount']
    if nm in funding_dict:
        funding_dict[nm] += amt
    else:
        funding_dict[nm] = amt

print(f"DEBUG: Found {len(extracted_projects)} projects in text.")

for p in extracted_projects:
    # Filter: Park related
    if "park" not in p['topics']:
        continue
    
    # Filter: Completed
    if p['status'] != "completed":
        continue
        
    # Filter: Completed in 2022
    if not p['completion_date']:
        continue
    if "2022" not in p['completion_date']:
        continue
        
    # Join with funding
    p_name = p['Project_Name'].strip()
    
    # Try exact match first
    amount = 0
    if p_name in funding_dict:
        amount = funding_dict[p_name]
    else:
        # Try fuzzy or clean up?
        # The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
        # So maybe just simple strip is enough.
        # But let's check for "Project" suffix or similar differences just in case.
        # But for now assume exact match.
        pass
    
    if amount > 0:
        matched_projects.append({"name": p_name, "amount": amount, "date": p['completion_date']})
        total_funding += amount

print("__RESULT__:")
print(json.dumps(matched_projects))"""

env_args = {'var_function-call-17402731764388360423': 'file_storage/function-call-17402731764388360423.json', 'var_function-call-17402731764388360612': 'file_storage/function-call-17402731764388360612.json'}

exec(code, env_args)
