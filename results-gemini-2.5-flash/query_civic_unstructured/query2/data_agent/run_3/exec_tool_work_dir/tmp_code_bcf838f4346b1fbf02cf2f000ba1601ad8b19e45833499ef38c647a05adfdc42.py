code = """import json
import re

text_data = json.loads(open(locals()['var_function-call-11212154310918055831'], 'r').read())

park_projects_completed_2022 = []

for doc in text_data:
    text = doc['text']
    
    # Regex to find project names and their details
    # This regex looks for a project name, then updates, and finally a completion date.
    # It assumes project details like updates and schedule are directly after the project name.
    # It also looks for "park" in the project name or updates for park-related projects.
    
    # General pattern for projects with "Updates" and "Complete Construction" or "Construction was completed"
    pattern = r"([A-Za-z0-9][A-Za-z0-9\s,\(\)\&\/\-\.]+?)\n\\n\(cid:190\) Updates:(.*?)(?=\n\\n\(cid:190\) Project Schedule:|\n\\n\(cid:190\) Estimated Schedule:|\n\\n\(cid:190\) Complete Construction:|\\n\(cid:190\) Construction was completed:|\n\\n\(cid:190\) Project Description:)"
    
    # Find all potential project blocks
    project_blocks = re.findall(pattern, text, re.DOTALL)

    for name, details in project_blocks:
        project_name = name.strip()
        project_name = re.sub(r'\(cid:\d+\)\s*', '', project_name) # Remove (cid:xxx)
        details = re.sub(r'\(cid:\d+\)\s*', '', details) # Remove (cid:xxx)
        
        # Check for 'park' in project name or details
        is_park_related = re.search(r"park", project_name, re.IGNORECASE) or re.search(r"park", details, re.IGNORECASE)

        if is_park_related:
            # Check for completion in 2022
            completed_2022 = False
            # Look for "Complete Construction: [Date]"
            match_complete_date = re.search(r"Complete Construction:\s*(.*?)(?=\n)", details)
            if match_complete_date and "2022" in match_complete_date.group(1):
                completed_2022 = True
            
            # Look for "Construction was completed, [Date]"
            match_construction_completed = re.search(r"Construction was completed,\s*(.*?)(?=\n)", details)
            if match_construction_completed and "2022" in match_construction_completed.group(1):
                completed_2022 = True

            # Bluffs Park Shade Structure example, "Construction was completed November 2022" is directly after "Updates:"
            if "Bluffs Park Shade Structure" in project_name:
                if "Construction was completed November 2022" in details:
                    completed_2022 = True

            if completed_2022:
                park_projects_completed_2022.append(project_name)

print("__RESULT__:")
print(json.dumps(park_projects_completed_2022)))"""

env_args = {'var_function-call-7966081085860802872': ['civic_docs'], 'var_function-call-11212154310918055831': 'file_storage/function-call-11212154310918055831.json'}

exec(code, env_args)
