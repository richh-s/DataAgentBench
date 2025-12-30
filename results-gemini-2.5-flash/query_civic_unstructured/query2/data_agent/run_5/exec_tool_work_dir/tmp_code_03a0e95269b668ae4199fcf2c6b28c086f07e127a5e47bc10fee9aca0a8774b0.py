code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_related_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_indicators = ["completed", "complete construction", "notice of completion filed"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check if the current line indicates completion in 2022
        if "2022" in stripped_line.lower() and any(indicator in stripped_line.lower() for indicator in completion_indicators):
            
            # Look for a project name in the preceding lines (up to 5 lines back)
            project_name_found = None
            for j in range(max(0, i - 5), i):
                prev_line = lines[j].strip()
                
                # Heuristic for a project name line: starts with a capital letter, reasonably long, and contains a project-like term.
                # Also check if it's park-related.
                if (re.match(r'^[A-Z][a-zA-Z0-9 &\-/\']{5,99}$\', prev_line) and 
                    any(kw in prev_line for kw in ["Project", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"]) and
                    any(park_kw in prev_line.lower() for park_kw in park_related_keywords)):
                    project_name_found = prev_line
                    break # Found the most immediate project name
            
            if project_name_found:
                cleaned_project_name = re.sub(r'\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', project_name_found).strip()
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
