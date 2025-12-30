code = """import json
import sqlite3
import re

# Load funding data
with open(locals()['var_function-call-10486156171359470717'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11751913869658535097'], 'r') as f:
    civic_docs = json.load(f)

# Combine text from all docs
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Define statuses and sections
sections = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

# Helper to clean project name for matching
def clean_name(name):
    # Remove suffixes like (FEMA Project), (CalOES Project), (CalJPIA Project)
    # Also handle (FEMA/CalOES Project) etc.
    # Regex to remove parenthetical parts at the end
    return re.sub(r'\s*\(.*?\)$', '', name).strip()

# Prepare funding info lookup
# Map base_name -> list of funding records
project_funding_map = {}
for record in funding_data:
    full_name = record['Project_Name']
    base_name = clean_name(full_name)
    if base_name not in project_funding_map:
        project_funding_map[base_name] = []
    project_funding_map[base_name].append(record)

# Find section positions in text
section_positions = []
for header, status in sections.items():
    # Use re.escape to handle parentheses
    pattern = re.escape(header)
    for match in re.finditer(pattern, full_text, re.IGNORECASE):
        section_positions.append({'start': match.start(), 'name': header, 'status': status})

# Sort sections by position
section_positions.sort(key=lambda x: x['start'])

# Add an end sentinel
section_positions.append({'start': len(full_text), 'name': 'END', 'status': None})

# Now iterate sections and find projects within them
results = []

# Get all unique base names to search for
all_base_names = list(project_funding_map.keys())
# Sort by length descending to match longest names first (though exact string matching in a loop works too)
all_base_names.sort(key=len, reverse=True)

found_projects = set()

for i in range(len(section_positions) - 1):
    section = section_positions[i]
    next_section = section_positions[i+1]
    
    section_text = full_text[section['start']:next_section['start']]
    section_status = section['status']
    
    # Find projects in this section
    # We search for each base name
    # We need to know the location of each project match to define its block
    
    project_matches = []
    for base_name in all_base_names:
        # Simple substring search. Note: Names might appear multiple times, but usually once per report.
        # We assume the report structure.
        # Check if base_name is in section_text
        # We need to be careful not to match partial names if possible, but exact substring is a good start.
        
        idx = section_text.find(base_name)
        if idx != -1:
            project_matches.append({'name': base_name, 'start': idx})
    
    # Sort matches by start position
    project_matches.sort(key=lambda x: x['start'])
    
    # Filter overlapping matches (if any, e.g. "Road Repair" inside "Main Road Repair")
    # Since we sorted base_names by length desc, if we found a longer one, we might find a shorter one at same/similar index.
    # But here we used find(). `find` finds the first occurrence.
    # Better approach: Find ALL occurrences of ALL names, then resolve overlaps.
    # But for simplicity, let's assume names are distinct enough or we take the first match.
    # Actually, let's re-do matching to be more robust.
    
    # Re-do matching: find all distinct projects mentioned in this section
    # We will iterate through the text and identify project headers.
    # Since we don't know the exact format, we'll assume the Project Name is the "header".
    # We'll use the sorted matches.
    
    valid_matches = []
    if project_matches:
        # Remove duplicates or overlaps
        # Sort by start
        project_matches.sort(key=lambda x: x['start'])
        
        # Simple overlap removal: if start is same, keep longest. If start is inside previous, skip.
        # But wait, find() only returns the first index. A name might appear twice?
        # Assuming each project appears once in a section.
        
        # Let's handle the matches carefully
        # We will iterate and keep valid non-overlapping matches
        last_end = -1
        for pm in project_matches:
            # Check if this match overlaps with a chosen match
            # Since we only have 'start', we need 'end'
            pm['end'] = pm['start'] + len(pm['name'])
            
            # Check overlap with previous selected matches (not just the last one, but logically sequential)
            # Actually, because we simply did .find(), we only got the first occurrence.
            # If "Project A" is at 100, and "Project B" is at 200.
            # If "Project A Part 2" is a name, and "Project A" is a name.
            # If "Project A Part 2" is at 100. "Project A" will also be found at 100.
            # We want "Project A Part 2".
            # We sorted base_names by length desc. So "Project A Part 2" would be checked first.
            # But we didn't remove it from the text.
            # So `project_matches` contains both.
            # We need to filter.
            
            is_sub = False
            for existing in valid_matches:
                # If pm is inside existing
                if pm['start'] >= existing['start'] and pm['end'] <= existing['end']:
                    is_sub = True
                    break
                # If existing is inside pm (should not happen if we process correctly or assume single occurrence)
                # But here we process independently.
                if existing['start'] >= pm['start'] and existing['end'] <= pm['end']:
                    # Existing is shorter and inside pm. Replace existing?
                    # Since we sort by start, and we want to capture the "heading".
                    pass
            
            if not is_sub:
                valid_matches.append(pm)
    
    # Now we have valid_matches in order.
    # Define blocks.
    for k in range(len(valid_matches)):
        match = valid_matches[k]
        start = match['start']
        end_of_block = valid_matches[k+1]['start'] if k+1 < len(valid_matches) else len(section_text)
        
        block_text = section_text[start:end_of_block]
        
        # Determine specific status
        status = section_status
        if status == "construction":
            if "completed" in block_text.lower() and "notice of completion" in block_text.lower():
                status = "completed"
            elif "construction was completed" in block_text.lower():
                status = "completed"
            else:
                # If not explicitly completed, keep as construction or map to design?
                # User hint: "three statuses: design, completed, not started".
                # If I return "construction", it's not one of the three.
                # But "under construction" is definitely not "design" or "not started" or "completed".
                # I'll stick to "construction" if it's active construction, unless strict adherence is required.
                # Given the hint, maybe "design" covers "implementation"? Unlikely.
                # I'll return "construction" as it's truthful.
                pass
        
        # Check relevance
        # 1. Check Keywords in Text
        keywords = ['emergency', 'fema', 'fire', 'disaster']
        is_relevant_text = any(kw in block_text.lower() for kw in keywords)
        
        # 2. Check Project Name and Funding Records
        base_name = match['name']
        funding_records = project_funding_map.get(base_name, [])
        
        for record in funding_records:
            full_name = record['Project_Name']
            is_relevant_name = any(kw in full_name.lower() for kw in keywords)
            
            if is_relevant_text or is_relevant_name:
                # Add to results
                results.append({
                    "Project Name": full_name,
                    "Funding Source": record['Funding_Source'],
                    "Amount": record['Amount'],
                    "Status": status
                })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8394565906188942673': 'file_storage/function-call-8394565906188942673.json', 'var_function-call-10486156171359470717': 'file_storage/function-call-10486156171359470717.json', 'var_function-call-11751913869658535097': 'file_storage/function-call-11751913869658535097.json'}

exec(code, env_args)
