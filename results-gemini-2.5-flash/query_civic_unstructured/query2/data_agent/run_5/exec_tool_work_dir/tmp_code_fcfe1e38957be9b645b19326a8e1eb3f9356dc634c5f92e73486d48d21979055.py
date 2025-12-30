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
    
    for i, line in enumerate(lines):
        stripped_line = line.strip().lower()

        # Check if the current line indicates completion in 2022
        if "2022" in stripped_line and any(indicator in stripped_line for indicator in completion_indicators):
            
            # If a completion in 2022 is found, look backward for a project name
            project_name_found = None
            for j in range(max(0, i - 5), i):
                prev_line = lines[j].strip()
                
                # Heuristic for a project name line: starts with a capital letter, is reasonably long (min 5 chars),
                # and contains common project-related words. Using `re.search` instead of `re.match` for flexibility.
                # The regex for allowed characters inside project name is simplified to avoid syntax issues.
                if (re.search(r'^[A-Z][a-zA-Z0-9 &/-]{4,99}$', prev_line) is not None and 
                    any(keyword in prev_line for keyword in ["Project", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"])):
                    
                    # Check if the potential project name is park-related
                    if any(park_kw in prev_line.lower() for park_kw in park_keywords):
                        project_name_found = prev_line
                        break # Found the most immediate park-related project name
            
            if project_name_found:
                # Clean the project name by removing suffixes like (FEMA Project)
                cleaned_project_name = re.sub(r'\s*\(FEMA Project\)|\s*\(CalJPIA Project\)|\s*\(CalOES Project\)', '', project_name_found).strip()
                
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)

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
    # Join the two Dataframes on 'Project_Name' to link projects with their funding.
    merged_df = pd.merge(df_park_projects, df_funding, on='Project_Name', how='inner')
    
    # Calculate the sum of 'Amount' for the merged projects.
    total_funding = merged_df['Amount'].sum()

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
