code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_indicators = ["completed", "complete construction", "notice of completion filed"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for project name: starts with a capital letter, reasonably long, and contains a project-like term.
        # The regex pattern for `project_name_pattern` and `project_indicator_present` is complex, simplifying.
        # Instead of a regex for the entire project name line, let's look for certain keywords in capitalized lines.
        is_potential_project_name_line = (
            len(stripped_line) > 10 and 
            re.match(r'^[A-Z]', stripped_line) and 
            any(keyword in stripped_line for keyword in ["Project", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"])
        )
        
        if is_potential_project_name_line:
            # If it's a potential project name line, store it as a candidate.
            current_project_candidate = stripped_line
        
        # Check for completion in 2022 in the current line if a project candidate is active
        if current_project_candidate and "2022" in stripped_line.lower() and 
           any(indicator in stripped_line.lower() for indicator in completion_indicators):
            
            # If completion in 2022 is found, check if the candidate project name is park-related
            if any(park_kw in current_project_candidate.lower() for park_kw in park_keywords):
                # Clean the project name by removing suffixes like (FEMA Project)
                cleaned_project_name = re.sub(r'\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', current_project_candidate).strip()
                
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)
            
            # Reset the candidate after processing a potential completion event
            current_project_candidate = None
        
        # If a new major section header appears, reset the current project candidate
        elif stripped_line.lower().startswith("capital improvement projects") or stripped_line.lower().startswith("disaster recovery projects"):
            current_project_candidate = None

# Load funding data
with open(locals()['var_function-call-4442267602916977481'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

df_park_projects = pd.DataFrame(park_projects_2022_completed)

if not df_park_projects.empty:
    merged_df = pd.merge(df_park_projects, df_funding, on='Project_Name', how='inner')
    total_funding = merged_df['Amount'].sum()
else:
    total_funding = 0

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
