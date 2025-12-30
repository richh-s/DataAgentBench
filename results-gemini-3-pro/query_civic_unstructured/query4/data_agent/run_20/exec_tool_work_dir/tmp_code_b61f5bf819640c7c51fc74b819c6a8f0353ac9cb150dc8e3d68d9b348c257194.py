code = """import json
import re

# Load data
with open(locals()['var_function-call-8460811092792669481'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8460811092792670416'], 'r') as f:
    civic_docs = json.load(f)

projects = []

# Helper to normalize dates
def is_spring_2022(date_str):
    if not date_str: return False
    ds = date_str.lower()
    if "2022" in ds:
        if "spring" in ds: return True
        # Check months
        if "march" in ds or "april" in ds or "may" in ds: return True
        # Check numeric format 03, 04, 05
        # patterns like 03/2022, 2022-03
        if "03/" in ds or "04/" in ds or "05/" in ds: return True
        if "-03" in ds or "-04" in ds or "-05" in ds: return True
    return False

# Extract projects from text
# We iterate over all docs
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split lines
    lines = text.split('\n')
    
    # Identify project start indices
    # We look for lines containing "(cid:190) Updates:" or "(cid:190) Project Description:"
    # The line before (skipping empty) is the Project Name.
    
    # We'll create a list of (line_index, project_name)
    proj_indices = []
    
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "(cid:190) Project Description:" in line:
            # Look back for name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                # Check if we already added this index (in case of multiple markers close by?)
                # Actually, usually Updates and Description are distinct. A project usually has one or the other as the first section.
                # But sometimes both? 
                # "Malibu Canyon Road Traffic Study" has "Project Description:" then "Project Updates:".
                # If we detect "Project Description:", we get the name.
                # Later if we detect "Project Updates:" for the same project, we might detect the name again if it's repeated, 
                # OR we might detect "Project Description" line as the name? No.
                # In "Malibu Canyon Road Traffic Study":
                # Line X: Malibu Canyon Road Traffic Study
                # Line X+1: (cid:190) Project Description: ...
                # ...
                # Line Y: (cid:190) Project Updates:
                # The line before Y is likely part of the description text.
                # So we must be careful.
                # Rule: A project name line is usually short, capitalized, and NOT a bullet point.
                # Also, we can filter against the known Funding project names if possible, but we should rely on extraction.
                
                # Better approach: Scan the text. 
                # If we find a Project Name (matches list or heuristic), we start a block.
                # But we don't know the list perfectly (we have Funding list).
                # Let's use the Funding list to identifying Project Names in the text!
                # This is much safer.
                pass

# Alternative Extraction Strategy using Funding Project Names
funding_names = set(item['Project_Name'] for item in funding_data)
# Also normalize funding names for matching (strip, etc)
funding_names_norm = {name.strip().lower(): name for name in funding_names}

project_info = []

for doc in civic_docs:
    text = doc['text']
    # We want to find where each project is discussed.
    # We can search for the project name in the text.
    # If found, we look at the text following it until the next project name.
    
    # Find all occurrences of known project names
    found_locations = []
    for fn_lower, fn_original in funding_names_norm.items():
        # strict matching might fail if there are typos or extra spaces
        # But let's try strict substring search first.
        # "2022 Morning View Resurfacing & Storm Drain Improvements"
        if fn_original in text:
            # Find index
            start_idx = text.find(fn_original)
            found_locations.append((start_idx, fn_original))
        else:
            # Try case insensitive
            pass # simplified
            
    # Sort locations by index
    found_locations.sort(key=lambda x: x[0])
    
    # Now iterate and define blocks
    for i in range(len(found_locations)):
        start, name = found_locations[i]
        end = found_locations[i+1][0] if i+1 < len(found_locations) else len(text)
        
        block = text[start:end]
        
        # Analyze block for start date
        # Look for "Begin Construction: <Date>"
        # or "Start Date: <Date>"
        # or "Schedule" section and find the start.
        
        # Regex for Begin Construction
        # "(cid:131) Begin Construction: Fall 2023"
        # We need to capture the value.
        match = re.search(r"Begin Construction:\s*(.*)", block, re.IGNORECASE)
        start_date = None
        if match:
            start_date = match.group(1).strip()
        else:
            # Try "Start:" or "Estimated Schedule:" then "Begin Construction"
            # Maybe the text has newlines between "Begin Construction:" and date?
            # The sample shows "Begin Construction: Fall 2023" on one line.
            pass
            
        if start_date and is_spring_2022(start_date):
            project_info.append(name)

# Calculate result
# Filter funding
total_funding = 0
count = 0
matched_projects = set(project_info)

for p in matched_projects:
    # Get amount from funding
    # Note: Funding table might have duplicates? "Birdview Avenue Improvements" has 3 entries with different suffixes in Funding DB.
    # The extraction from text found "Birdview Avenue Improvements".
    # Does the text distinguish?
    # If text is "Birdview Avenue Improvements", does it imply the base one or others?
    # The Funding DB has specific names: "Birdview Avenue Improvements (CalOES Project)".
    # If the text has "Birdview Avenue Improvements (CalOES Project)", our search for "Birdview Avenue Improvements" (substring) would also find it.
    # But we found longest match?
    # Actually, we should match longest names first to avoid partial matches.
    pass

# Refined extraction logic in the actual code execution
# 1. Sort funding names by length descending.
# 2. Scan text, replace found names with placeholders or just record indices to ensure greedy matching.
# 3. Extract blocks.
# 4. Check dates.

print("__RESULT__:")
print(json.dumps("place_holder"))"""

env_args = {'var_function-call-15438762544756245875': 'file_storage/function-call-15438762544756245875.json', 'var_function-call-15438762544756246872': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8460811092792669481': 'file_storage/function-call-8460811092792669481.json', 'var_function-call-8460811092792670416': 'file_storage/function-call-8460811092792670416.json'}

exec(code, env_args)
