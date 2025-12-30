code = """import json
import re

funding_data = json.load(open(locals()['var_function-call-11819915285845147095'], 'r'))
civic_docs = json.load(open(locals()['var_function-call-13092724548813218485'], 'r'))

project_details = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document text into potential project blocks based on common headings for projects
    # Capital Improvement Projects (Design), Capital Improvement Projects (Construction), Capital Improvement Projects (Not Started), Disaster Recovery Projects
    project_sections = re.split(r'(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects)\\n', text)
    
    for section in project_sections:
        if not section.strip():
            continue

        # Each section may contain multiple projects, or a main heading. Focus on project descriptions.
        # A project typically starts with a title followed by updates or schedule.
        # Look for a pattern like: Project_Name\n(cid:190) Updates: or Project_Name\n(cid:190) Project Schedule:
        
        # Regex to find project names and their descriptions. This will be an iterative process.
        # Attempt to capture project name and its subsequent details until another project or section end.
        projects_in_section = re.findall(r'([A-Z][a-zA-Z0-9&\\s,-]+?)\\n\\(cid:190\\) (Updates|Project Schedule|Estimated Schedule|Project Description):.*?(?=(?:[A-Z][a-zA-Z0-9&\\s,-]+?)\\n\\(cid:190\\) (Updates|Project Schedule|Estimated Schedule|Project Description):|Capital Improvement Projects \(.*?\)|Disaster Recovery Projects|$)', section, re.DOTALL)

        for project_name, _, details in projects_in_section:
            project_name = project_name.strip()
            details = details.strip()
            
            is_park_related = "park" in project_name.lower() or "park" in details.lower()

            status = 'unknown'
            end_date_str = ''
            
            # Check for completion status and date in the details section of the project
            if re.search(r'Construction was completed, (.*?)(?:\\n|$)', details):
                status = 'completed'
                end_date_match = re.search(r'Construction was completed, (.*?)(?:\\n|$)', details)
                if end_date_match:
                    end_date_str = end_date_match.group(1).strip()
            elif re.search(r'Complete (?:Construction|Design|Project|Work|Completion):\\s*(.*?)(?:\\n|$)', details, re.IGNORECASE):
                status = 'completed' # Assuming if a completion date is given, it means completed.
                end_date_match = re.search(r'Complete (?:Construction|Design|Project|Work|Completion):\\s*(.*?)(?:\\n|$)', details, re.IGNORECASE)
                if end_date_match:
                    end_date_str = end_date_match.group(1).strip()

            if is_park_related and status == 'completed' and '2022' in end_date_str:
                project_details.append({
                    'Project_Name': project_name,
                    'End_Date': end_date_str
                })


# Filter funding data for relevant projects
park_projects_2022_names = {proj['Project_Name'] for proj in project_details}
total_funding = 0

for item in funding_data:
    if item['Project_Name'] in park_projects_2022_names:
        try:
            total_funding += int(item['Amount'])
        except ValueError:
            pass # Handle cases where 'Amount' might not be a valid integer

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-11819915285845147095': 'file_storage/function-call-11819915285845147095.json', 'var_function-call-13092724548813218485': 'file_storage/function-call-13092724548813218485.json', 'var_function-call-16377781267203041949': 0, 'var_function-call-5400263439931074167': ['civic_docs']}

exec(code, env_args)
