code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-6201891487600376940'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-6201891487600376067'], 'r') as f:
    civic_docs = json.load(f)

# Get unique project names from funding
project_names = funding_df['Project_Name'].unique().tolist()
# Sort by length descending to match longest names first
project_names.sort(key=len, reverse=True)

completed_park_projects = set()

# Helper to check if text indicates completion in 2022
def is_completed_in_2022(text):
    text = text.lower()
    # Check for 2022
    if '2022' not in text:
        return False
    
    # Check for "completed"
    if 'completed' not in text:
        return False
        
    # More specific checks
    # Look for "construction was completed" ... "2022"
    # or "completed" ... "2022"
    # Avoid "complete design" associated with 2022 if that's the only match.
    
    # Regex to find "completed" and check context
    # We look for "completed" not followed immediately by "design"
    # and having "2022" in the vicinity (e.g. within 50 chars or same line)
    
    # Split into lines to be safer?
    lines = text.split('\n')
    for line in lines:
        if '2022' in line and 'completed' in line:
            # Check if it is "complete design"
            if 'design' in line:
                # E.g. "Complete Design: Spring 2022" -> Skip
                # But "Design completed 2021, Construction completed 2022" -> Keep?
                # If line has "construction" and "completed" and "2022", it's good.
                if 'construction' in line:
                    return True
                # If only "complete design", skip
                if 'complete design' in line or 'design complete' in line:
                    continue
            else:
                # Found "completed" and "2022" and no "design". Likely good.
                # E.g. "Construction was completed, November 2022"
                return True
    
    # Also check if sentences span lines? The docs seem to use lines for bullet points.
    # What if "Construction was completed" is on one line and "November 2022" on next?
    # The preview shows them on same line or close.
    # "Construction was completed, November 2022"
    
    return False

# Iterate docs
for doc in civic_docs:
    content = doc['text']
    
    # Find positions of all project names
    # We will create a list of (start_index, project_name)
    positions = []
    content_lower = content.lower()
    
    for p_name in project_names:
        # Simple string search. Note: Names in text might be slightly different or have extra spaces.
        # But instructions say "Project_Name ... matches ... extracted".
        # We'll assume exact match or case-insensitive match.
        idx = content_lower.find(p_name.lower())
        while idx != -1:
            positions.append((idx, p_name))
            idx = content_lower.find(p_name.lower(), idx + 1)
            
    # Sort positions
    positions.sort(key=lambda x: x[0])
    
    # Filter overlapping matches (if any, due to substrings)
    # Since we sorted project_names by length desc, if we find a long one, we might find a short one inside it.
    # But finding positions in the full text handles this differently.
    # Example: "Project A" and "Project A Phase 2".
    # "Project A Phase 2" starts at 10. "Project A" starts at 10.
    # We should keep "Project A Phase 2" and ignore "Project A" at that same location.
    
    unique_positions = []
    if positions:
        curr_idx, curr_name = positions[0]
        unique_positions.append((curr_idx, curr_name))
        for i in range(1, len(positions)):
            idx, name = positions[i]
            last_idx, last_name = unique_positions[-1]
            # If new match starts within the previous match, ignore it (substring)
            if idx < last_idx + len(last_name):
                continue
            unique_positions.append((idx, name))
            
    # Now process segments
    for i in range(len(unique_positions)):
        start_idx, p_name = unique_positions[i]
        # End index is start of next project or end of text
        if i < len(unique_positions) - 1:
            end_idx = unique_positions[i+1][0]
        else:
            end_idx = len(content)
            
        segment = content[start_idx:end_idx]
        
        # Check topic
        is_park = False
        if 'park' in p_name.lower() or 'playground' in p_name.lower():
            is_park = True
        elif 'park' in segment.lower() or 'playground' in segment.lower():
             is_park = True
             
        if is_park:
            if is_completed_in_2022(segment):
                completed_park_projects.add(p_name)

# Calculate total funding
total_funding = 0
matched_rows = funding_df[funding_df['Project_Name'].isin(completed_park_projects)]
total_funding = matched_rows['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-6201891487600376067': 'file_storage/function-call-6201891487600376067.json', 'var_function-call-6201891487600376940': 'file_storage/function-call-6201891487600376940.json'}

exec(code, env_args)
