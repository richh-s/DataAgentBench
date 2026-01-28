code = """import pandas as pd
import re
import json

# Load the full result from the file
with open(locals()['var_function-call-13801791921657955456'], 'r') as f:
    civic_docs_data = json.load(f)

projects_from_docs = []

# Regex to identify potential project names. It looks for lines starting with a capital letter,
# followed by words, numbers, spaces, and certain symbols, optionally ending with a project suffix.
project_name_regex = re.compile(r'^[A-Z][a-zA-Z0-9\s&,-]+(?:\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))?', re.MULTILINE)

for doc in civic_docs_data:
    text = doc['text']
    
    for match in project_name_regex.finditer(text):
        project_name = match.group(0).strip()
        
        # Define a search window around the project name to find related details.
        # This window is a heuristic and might need adjustment based on document structure.
        start_index = max(0, match.start() - 500) # Look back 500 characters
        end_index = min(len(text), match.end() + 1000) # Look forward 1000 characters
        search_window = text[start_index:end_index]

        # Check if 'emergency' or 'FEMA' is in the project name or the search window
        if re.search(r'emergency|FEMA|disaster', project_name, re.IGNORECASE) or \
           re.search(r'emergency|FEMA|disaster', search_window, re.IGNORECASE):
            
            status = "unknown"
            if re.search(r'currently under construction', search_window, re.IGNORECASE):
                status = "under construction"
            elif re.search(r'Construction was completed|Construction completed|Notice of completion filed', search_window, re.IGNORECASE):
                status = "completed"
            elif re.search(r'preliminary design phase|design plans for this project|Plans are under review|working with the consultant to finalize', search_window, re.IGNORECASE):
                status = "design"
            elif re.search(r'not started|identified but not begun|waiting for the agreement|Project to be discussed', search_window, re.IGNORECASE):
                status = "not started"

            project_type = "unknown"
            if re.search(r'Capital Improvement Projects', search_window, re.IGNORECASE):
                project_type = "capital"
            if re.search(r'Disaster Recovery Projects', search_window, re.IGNORECASE):
                project_type = "disaster"
            
            # Extract topics based on keywords in the search window
            topic_list = []
            if re.search(r'emergency', search_window, re.IGNORECASE):
                topic_list.append('emergency')
            if re.search(r'FEMA', search_window, re.IGNORECASE):
                topic_list.append('FEMA')
            if re.search(r'fire', search_window, re.IGNORECASE):
                topic_list.append('fire')
            if re.search(r'storm drain|drainage', search_window, re.IGNORECASE):
                topic_list.append('storm drain/drainage')
            
            projects_from_docs.append({
                "Project_Name": project_name,
                "topic": ", ".join(list(set(topic_list))),
                "type": project_type,
                "status": status
            })

projects_df = pd.DataFrame(projects_from_docs)

# Clean project names: remove extra newlines and report suffixes that may not be in funding db
projects_df['Project_Name'] = projects_df['Project_Name'].str.replace('\\nReport', '', regex=True).str.strip()
projects_df['Project_Name'] = projects_df['Project_Name'].str.replace('Capital Improvement Projects and Disaster Recovery Projects Status', '', regex=False).str.strip()

# Remove duplicates and filter for actual relevant projects (topic or type)
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])
projects_df = projects_df[projects_df['topic'].str.contains('emergency|FEMA', case=False, na=False) | (projects_df['type'] == 'disaster')]

# Load funding data
with open(locals()['var_function-call-1436889616550713528'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Clean funding project names for merging
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()

# Merge the dataframes
merged_df = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')

# Select and order the required columns
result_df = merged_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-13801791921657955456': 'file_storage/function-call-13801791921657955456.json', 'var_function-call-5324861962937878091': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-1436889616550713528': 'file_storage/function-call-1436889616550713528.json', 'var_function-call-1498558563852563849': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-13325195689292245800': [], 'var_function-call-3957231328364284889': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': '', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Disaster Projects', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'None at this time\n\nDisaster Projects', 'topic': 'emergency, fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'topic': 'fire, FEMA, storm drain/drainage', 'type': 'capital', 'status': 'unknown'}], 'var_function-call-5759847907952982018': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'topic': 'FEMA', 'type': 'disaster', 'status': 'unknown'}]}

exec(code, env_args)
