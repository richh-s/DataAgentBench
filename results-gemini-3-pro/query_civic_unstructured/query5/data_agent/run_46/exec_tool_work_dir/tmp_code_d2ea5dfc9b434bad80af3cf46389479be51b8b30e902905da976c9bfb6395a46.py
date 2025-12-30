code = """import json
import pandas as pd

# Keys for storage
key_funding = locals()['var_function-call-10032448971430008742']
key_docs = locals()['var_function-call-17801199440429665660']

# Load data
with open(key_funding, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Map Project Name to Amount(s)
# Since there might be multiple entries, we'll store them in a way to lookup.
# Actually, Project_Name is unique per row? The output shows IDs.
# Let's create a lookup dictionary.
funding_lookup = {}
for _, row in df_funding.iterrows():
    funding_lookup[row['Project_Name']] = row['Amount']

valid_projects = set(funding_lookup.keys())

with open(key_docs, 'r') as f:
    civic_docs = json.load(f)

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey']
section_keywords = ['Disaster Recovery']

matched_records = []

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_project = None
    project_text_block = []
    
    # We first segment the text into project blocks
    # A block starts with a Project Name line
    # And ends at the next Project Name line or Section Header
    
    # Identify lines that are project names
    project_indices = []
    for idx, line in enumerate(lines):
        clean = line.strip()
        if clean in valid_projects:
            project_indices.append((idx, clean))
    
    # Now process blocks
    for i in range(len(project_indices)):
        start_idx, p_name = project_indices[i]
        end_idx = project_indices[i+1][0] if i+1 < len(project_indices) else len(lines)
        
        # Get the text block
        block_lines = lines[start_idx:end_idx]
        block_text = " ".join(block_lines).lower()
        
        # Check start date
        # Look for "begin construction" or "start date" or "st:" followed by "2022"
        # We search within a small window or the whole block? Whole block is fine.
        start_2022 = False
        if 'begin construction' in block_text or 'start date' in block_text or 'st:' in block_text:
            # We need to be careful. "Begin construction: Fall 2023" should not match.
            # We need to check if "2022" is associated with the start keyword.
            # Simple check: Is "2022" in the same line or nearby?
            # Let's iterate lines in block
            for bl in block_lines:
                bl_lower = bl.lower()
                if ('begin construction' in bl_lower or 'start date' in bl_lower or 'st:' in bl_lower):
                    if '2022' in bl_lower:
                        start_2022 = True
                        break
        
        if not start_2022:
            continue
            
        # Check if disaster related
        is_disaster = False
        # 1. Name contains keyword
        if any(k in p_name for k in disaster_keywords):
            is_disaster = True
        # 2. Block text contains keyword
        elif any(k.lower() in block_text for k in disaster_keywords):
            is_disaster = True
        
        if is_disaster:
            # Determine which funding record to use
            # If p_name already has suffix, use it.
            # If p_name is generic, check if a suffix version exists in valid_projects?
            # But we extracted p_name from valid_projects, so p_name IS a valid key.
            # If the text matched "Project X", and "Project X" is in funding.
            # If "Project X (FEMA Project)" is ALSO in funding, and the text implies FEMA.
            # We should probably use the FEMA one.
            # Let's check for "suffix extensions".
            
            best_match = p_name
            # Try to find a more specific FEMA/Disaster name in funding_lookup
            potential_suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']
            for suffix in potential_suffixes:
                candidate = p_name + suffix
                if candidate in funding_lookup:
                    best_match = candidate
                    break
            
            # Store match (use a set to avoid duplicates? Or list?)
            # The same project might be mentioned in multiple docs.
            # We should count it once.
            matched_records.append(best_match)

# Unique projects
unique_projects = list(set(matched_records))

total = sum(funding_lookup[p] for p in unique_projects)

print("__RESULT__:")
print(json.dumps({
    "projects": unique_projects,
    "total_funding": total
}))"""

env_args = {'var_function-call-10032448971430008742': 'file_storage/function-call-10032448971430008742.json', 'var_function-call-17801199440429665660': 'file_storage/function-call-17801199440429665660.json'}

exec(code, env_args)
