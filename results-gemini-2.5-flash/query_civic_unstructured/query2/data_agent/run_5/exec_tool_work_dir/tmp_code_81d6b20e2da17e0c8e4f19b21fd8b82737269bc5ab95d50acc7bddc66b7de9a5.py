code = """import json
import re
import pandas as pd

# Load civic documents data
with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs park", "trancas canyon park", "bluffs", "trancas canyon"]
completion_indicators = ["completed", "complete construction", "notice of completion filed", "completion was"]
project_name_identifiers = ["Project", "Program", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment", "Road", "Drainage", "Study"]

# Regex for cleaning project name suffixes, using raw string literal with single quotes.
# This ensures backslashes are interpreted literally by Python for the regex engine.
project_suffix_cleaner = re.compile(r'\s*\((FEMA|CalJPIA|CalOES) Project\)')

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        lower_stripped_line = stripped_line.lower()

        # Heuristic for a potential project name line:
        # 1. Starts with a capital letter and is not empty.
        # 2. Is reasonably long (e.g., at least 5 characters, up to 100).
        # 3. Contains at least one common project indicator keyword.
        # Using a raw string literal for the regex pattern for `re.match`.
        # The hyphen in the character class `[a-zA-Z0-9 &-/]` is fine unescaped when at the end or start of a character class in a raw string.
        is_potential_project_name_line = (
            len(stripped_line) >= 5 and len(stripped_line) <= 100 and
            stripped_line and stripped_line[0].isupper() and 
            re.match(r'^[A-Z][a-zA-Z0-9 &-/]{4,99}$', stripped_line) is not None and
            any(keyword in stripped_line for keyword in project_name_identifiers)
        )
        
        if is_potential_project_name_line:
            current_project_candidate = stripped_line
        
        # If a project candidate is active, check the current line for completion in 2022.
        if current_project_candidate and "2022" in lower_stripped_line and \
           any(indicator in lower_stripped_line for indicator in completion_indicators):
            
            # If completion in 2022 is found, check if the candidate project name is park-related.
            if any(park_kw in current_project_candidate.lower() for park_kw in park_keywords):
                # Clean the project name by removing suffixes.
                cleaned_project_name = project_suffix_cleaner.sub('', current_project_candidate).strip()
                
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)
            
            # Reset the candidate after processing a potential completion event.
            current_project_candidate = None
        
        # If a new major section header appears, reset the current project candidate.
        elif lower_stripped_line.startswith("capital improvement projects") or lower_stripped_line.startswith("disaster recovery projects"):
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
    merged_df = pd.merge(df_park_projects, df_funding, on='Project_Name', how='inner')
    
    # Calculate the sum of 'Amount' for the merged projects.
    total_funding = int(merged_df['Amount'].sum()) # Convert to int for JSON serialization

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
