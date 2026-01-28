code = """import json
import re

# Load data
with open(locals()['var_function-call-18183921602987609697'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-18183921602987608670'], 'r') as f:
    civic_docs = json.load(f)

projects = {} # name -> {start_date, is_disaster, amount}

# Create a lookup for funding amount
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())

# Sort project names by length descending to match longest first (avoid partial matches like "Project A" matching "Project A Phase 2")
project_names.sort(key=len, reverse=True)

# Helper to check if name implies disaster
def is_disaster_name(name):
    keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey"]
    return any(k in name for k in keywords)

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections
    # We want to know valid ranges for "Disaster Recovery Projects"
    # Sections seem to start with lines like "Capital Improvement Projects..." or "Disaster Recovery Projects..."
    # Let's find all section headers
    
    # Regex for headers might be tricky, let's look for specific known headers or just "Projects"
    # Based on preview: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", etc.
    # And we expect "Disaster Recovery Projects"
    
    # Let's just find positions of the keywords
    
    disaster_headers_iter = re.finditer(r"Disaster Recovery Projects", text, re.IGNORECASE)
    capital_headers_iter = re.finditer(r"Capital Improvement Projects", text, re.IGNORECASE)
    
    disaster_starts = [m.start() for m in disaster_headers_iter]
    capital_starts = [m.start() for m in capital_headers_iter]
    
    # We can assume a project belongs to the header immediately preceding it.
    # Let's create a list of (index, type)
    sections = []
    for pos in disaster_starts:
        sections.append((pos, 'disaster'))
    for pos in capital_starts:
        sections.append((pos, 'capital'))
    
    sections.sort()
    
    # Locate projects in text
    for name in project_names:
        # Find all occurrences of the project name
        # We use re.escape to handle parentheses in names
        try:
            matches = list(re.finditer(re.escape(name), text))
        except:
            continue
            
        for m in matches:
            start_pos = m.start()
            end_pos = m.end()
            
            # Determine type from section
            project_type = "unknown"
            # Find the section header that is closest before this project
            current_section_type = None
            for sec_pos, sec_type in sections:
                if sec_pos < start_pos:
                    current_section_type = sec_type
                else:
                    break
            
            # Use name heuristic as override or fallback
            if is_disaster_name(name):
                project_type = "disaster"
            elif current_section_type == 'disaster':
                project_type = "disaster"
            else:
                project_type = "capital"
            
            # Extract start date
            # Look at the text following the name (up to say 2000 chars or next project match?)
            # A safe bet is a smaller window, e.g., 1000 chars
            context = text[end_pos:end_pos+1000]
            
            # Look for "Begin Construction" or "Start"
            # Patterns:
            # "Begin Construction: <Date>"
            # "Start Date: <Date>"
            # "Project Schedule: ... Begin Construction: <Date>"
            
            date_match = re.search(r"(Begin Construction|Start Date|Construction Start)\s*[:\-]?\s*([A-Za-z0-9\s,]+)", context, re.IGNORECASE)
            
            st = None
            if date_match:
                st = date_match.group(2).strip()
                # Clean up the date string (take first line or few words)
                st = st.split('\n')[0]
            
            # Store found info
            # If project already found, valid start date overrides None?
            # Or if we found a mention with a start date, we keep it.
            if name not in projects:
                projects[name] = {'type': project_type, 'st': st, 'amount': funding_map[name]}
            else:
                # Update if we found a start date and didn't have one
                if projects[name]['st'] is None and st is not None:
                    projects[name]['st'] = st
                    projects[name]['type'] = project_type # Update type too if we are more confident?
                # If we have a start date, prefer the one that says "Disaster" if conflict?
                if project_type == 'disaster':
                    projects[name]['type'] = 'disaster'

# Calculate total funding
total_funding = 0
found_projects = []

print("Debugging Project Extraction:")
for name, info in projects.items():
    if info['type'] == 'disaster':
        start_date = info.get('st', '')
        if start_date and '2022' in start_date:
            print(f"MATCH: {name}, Date: {start_date}, Amount: {info['amount']}")
            total_funding += info['amount']
            found_projects.append(name)
        elif start_date:
             # Check for "started in 2022" - could be substring
             pass

print(f"Total Funding: {total_funding}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-18183921602987609697': 'file_storage/function-call-18183921602987609697.json', 'var_function-call-18183921602987608670': 'file_storage/function-call-18183921602987608670.json'}

exec(code, env_args)
