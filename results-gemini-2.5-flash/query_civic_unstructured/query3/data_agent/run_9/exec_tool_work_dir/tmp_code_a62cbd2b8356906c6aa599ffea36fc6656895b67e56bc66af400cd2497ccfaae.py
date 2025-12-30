code = """import re
import json

docs = json.loads(open(locals()['var_function-call-17046440918725083585'], 'r').read())
projects_data = []

keywords = ['emergency', 'FEMA']

# Regex to find project titles and their starting positions.
# Project titles are typically on a new line, start with a capital, and end before a newline followed by (cid:190) or "Updates:" or "Project Description:"
# The regex is carefully constructed and escaped for the `code` argument.
project_title_pattern = re.compile(r'\\n([A-Z][a-zA-Z0-9&\\s,-\/()]+?)\\n(?:\\(cid:190\\)|\\s*Updates:|\\s*Project Description:|\\s*Project Schedule:)', re.DOTALL)

for doc in docs:
    text = doc['text']
    
    # Find all project titles and their spans
    project_matches = []
    for m in project_title_pattern.finditer(text):
        # Store the project name (group 1) and its starting index
        project_matches.append((m.group(1).strip(), m.start()))

    # Now, iterate through the matches to extract content for each project
    for i in range(len(project_matches)):
        project_name, start_idx = project_matches[i]
        
        # Determine the end index for the current project's content
        if i + 1 < len(project_matches):
            end_idx = project_matches[i+1][1] # Content ends before the next project's start
        else:
            end_idx = len(text) # Last project, goes to end of document

        project_content = text[start_idx:end_idx]

        # Clean up project name - remove any trailing descriptions that might have been picked up
        # Example: "Project Name (FEMA Project)" -> "Project Name"
        clean_project_name = re.sub(r'\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\)|\\(FEMA/CalOES Project\\)', '', project_name).strip()

        # Check if 'emergency' or 'FEMA' is in the project name or content
        if any(keyword.lower() in clean_project_name.lower() or keyword.lower() in project_content.lower() for keyword in keywords):
            status = "N/A"
            if "completed" in project_content.lower():
                status = "completed"
            elif "under construction" in project_content.lower() or "begin construction" in project_content.lower():
                status = "construction"
            elif "design" in project_content.lower() or "preliminary design" in project_content.lower() or "awaiting final fema/caloes approval" in project_content.lower():
                status = "design"
            elif "not started" in project_content.lower() or "identified but not begun" in project_content.lower():
                status = "not started"

            # More specific check for project name after cleaning
            # to ensure only relevant projects are added
            if any(keyword.lower() in clean_project_name.lower() for keyword in keywords) or \
               any(keyword.lower() in project_content.lower() for keyword in keywords):
                projects_data.append({
                    "Project_Name": clean_project_name,
                    "Status": status
                })

print('__RESULT__:')
print(json.dumps(projects_data))"""

env_args = {'var_function-call-6356119364886939959': ['civic_docs'], 'var_function-call-17046440918725083585': 'file_storage/function-call-17046440918725083585.json', 'var_function-call-5623330767657936695': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Status': 'construction'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview\nAvenue. This project is scheduled to be accepted by the Council at the\nJanuary 24, 2022 meeting.\n\nClover Heights Storm Drain (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES\nProject)', 'Status': 'construction'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Status': 'construction'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Status': 'design'}, {'Project_Name': 'Disaster Projects (Construction)\nNone at this time\n\nDisaster Projects (Completed)\nGuardrail Replacement Citywide (FEMA/CalOES Project)', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Canyon Road that was damaged from a failed storm drain.\n\nDisaster Projects (Not Started)\nClover Heights Storm Drain (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Status': 'construction'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Status': 'construction'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Status': 'construction'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Status': 'design'}, {'Project_Name': 'Disaster Projects (Construction)\nNone at this time\n\nDisaster Projects (Completed)\nGuardrail Replacement Citywide (FEMA/CalOES Project)', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Canyon Road that was damaged from a failed storm drain.\n\nDisaster Projects (Not Started)\nClover Heights Storm Drain (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Status': 'construction'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Status': 'N/A'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Status': 'N/A'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Proposals are due in April 14, 2022.\n\nLatigo Canyon Road Culvert Repairs (FEMA Project)', 'Status': 'construction'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Cuthbert Road, Morning View Drive, Busch Drive at Harvester Road. The project also\nincluded the repair of a storm drainage facility on Birdview Avenue. The project was\naccepted by the Council on January 24, 2022\n\nCorral Canyon Culvert Repairs (FEMA Project)', 'Status': 'N/A'}]}

exec(code, env_args)
