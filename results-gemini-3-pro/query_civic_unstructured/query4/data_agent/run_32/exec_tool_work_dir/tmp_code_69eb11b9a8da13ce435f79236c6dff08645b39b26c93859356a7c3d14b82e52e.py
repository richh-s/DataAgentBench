code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12378432267433041329'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding table
funding_data = locals()['var_function-call-7193024232373872920']
# funding_data is a list of dicts.

# Prepare Funding dict for easy lookup
funding_map = {} # Project_Name -> Amount
for row in funding_data:
    funding_map[row['Project_Name']] = int(row['Amount'])

# Keywords for Spring 2022
spring_months = ['march', 'april', 'may']
target_year = '2022'
target_season = 'spring 2022'

# Helper to check date string
def is_spring_2022(date_str):
    ds = date_str.lower()
    if 'spring 2022' in ds:
        return True
    if 'spring, 2022' in ds:
        return True
    # Check for Month + 2022
    if '2022' in ds:
        for m in spring_months:
            if m in ds:
                return True
        # Check numerical dates 03/2022, 04/22 etc? 
        # But text usually has full words or seasons.
        # Let's check regex for 03/.../2022
        if re.search(r'(03|04|05)[/-].*2022', ds):
            return True
        if re.search(r'2022.*(03|04|05)', ds): # 2022-03
            return True
    return False

projects_started_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    # We iterate lines.
    # Logic to identify project name:
    # A line that is non-empty, and followed by a line starting with (cid:190)
    # Note: The text has (cid:190) as bullet.
    
    # Let's clean up lines first
    lines = [l.strip() for l in lines]
    
    for i, line in enumerate(lines):
        if not line:
            continue
            
        # Check if this line is a project header
        # Look ahead for (cid:190)
        is_project_header = False
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if next_line.startswith('(cid:190)') or next_line.startswith('updates:') or next_line.startswith('project description:'):
                # Verify it's not a section header like "Capital Improvement Projects (Design)"
                if "capital improvement projects" not in line.lower() and "updates:" not in line.lower():
                    is_project_header = True
                    # Double check if next line is empty and the one after is (cid:190)
                    # The split/strip might have removed empty lines.
                    pass
        
        # Sometimes there's an empty line between name and updates
        if not is_project_header and i + 2 < len(lines):
             if not lines[i+1] and lines[i+2].startswith('(cid:190)'):
                 if "capital improvement projects" not in line.lower():
                     is_project_header = True

        if is_project_header:
            current_project = line
            # Clean project name (remove trailing spaces, etc)
            # Sometimes name is split across lines? Assuming single line for now.
            continue
        
        if current_project:
            # Look for dates
            # "Begin Construction: ..."
            # "Start Date: ..."
            # "Construction Start: ..."
            
            # Use regex to capture value after colon
            # Check for "Begin Construction"
            match = re.search(r'begin construction[:\s]+(.*)', line, re.IGNORECASE)
            if match:
                val = match.group(1)
                if is_spring_2022(val):
                    projects_started_spring_2022.add(current_project)
            
            # Check for "Start"
            # match = re.search(r'start[:\s]+(.*)', line, re.IGNORECASE)
            # if match:
            #     val = match.group(1)
            #     if is_spring_2022(val):
            #         projects_started_spring_2022.add(current_project)
                    
            # Check for "Updates:" that say "Construction started..."
            if "construction started" in line.lower() or "construction began" in line.lower():
                if is_spring_2022(line):
                     projects_started_spring_2022.add(current_project)

# Calculate totals
found_projects = []
total_funding = 0

for p_name in projects_started_spring_2022:
    # Try exact match first
    if p_name in funding_map:
        found_projects.append(p_name)
        total_funding += funding_map[p_name]
    else:
        # Try to find partial match or match with stripped whitespace
        # Or maybe the text name is "Project Name\n" or something? I stripped lines.
        # Try to find if p_name is substring of a funding key or vice versa
        # But be careful of false positives.
        
        # Let's check keys in funding_map
        matched = False
        for k in funding_map:
            # Case insensitive match
            if k.lower() == p_name.lower():
                found_projects.append(k) # Use the key from map to avoid duplicates if any
                total_funding += funding_map[k]
                matched = True
                break
        
        if not matched:
            # Try cleaning p_name more?
            # E.g. "2022 Morning View..." -> "Morning View..."? No, year is part of name usually.
            # print(f"Unmatched: {p_name}")
            pass

result = {
    "count": len(found_projects),
    "total_funding": total_funding,
    "projects": found_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9316415891576363491': ['Funding'], 'var_function-call-9316415891576362210': ['civic_docs'], 'var_function-call-10848218127933448238': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10848218127933449745': 'file_storage/function-call-10848218127933449745.json', 'var_function-call-12378432267433041329': 'file_storage/function-call-12378432267433041329.json', 'var_function-call-7193024232373872920': 'file_storage/function-call-7193024232373872920.json'}

exec(code, env_args)
