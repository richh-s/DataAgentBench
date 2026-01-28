code = """import json
import re

# Load data
funding_data = json.load(open('var_function-call-2809487722948638107.json'))
civic_docs = json.load(open('var_function-call-2809487722948637720.json'))

# Extract project names from funding database
project_names = set(item['Project_Name'] for item in funding_data)

# Helper to normalize strings for matching
def normalize(s):
    return s.strip().lower()

# Identify park projects in funding database (based on name)
# But description says topic keywords are in the documents. 
# However, "park" in the name is a strong indicator.
# I'll rely on text extraction for confirmation if possible, but name is good primary filter.
park_projects_funding = [p for p in project_names if 'park' in p.lower() or 'playground' in p.lower() or 'recreation' in p.lower()]

# We need to find which of these were completed in 2022 based on the docs.
completed_2022_projects = set()

# Normalize project names for searching in text
# Sort by length descending to match longer names first (to avoid partial matching issues)
sorted_project_names = sorted(list(project_names), key=len, reverse=True)

# Regex to find dates like "November 2022", "Fall 2022", "2022"
date_regex = re.compile(r'(completed|complete construction).*?2022', re.IGNORECASE)

# Iterate over documents
for doc in civic_docs:
    text = doc['text']
    # Split text into lines to process somewhat structurally
    # Or just search for project names and look at context.
    
    # Let's find indices of all project names in this text
    # We store (index, project_name)
    found_projects = []
    for name in sorted_project_names:
        # Simple string search might be enough, but check for exact name match to avoid substrings if possible
        # Given names are specific like "Bluffs Park Shade Structure", string search is okay.
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            found_projects.append((idx, name))
            start = idx + len(name)
            
    # Sort by appearance in text
    found_projects.sort(key=lambda x: x[0])
    
    # Now iterate through found projects and look at the text following them
    for i in range(len(found_projects)):
        start_idx, name = found_projects[i]
        # End index is the start of the next project or end of text
        if i + 1 < len(found_projects):
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        # Check if project is park-related (either in name or description)
        is_park = 'park' in name.lower() or 'playground' in name.lower() or 'recreation' in name.lower()
        if not is_park:
            # Check segment for topic keywords if not in name
            # Hints say topic keywords: "park", ...
            # But the segment contains updates. 
            if 'park' in segment.lower():
                is_park = True
        
        if is_park:
            # Check for completion in 2022
            # Look for "completed ... 2022" or similar
            if date_regex.search(segment):
                # Double check it doesn't say "completed design" if we only want construction
                # The query asks for "projects that were completed". Usually implies construction.
                # Segment often contains "(cid:190) Updates: Construction was completed..."
                if "construction was completed" in segment.lower() or "complete construction: 2022" in segment.lower() or "complete construction: november 2022" in segment.lower():
                     completed_2022_projects.add(name)

# Now sum funding
total_funding = 0
found_details = []
for name in completed_2022_projects:
    # Find amount in funding_data
    records = [r for r in funding_data if r['Project_Name'] == name]
    for r in records:
        total_funding += int(r['Amount'])
        found_details.append({"name": name, "amount": r['Amount']})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_details}))"""

env_args = {'var_function-call-2809487722948638107': 'file_storage/function-call-2809487722948638107.json', 'var_function-call-2809487722948637720': 'file_storage/function-call-2809487722948637720.json'}

exec(code, env_args)
