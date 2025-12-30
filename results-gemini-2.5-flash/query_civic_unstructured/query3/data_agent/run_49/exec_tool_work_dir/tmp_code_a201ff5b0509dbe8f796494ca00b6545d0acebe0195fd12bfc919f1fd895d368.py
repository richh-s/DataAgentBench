code = """import pandas as pd
import re
import json

# Load the full result from the file
with open(locals()['var_function-call-13801791921657955456'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []

# A more flexible regex for project names. 
# It looks for lines that start with a capital letter, followed by words, 
# possibly including numbers, & or - characters, and optional suffixes.
project_name_pattern = re.compile(
    r"^[A-Z][a-zA-Z0-9\\s&,-]+(?:\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\))?", 
    re.MULTILINE
)

for doc in civic_docs_data:
    text = doc['text']
    
    # Split the document into potential project blocks based on common section headers or patterns.
    # This is a heuristic and might need to be adjusted.
    sections = re.split(r'(?m)^(?=Capital Improvement Projects \(|Disaster Recovery Projects |RECOMMENDED ACTION:|DISCUSSION:)', text)

    for section in sections:
        # Look for project names within each section
        for name_match in project_name_pattern.finditer(section):
            project_name = name_match.group(0).strip()
            
            # Filter for projects related to 'emergency' or 'FEMA' in the project name itself.
            if re.search(r'emergency|FEMA|disaster', project_name, re.IGNORECASE):

                status = "unknown"
                if re.search(r'Updates: Project is currently under construction', section, re.IGNORECASE):
                    status = "under construction"
                elif re.search(r'Construction was completed|Construction completed', section, re.IGNORECASE):
                    status = "completed"
                elif re.search(r'preliminary design phase|working with the consultant to finalize the design plans|Plans are under review', section, re.IGNORECASE):
                    status = "design"
                elif re.search(r'identified but not begun|waiting for the agreement|Project to be discussed', section, re.IGNORECASE):
                    status = "not started"
                
                project_type = "unknown"
                if re.search(r'Capital Improvement Projects', section, re.IGNORECASE):
                    project_type = "capital"
                if re.search(r'Disaster Recovery Projects', section, re.IGNORECASE):
                    project_type = "disaster"

                topic = []
                if re.search(r'emergency', section, re.IGNORECASE):
                    topic.append('emergency')
                if re.search(r'FEMA', section, re.IGNORECASE):
                    topic.append('FEMA')
                if re.search(r'fire', section, re.IGNORECASE):
                    topic.append('fire')
                if re.search(r'storm drain|drainage', section, re.IGNORECASE):
                    topic.append('storm drain/drainage')
                
                projects.append({
                    "Project_Name": project_name,
                    "topic": ", ".join(list(set(topic))),
                    "type": project_type,
                    "status": status
                })

projects_df = pd.DataFrame(projects)

# Remove duplicates based on Project_Name and ensure only relevant projects are included
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])
projects_df = projects_df[projects_df['topic'].str.contains('emergency|FEMA', case=False, na=False) | projects_df['type'].str.contains('disaster', case=False, na=False)]

print("__RESULT__:")
print(projects_df.to_json(orient='records'))"""

env_args = {'var_function-call-13801791921657955456': 'file_storage/function-call-13801791921657955456.json', 'var_function-call-5324861962937878091': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-1436889616550713528': 'file_storage/function-call-1436889616550713528.json', 'var_function-call-1498558563852563849': [{'Project_Name': 'Capital Improvement Projects and Disaster Recovery Projects Status\nReport', 'topic': 'storm drain/drainage', 'type': 'disaster', 'status': 'design'}], 'var_function-call-13325195689292245800': []}

exec(code, env_args)
