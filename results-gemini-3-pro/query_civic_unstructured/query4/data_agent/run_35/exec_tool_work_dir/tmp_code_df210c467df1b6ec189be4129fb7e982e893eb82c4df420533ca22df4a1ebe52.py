code = """import json
import re
import pandas as pd

# Load data
with open('var_function-call-16246873831533624735.json', 'r') as f:
    civic_docs = json.load(f)
    
with open('var_function-call-7325626147316931914.json', 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Helper to check if date is Spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    if 'spring 2022' in date_str or '2022-spring' in date_str:
        return True
    if '2022' in date_str:
        # Check for months
        if 'march' in date_str or 'april' in date_str or 'may' in date_str:
            return True
        # Check for numeric months 03, 04, 05 with 2022
        # e.g. 03/2022, 03-2022, 2022-03
        if re.search(r'(03|04|05)[/-]2022', date_str) or re.search(r'2022[/-](03|04|05)', date_str):
            return True
    return False

projects_started_spring_2022 = set()

# Regex to find project blocks
# Looking for lines that appear to be headers followed by (cid:190)
# Based on preview: "Project Name\n\n(cid:190)"
# Note: The text might have multiple newlines.
# We'll try to split by the bullet point `(cid:190)` and look at the preceding lines for the name.
# Or better, identifying the structure:
# Name
# (cid:190) ...
# ...

for doc in civic_docs:
    text = doc['text']
    # Split by something that looks like a new project start?
    # Actually, the format seems consistent: Name followed by new line(s) and (cid:190)
    # Let's find all indices of (cid:190)
    # This symbol might be encoded. The preview shows (cid:190).
    # Let's assume the text contains the actual character or the string "(cid:190)".
    # The preview string "(cid:190)" suggests it might be the literal string.
    
    # Let's try to regex for the project header.
    # Pattern: a non-empty line, followed by optional whitespace/newlines, followed by (cid:190)
    # We iterate through the text to find matches.
    
    # We'll split the text into chunks based on Project Headers.
    # But first, let's normalize the text slightly to handle newlines.
    
    # Regex explanation:
    # ^(.+?)\s*\n\s*\(cid:190\) matches a line that is a name, followed by (cid:190)
    # We use Multiline mode.
    
    pattern = re.compile(r'^(.+?)\s*\n\s*\(cid:190\)', re.MULTILINE)
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        
        # The content of this project is from the start of this match (or after the name)
        # to the start of the next match (or end of text).
        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        project_content = text[start_idx:end_idx]
        
        # Now search for start date in project_content
        # We look for "Begin Construction: <date>" or "Start Date: <date>"
        # Also "Advertise" might be considered start if "Begin Construction" is not there? 
        # But usually "Begin Construction" is the start.
        # Or maybe "Project Schedule:" followed by bullet points.
        
        # Let's look for "Begin Construction[:\s]+(.*?)\n"
        # Or "Start[:\s]+(.*?)\n"
        
        date_match = re.search(r'(?:Begin Construction|Start Date|Construction Start)[:\s]+(.*?)(?:\n|$)', project_content, re.IGNORECASE)
        start_date = None
        if date_match:
            start_date = date_match.group(1).strip()
        
        # Sometimes the date might be on the next line or formatted differently.
        # But let's check what we found.
        
        if is_spring_2022(start_date):
            projects_started_spring_2022.add(project_name)

# Now we have a list of project names.
# We need to fuzzy match or exact match with Funding table.
# The hint says "Project_Name in the Funding SQLite table matches the project names that can be extracted".
# So exact match or simple stripping should work.

# Filter funding table
# We check if project_name from funding is in our set.
matched_projects = []
total_funding = 0

for index, row in df_funding.iterrows():
    f_name = row['Project_Name'].strip()
    if f_name in projects_started_spring_2022:
        matched_projects.append(f_name)
        total_funding += row['Amount']

# Output results
result = {
    "count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16246873831533624735': 'file_storage/function-call-16246873831533624735.json', 'var_function-call-7325626147316931914': 'file_storage/function-call-7325626147316931914.json'}

exec(code, env_args)
