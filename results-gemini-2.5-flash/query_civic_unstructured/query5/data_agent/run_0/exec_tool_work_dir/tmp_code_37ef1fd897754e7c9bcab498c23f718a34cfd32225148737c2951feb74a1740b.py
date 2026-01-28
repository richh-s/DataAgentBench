code = """import pandas as pd
import json
import re

# Read the full result from the file
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs_data:
    text = doc['text']
    # Regex to capture project name and its schedule
    # Looking for patterns like "Project Name
(cid:190) Updates:
...
(cid:190) Project Schedule:
(cid:131) Begin Construction: Fall 2023"
    # or "Project Name (FEMA Project)"

    # Identify disaster-related sections or keywords first
    is_disaster_section = "Disaster Recovery Projects" in text or "FEMA Project" in text or "CalOES Project" in text or "CalJPIA Project" in text

    # Regex to find project names and their associated schedule information
    # This regex is simplified and might need adjustments based on actual document variability
    # It tries to capture a project name followed by updates and then a schedule, focusing on "Begin Construction" or similar.
    project_pattern = r"(?P<Project_Name>[A-Za-z0-9\s&,-_':\/.()]+?)(?:\n\(cid:190\)\sUpdates:.*?\n)?\(cid:190\)\s(?:Project|Estimated)\sSchedule:\n(?:\(cid:131\).*?\n)*?\(cid:131\)\s(?:Begin|Advertise|Complete Design|Final Design|Project is delayed due to the Cultural Resource review|City will be issuing a RFQ/P for design services in the summer of 2023|Complete Construction):\s*(?P<Start_Date>\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b(?:[-\s]\d{2})?(?:[-\s]\d{4})?)?"
    
    # This regex is an attempt to capture project names and their associated begin construction dates.
    # It looks for a project name followed by schedule information.
    # The project name is expected to be on its own line or followed by a paragraph, then a schedule.
    # I'll refine this if it doesn't work.

    # Re-evaluating the extraction based on the provided hint and preview structure
    # The preview shows "Capital Improvement Projects (Design)" and then listed projects.
    # It also mentions "Capital Improvement Projects and Disaster Recovery Projects Status Report" at the beginning of the document.
    
    # A more robust approach might be to split the document into sections and then parse within sections.
    
    sections = re.split(r"(Capital Improvement Projects|Disaster Recovery Projects)", text)
    
    current_section_type = ""
    
    for i in range(len(sections)):
        section_text = sections[i]
        
        if "Disaster Recovery Projects" in section_text:
            current_section_type = "disaster"
        elif "Capital Improvement Projects" in section_text:
            current_section_type = "capital"
        
        if current_section_type == "disaster":
            # Now, extract projects from this section
            # Projects are usually on a new line and then followed by indented updates/schedule
            # I will try to match project names that are followed by "Updates" or "Project Schedule"
            project_lines = re.findall(r"^(.*?)\n\(cid:190\)\sUpdates:", section_text, re.MULTILINE)
            if not project_lines: # If no "Updates" follow, try "Project Schedule" directly
                project_lines = re.findall(r"^(.*?)\n\(cid:190\)\s(?:Project|Estimated)\sSchedule:", section_text, re.MULTILINE)
            
            for project_name_raw in project_lines:
                project_name = project_name_raw.strip()
                
                # Further refine the start date extraction for the found project
                # Find the schedule block for this specific project
                
                # Escape special characters in project_name for regex
                escaped_project_name = re.escape(project_name)

                # Adjusted regex to capture schedule for the *specific* project
                # Look for the project name, then updates (optional), then schedule, then begin construction.
                schedule_match = re.search(
                    rf"{escaped_project_name}\n(?:\(cid:190\)\sUpdates:[^\n]*\n)*?\(cid:190\)\s(?:Project|Estimated)\sSchedule:\n(?:\(cid:131\)[^\n]*\n)*?\(cid:131\)\s(?:Begin\sConstruction|Advertise|Complete\sDesign|Final\sDesign):\s*(?P<Start_Date>\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b(?:[-\s]\d{{2}})?(?:[-\s]\d{{4}})?(?:\s\w+)?(?:\s\d{{4}})?(?:\s\d{{2}})?)",
                    section_text
                )
                
                if schedule_match:
                    start_date_str = schedule_match.group("Start_Date")
                    
                    if start_date_str and "2022" in start_date_str:
                        disaster_projects_2022.append({"Project_Name": project_name, "Start_Date": start_date_str, "type": current_section_type})
        
        # Also check for disaster keywords in project names even if not in a "Disaster Recovery Projects" section
        project_name_matches_anywhere = re.findall(r"([A-Za-z0-9\s&,-_':\/.()]+?)(?:\s\(FEMA Project\)|\s\(CalJPIA Project\)|\s\(CalOES Project\))", section_text)
        
        for p_name_match in project_name_matches_anywhere:
            project_name = p_name_match.strip()
            
            escaped_project_name = re.escape(project_name)

            schedule_match_anywhere = re.search(
                rf"{escaped_project_name}\n(?:\(cid:190\)\sUpdates:[^\n]*\n)*?\(cid:190\)\s(?:Project|Estimated)\sSchedule:\n(?:\(cid:131\)[^\n]*\n)*?\(cid:131\)\s(?:Begin\sConstruction|Advertise|Complete\sDesign|Final\sDesign):\s*(?P<Start_Date>\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b(?:[-\s]\d{{2}})?(?:[-\s]\d{{4}})?(?:\s\w+)?(?:\s\d{{4}})?(?:\s\d{{2}})?)",
                section_text
            )
            
            if schedule_match_anywhere:
                start_date_str = schedule_match_anywhere.group("Start_Date")
                if start_date_str and "2022" in start_date_str:
                    disaster_projects_2022.append({"Project_Name": project_name, "Start_Date": start_date_str, "type": "disaster"})
    

# Manual inspection and refinement of the extracted list based on the preview
# The project "Latigo Canyon Road Retaining Wall Repair Project" is mentioned with "Awaiting final FEMA/CalOES approval"
# And its schedule "Begin Construction: Summer 2023" -- this doesn't fit 2022 criteria.

# The project "Malibu Bluffs Park South Walkway Repairs" is mentioned with "Estimated Schedule: Complete Design: Summer 2023"

# The project "Bluffs Park Shade Structure" says "Construction was completed November 2022"
# This project is a Capital Improvement Project based on the heading. So I need to verify its type.
# The question is about *disaster-related* projects.

# Let's refine the approach:
# 1. Identify all project names and their associated start dates.
# 2. For each project, determine if it's "disaster-related" by looking for keywords like "FEMA", "CalOES", "CalJPIA", or being under a "Disaster Recovery Projects" heading.
# 3. Filter for projects that started in 2022.

all_projects = []
project_and_schedule_pattern = r"(?P<Project_Name>[A-Za-z0-9\s&,-_':\/.()]+?)\n(?:\(cid:190\)\sUpdates:[^\n]*\n)*?\(cid:190\)\s(?:Project|Estimated)\sSchedule:\n(?:\(cid:131\)[^\n]*\n)*?\(cid:131\)\s(?:Begin\sConstruction|Advertise|Complete\sDesign|Final\sDesign|Construction\swas\scompleted|Complete\sConstruction):\s*(?P<Start_Date>\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b(?:[-\s]\d{{2}})?(?:[-\s]\d{{4}})?(?:\s\w+)?(?:\s\d{{4}})?(?:\s\d{{2}})?)?"


for doc in civic_docs_data:
    text = doc['text']
    for match in re.finditer(project_and_schedule_pattern, text, re.MULTILINE):
        project_name = match.group("Project_Name").strip()
        start_date_str = match.group("Start_Date") if match.group("Start_Date") else ""

        is_disaster = False
        if "Disaster Recovery Projects" in text and match.start() < text.find("Disaster Recovery Projects") + len("Disaster Recovery Projects") and match.end() > text.find("Disaster Recovery Projects"):
             # This check is not accurate, it should be within the section
            pass # I will check this later by looking for keywords
        
        # Check for disaster keywords in the project description text around the project
        context_start = max(0, match.start() - 500)
        context_end = min(len(text), match.end() + 500)
        project_context = text[context_start:context_end]
        
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster and "2022" in start_date_str:
            all_projects.append({"Project_Name": project_name, "Start_Date": start_date_str, "type": "disaster"})

# Filter out duplicates based on Project_Name and Start_Date, prioritizing 'disaster' type if multiple types are found for a project.
# Since the `all_projects` list is built by finding disaster projects, this is implicitly handled.
# A small cleaning to remove duplicates is helpful.
unique_disaster_projects_2022 = pd.DataFrame(all_projects).drop_duplicates().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json'}

exec(code, env_args)
