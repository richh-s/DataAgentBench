code = """import re
import json

docs = json.load(open(locals()['var_function-call-12914571133745161145'], 'r'))

def extract_project_info(text):
    projects = []
    # Pattern to find a project heading and its associated block of text
    project_blocks_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9\s&,/-]+?)\n\n'  # Project name followed by two newlines
        r'\(cid:190\) (Updates:|Project Description:|Project Schedule:|Estimated Schedule:)\n'  # (cid:190) pattern and heading
        r'(.*?)(?=\n[A-Z][a-zA-Z0-9\s&,/-]+?\n\n\(cid:190\)|$)',  # Details, up to next project or end of string
        re.DOTALL
    )

    for match in project_blocks_pattern.finditer(text):
        project_name = match.group(1).strip()
        details = match.group(3).strip() # group 1 is project_name, group 2 is heading, group 3 is details

        status = None
        et = None
        topic = []

        # Determine status
        if "completed" in details.lower() or "construction was completed" in details.lower() or "construction completed" in details.lower():
            status = "completed"
        elif "design" in details.lower() or "planning phase" in details.lower():
            status = "design"
        elif "not started" in details.lower() or "identified but not begun" in details.lower():
            status = "not started"
        elif "under construction" in details.lower():
            status = "under construction"

        # Extract end time (et)
        et_match = re.search(
            r'(?:Complete Construction|Construction was completed|Complete Design|Final Design|completed):\s*' # Non-capturing group for keywords, escaped colon
            r'([A-Za-z]+\s*\d{4}|\d{4}-[A-Za-z]+|\d{4}-\d{2}|\w+\s+\d{4})', # Date formats: Month Year, Year-Month, Year-Fall/Spring etc., escaped backslashes
            details, re.IGNORECASE
        )
        if et_match:
            et = et_match.group(1).strip()

        # If the above didn\'t catch it, try to find "completed [Month] [Year]"
        elif re.search(r'completed\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE): # escaped backslashes
            et_match = re.search(r'completed\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE) # escaped backslashes
            if et_match:
                et = et_match.group(1).strip()
        # Look for "Construction was completed, Month Year" or "Construction was completed Month Year"
        elif re.search(r'Construction was completed,?\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE): # escaped backslashes
            et_match = re.search(r'Construction was completed,?\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE) # escaped backslashes
            if et_match:
                et = et_match.group(1).strip()
        elif re.search(r'Complete Construction:\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE): # escaped backslashes
            et_match = re.search(r'Complete Construction:\s*([A-Za-z]+\s+\d{4})', details, re.IGNORECASE) # escaped backslashes
            if et_match:
                et = et_match.group(1).strip()
        elif re.search(r'Construction was completed November 2022', details, re.IGNORECASE):
            et = "November 2022"


        # Determine topic - simple keyword search, case-insensitive
        # Prefer project name for primary topic, details for secondary
        if re.search(r'park|playground|bluffs park|trancas canyon park|skate park', project_name, re.IGNORECASE):
            topic.append("park")
        if re.search(r'road|highway|PCH|canyon road', project_name, re.IGNORECASE):
            topic.append("road")
        if re.search(r'FEMA', details, re.IGNORECASE):
            topic.append("FEMA")
        if re.search(r'fire', details, re.IGNORECASE):
            topic.append("fire")
        if re.search(r'emergency', details, re.IGNORECASE):
            topic.append("emergency")
        if re.search(r'drainage|storm drain', project_name, re.IGNORECASE) or re.search(r'drainage|storm drain', details, re.IGNORECASE):
            topic.append("drainage")
        if re.search(r'water treatment', project_name, re.IGNORECASE) or re.search(r'water treatment', details, re.IGNORECASE):
            topic.append("water treatment")

        projects.append({
            "Project_Name": project_name,
            "topic": ", ".join(topic) if topic else None,
            "status": status,
            "et": et
        })
    return projects

all_projects = []
for doc in docs:
    all_projects.extend(extract_project_info(doc['text']))

# Filter for park-related projects completed in 2022
filtered_projects = [
    p for p in all_projects
    if p["status"] == "completed" and p["topic"] and "park" in p["topic"].lower() and p["et"] and "2022" in p["et"]
]

# Get unique project names to avoid duplicates in funding query
unique_project_names = list(set([p["Project_Name"] for p in filtered_projects]))

print('__RESULT__:')
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-7964308287440170398': ['civic_docs'], 'var_function-call-12914571133745161145': 'file_storage/function-call-12914571133745161145.json'}

exec(code, env_args)
