code = """import pandas as pd
import json
import re

# Read the full result from the file
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

# Regex to capture a project block (project name and its details until next similar heading or end of text)
# This pattern looks for a line that might be a project name, followed by indented bullet points
# and captures the text until a similar non-indented line or the end.
project_block_pattern = re.compile(
    r"^([A-Za-z0-9\\s&,-_':\\/.()]+?)\\n(?:\\(cid:[0-9]+?\\)[\\s\\S]*?)*?" # Project Name and following indented lines
    r"(?:(?=^[A-Za-z0-9\\s&,-_':\\/.()]+?\\n(?:\\(cid:[0-9]+?\\)[\\s\\S]*?)?$)|$)", # Until next project name or end
    re.MULTILINE
)

# Simpler project name and date pattern within a block, looking for keywords that indicate start/completion.
# This pattern will be applied *within* the extracted project blocks.
project_details_pattern = re.compile(
    r"(?P<Project_Name>[A-Za-z0-9\\s&,-_':\\/.()]+?)\\n(?:[\\s\\S]*?)"
    r"(?:(?:Begin|Complete|Construction\\swas\\scompleted):\\s*(?P<Start_Date>\\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\\b(?:[-\\s]\\d{2})?(?:[-\\s]\\d{4})?(?:\\s\\w+)?(?:-\\d{2})?(?:\\s\\d{4})?(?:\\s\\d{2})?))",
    re.MULTILINE
)

for doc in civic_docs_data:
    text = doc['text']
    
    # Check if the document itself has general disaster keywords or sections
    doc_contains_disaster_keywords = bool(re.search(r"Disaster Recovery Projects|FEMA|CalOES|CalJPIA", text, re.IGNORECASE))

    # Extract project blocks first
    for block_match in re.finditer(project_block_pattern, text):
        project_block_text = block_match.group(0) # The entire matched block
        
        # Now, try to extract project name and dates within this block
        details_match = project_details_pattern.search(project_block_text)
        
        if details_match:
            project_name = details_match.group("Project_Name").strip()
            start_date_str = details_match.group("Start_Date") if details_match.group("Start_Date") else ""
            
            is_project_disaster_related = False
            
            # Check for disaster keywords within the specific project block
            if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_block_text, re.IGNORECASE):
                is_project_disaster_related = True
            
            # Combine document-level and project-block-level disaster identification
            if (is_project_disaster_related or doc_contains_disaster_keywords) and "2022" in start_date_str:
                extracted_projects.append({"Project_Name": project_name, "Start_Date": start_date_str})

# Remove duplicates based on Project_Name and Start_Date
unique_disaster_projects_2022 = pd.DataFrame(extracted_projects).drop_duplicates(subset=["Project_Name"]).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': []}

exec(code, env_args)
