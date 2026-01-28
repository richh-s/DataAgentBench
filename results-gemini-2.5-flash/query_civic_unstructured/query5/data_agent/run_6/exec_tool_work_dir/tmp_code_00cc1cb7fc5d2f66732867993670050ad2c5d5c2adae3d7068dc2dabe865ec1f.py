code = """import json
import re

def extract_project_info(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    # Determine if the document generally refers to disaster recovery projects
    global_disaster_context = "Disaster Recovery Projects" in text or "FEMA" in text or "CalOES" in text

    # Regex for project names, flexible to include common suffixes and handle potential inconsistencies
    # Using re.IGNORECASE for broader matching
    project_name_pattern = re.compile(r"^(.*?Project)(?:\s*\((?:FEMA|CalJPIA|CalOES|Design|Construction|Not Started) Project\))?$", re.IGNORECASE)
    
    # Regex for extracting start time keywords from schedule lines
    start_time_keywords_pattern = re.compile(r"(Begin Construction|Advertise):\s*([^\n]+)", re.IGNORECASE)
    date_pattern = re.compile(r"\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b", re.IGNORECASE)
    
    # Regex for disaster-related suffixes in project names
    disaster_suffix_pattern = re.compile(r"\((FEMA|CalJPIA|CalOES) Project\)", re.IGNORECASE)

    for i, line in enumerate(lines):
        line = line.strip()

        project_name_match = project_name_pattern.search(line)
        
        # Conditions to identify a valid project name line
        is_project_header = (
            project_name_match and 
            not line.startswith("Capital Improvement Projects") and
            not line.startswith("Disaster Recovery Projects") and
            "(cid:190)" not in line and # Filter out lines that are likely section sub-headers
            "Updates:" not in line and # Filter out update lines that might contain 'Project'
            "Schedule:" not in line and # Filter out schedule lines
            len(line) > 10 and # Ensure it's a sufficiently long name
            not line.isupper() and # Filter out all-caps section titles
            "Agenda Item" not in line and
            "RECOMMENDED ACTION:" not in line and
            "DISCUSSION:" not in line
        )

        if is_project_header:
            if current_project: # If we have a project currently being parsed, add it to the list
                projects.append(current_project)
            
            project_name = project_name_match.group(1).strip() # Extract the base project name
            
            current_project = {
                "Project_Name": project_name,
                "type": "capital", # Default to capital
                "st": None
            }
            # Check if the original line (before cleaning) contains disaster suffixes
            if disaster_suffix_pattern.search(line):
                current_project["type"] = "disaster"
            continue

        # If we are currently parsing a project, look for more details in subsequent lines
        if current_project:
            # Refine project type if disaster keywords are found in surrounding lines
            if (current_project["type"] == "capital" and 
                ("FEMA" in line or "CalOES" in line or "Disaster Recovery" in line)):
                current_project["type"] = "disaster"

            # Extract start time from project schedule information
            if "(cid:190) Project Schedule:" in line: # This indicates the start of schedule details
                for j in range(i + 1, min(i + 6, len(lines))): # Look up to 5 lines ahead
                    schedule_detail_line = lines[j].strip()
                    
                    start_time_match = start_time_keywords_pattern.search(schedule_detail_line)
                    if start_time_match:
                        current_project["st"] = start_time_match.group(2).strip()
                        break # Found a specific start date, no need to look further
                    
                    # Fallback: look for year/season/month if specific phrases aren't found
                    date_match = date_pattern.search(schedule_detail_line)
                    if date_match:
                        current_project["st"] = date_match.group(0).strip()
                        break # Found a date, no need to look further
    
    # Add the last project if any were found and not yet appended
    if current_project:
        projects.append(current_project)

    # Final pass to apply global disaster context if individual project didn't explicitly state it
    for project in projects:
        if project["type"] == "capital" and global_disaster_context:
            project["type"] = "disaster"

    return projects

# Load data from civic_docs_database
file_path_docs = locals()['var_function-call-6524522302801542169']
with open(file_path_docs, "r") as f:
    docs_data = json.load(f)

all_projects_extracted = []
for doc in docs_data:
    all_projects_extracted.extend(extract_project_info(doc["text"]))

# Filter for disaster projects that started in 2022
disaster_projects_2022_names = set()
for project in all_projects_extracted:
    if project["type"] == "disaster" and project["st"] and "2022" in str(project["st"]):
        disaster_projects_2022_names.add(project["Project_Name"])

# Load funding data from funding_database
file_path_funding = locals()['var_function-call-7943208518371631309']
with open(file_path_funding, "r") as f:
    funding_data = json.load(f)

total_funding = 0

# Regex to clean project names for matching (remove suffixes like (FEMA Project))
clean_name_pattern = re.compile(r"\s*\((?:FEMA|CalJPIA|CalOES|Design|Construction|Not Started) Project\)", re.IGNORECASE)

for project_name in disaster_projects_2022_names:
    for funding_record in funding_data:
        # Clean both extracted project name and funding record project name for robust matching
        clean_extracted_name = clean_name_pattern.sub("", project_name).strip()
        clean_funding_name = clean_name_pattern.sub("", funding_record["Project_Name"]).strip()
        
        if clean_extracted_name.lower() == clean_funding_name.lower(): # Case-insensitive comparison
            total_funding += int(funding_record["Amount"])
            break # Move to the next extracted project after finding a match

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json', 'var_function-call-6538230662028118532': [], 'var_function-call-3229506228145922907': 0}

exec(code, env_args)
