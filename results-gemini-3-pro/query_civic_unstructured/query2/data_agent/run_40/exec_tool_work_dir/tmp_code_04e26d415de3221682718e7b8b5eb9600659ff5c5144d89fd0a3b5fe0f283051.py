code = """import json
import re

# Load data
with open(locals()['var_function-call-13888598528909911574'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-13888598528909910147'], 'r') as f:
    funding_data = json.load(f)

# Build Funding Map
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip().lower()
    amount = int(item['Amount'])
    # Handle duplicates if any (sum them up?)
    # Assuming unique per project or just sum all funding records for the project
    if name in funding_map:
        funding_map[name] += amount
    else:
        funding_map[name] = amount

found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify indices where a project block starts
    # Criteria: Line starts with (cid:190) Updates or (cid:190) Project Description
    # Note: (cid:190) might be encoded differently or just text.
    # The preview showed: "(cid:190) Updates:"
    
    project_indices = []
    for idx, line in enumerate(lines):
        line_s = line.strip()
        if line_s.startswith('(cid:190) Updates') or \
           line_s.startswith('(cid:190) Project Description') or \
           line_s.startswith('(cid:190) Project Updates') or \
           'Updates:' in line_s and line_s.startswith('(cid:190)'):
            project_indices.append(idx)
            
    # Now extract projects
    for i, start_idx in enumerate(project_indices):
        # 1. Get Name
        # Look backwards from start_idx
        name = "Unknown"
        k = start_idx - 1
        while k >= 0:
            candidate = lines[k].strip()
            if candidate:
                name = candidate
                # Check if the line before is also part of the name?
                # Sometimes names are split. But usually headers are one line or short.
                # Let's verify if the line before is "Capital Improvement Projects..." which is a header.
                # If so, ignore it.
                break
            k -= 1
        
        # 2. Get Block Content
        # From start_idx to the next project's name line
        # The next project's name line is immediately before project_indices[i+1]
        # So block goes from start_idx to project_indices[i+1] - (lines to skip for name)
        # Actually, let's just take text until project_indices[i+1]
        
        if i + 1 < len(project_indices):
            next_start = project_indices[i+1]
            # The name of the next project is likely at next_start - X.
            # So the block ends around next_start - X.
            # We can just take up to next_start for searching keywords/dates, 
            # filtering out the next project's name is not critical for "contains 2022" 
            # unless the name contains 2022 (e.g. "2022 Road Repair").
            # But "2022" in name is not "completed in 2022".
            # So safely taking lines[start_idx : next_start] is okay.
            block_lines = lines[start_idx : next_start]
        else:
            block_lines = lines[start_idx:]
            
        block_text = " ".join(block_lines).lower()
        
        # 3. Analyze
        # Topic: "park", "playground", "recreation"
        keywords = ["park", "playground", "recreation", "open space", "walkway"] 
        # Added "walkway" as "Malibu Bluffs Park South Walkway" is relevant
        # Note: "Bluffs Park Shade Structure" -> "park" is in name.
        
        name_lower = name.lower()
        is_park = any(kw in name_lower for kw in keywords) or any(kw in block_text for kw in keywords)
        
        # Status: Completed in 2022
        is_completed_2022 = False
        
        # Search for patterns
        # "construction was completed [month] 2022"
        # "complete construction: [month] 2022"
        
        # Using simple string checks first
        if "2022" in block_text:
            if "construction was completed" in block_text and "2022" in block_text:
                # Need to be sure they are close or in same sentence
                # Regex is better
                if re.search(r'construction was completed.{0,50}2022', block_text):
                    is_completed_2022 = True
            if "complete construction" in block_text and "2022" in block_text:
                 if re.search(r'complete construction.{0,50}2022', block_text):
                     is_completed_2022 = True
            if "construction completed" in block_text and "2022" in block_text:
                 if re.search(r'construction completed.{0,50}2022', block_text):
                     is_completed_2022 = True
                     
        if is_park and is_completed_2022:
            found_projects.append(name)

# Deduplicate
found_projects = list(set(found_projects))

total_funding = 0
matched_details = []

print("Identified Projects:")
for p in found_projects:
    print(p)
    # Match funding
    # Try exact match
    p_clean = p.strip().lower()
    
    matched = False
    
    # Check exact
    if p_clean in funding_map:
        amt = funding_map[p_clean]
        total_funding += amt
        matched_details.append((p, amt))
        matched = True
    else:
        # Check fuzzy
        # Iterate all funding keys
        best_match = None
        for f_name in funding_map:
            # Check for inclusion
            if p_clean in f_name or f_name in p_clean:
                # "Bluffs Park Shade Structure"
                # "Broad Beach Road Water Quality Repair"
                # Check for high similarity?
                # If one contains the other, assume match?
                # Be careful: "Malibu Road" vs "Malibu Road Slope Repairs"
                # But here p is likely the full name from the doc.
                
                # Let's match if the document name contains the funding name or vice versa
                # But funding name "Bluffs Park Shade Structure" ($21000)
                # Doc Name "Bluffs Park Shade Structure"
                # They should match exactly if cleaned.
                
                # Check for "Bluffs Park Shade Structure" vs "Bluffs Park Shade Structure"
                
                # Let's just print matches for verification.
                # If duplicate matches found? (e.g. "Park Repair" matches "Park Repair" and "Park Repair Phase 2")
                # We should pick the best one.
                
                # For now, take the first robust match.
                # Or sum if multiple? No, funding records are specific.
                
                # Let's assume the Funding Name is the canonical one.
                # If Doc Name contains Funding Name?
                if f_name in p_clean: 
                    # Doc: "Bluffs Park Shade Structure Project"
                    # Funding: "Bluffs Park Shade Structure"
                    amt = funding_map[f_name]
                    total_funding += amt
                    matched_details.append((p, amt))
                    matched = True
                    break
                elif p_clean in f_name:
                    # Doc: "Bluffs Park"
                    # Funding: "Bluffs Park Project"
                    amt = funding_map[f_name]
                    total_funding += amt
                    matched_details.append((p, amt))
                    matched = True
                    break
    
    if not matched:
        print(f" -> No funding match found for '{p}'")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_details}))"""

env_args = {'var_function-call-18388695237617749918': ['civic_docs'], 'var_function-call-18388695237617747301': ['Funding'], 'var_function-call-18388695237617748780': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18388695237617746163': 'file_storage/function-call-18388695237617746163.json', 'var_function-call-13888598528909911574': 'file_storage/function-call-13888598528909911574.json', 'var_function-call-13888598528909910147': 'file_storage/function-call-13888598528909910147.json'}

exec(code, env_args)
