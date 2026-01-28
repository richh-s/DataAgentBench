code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

project_indicator_keywords = ["Project", "Program", "Improvements", "Study", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"]
park_specific_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_year_keywords = ["completed", "complete construction", "2022", "november 2022", "december 2022", "october 2022", "september 2022", "august 2022", "july 2022", "june 2022", "may 2022", "april 2022", "march 2022", "february 2022", "january 2022"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        
        # Heuristic: A line is a potential project name if it starts with a capital letter,
        # is reasonably long, and contains at least one project indicator keyword.
        is_potential_project_name_line = (
            len(stripped_line) > 10 and 
            re.match("^[A-Z]", stripped_line) and 
            any(kw in stripped_line for kw in project_indicator_keywords)
        )
        
        if is_potential_project_name_line:
            potential_project_name = stripped_line
            
            # Check if it's a park-related project
            if any(park_kw in potential_project_name.lower() for park_kw in park_specific_keywords):
                
                # Search for completion in 2022 in the current and next few lines
                for j in range(i, min(i + 5, len(lines))):
                    search_line = lines[j].strip().lower()
                    
                    # Ensure both a completion keyword (excluding just "2022") AND "2022" are present
                    if any(comp_kw in search_line for comp_kw in completion_year_keywords if comp_kw != "2022") and "2022" in search_line:
                        
                        cleaned_project_name = re.sub('\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', potential_project_name).strip()
                        
                        project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                        if project_info not in park_projects_2022_completed:
                            park_projects_2022_completed.append(project_info)
                        break

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
