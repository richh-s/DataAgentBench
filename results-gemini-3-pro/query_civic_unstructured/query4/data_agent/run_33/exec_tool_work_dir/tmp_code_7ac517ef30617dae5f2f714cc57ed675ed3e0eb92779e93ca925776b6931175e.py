code = """import json
import re
import pandas as pd

# Load Funding Data
with open('var_function-call-2782363778885918640', 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open('var_function-call-9895724899221676838', 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    if 'spring 2022' in date_str or 'spring, 2022' in date_str:
        return True
    # Check for months March, April, May 2022
    if '2022' in date_str:
        if 'march' in date_str or 'april' in date_str or 'may' in date_str:
            return True
        # Check numeric 03/2022, 04/2022, 05/2022 etc if format exists
        # Basic check for YYYY-MM or MM-YYYY
        # regex for numeric dates?
        pass
    return False

# Regex to find projects
# We look for lines that look like a project name followed by "Updates:" or "(cid:190) Updates:"
# The structure seems to be: Name \n+ (cid:190) Updates:
# We will iterate through the text looking for this pattern.

# Pattern to capture Project Name and the following block until the next project
# It's hard to define "next project", but usually they are separated by newlines and headers.
# A simpler approach: Split by double newlines or scan line by line.

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Normalize text to handle extracted characters
    text = text.replace('(cid:190)', '•').replace('(cid:131)', '-') 
    
    # Split by "Agenda Item" or similar if needed, but let's try to regex project blocks.
    # Projects seem to be headers. 
    # Let's find the start of a project block: "• Updates:"
    # The line before it (ignoring empty lines) is the Project Name.
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Updates:' in line and '•' in line:
            # Found a project block start.
            # Look backwards for Project Name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                project_name = lines[j].strip()
                
                # Now look forwards for "Begin Construction" or "Start Date"
                # Scan until next "• Updates:" or end of text.
                start_date = None
                k = i + 1
                while k < len(lines):
                    if 'Updates:' in lines[k] and '•' in lines[k]:
                        break # Next project
                    
                    # Check for start date
                    # Patterns: "Begin Construction:", "Start Date:", "Construction Start:"
                    # Also "Advertise:" is not start.
                    
                    content = lines[k].strip()
                    if 'Begin Construction:' in content:
                        start_date = content.split('Begin Construction:')[1].strip()
                        break
                    if 'Start Date:' in content:
                        start_date = content.split('Start Date:')[1].strip()
                        break
                    
                    k += 1
                
                if project_name and start_date:
                    extracted_projects.append({
                        'Project_Name': project_name,
                        'Start_Date': start_date
                    })

# Filter for Spring 2022
target_projects = []
for p in extracted_projects:
    if is_spring_2022(p['Start_Date']):
        target_projects.append(p['Project_Name'])

# Remove duplicates if any
target_projects = list(set(target_projects))

# Filter funding
# We need to match Project_Name. The names might vary slightly (case, whitespace).
# Let's normalize both sides.
target_projects_norm = [n.lower().strip() for n in target_projects]
funding_df['Project_Name_Norm'] = funding_df['Project_Name'].str.lower().str.strip()

matched_funding = funding_df[funding_df['Project_Name_Norm'].isin(target_projects_norm)]

# Calculate results
count = len(matched_funding)
# Note: Count of projects, or count of funding records?
# Query: "How many projects... and what is their total funding?"
# It's possible one project has multiple funding records.
# The question asks "How many projects", which implies unique projects.
# But if I have multiple funding records for one project, I should count the project once.
# Let's check unique projects in matched_funding.

unique_projects_count = matched_funding['Project_Name_Norm'].nunique()
total_funding = matched_funding['Amount'].astype(float).sum()

result = {
    "extracted_projects": extracted_projects,
    "target_projects": target_projects,
    "unique_projects_count": unique_projects_count,
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4138183868648967311': ['civic_docs'], 'var_function-call-15559280801211844213': 'file_storage/function-call-15559280801211844213.json', 'var_function-call-2782363778885918640': 'file_storage/function-call-2782363778885918640.json', 'var_function-call-9895724899221676838': 'file_storage/function-call-9895724899221676838.json'}

exec(code, env_args)
