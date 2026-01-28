code = """import json
import re

# Load data
funding_path = locals()['var_function-call-1630870777495368104']
docs_path = locals()['var_function-call-1630870777495368997']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Concatenate all text
full_text = "\n".join([d['text'] for d in docs_data])

# Project names from funding
projects = []
for row in funding_data:
    projects.append({
        'name': row['Project_Name'],
        'amount': float(row['Amount']),
        'id': row['Funding_ID']
    })

total_funding = 0
matched_projects = []

# Define keywords
disaster_suffixes = ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)"]
disaster_keywords = ["FEMA", "CalOES", "Woolsey Fire", "Disaster", "Emergency", "CalJPIA", "fire", "emergency warning"]

# Helper to find project in text
def find_project_context(name, text):
    # Try exact match
    pattern = re.escape(name)
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    # If not found, try root name (remove suffix)
    if not matches:
        root = re.sub(r"\s*\(.*?\)$", "", name)
        if root != name and len(root) > 5: # prevent short roots
            pattern = re.escape(root)
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    if not matches:
        return None
        
    # Pick the best match? Or iterate all?
    # Usually a project is listed once as a header. 
    # The documents seem to be "Status Reports", so each project is listed with details.
    # We'll take the context from the match that looks most like a header (e.g. followed by newlines or bullets)
    # For now, just take the first match that is followed by typical content structure?
    # Let's simply concatenate contexts from all occurrences to be safe (might be mentioned in multiple agendas).
    
    combined_context = ""
    for m in matches:
        start = m.end()
        # grab next 1500 chars
        combined_context += text[start : start + 1500] + "\n"
    
    return combined_context

debug_log = []

for p in projects:
    name = p['name']
    amount = p['amount']
    
    # Check if name implies disaster
    name_is_disaster = any(s in name for s in disaster_suffixes)
    
    # Find context
    context = find_project_context(name, full_text)
    
    if not context:
        # If not found in text, we can't determine start date (unless we assume something?)
        # But we must satisfy "started in 2022".
        continue
        
    # Check context for disaster keywords
    context_is_disaster = any(k.lower() in context.lower() for k in disaster_keywords)
    
    is_disaster = name_is_disaster or context_is_disaster
    
    if not is_disaster:
        continue
        
    # Check Start Date in context
    # Look for 2022
    # Specific patterns
    # (cid:131) Begin Construction: Fall 2023
    # We want "2022"
    
    # Pattern 1: Begin Construction ... 2022
    start_match = re.search(r"(Begin Construction|Start Date|Construction Start)[:\s]+.*?2022", context, re.IGNORECASE)
    
    # Pattern 2: "Advertise: ... 2022" -> This might be start.
    # But "Begin Construction" is better.
    # What if construction was completed in 2022? "Construction was completed... 2022".
    # The prompt asks for "started in 2022".
    # If completed in 2022, it *might* have started in 2022 (short project) or 2021.
    # Let's check for "started" or "begin".
    
    # What if the date is just "2022" without label? Too risky.
    
    is_started_2022 = False
    if start_match:
        is_started_2022 = True
    else:
        # Check for looser "Start ... 2022"
        # Or "Schedule: ... 2022"
        # Example from text: "Begin Construction: Fall 2023"
        # Check if there is "Begin Construction: ... 2022"
        pass
    
    # Special check: "Construction was completed November 2022"
    # If a project is completed in Nov 2022, did it start in 2022?
    # Some small projects (e.g. repairs) take < 1 year.
    # "Bluffs Park Shade Structure ... Construction was completed November 2022."
    # "Broad Beach Road Water Quality Repair ... Construction was completed, November 2022"
    # These might have started in 2022.
    # Let's look for "Notice to Proceed ... 2022" or "Awarded ... 2022".
    # Snippet: "On February 27, 2023, City Council awarded..." -> Start 2023.
    # Snippet: "Construction was completed, January 2023" -> Started 2022?
    # Let's conservatively look for "Begin Construction: ... 2022" or "Start: ... 2022".
    
    # Let's broaden the regex to capture lines with 2022 that imply start.
    # "Begin Construction: <Season> 2022"
    # "Advertise: <Season> 2022" (Advertising is a start of the procurement phase).
    # "Design: ... 2022" -> Start of design?
    # The query asks for "projects that started in 2022".
    # Usually implies the main phase (Construction) or the project itself initiated?
    # "Projects have three statuses: design, completed, not started".
    # If status is "Design" and design started in 2022?
    # If status is "Completed" and it started in 2022?
    # I'll stick to "Begin Construction" or "Advertise" (which starts the project execution) in 2022.
    # Or "Awarded ... 2022".
    
    keywords_start = ["Begin Construction", "Advertise", "Awarded", "Construction Start", "Start Date"]
    for kw in keywords_start:
        if re.search(rf"{kw}.*?2022", context, re.IGNORECASE):
            is_started_2022 = True
            break
            
    if is_started_2022:
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})
        
print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matches': matched_projects}))"""

env_args = {'var_function-call-1630870777495368104': 'file_storage/function-call-1630870777495368104.json', 'var_function-call-1630870777495368997': 'file_storage/function-call-1630870777495368997.json'}

exec(code, env_args)
