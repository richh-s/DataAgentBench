code = """import json
import re

# Load data
with open(locals()['var_function-call-62592550053274037'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-62592550053277018'], 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([d.get('text', '') for d in civic_docs])

# Define keywords
keywords = ['emergency', 'fema']

# Helper to check keywords
def has_keywords(text):
    return any(k in text.lower() for k in keywords)

# Helper to normalize name (strip suffixes)
def normalize_name(name):
    # Strip common suffixes like (FEMA Project), (CalOES Project), etc.
    # The hint mentions suffixes.
    # Let's strip anything in parentheses at the end if it contains FEMA, CalOES, CalJPIA
    clean = re.sub(r'\s*\((?:.*?(?:FEMA|CalOES|CalJPIA).*?)\)$', '', name, flags=re.IGNORECASE)
    return clean.strip()

# 1. Identify all unique normalized names from Funding to search in text
unique_names = set()
for item in funding_data:
    unique_names.add(normalize_name(item['Project_Name']))
    unique_names.add(item['Project_Name']) # Also add original name just in case

# 2. Find positions of these names in the text
# We want to find the headers too to determine status
headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

# Map positions to headers
header_positions = []
for h in headers:
    for m in re.finditer(re.escape(h), full_text, re.IGNORECASE):
        header_positions.append((m.start(), "HEADER", h))

# Find project positions
project_positions = []
for name in unique_names:
    if len(name) < 5: continue # Skip short abbreviations if any
    # Search for name at start of line or following newlines? 
    # The text structure in preview: "Project Name\n\n(cid:190) Updates:"
    # So we look for name followed by newline
    # Or just name. Simple is better.
    # But common words might match. Project names are usually specific.
    # Let's search exact string.
    for m in re.finditer(re.escape(name), full_text, re.IGNORECASE):
        # We try to ensure it's a "heading" usage, not a reference.
        # In the text: "2022 Morning View Resurfacing..." followed by newline.
        # Let's accept all occurrences and pick the one that looks like a section header if possible?
        # Or just take the first one?
        # Or take all and see which one is followed by "Updates:"?
        # Let's store all matches.
        project_positions.append((m.start(), "PROJECT", name))

# Sort all positions
all_positions = sorted(header_positions + project_positions, key=lambda x: x[0])

# Determine status for each project mentioned in text
project_status_map = {} # Name -> Status
current_header = "Unknown"

for i in range(len(all_positions)):
    pos, type_, content = all_positions[i]
    
    if type_ == "HEADER":
        current_header = content
    elif type_ == "PROJECT":
        # Check if this occurrence is likely a section header
        # Look at text following it until next position
        next_pos = all_positions[i+1][0] if i+1 < len(all_positions) else len(full_text)
        segment = full_text[pos:next_pos]
        
        # Heuristic: A project section usually contains "Updates:" or "Project Schedule:"
        # The preview shows: "(cid:190) Updates:" or just "Updates:"
        if "Updates:" in segment or "Project Schedule:" in segment or "Project Description:" in segment:
            # Determine status
            status = "Unknown"
            if "Design" in current_header:
                status = "design"
            elif "Not Started" in current_header:
                status = "not started"
            elif "Construction" in current_header:
                if "completed" in segment.lower():
                    status = "completed"
                else:
                    status = "construction" # Or 'design' (active)
            
            # Additional check: text might override status?
            # "Status: ..."
            
            # Store it. Using the "content" (name) as key.
            # Warning: matches might include substrings. 
            # We want to favor the longest match?
            # The 'content' is the name we searched for.
            project_status_map[content] = status
            
            # Check for keywords in segment to mark relevance
            # If segment has keywords, we should remember this project is relevant
            if has_keywords(segment):
                # We can store relevance too, but easier to just check later
                pass 

# Now build the result
results = []
seen_funding_ids = set()

for item in funding_data:
    f_id = item['Funding_ID']
    if f_id in seen_funding_ids: continue
    
    p_name = item['Project_Name']
    amount = item['Amount']
    source = item['Funding_Source']
    
    # Check relevance (Name or Text)
    # 1. Name relevance
    is_relevant_name = has_keywords(p_name)
    
    # 2. Find status and text relevance
    # We try normalized name first, then exact name
    norm_name = normalize_name(p_name)
    
    status = "not started" # Default? Or None?
    # Wait, if not found in text, maybe it's "not started" or we don't know.
    # The hint says "Projects have three statuses...".
    # I'll default to "not started" if I can't find it? Or better, omit status?
    # User asks "What are the ... statuses".
    # If I can't find it in the docs, I might skip it? 
    # BUT if the project name has "FEMA", I must report it.
    
    found_status = None
    is_relevant_text = False
    
    # Check if we found this project in the text
    # We prefer the longest key match in project_status_map that equals norm_name or p_name
    if p_name in project_status_map:
        found_status = project_status_map[p_name]
        # We need to re-check the text segment for keywords?
        # I didn't store the segment.
        # Let's re-verify relevance if name is not relevant.
        pass
    elif norm_name in project_status_map:
        found_status = project_status_map[norm_name]
    
    # If we found a status, we assume we found the project.
    # Now check relevance in text if name is not relevant.
    # This is expensive to re-find.
    # Let's optimize: Store relevance in project_status_map?
    # I'll modify the loop above to store (status, has_keywords_in_text).
    
    # Refined loop logic needed. I'll rely on name matching for now.
    # If p_name has keywords -> relevant.
    # If norm_name found in text -> check keywords in that text segment.
    
    # Let's assume if I need to output it, I must know the status.
    # If p_name has keywords, I want to output it. If status unknown, I'll say "unknown" or "not started".
    
    # Let's just output what I have.
    if found_status:
        status = found_status
    
    # How to check text relevance?
    # Re-extract segment?
    # Let's do a quick check: if is_relevant_name is False, we NEED text relevance.
    # If is_relevant_name is True, we keep it regardless.
    
    if is_relevant_name:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": source,
            "Amount": amount,
            "Status": status
        })
    elif found_status: 
        # Project is in text. Check if text has keywords.
        # I need to know if the text segment had keywords.
        # I will hack this: search for keywords in the FULL TEXT around the project name?
        # No, that's messy.
        
        # Let's update the map creation to store (status, is_relevant_segment).
        pass

# Re-running logic with map update
project_info_map = {} # Name -> {'status': s, 'relevant': bool}

for i in range(len(all_positions)):
    pos, type_, content = all_positions[i]
    if type_ == "HEADER":
        current_header = content
    elif type_ == "PROJECT":
        next_pos = all_positions[i+1][0] if i+1 < len(all_positions) else len(full_text)
        segment = full_text[pos:next_pos]
        if "Updates:" in segment or "Project Schedule:" in segment or "Project Description:" in segment:
            status = "Unknown"
            if "Design" in current_header: status = "design"
            elif "Not Started" in current_header: status = "not started"
            elif "Construction" in current_header:
                status = "completed" if "completed" in segment.lower() else "construction"
            
            relevant = has_keywords(segment)
            project_info_map[content] = {'status': status, 'relevant': relevant}

# Final Result Construction
final_output = []
for item in funding_data:
    p_name = item['Project_Name']
    norm_name = normalize_name(p_name)
    
    info = project_info_map.get(p_name) or project_info_map.get(norm_name)
    
    # Determine relevance
    name_relevant = has_keywords(p_name)
    text_relevant = info['relevant'] if info else False
    
    if name_relevant or text_relevant:
        final_output.append({
            "Project_Name": p_name,
            "Funding_Source": item['Funding_Source'],
            "Amount": item['Amount'],
            "Status": info['status'] if info else "not started" # Default if relevant by name but not in text?
        })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-2440996547258625204': ['Funding'], 'var_function-call-2440996547258622967': ['civic_docs'], 'var_function-call-2122594864921453126': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-2122594864921454085': 'file_storage/function-call-2122594864921454085.json', 'var_function-call-62592550053274037': 'file_storage/function-call-62592550053274037.json', 'var_function-call-62592550053277018': 'file_storage/function-call-62592550053277018.json'}

exec(code, env_args)
