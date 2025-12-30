code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-6790771977792377935'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-17703270697767214172'], 'r') as f:
    civic_docs = json.load(f)

# Helper function to check if text mentions Spring 2022 start
def check_start_date(text_block):
    # Regex for start dates
    # Patterns: "Begin Construction: Spring 2022", "Start: March 2022", etc.
    # Also "Advertise" if that counts? Let's stick to "Begin Construction" or "Construction Start" or just "Start" 
    # and the date.
    # The text uses "(cid:131)" as bullet.
    
    # Normalize text
    text_block = text_block.replace('\n', ' ')
    
    # Look for "Begin Construction" or "Start" near "Spring 2022" or "March 2022" etc.
    # Flexible regex: (Begin Construction|Start|Construction to begin|Construction scheduled to begin).*?(Spring 2022|March 2022|April 2022|May 2022)
    # Be careful not to match across different list items too far.
    
    # Let's start by finding all mentions of 2022 dates and seeing context.
    # Actually, let's look for specific phrases.
    
    patterns = [
        r"Begin Construction:?\s*(Spring 2022|March 2022|April 2022|May 2022)",
        r"Construction Start:?\s*(Spring 2022|March 2022|April 2022|May 2022)",
        r"Construction to begin:?\s*(Spring 2022|March 2022|April 2022|May 2022)",
        r"Scheduled to begin:?\s*(Spring 2022|March 2022|April 2022|May 2022)",
        r"Start Date:?\s*(Spring 2022|March 2022|April 2022|May 2022)",
        # Also check for exact matches in schedule lists
        r"Complete Design:.*?Advertise:.*?Begin Construction:?\s*(Spring 2022|March 2022|April 2022|May 2022)"
    ]
    
    for pat in patterns:
        if re.search(pat, text_block, re.IGNORECASE):
            return True
    return False

projects_started_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    # Iterate lines to find projects
    # Structure: Project Name \n (cid:190) Updates:
    # We'll accumulate lines until we hit a new project start
    
    # First pass: Identify project start indices
    project_indices = []
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "(cid:190) Project Description:" in line:
            # The project name is likely in the lines before this.
            # Usually the immediate previous non-empty line.
            # But sometimes the header is "Capital Improvement Projects (Design)" which is not a project.
            # The project name is the one before the Updates line.
            
            # Find previous non-empty line
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            
            if j >= 0:
                name = lines[j].strip()
                # Check if it's a category header. Category headers usually don't have "Updates:" immediately following?
                # Actually, the category headers "Capital Improvement Projects (Design)" are followed by project names, not Updates.
                # So the logic holds.
                project_indices.append((j, name))
    
    # Now extract blocks
    for k in range(len(project_indices)):
        start_idx, name = project_indices[k]
        # End index is the start of the next project or end of text
        if k < len(project_indices) - 1:
            end_idx = project_indices[k+1][0]
        else:
            end_idx = len(lines)
            
        block_text = "\n".join(lines[start_idx:end_idx])
        
        # Check if this project block contains the start date
        if check_start_date(block_text):
            projects_started_spring_2022.add(name)

# Normalize project names
# Remove punctuation or extra spaces?
# The Funding table has clean names. The docs might have slightly different formatting.
# Let's clean up the extracted names.
clean_projects = set()
for p in projects_started_spring_2022:
    # Remove leading/trailing whitespace
    p_clean = p.strip()
    clean_projects.add(p_clean)

# Now filter funding
# We need to match clean_projects with funding_df['Project_Name']
# Direct match might fail if there are minor diffs.
# Let's try direct match first, then fuzzy if needed.
# But for now, let's print the projects found to verify.

matched_funding = funding_df[funding_df['Project_Name'].isin(clean_projects)]

# Result
print("__RESULT__:")
print(json.dumps({
    "found_projects": list(clean_projects),
    "matched_projects": matched_funding['Project_Name'].tolist(),
    "matched_count": len(matched_funding),
    "total_funding": int(matched_funding['Amount'].astype(int).sum())
}))"""

env_args = {'var_function-call-6629743294879476725': ['civic_docs'], 'var_function-call-6629743294879475928': ['Funding'], 'var_function-call-6790771977792377935': 'file_storage/function-call-6790771977792377935.json', 'var_function-call-6790771977792376994': 'file_storage/function-call-6790771977792376994.json', 'var_function-call-17703270697767214172': 'file_storage/function-call-17703270697767214172.json'}

exec(code, env_args)
