code = """import json
import re

with open(locals()["var_function-call-5170959527222557152"], "r") as f:
    funded_projects_data = json.load(f)

with open(locals()["var_function-call-1640262124798972523"], "r") as f:
    civic_docs_data = json.load(f)

funded_project_names = {project["Project_Name"] for project in funded_projects_data}

capital_design_projects = set()

for doc in civic_docs_data:
    text = doc["text"]
    
    # Regex to find the 'Capital Improvement Projects (Design)' section.
    # Using a raw string with double quotes for the regex pattern.
    # All parentheses are escaped with double backslashes for literal matching.
    # The non-greedy '.*?' is used to capture the content until the next section.
    design_section_pattern = r"Capital Improvement Projects \\(Design\\)(.*?)(?:Capital Improvement Projects \\(Construction\\)|Capital Improvement Projects \\(Not Started\\)|Disaster Recovery Projects|RECOMMENDED ACTION:|Staff has also prepared a Public Works Quarterly Update flier|Page \\d of \\d|$)"
    design_section_match = re.search(design_section_pattern, text, re.DOTALL)

    if design_section_match:
        design_section_text = design_section_match.group(1)
        
        # Regex to find project names within the identified design section.
        # A project name is typically a line of text (non-greedy, captured in group 1)
        # that is immediately followed by a newline, optional spaces,
        # then '(cid:190)' and one of the status/schedule indicators (non-capturing group).
        project_name_matches = re.findall(r"([^\\n]+?)\\n\\s*\\(cid:190\\) (?:Updates:|Project Schedule:|Estimated Schedule:|Project Description:)", design_section_text, re.DOTALL)
        
        for name in project_name_matches:
            cleaned_name = name.strip()
            # Filter out known non-project names (headers, footers, discussion items etc.)
            if cleaned_name and not cleaned_name.startswith(("Discussion", "Recommended Action", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "Page", "Agenda Item")):
                capital_design_projects.add(cleaned_name)

# Find the intersection of funded projects and capital projects in the design phase.
intersecting_projects = funded_project_names.intersection(capital_design_projects)

# Print the count of intersecting projects as a JSON string.
__RESULT__:
print(json.dumps(len(intersecting_projects)))"""

env_args = {'var_function-call-5170959527222557152': 'file_storage/function-call-5170959527222557152.json', 'var_function-call-1640262124798972523': 'file_storage/function-call-1640262124798972523.json'}

exec(code, env_args)
