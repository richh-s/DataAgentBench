code = """import json
import re

# Load funding results
with open(locals()['var_function-call-9124692178282648902'], 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of project names to amounts (or just a set of names if filtering is done)
# The SQL query already filtered for > 50000.
# Normalize names for matching
high_funding_projects = set()
for record in funding_data:
    name = record['Project_Name'].strip().lower()
    high_funding_projects.add(name)

# Load civic docs
with open(locals()['var_function-call-10183875392572160973'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Identify Capital Projects (Design) section
    # We look for "Capital Improvement Projects (Design)"
    # And we stop at the next section header which likely starts with "Capital Improvement Projects" or "Disaster Recovery" or ends the list.
    
    # We can split by headers.
    # Pattern to find the specific section:
    # It starts with "Capital Improvement Projects (Design)" (case insensitive?)
    # The preview has it exactly as "Capital Improvement Projects (Design)"
    
    # Let's verify if there are other headers
    # Note: text content might be messy.
    
    # Regex to capture the block:
    # Start: Capital Improvement Projects \(Design\)
    # End: Capital Improvement Projects \(Construction\) | Capital Improvement Projects \(Not Started\) | Disaster Recovery | Agenda Item | $
    
    pattern = re.compile(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects|Disaster Recovery|Agenda Item|\Z)", re.DOTALL | re.IGNORECASE)
    
    matches = pattern.findall(text)
    
    for section_text in matches:
        # Now extract project names within this section
        # Project names appear to be lines immediately followed by a line starting with (cid:190)
        # Note: (cid:190) is \u00be
        
        # Regex to find lines before "(cid:190)" or similar bullets
        # looking for:  \n<Project Name>\n\n(cid:190)
        
        # Refined regex for project name:
        # It should be a non-empty line, stripped.
        # Followed optionally by newlines, then the bullet.
        
        proj_pattern = re.compile(r"\n([^\n]+)\s*\n\s*(?:\(cid:190\)|\u00be)", re.MULTILINE)
        
        projects = proj_pattern.findall(section_text)
        
        for p in projects:
            p_clean = p.strip()
            # Basic cleanup: remove page numbers or weird artifacts if any
            # The preview looked clean: "PCH Median Improvements Project"
            if len(p_clean) > 3: # valid name length
                found_projects.add(p_clean.lower())

# Now intersect found_projects with high_funding_projects
# Since exact match might be tricky, I'll check if the extracted name is in the high_funding set.

count = 0
matched_names = []

for p in found_projects:
    if p in high_funding_projects:
        count += 1
        matched_names.append(p)
    else:
        # Try checking if the project name from text is a substring or vice versa
        # Example: "PCH Median Improvements" vs "PCH Median Improvements Project"
        # The prompt implies names match. "The Project_Name ... matches ...".
        # Let's check for fuzzy match if exact fails.
        pass

# Double check the intersection logic.
# The user wants "How many capital projects with a 'design' status have funding greater than $50,000?"
# I have the set of high funding projects.
# I have the set of "Capital Projects (Design)".
# Intersection is the answer.

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matched_names, "extracted_capital_design": list(found_projects), "high_funding_sample": list(high_funding_projects)[:10]}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json'}

exec(code, env_args)
