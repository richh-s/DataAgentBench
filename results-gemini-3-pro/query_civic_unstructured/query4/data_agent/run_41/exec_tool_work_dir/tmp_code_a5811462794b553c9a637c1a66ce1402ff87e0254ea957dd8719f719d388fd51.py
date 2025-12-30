code = """import json
import sqlite3
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-870935293140318429']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Normalize project names and group funding
def get_base_name(name):
    # Remove common suffixes
    name = re.sub(r'\s*\(FEMA(?:/CalOES)?(?: Project)?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES(?: Project)?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA(?: Project)?\)', '', name, flags=re.IGNORECASE)
    # Handle " - Design" or similar if needed. 
    # Example: "Outdoor Warning Sirens - Design". 
    # If the text says "Outdoor Warning Sirens", then "Outdoor Warning Sirens - Design" might be a separate phase or same project?
    # Usually "Design" and "Construction" are phases of the same project. 
    # But Funding might separate them.
    # Let's strip " - Design" as well to be safe, assuming the main project name is the key.
    name = re.sub(r'\s*-\s*Design', '', name, flags=re.IGNORECASE)
    return name.strip()

df_funding['Base_Project_Name'] = df_funding['Project_Name'].apply(get_base_name)

# Create a map from Base Name to Total Amount
# However, I should first find the projects in the text, then match to this.
# Let's keep the grouped dataframe handy.
funding_summary = df_funding.groupby('Base_Project_Name')['Amount'].sum().to_dict() # Wait, Amount is string in JSON?

# Check amount type
# In the preview: "Amount": "24000". It is a string. Need to convert to int/float.
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])
funding_summary = df_funding.groupby('Base_Project_Name')['Amount'].sum().to_dict()
base_names_list = list(funding_summary.keys())

# Load civic docs
docs_path = locals()['var_function-call-870935293140317738']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Sort docs by date in filename
def extract_date_from_filename(fname):
    # formats: "malibucity_agenda__01262022-1835.txt" or "malibucity_agenda_03222023-2060.txt"
    # match 8 digits
    m = re.search(r'(\d{8})', fname)
    if m:
        d = m.group(1)
        # MMDDYYYY
        return f"{d[4:]}-{d[:2]}-{d[2:4]}" # YYYY-MM-DD
    return "0000-00-00"

docs_data.sort(key=lambda x: extract_date_from_filename(x['filename']), reverse=True)

# Parse text to find projects and start dates
project_start_dates = {} # Base_Name -> Start_Date_String

# Regex for start date
# Look for "Begin Construction: <date>"
# pattern: Begin Construction[:\s]+(.*)
# Also consider the bullets. \W*Begin Construction...
start_pattern = re.compile(r'Begin Construction[:\s]+([^\n\r]+)', re.IGNORECASE)

# We need to find where each project starts in the text.
# We will search for all base_names in the text.
# To avoid partial matches (e.g. "Park" matching "Park Improvements"), we sort base_names by length desc.
base_names_list.sort(key=len, reverse=True)

found_projects = set()

for doc in docs_data:
    text = doc['text']
    # Find all project occurrences
    # We want to segment the text by project.
    # Create a list of (start_index, project_name)
    occurrences = []
    for name in base_names_list:
        # Simple string find might be too loose, but let's try. 
        # Ideally we match whole words or lines.
        # Project headers usually are standalone or at start of line.
        # Let's look for name literally.
        # Since we iterate distinct names, use re.finditer to get all positions
        for match in re.finditer(re.escape(name), text, re.IGNORECASE):
            occurrences.append((match.start(), name))
    
    # Sort by position
    occurrences.sort(key=lambda x: x[0])
    
    # Now iterate and extract text chunk for each project
    for i in range(len(occurrences)):
        idx, name = occurrences[i]
        
        # If we already found a schedule for this project in a later document, skip?
        # But maybe this doc has better info? 
        # We sorted docs by date DESC. So the first time we process a project, it's the latest info.
        if name in project_start_dates:
            continue
            
        # Define text chunk end
        if i < len(occurrences) - 1:
            end_idx = occurrences[i+1][0]
        else:
            end_idx = len(text)
            
        chunk = text[idx:end_idx]
        
        # Search for start date in chunk
        m = start_pattern.search(chunk)
        if m:
            date_str = m.group(1).strip()
            project_start_dates[name] = date_str

# Now filter for Spring 2022
spring_2022_projects = []
# Spring 2022: March, April, May 2022. 
# "Spring 2022", "2022-Spring", "Spring, 2022"
# "March 2022", "April 2022", "May 2022"
# "03/2022", "04/2022", "05/2022" (or - separators)

def is_spring_2022(d_str):
    d_str = d_str.lower()
    if 'spring' in d_str and '2022' in d_str:
        return True
    # Check specific months
    if '2022' in d_str:
        if 'march' in d_str or 'april' in d_str or 'may' in d_str:
            return True
        # Check numeric months 03, 04, 05
        # Regex for MM/YYYY or YYYY-MM
        # 03/2022, 04/2022, 05/2022
        if re.search(r'(03|04|05)[/-]2022', d_str):
            return True
        if re.search(r'2022[/-](03|04|05)', d_str):
            return True
    return False

for name, d_str in project_start_dates.items():
    if is_spring_2022(d_str):
        spring_2022_projects.append(name)

# Calculate totals
total_funding = 0
count = len(spring_2022_projects)

for name in spring_2022_projects:
    total_funding += funding_summary.get(name, 0)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "total_funding": total_funding,
    "projects": spring_2022_projects,
    "project_dates": {p: project_start_dates[p] for p in spring_2022_projects}
}))"""

env_args = {'var_function-call-870935293140317738': 'file_storage/function-call-870935293140317738.json', 'var_function-call-870935293140318429': 'file_storage/function-call-870935293140318429.json'}

exec(code, env_args)
