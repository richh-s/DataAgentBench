code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
con = sqlite3.connect('funding_database.db') # Assuming local DB file access via tool not possible directly, but previous query saved result.
# Wait, I cannot connect to the DB file directly if it's not in the environment. I must use the result from query_db.
# I saved the query_db result for "SELECT * FROM Funding" in var_function-call-15139260812561284578

with open('15139260812561284578.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open('12991954254927401902.json', 'r') as f:
    civic_docs = json.load(f)

# Combine all text
full_text = "\n".join([d['text'] for d in civic_docs])

# Normalize funding names for matching
# Remove suffixes like "(FEMA Project)", "(CalOES Project)", "(FEMA/CalOES Project)", "(FEMA)"
def normalize_name(name):
    name = re.sub(r'\s*\(.*?\)\s*', '', name)
    return name.strip().lower()

funding_df['normalized_name'] = funding_df['Project_Name'].apply(normalize_name)

# Identify sections in text
lines = full_text.split('\n')
current_status = None
project_blocks = []
current_project = None
current_block = []

# Known normalized names for quick lookup
known_names = set(funding_df['normalized_name'].tolist())

# Regex for headers
header_re = re.compile(r'Capital Improvement Projects \((.*?)\)', re.IGNORECASE)

for line in lines:
    line_stripped = line.strip()
    if not line_stripped:
        continue
    
    # Check for header
    header_match = header_re.search(line_stripped)
    if header_match:
        current_status = header_match.group(1).lower()
        # Reset current project
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status, # store the status when the project was found
                'text': "\n".join(current_block)
            })
            current_project = None
            current_block = []
        continue
    
    # Check if line is a project name
    # We check if the line (normalized) is in our known names
    norm_line = normalize_name(line_stripped)
    if norm_line in known_names and len(norm_line) > 5: # length check to avoid false positives
        # Save previous project
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status,
                'text': "\n".join(current_block)
            })
        
        current_project = line_stripped # Store the name found in text
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

# Now process the blocks
results = []
for block in project_blocks:
    # Determine if relevant
    # 1. Check for keywords in text
    text_lower = block['text'].lower()
    is_relevant = False
    if 'emergency' in text_lower or 'fema' in text_lower:
        is_relevant = True
    
    # 2. Check if the project name in Funding has "FEMA" or "Emergency"
    # Find matching funding records
    norm_name = normalize_name(block['name'])
    matches = funding_df[funding_df['normalized_name'] == norm_name]
    
    for idx, row in matches.iterrows():
        funding_name = row['Project_Name']
        if 'fema' in funding_name.lower() or 'emergency' in funding_name.lower():
            is_relevant = True
        
        # Check text for specific status updates (completed)
        status = block['status']
        if 'completed' in text_lower and 'updates' in text_lower:
             status = 'completed'
        
        if is_relevant:
            results.append({
                'Project_Name': funding_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': status
            })

# Remove duplicates
final_results = pd.DataFrame(results).drop_duplicates().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-7580785904433881642': ['Funding'], 'var_function-call-7580785904433881717': ['civic_docs'], 'var_function-call-15139260812561284578': 'file_storage/function-call-15139260812561284578.json', 'var_function-call-15139260812561285023': 'file_storage/function-call-15139260812561285023.json', 'var_function-call-12991954254927401902': 'file_storage/function-call-12991954254927401902.json'}

exec(code, env_args)
