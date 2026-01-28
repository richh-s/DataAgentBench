code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_indicators = ["completed", "complete construction", "notice of completion filed"]
project_name_indicators = ["Project", "Program", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for a project name line: starts with a capital letter, is reasonably long (min 5 chars),
        # and contains at least one common project indicator keyword.
        is_potential_project_name_line = (
            len(stripped_line) >= 5 and 
            re.match(r'^[A-Z]', stripped_line) and 
            any(keyword in stripped_line for keyword in project_name_indicators)
        )
        
        if is_potential_project_name_line:
            # If it's a potential project name line, store it as a candidate.
            current_project_candidate = stripped_line
        
        # If a project candidate is active, check the current line for completion in 2022.
        if current_project_candidate and "2022" in stripped_line.lower() and \
           any(indicator in stripped_line.lower() for indicator in completion_indicators):
            
            # If completion in 2022 is found, check if the candidate project name is park-related.
            if any(park_kw in current_project_candidate.lower() for park_kw in park_keywords):
                # Clean the project name by removing suffixes like (FEMA Project) using re.sub with raw string for pattern.
                cleaned_project_name = re.sub(r'\s*\(FEMA Project\)|\s*\(CalJPIA Project\)|\s*\(CalOES Project\)', '', current_project_candidate).strip()
                
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)
            
            # Reset the candidate after processing a potential completion event, regardless if it was park-related or not.
            current_project_candidate = None
        
        # If a new major section header appears (e.g., "Capital Improvement Projects"), reset the current project candidate.
        # This prevents associating a completion status with an old project name from a previous section.
        elif stripped_line.lower().startswith("capital improvement projects") or stripped_line.lower().startswith("disaster recovery projects"):
            current_project_candidate = None

# Load funding data from the stored JSON file.
with open(locals()['var_function-call-4442267602916977481'], 'r') as f:
    funding_data = json.load(f)

# Convert funding data to a Pandas DataFrame.
df_funding = pd.DataFrame(funding_data)
# Convert 'Amount' column to numeric type for calculations.
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Convert extracted park projects to a Pandas DataFrame.
df_park_projects = pd.DataFrame(park_projects_2022_completed)

total_funding = 0
if not df_park_projects.empty:
    # Join the two DataFrames on 'Project_Name' to link projects with their funding.
    # Using an inner join to only include projects that exist in both datasets.
    merged_df = pd.merge(df_park_projects, df_funding, on='Project_Name', how='inner')
    
    # Calculate the sum of 'Amount' for the merged projects.
    total_funding = merged_df['Amount'].sum()

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
