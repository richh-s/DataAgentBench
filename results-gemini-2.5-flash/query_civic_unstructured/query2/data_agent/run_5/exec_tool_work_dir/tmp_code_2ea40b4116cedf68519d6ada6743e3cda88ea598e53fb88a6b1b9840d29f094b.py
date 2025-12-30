code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs", "trancas canyon"]
completion_phrases = ["completed", "complete construction", "notice of completion filed"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for project name: capitalized, contains 'Project' or similar, reasonably long
        # Removed the problematic single quote from the regex character class
        project_name_pattern = re.compile(r'^[A-Z][a-zA-Z0-9 &/-]{5,100}$')
        
        # A more robust check for project indicator keywords. Instead of `any(kw in stripped_line for kw in [...]`,
        # let's directly check for some common project indicators that are usually part of a project name.
        is_project_indicator_present = any(proj_kw in stripped_line for proj_kw in ["Project", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"])

        if project_name_pattern.match(stripped_line) and is_project_indicator_present:
            current_project_candidate = stripped_line
        
        # Check if the current line indicates completion in 2022 and if there's a recent project candidate
        if current_project_candidate and "2022" in stripped_line.lower() and \
           any(indicator in stripped_line.lower() for indicator in completion_phrases):
            # Verify if the candidate project name is park-related
            if any(park_kw in current_project_candidate.lower() for park_kw in park_keywords):
                cleaned_project_name = re.sub(r'\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', current_project_candidate).strip()
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)
            current_project_candidate = None # Reset for next project
        elif stripped_line.lower().startswith("capital improvement projects") or stripped_line.lower().startswith("disaster recovery projects"):
            current_project_candidate = None # Reset if a section header is encountered

# Now, let's process the funding data
with open(locals()['var_function-call-4442267602916977481'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

df_park_projects = pd.DataFrame(park_projects_2022_completed)

if not df_park_projects.empty:
    # Join the two dataframes on Project_Name
    merged_df = pd.merge(df_park_projects, df_funding, on='Project_Name', how='inner')
    
    # Calculate total funding
    total_funding = merged_df['Amount'].sum()
else:
    total_funding = 0

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
