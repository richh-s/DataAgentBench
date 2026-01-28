code = """import json
import pandas as pd
import re

# Load data
civic_docs = json.load(open('var_function-call-445312601869862601'))
funding_data = json.load(open('var_function-call-445312601869864330'))

df_funding = pd.DataFrame(funding_data)
# Ensure Amount is numeric
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Get text
text_content = ""
for doc in civic_docs:
    text_content += doc.get('text', '') + "\n\n"

# Helper to normalize spaces
def clean_text(t):
    return " ".join(t.split())

# We need to identify projects and their status/dates
# Strategy: Split text by project headers or iterate line by line
# The text has lines. Project headers seem to be lines that appear in Funding Project_Names
# or we can try to parse the structure. 
# Given the Funding table has the exact names, let's locate each funded project in the text.

project_names = df_funding['Project_Name'].unique().tolist()
# Sort project names by length desc to match longest first (though exact match is key)
project_names.sort(key=len, reverse=True)

# We will search for each project name in the text.
# If found, we look at the text following it (until the next project name or end of section)
# to find "completed" and "2022".

# To do this reliably, let's map the text positions of all project names found.
found_projects = []
for pname in project_names:
    # Escape for regex
    pattern = re.escape(pname)
    # Find all occurrences
    for match in re.finditer(pattern, text_content, re.IGNORECASE):
        found_projects.append({
            'name': pname,
            'start': match.start(),
            'end': match.end()
        })

# Sort by position
found_projects.sort(key=lambda x: x['start'])

# Remove overlaps (if "Park Project" and "Park Project Phase 2" both match, keep the longer/correct one)
# Since we sorted names by length desc, earlier matches in the loop were longer. 
# But here we sorted by position. If positions overlap, we should keep the longest name.
# Actually, if we have "Project A" at pos 10 and "Project A Phase 2" at pos 10, the loop found both.
# We want "Project A Phase 2".
# Simple clean up: iterate and skip if start pos is inside previous end pos.
cleaned_projects = []
last_end = -1
# We need to prefer longer matches at the same position. 
# Re-sort: primary key start, secondary key end (descending) to put longer matches first?
# No, if "Project A Phase 2" starts at 10 (len 15) and "Project A" starts at 10 (len 9).
# Sorting by start asc, then length desc (end desc).
found_projects.sort(key=lambda x: (x['start'], -x['end']))

for p in found_projects:
    if p['start'] >= last_end:
        cleaned_projects.append(p)
        last_end = p['end']

# Now iterate through cleaned_projects and check the text chunk between this and next.
completed_2022_projects = set()

for i, p in enumerate(cleaned_projects):
    pname = p['name']
    start_pos = p['end']
    # End pos is start of next project or a reasonable limit
    if i < len(cleaned_projects) - 1:
        end_pos = cleaned_projects[i+1]['start']
    else:
        end_pos = start_pos + 2000 # Look ahead 2000 chars
    
    chunk = text_content[start_pos:end_pos]
    
    # Check for completed in 2022
    # Patterns: 
    # "Construction was completed November 2022"
    # "Complete Construction: November 2022"
    # "Construction was completed, November 2022"
    # "Status: Completed ... 2022"
    
    # Normalize chunk for easier matching
    chunk_norm = " ".join(chunk.split())
    
    # Look for "completed" and "2022" in close proximity
    # Regex for completion phrase
    # (completed|complete construction|construction complete).*?(january|february|march|april|may|june|july|august|september|october|november|december).*?2022
    
    completion_pattern = re.compile(r"(completed|complete construction|construction complete|construction was completed)\D{0,50}(january|february|march|april|may|june|july|august|september|october|november|december)\D{0,10}2022", re.IGNORECASE)
    
    if completion_pattern.search(chunk_norm):
        # Additional check: exclude if it says "November 2023" or "2021" closer?
        # The regex enforces 2022 follows the month.
        completed_2022_projects.add(pname)

# Filter for park related
park_projects_completed_2022 = []
for pname in completed_2022_projects:
    # Check keywords in name
    lower_name = pname.lower()
    if 'park' in lower_name or 'playground' in lower_name or 'recreation' in lower_name:
        park_projects_completed_2022.append(pname)

# Sum funding
total_funding = 0
matched_rows = df_funding[df_funding['Project_Name'].isin(park_projects_completed_2022)]
total_funding = matched_rows['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "park_projects": park_projects_completed_2022,
    "matched_funding_rows": matched_rows.to_dict(orient='records'),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-18426906873258029198': ['civic_docs'], 'var_function-call-18426906873258031577': ['Funding'], 'var_function-call-8821001174791641027': 'file_storage/function-call-8821001174791641027.json', 'var_function-call-8821001174791641856': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-445312601869862601': 'file_storage/function-call-445312601869862601.json', 'var_function-call-445312601869864330': 'file_storage/function-call-445312601869864330.json'}

exec(code, env_args)
