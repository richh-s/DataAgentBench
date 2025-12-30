code = """import json
import re

# Load data
with open(locals()['var_function-call-7626705312140276657'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7626705312140279754'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for row in funding_data:
    projects.append({
        "name": row['Project_Name'],
        "amount": int(row['Amount']),
        "is_disaster": False,
        "started_2022": False,
        "raw_text": ""
    })

# Helper to check if project is disaster related
def check_is_disaster(name, text_context):
    # Check Name Suffixes
    if any(x in name for x in ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)"]):
        return True
    # Check Text Context for "Disaster Recovery Projects" header or keywords
    # This is a bit weak without structured parsing, but let's look for proximity to "Disaster Recovery"
    if "Disaster Recovery Projects" in text_context and name in text_context:
        # Check if the name appears under this header. 
        # Simplified: If "Disaster Recovery Projects" appears before the name in the text block?
        pass
    return False

# Regex for start date
# Patterns: "Begin Construction: <date>", "Start Date: <date>", "Construction Start: <date>"
start_patterns = [
    r"Begin Construction[:\s]+(.*?)(?:\n|$)",
    r"Start Date[:\s]+(.*?)(?:\n|$)",
    r"Construction Start[:\s]+(.*?)(?:\n|$)",
    r"Advertise[:\s]+(.*?)(?:\n|$)" # Sometimes advertise is the start step mentioned
]

# We also need to be careful about "Construction was completed" if that's the only info?
# But "started" is the query.
# Let's try to extract dates linked to these patterns.

total_funding = 0
debug_projects = []

for p in projects:
    p_name = p['name']
    
    # 1. Determine Type based on Name first (High confidence)
    if any(sub in p_name for sub in ["FEMA", "CalOES", "CalJPIA", "Disaster"]):
        p['is_disaster'] = True
    
    # 2. Scan docs
    found_start_2022 = False
    
    for doc in civic_docs:
        text = doc['text']
        if p_name in text:
            # Extract a window of text around the project name
            # Find all occurrences
            for match in re.finditer(re.escape(p_name), text):
                start_idx = match.start()
                # Take context: from start_idx to next double newline or next project?
                # Let's take 1000 chars forward
                context = text[start_idx:start_idx+1500]
                
                # Check for "Disaster" in context headers if not already found
                # Reverse search for header?
                # Look backwards for "Capital Improvement Projects" or "Disaster Recovery Projects"
                # This is hard. Rely on Name Suffixes and maybe keywords in the immediate lines.
                
                # Check for Start Date
                for pat in start_patterns:
                    date_match = re.search(pat, context, re.IGNORECASE)
                    if date_match:
                        date_str = date_match.group(1).strip()
                        # Check if 2022 is in date_str
                        if "2022" in date_str:
                            # Verify it's not "Spring 2023" (which contains no 2022)
                            # But date_str is extracted.
                            # Just check string containment of "2022"
                            found_start_2022 = True
                            # Extract specific date for debugging
                            p['start_date_found'] = date_str
                            break
                
                if found_start_2022: break
        if found_start_2022: break
    
    if found_start_2022:
        p['started_2022'] = True
        
    if p['is_disaster'] and p['started_2022']:
        total_funding += p['amount']
        debug_projects.append(p)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": debug_projects}))"""

env_args = {'var_function-call-7626705312140276657': 'file_storage/function-call-7626705312140276657.json', 'var_function-call-7626705312140279754': 'file_storage/function-call-7626705312140279754.json'}

exec(code, env_args)
