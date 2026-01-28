code = """import pandas as pd
import re
import json

# Load the full result from the file
with open(locals()['var_function-call-13801791921657955456'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find project blocks based on common patterns
    # This pattern looks for a project name followed by details (updates, schedule, description)
    # It tries to capture the project name and the block of text associated with it.
    project_blocks_matches = re.finditer(
        r'(?P<project_name>^[A-Z][a-zA-Z0-9\\s&,-]+(?:\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\))?)(?:\\n\\(cid:190\\)|\\n\\(cid:131\\)|\\nUpdates:|\\nProject Schedule:|\\nEstimated Schedule:|\\nProject Description:)(?P<description_details>[\\s\\S]*?)(?=(?:\\n\\n^[A-Z][a-zA-Z0-9\\s&,-]+(?:\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\))?)|\\Z)', 
        text, 
        re.MULTILINE
    )

    for match in project_blocks_matches:
        project_name = match.group('project_name').strip()
        description_details = match.group('description_details')
        
        # Ensure the project name or description contains 'emergency' or 'FEMA'
        if re.search(r'emergency|FEMA|disaster', project_name, re.IGNORECASE) or \
           re.search(r'emergency|FEMA|disaster', description_details, re.IGNORECASE):

            status = "unknown"
            if re.search(r'Project is currently under construction', description_details, re.IGNORECASE):
                status = "under construction"
            elif re.search(r'Construction was completed|Construction completed', description_details, re.IGNORECASE):
                status = "completed"
            elif re.search(r'preliminary design phase|working with the consultant to finalize the design plans|Plans are under review', description_details, re.IGNORECASE):
                status = "design"
            elif re.search(r'identified but not begun|waiting for the agreement|Project to be discussed', description_details, re.IGNORECASE):
                status = "not started"
            
            project_type = "unknown"
            if re.search(r'Capital Improvement Projects', text, re.IGNORECASE) or re.search(r'Capital Improvement Projects', description_details, re.IGNORECASE):
                project_type = "capital"
            if re.search(r'Disaster Recovery Projects', text, re.IGNORECASE) or re.search(r'Disaster Recovery Projects', description_details, re.IGNORECASE):
                project_type = "disaster"

            topic = []
            if re.search(r'emergency', description_details, re.IGNORECASE):
                topic.append('emergency')
            if re.search(r'FEMA', description_details, re.IGNORECASE):
                topic.append('FEMA')
            if re.search(r'fire', description_details, re.IGNORECASE):
                topic.append('fire')
            if re.search(r'storm drain|drainage', description_details, re.IGNORECASE):
                topic.append('storm drain/drainage')
            
            projects.append({
                "Project_Name": project_name,
                "topic": ", ".join(list(set(topic))),
                "type": project_type,
                "status": status
            })

projects_df = pd.DataFrame(projects)

# Remove duplicates and ensure relevance
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])
projects_df = projects_df[projects_df['topic'].str.contains('emergency|FEMA', case=False, na=False) | projects_df['type'].str.contains('disaster', case=False, na=False)]

print("__RESULT__:")
print(projects_df.to_json(orient='records'))"""

env_args = {'var_function-call-13801791921657955456': 'file_storage/function-call-13801791921657955456.json', 'var_function-call-5324861962937878091': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-1436889616550713528': 'file_storage/function-call-1436889616550713528.json', 'var_function-call-1498558563852563849': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-13325195689292245800': [], 'var_function-call-3957231328364284889': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': '', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Disaster Projects', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'None at this time\n\nDisaster Projects', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'topic': 'fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}]}

exec(code, env_args)
