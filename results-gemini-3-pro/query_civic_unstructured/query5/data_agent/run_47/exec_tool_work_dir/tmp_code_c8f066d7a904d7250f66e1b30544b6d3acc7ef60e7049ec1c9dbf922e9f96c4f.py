code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-17465459041874363350'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

with open(locals()['var_function-call-17465459041874365577'], 'r') as f:
    civic_docs = json.load(f)

# Group funding by clean_name
project_groups = {}
disaster_keywords_suffixes = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey']

for idx, row in funding_df.iterrows():
    full_name = row['Project_Name']
    if full_name == "Discussion": continue
    
    clean_name = re.sub(r'\s*\(.*?\)', '', full_name).strip()
    
    # Check if this specific record implies disaster
    is_disaster_record = any(k in full_name.lower() for k in disaster_keywords_suffixes)
    
    if clean_name not in project_groups:
        project_groups[clean_name] = {
            'total_amount': 0,
            'is_disaster_flag': False,
            'full_names': set()
        }
    
    project_groups[clean_name]['total_amount'] += row['Amount']
    if is_disaster_record:
        project_groups[clean_name]['is_disaster_flag'] = True
    project_groups[clean_name]['full_names'].add(full_name)

# List of clean names to search
search_names = list(project_groups.keys())
# Sort by length descending to prioritize longest matches
search_names.sort(key=len, reverse=True)

final_funded_projects = set()
total_funding = 0
debug_log = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all matches
    # Store (start, end, clean_name)
    matches = []
    for name in search_names:
        # Use regex to find matches to ensure we handle case/spacing if needed, 
        # but exact string find is safer for names with special chars.
        # But we need word boundaries? "Park" vs "Parker".
        # Let's use simple find for now, and rely on longest match filtering.
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            matches.append((idx, idx + len(name), name))
            start = idx + 1
            
    # Filter matches: Keep only non-overlapping or longest
    # Sort by start position
    matches.sort(key=lambda x: x[0])
    
    filtered_matches = []
    if matches:
        curr = matches[0]
        for next_match in matches[1:]:
            # Check overlap
            if next_match[0] < curr[1]:
                # Overlap. Since we sorted names by length descending, 
                # we might have smaller inside larger?
                # Actually, `search_names` was sorted by length. But `matches` is sorted by position.
                # If we have "Annual Street Maintenance" (short) inside "2021 Annual Street Maintenance" (long).
                # The long one starts at X. The short one starts at X+5.
                # If we processed long one first (it's longer), we found it.
                # But here we found ALL.
                # We want to pick the Longest covering a range.
                pass
            else:
                filtered_matches.append(curr)
                curr = next_match
        filtered_matches.append(curr)
    
    # This overlap logic is weak. Let's do a better one:
    # 1. Create a mask of covered indices? No.
    # 2. Iterate matches sorted by length descending. If interval free, take it.
    
    matches.sort(key=lambda x: (x[1]-x[0]), reverse=True) # Longest first
    accepted_matches = []
    occupied_indices = set()
    
    for m in matches:
        start, end, name = m
        # Check if any part of [start, end) is occupied
        is_free = True
        for i in range(start, end):
            if i in occupied_indices:
                is_free = False
                break
        if is_free:
            accepted_matches.append(m)
            for i in range(start, end):
                occupied_indices.add(i)
                
    # Sort accepted matches by position
    accepted_matches.sort(key=lambda x: x[0])
    
    # Now process blocks
    for i in range(len(accepted_matches)):
        start, end, name = accepted_matches[i]
        
        # Determine end of block (start of next project or reasonable limit)
        if i < len(accepted_matches) - 1:
            block_end = accepted_matches[i+1][0]
        else:
            block_end = min(len(text), end + 3000)
            
        block = text[end:block_end] # Text AFTER the name
        
        # Determine Type
        # 1. Check Funding Data flag
        is_disaster = project_groups[name]['is_disaster_flag']
        
        # 2. Check Text Context (Section Header)
        # Scan backwards from start for headers
        pre_text = text[:start]
        # Look for headers
        # We search for the last occurrence of known headers
        header_map = {
            "Capital Improvement Projects": "capital",
            "Disaster Recovery Projects": "disaster"
        }
        last_header_pos = -1
        found_type = None
        
        for h, t in header_map.items():
            h_pos = pre_text.rfind(h)
            if h_pos > last_header_pos:
                last_header_pos = h_pos
                found_type = t
                
        if found_type == "disaster":
            is_disaster = True
        # Note: If found_type is capital, we don't necessarily negate is_disaster 
        # because the specific project might be a FEMA sub-project. 
        # But generally, section headers are strong.
        # If funding flag says Disaster (e.g. FEMA suffix), keep it True.
        
        # 3. Check Block Keywords (weakest)
        # if "FEMA" in block or "Disaster" in block...
        # Only if not already decided?
        if not is_disaster:
            if any(k in block.lower() for k in disaster_keywords_suffixes):
                is_disaster = True
        
        # Determine Start Date
        # Look for "Begin Construction: <Date>" etc in block
        if is_disaster:
            # Check 2022
            patterns = [
                r"Begin Construction[:\s]+(.*)",
                r"Start Date[:\s]+(.*)",
                r"Construction began[:\s]+(.*)",
                r"Construction Start[:\s]+(.*)",
                r"Advertise[:\s]+(.*)", # Advertise is early stage.
                r"Construction was completed[:\s]+(.*)" # Maybe started 2022?
            ]
            
            started_2022 = False
            for pat in patterns:
                ms = re.findall(pat, block, re.IGNORECASE)
                for date_str in ms:
                    # Cleanup date_str (take first 50 chars)
                    date_str_clean = date_str[:50]
                    if "2022" in date_str_clean:
                        # Check "Completed ... 2022" context
                        # If completed in 2022, did it start in 2022?
                        # If it says "completed November 2022", it might have started in 2022.
                        # If "completed January 2022", probably started 2021.
                        # To be strict: "Started in 2022" query usually looks for start date.
                        # But small projects complete in months.
                        # Let's count it if "Begin" or "Start" or "Advertise" is 2022.
                        if "completed" in pat.lower():
                             # Maybe extract month?
                             pass
                        else:
                             started_2022 = True
            
            if started_2022 and name not in final_funded_projects:
                total_funding += project_groups[name]['total_amount']
                final_funded_projects.add(name)
                debug_log.append(f"Added {name}: {project_groups[name]['total_amount']}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(final_funded_projects), "debug": debug_log}))"""

env_args = {'var_function-call-17465459041874363350': 'file_storage/function-call-17465459041874363350.json', 'var_function-call-17465459041874365577': 'file_storage/function-call-17465459041874365577.json', 'var_function-call-9026625459082643704': {'total_funding': 2374000, 'projects': ['Storm Drain Master Plan', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Birdview Avenue Improvements (CalOES Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs', 'Storm Drain Master Plan (FEMA Project)', 'Annual Street Maintenance', 'Trancas Playground Resurfacing', 'Latigo Canyon Road Culvert Repairs', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Civic Center Way Improvements', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Malibu Park Drainage Improvements', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Clover Heights Storm Drain', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Malibu Bluffs Park South Walkway', 'Trancas Canyon Park Slope Stabilization Project', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Legacy Park Paver Repair Project', 'Malibu Road Slope Repairs', 'Corral Canyon Culvert Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Civic Center Stormwater Diversion Structure', 'Guardrail Replacement Citywide (FEMA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Birdview Avenue Improvements', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', '2021 Annual Street Maintenance', 'Malibu Road Slope Repairs (CalOES Project)', 'Guardrail Replacement Citywide'], 'debug': ['Matched: Malibu Road Slope Repairs (CalOES Project), Amount: 37000', 'Matched: 2021 Annual Street Maintenance, Amount: 24000', 'Matched: Annual Street Maintenance, Amount: 23000', 'Matched: Birdview Avenue Improvements, Amount: 79000', 'Matched: Birdview Avenue Improvements (CalOES Project), Amount: 85000', 'Matched: Birdview Avenue Improvements (FEMA/CalOES Project), Amount: 14000', 'Matched: Broad Beach Road Water Quality Infrastructure Repairs, Amount: 87000', 'Matched: Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project), Amount: 81000', 'Matched: Civic Center Stormwater Diversion Structure, Amount: 64000', 'Matched: Civic Center Way Improvements, Amount: 37000', 'Matched: Clover Heights Storm Drain, Amount: 53000', 'Matched: Clover Heights Storm Drain (FEMA Project), Amount: 21000', 'Matched: Corral Canyon Culvert Repairs, Amount: 54000', 'Matched: Corral Canyon Culvert Repairs (FEMA Project), Amount: 43000', 'Matched: Corral Canyon Culvert Repairs (FEMA/CalOES Project), Amount: 15000', 'Matched: Corral Canyon Road Bridge Repairs, Amount: 68000', 'Matched: Corral Canyon Road Bridge Repairs (FEMA Project), Amount: 25000', 'Matched: Corral Canyon Road Bridge Repairs (FEMA/CalOES Project), Amount: 58000', 'Matched: Encinal Canyon Road Drainage Improvements, Amount: 34000', 'Matched: Encinal Canyon Road Drainage Improvements (CalOES Project), Amount: 18000', 'Matched: Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project), Amount: 94000', 'Matched: Guardrail Replacement Citywide, Amount: 39000', 'Matched: Guardrail Replacement Citywide (FEMA Project), Amount: 22000', 'Matched: Guardrail Replacement Citywide (FEMA/CalOES Project), Amount: 45000', 'Matched: Latigo Canyon Road Culvert Repairs, Amount: 57000', 'Matched: Latigo Canyon Road Culvert Repairs (FEMA Project), Amount: 36000', 'Matched: Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project), Amount: 44000', 'Matched: Latigo Canyon Road Roadway/Retaining Wall Improvements, Amount: 19000', 'Matched: Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project), Amount: 91000', 'Matched: Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project), Amount: 78000', 'Matched: Legacy Park Paver Repair Project, Amount: 69000', 'Matched: Malibu Bluffs Park South Walkway, Amount: 91000', 'Matched: Malibu Park Drainage Improvements, Amount: 17000', 'Matched: Malibu Road Slope Repairs, Amount: 44000', 'Matched: PCH Median Improvements at Paradise Cove and Zuma Beach, Amount: 27000', 'Matched: Storm Drain Master Plan, Amount: 77000', 'Matched: Storm Drain Master Plan (FEMA Project), Amount: 80000', 'Matched: Trancas Canyon Park Planting and Irrigation Repairs, Amount: 78000', 'Matched: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project), Amount: 44000', 'Matched: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project), Amount: 92000', 'Matched: Trancas Canyon Park Slope Stabilization Project, Amount: 68000', 'Matched: Trancas Canyon Park Slope Stabilization Project (CalJPIA Project), Amount: 43000', 'Matched: Trancas Canyon Park Slope Stabilization Project (CalOES Project), Amount: 32000', 'Matched: Trancas Playground Resurfacing, Amount: 90000', 'Matched: Westward Beach Road Shoulder Repairs (CalOES Project), Amount: 77000']}}

exec(code, env_args)
