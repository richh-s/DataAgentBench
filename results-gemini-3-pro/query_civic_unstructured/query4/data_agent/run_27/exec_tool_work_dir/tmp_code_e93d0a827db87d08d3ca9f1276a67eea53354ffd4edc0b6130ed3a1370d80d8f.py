code = """import json
import re

# Load data
with open(locals()['var_function-call-6904797110646759006'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-6371047367361917112'], 'r') as f:
    funding_recs = json.load(f)

funding_projects = [r['Project_Name'] for r in funding_recs]
# Sort by length descending to match longer names first
funding_projects.sort(key=len, reverse=True)

found_projects = set()

# Regex for Spring 2022
# Matches: Spring 2022, March 2022, April 2022, May 2022, March, 2022 etc.
date_pattern = re.compile(r'(?:Spring|March|April|May),?\s*2022', re.IGNORECASE)
start_pattern = re.compile(r'(?:Begin|Start)\s*(?:Construction|Work)', re.IGNORECASE)

# We also need to be careful about matching the Project Name in the text.
# The text has lines. We can try to identify sections.

matched_projects_with_dates = []

for doc in docs:
    text = doc['text']
    # Find positions of all known projects
    # We create a list of (start_pos, project_name)
    project_positions = []
    for proj in funding_projects:
        # Simple string search, assuming case matches mostly or ignore case
        # Using re.escape just in case
        for m in re.finditer(re.escape(proj), text, re.IGNORECASE):
            project_positions.append((m.start(), proj))
    
    # Sort by position
    project_positions.sort()
    
    # Filter overlapping matches (if any). If a longer name matches, a shorter substring might also match at same pos.
    # Since we sorted names by length descending, the first one encountered at a pos should be the longest.
    # We should skip subsequent matches that are inside the current one.
    final_positions = []
    if project_positions:
        curr_start, curr_name = project_positions[0]
        curr_end = curr_start + len(curr_name)
        final_positions.append((curr_start, curr_name))
        
        for start, name in project_positions[1:]:
            if start >= curr_end:
                final_positions.append((start, name))
                curr_start = start
                curr_name = name
                curr_end = start + len(name)
    
    # Now iterate through project sections
    for i in range(len(final_positions)):
        p_start, p_name = final_positions[i]
        # Text for this project goes until the next project start or end of text
        if i < len(final_positions) - 1:
            next_p_start = final_positions[i+1][0]
            section_text = text[p_start:next_p_start]
        else:
            section_text = text[p_start:]
        
        # Look for start date in this section
        # We specifically look for lines like "Begin Construction: <Date>"
        # Let's search for the "Begin Construction" pattern and extract the date part
        
        # There might be multiple "Begin Construction" mentions? Unlikely per project section.
        start_matches = list(start_pattern.finditer(section_text))
        for sm in start_matches:
            # Extract text after the match until newline
            after_match = section_text[sm.end():].split('\n')[0]
            # Check if this date string matches our target date
            if date_pattern.search(after_match):
                found_projects.add(p_name)
                matched_projects_with_dates.append((p_name, after_match.strip()))

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-17327225246919229533': 'file_storage/function-call-17327225246919229533.json', 'var_function-call-6904797110646759006': 'file_storage/function-call-6904797110646759006.json', 'var_function-call-15743062509627089682': ['Funding'], 'var_function-call-6371047367361917112': 'file_storage/function-call-6371047367361917112.json'}

exec(code, env_args)
