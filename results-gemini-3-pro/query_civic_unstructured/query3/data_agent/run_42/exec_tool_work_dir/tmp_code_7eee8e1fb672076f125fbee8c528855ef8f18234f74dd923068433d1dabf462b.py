code = """import json
import pandas as pd
import re
import os

# Access file paths from previous tool results
funding_file_path = locals()['var_function-call-15139260812561284578']
civic_docs_file_path = locals()['var_function-call-12991954254927401902']

# Load Funding Data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Combine all text
full_text = "\n".join([d['text'] for d in civic_docs])

# Normalize funding names for matching
def normalize_name(name):
    # Remove text in parentheses
    name = re.sub(r'\s*\(.*?\)', '', name)
    return name.strip().lower()

funding_df['normalized_name'] = funding_df['Project_Name'].apply(normalize_name)

# Identify sections in text
lines = full_text.split('\n')
current_status = 'unknown'
project_blocks = []
current_project = None
current_block = []

# Known normalized names for quick lookup
known_names = set(funding_df['normalized_name'].tolist())

# Regex for headers (e.g., "Capital Improvement Projects (Design)")
header_re = re.compile(r'Capital Improvement Projects \((.*?)\)', re.IGNORECASE)

for line in lines:
    line_stripped = line.strip()
    if not line_stripped:
        continue
    
    # Check for header
    header_match = header_re.search(line_stripped)
    if header_match:
        current_status = header_match.group(1).lower()
        # Close current project
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status,
                'text': "\n".join(current_block)
            })
            current_project = None
            current_block = []
        continue
    
    # Check if line is a project name
    norm_line = normalize_name(line_stripped)
    if norm_line in known_names and len(norm_line) > 5:
        # Close previous project
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status,
                'text': "\n".join(current_block)
            })
        
        current_project = line_stripped # Use text version
        block_status = current_status
        current_block = []
    else:
        if current_project:
            current_block.append(line_stripped)

# Add last project
if current_project:
    project_blocks.append({
        'name': current_project,
        'status': block_status,
        'text': "\n".join(current_block)
    })

# Process blocks to find relevant projects
results = []
found_projects = set()

for block in project_blocks:
    norm_name = normalize_name(block['name'])
    
    # Find matching funding records
    matches = funding_df[funding_df['normalized_name'] == norm_name]
    
    for idx, row in matches.iterrows():
        funding_name = row['Project_Name']
        text_lower = block['text'].lower()
        
        is_relevant = False
        # Check name for keywords
        if 'fema' in funding_name.lower() or 'emergency' in funding_name.lower():
            is_relevant = True
        
        # Check text for keywords
        if 'fema' in text_lower or 'emergency' in text_lower:
            is_relevant = True
            
        if is_relevant:
            # Refine status
            status = block['status']
            if 'completed' in text_lower and 'construction was completed' in text_lower:
                status = 'completed'
            elif 'construction' in status and 'under construction' in text_lower:
                status = 'construction' 
                # Keep 'construction' if specific, or map to 'design'/'completed' based on strict rules?
                # User prompt: "Projects have three statuses: 'design', 'completed', and 'not started'".
                # I should probably map 'construction' to 'design' (implementation) or keep it if it provides more info.
                # But to follow "Projects have three statuses" hint, maybe I should map.
                # However, "completed" is one. "not started" is one.
                # "Design" (in planning/design phase).
                # Construction is physically happening. It's neither design (planning) nor completed.
                # Maybe the hint implies "Construction" is not a status in the DB but I found it in text headers?
                # Let's check if I can map it. 
                # Or maybe the hint is just guidance. I will output 'construction' to be precise, or 'design' if I must.
                # Let's stick to 'construction' if text says so, as it is more accurate.
            
            # Map status to the 3 provided if possible?
            # Header: "Capital Improvement Projects (Design)" -> "design"
            # Header: "Capital Improvement Projects (Construction)" -> "construction"
            # Header: "Capital Improvement Projects (Not Started)" -> "not started"
            
            # If I must choose from 3: maybe Construction falls under Design (active)? Or Completed? No.
            # I'll just use the string I found, maybe lowercase.
            
            res_entry = {
                'Project_Name': funding_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': status
            }
            results.append(res_entry)
            found_projects.add(funding_name)

# Also check for projects in Funding that have FEMA/Emergency in name but were NOT found in text blocks
# This ensures we don't miss them if parsing failed.
# But for these, we won't have Status from text.
# We can try to infer status or leave it. The prompt asks for status.
# If I can't find it in text, maybe I can assume "not started" or "unknown"?
# Or maybe they ARE in text but I missed them.
# I'll add them with Status "Unknown" if they are clearly relevant.

for idx, row in funding_df.iterrows():
    funding_name = row['Project_Name']
    if funding_name not in found_projects:
        if 'fema' in funding_name.lower() or 'emergency' in funding_name.lower():
            results.append({
                'Project_Name': funding_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': 'Unknown' # or maybe try to find substring in text without block structure?
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7580785904433881642': ['Funding'], 'var_function-call-7580785904433881717': ['civic_docs'], 'var_function-call-15139260812561284578': 'file_storage/function-call-15139260812561284578.json', 'var_function-call-15139260812561285023': 'file_storage/function-call-15139260812561285023.json', 'var_function-call-12991954254927401902': 'file_storage/function-call-12991954254927401902.json'}

exec(code, env_args)
