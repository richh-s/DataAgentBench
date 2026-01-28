code = """import json
import re
import pandas as pd

# Load data
funding_path = locals()['var_function-call-4559408233983332253']
docs_path = locals()['var_function-call-4559408233983329834']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Get all unique project names from funding to help with extraction
funding_df = pd.DataFrame(funding_data)
all_project_names = funding_df['Project_Name'].unique().tolist()

# Helper to clean name (remove parenthetical suffixes)
def get_base_name(name):
    return re.sub(r'\s*\(.*?\)$', '', name).strip()

# Map base names to list of full names
base_to_full = {}
for name in all_project_names:
    base = get_base_name(name)
    if base not in base_to_full:
        base_to_full[base] = []
    base_to_full[base].append(name)

# Set of base names for easy lookup
base_names_set = set(base_to_full.keys())

# We need to find these projects in the text and extract metadata
project_metadata = {} # {base_name: {'st': '...', 'is_disaster': bool, 'text_snippet': '...'}}

# Sort base names by length desc to match longest first in text
sorted_base_names = sorted(list(base_names_set), key=len, reverse=True)

for doc in civic_docs:
    text = doc['text']
    # Find positions of all projects in this text
    # We use base names to match.
    # Note: A project name usually appears as a header.
    # We'll search for the name followed by newline or some delimiter? 
    # Or just occurance. The names are quite specific.
    
    found_positions = []
    for base_name in sorted_base_names:
        # Simple find. Maybe regex with boundary?
        # Names can be "2022 Morning View..." or "PCH Median..."
        # Let's try finding the name case-insensitive? Or exact? 
        # The text snippet had exact capitalization.
        matches = [m.start() for m in re.finditer(re.escape(base_name), text)]
        for pos in matches:
            found_positions.append((pos, base_name))
            
    # Sort by position
    found_positions.sort()
    
    # Filter overlapping matches (e.g. "Project A" and "Project A Phase 2")
    # Since we sorted names by length, we might have matched sub-names.
    # But we want the specific sections.
    # Actually, if "Project A" is at pos 100, and "Project A Phase 2" is at 100.
    # We want the longest match.
    # Let's deduplicate based on start position, keeping longest name.
    unique_positions = []
    if found_positions:
        curr_pos = -1
        for pos, name in found_positions:
            # If this match starts at the same pos as previous, skip (since shorter comes later due to our previous sort? No, we sorted by length first, then searched. 
            # Wait, we iterated names by length desc. So "Project A Phase 2" was found before "Project A".
            # Both have same start pos.
            # So `found_positions` contains both.
            # We want to keep the one that covers the text.
            # Actually, we should just iterate through `found_positions` and skip if contained in previous?
            # But `found_positions` is sorted by `pos`.
            # If pos is same, the order depends on search order.
            # We need to stabilize sort.
            pass
        
        # Better approach:
        # Sort by pos ASC, then length DESC.
        found_positions.sort(key=lambda x: (x[0], -len(x[1])))
        
        final_matches = []
        last_end = -1
        for pos, name in found_positions:
            if pos >= last_end:
                final_matches.append((pos, name))
                last_end = pos + len(name)
        
        # Now extract text blocks
        for i, (pos, name) in enumerate(final_matches):
            start_idx = pos
            end_idx = final_matches[i+1][0] if i+1 < len(final_matches) else len(text)
            
            block = text[start_idx:end_idx]
            
            # Extract Info
            # 1. Start Date (st)
            # Look for "Begin Construction: ..." or "Start Date: ..."
            st = None
            st_match = re.search(r'(?:Begin|Start)\s*Construction:?\s*([^\n]*)', block, re.IGNORECASE)
            if st_match:
                st = st_match.group(1).strip()
            
            # Check for "Construction was completed" if st not found?
            # The user asks for "started in 2022". Completed in 2022 doesn't guarantee start in 2022.
            # But let's verify if "began" is used.
            if not st:
                 st_match_2 = re.search(r'Construction\s*began:?\s*([^\n]*)', block, re.IGNORECASE)
                 if st_match_2:
                     st = st_match_2.group(1).strip()

            # 2. Is Disaster
            # Check keywords in block
            disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Fire', 'Disaster', 'Recovery', 'Emergency']
            is_disaster = False
            for kw in disaster_keywords:
                if kw.lower() in block.lower():
                    is_disaster = True
                    break
            
            # Update project_metadata
            # If we already have this project, merge info? 
            # (e.g. one doc has design, next has construction)
            # We prefer the one with a Start Date.
            if name not in project_metadata:
                project_metadata[name] = {'st': st, 'is_disaster': is_disaster}
            else:
                if st and not project_metadata[name]['st']:
                    project_metadata[name]['st'] = st
                if is_disaster:
                    project_metadata[name]['is_disaster'] = True

# Now we have metadata for base names found in text.
# We also need to check "derived" disaster status (if Funding has suffix).

# Determine which projects to include
included_funding_amounts = []
included_projects = []

for base_name in base_names_set:
    # Check if we found this base name in text
    meta = project_metadata.get(base_name)
    
    # If not found in text, we can't determine start date. Skip?
    # Unless we want to try fuzzy matching? 
    # Let's assume strict match for now.
    if not meta:
        continue
        
    st = meta['st']
    is_disaster_text = meta['is_disaster']
    
    # Check if started in 2022
    started_2022 = False
    if st and '2022' in st:
        started_2022 = True
    
    if not started_2022:
        continue
        
    # Check if disaster
    # 1. Text keywords
    # 2. Suffixes in ANY of the funding names for this base
    is_disaster = is_disaster_text
    funding_records = base_to_full[base_name]
    
    for fname in funding_records:
        if any(x in fname for x in ['FEMA', 'CalOES', 'CalJPIA']):
            is_disaster = True
            break
            
    if is_disaster:
        # Sum funding for ALL records of this base name
        # Wait, strictly, we should sum funding for the project.
        # If the project is disaster-related, all its funding counts?
        # Yes, usually.
        # Also, the Funding table might have duplicates or phases?
        # Assuming Project_Name + Funding_ID is unique.
        
        project_total = 0
        for fname in funding_records:
            # Get amount
            rows = funding_df[funding_df['Project_Name'] == fname]
            amount = rows['Amount'].astype(int).sum()
            project_total += amount
            
        included_funding_amounts.append(project_total)
        included_projects.append({'name': base_name, 'amount': project_total, 'st': st})

total_funding = sum(included_funding_amounts)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "projects": included_projects,
    "debug_metadata": {k:v for k,v in project_metadata.items() if '2022' in str(v.get('st'))}
}))"""

env_args = {'var_function-call-4559408233983329834': 'file_storage/function-call-4559408233983329834.json', 'var_function-call-4559408233983332253': 'file_storage/function-call-4559408233983332253.json'}

exec(code, env_args)
