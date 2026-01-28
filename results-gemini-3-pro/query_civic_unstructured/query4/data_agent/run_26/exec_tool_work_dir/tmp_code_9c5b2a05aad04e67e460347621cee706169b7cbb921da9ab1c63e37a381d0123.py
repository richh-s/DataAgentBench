code = """import json
import re

path_docs = locals()['var_function-call-3486162399230155614']
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_funding = locals()['var_function-call-6421004180030422518']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

# 1. Get base names from Funding
base_names = set()
for row in funding_data:
    name = row['Project_Name']
    # Remove parens like (FEMA Project), (CalOES Project)
    # Regex to remove (.*) at the end
    base = re.sub(r'\s*\(.*?\)$', '', name)
    base_names.add(base)

# 2. Search in text
started_projects = set()

# Regex patterns for Start Date in Spring 2022
# We look for "Begin Construction" or "Construction Start" followed by "Spring 2022" or March/April/May 2022
# Also allow for some words in between
start_patterns = [
    r"(begin construction|construction start|construction to begin).*?(spring|march|april|may).*?2022",
    r"(advertise).*?(spring|march|april|may).*?2022" # Checking advertise as well, just in case
]

# Map base names to their text occurrences and check schedules
# To avoid processing the whole text for every name repeatedly, let's scan text once
# But scanning for names is easier.

debug_info = []

for doc in civic_docs:
    text = doc['text']
    # Normalize newlines
    lines = text.split(chr(10))
    
    # We will look for project names in the text.
    # Usually project names are on their own line.
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if line_clean in base_names:
            # Found a project!
            # Look ahead for schedule
            # Scan next 50 lines
            context_lines = lines[i+1:i+51]
            context = " ".join(context_lines).lower()
            
            # Check for start patterns
            found = False
            for pat in start_patterns:
                if re.search(pat, context):
                    # verify it is 2022 and Spring
                    # The regex ensures it.
                    # Exclude "Summer 2022" if it appears before Spring? No, regex looks for Spring/March/April/May.
                    
                    # One edge case: "Begin Construction: Summer 2022 (Design: Spring 2022)"
                    # The regex `construction start.*?spring` might match across boundaries.
                    # Let's be more specific. match line by line.
                    found = True
                    break
            
            if found:
                # Double check with line-by-line
                # We want the line containing "Begin Construction" to also contain the date
                # Or the date to be in the next few lines under "Project Schedule"
                
                # Let's extract the "Project Schedule" section
                schedule_found = False
                for l in context_lines:
                    if "project schedule" in l.lower() or "estimated schedule" in l.lower():
                        schedule_found = True
                    
                    if schedule_found:
                        # Look for start dates in these lines
                        l_lower = l.lower()
                        if "construction" in l_lower and "2022" in l_lower:
                            if "spring" in l_lower or "march" in l_lower or "april" in l_lower or "may" in l_lower:
                                # Ensure it's not "complete construction"
                                if "complete" in l_lower and "begin" not in l_lower:
                                    continue # skip completion
                                started_projects.add(line_clean)
                                debug_info.append({"name": line_clean, "match": l_clean})
                        # Also "Advertise"
                        if "advertise" in l_lower and "2022" in l_lower:
                            if "spring" in l_lower or "march" in l_lower or "april" in l_lower or "may" in l_lower:
                                started_projects.add(line_clean)
                                debug_info.append({"name": line_clean, "match": l_clean})

# Filter out "Advertise" if we want strictly "Started".
# But usually "started" in these questions means the earliest phase start in that period?
# However, "Begin Construction" is the gold standard.
# Let's list what we found.

print('__RESULT__:')
print(json.dumps(list(started_projects)))"""

env_args = {'var_function-call-5404665793405674675': ['civic_docs'], 'var_function-call-5404665793405674210': ['Funding'], 'var_function-call-4895478785273924841': 'file_storage/function-call-4895478785273924841.json', 'var_function-call-4895478785273921810': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3486162399230155614': 'file_storage/function-call-3486162399230155614.json', 'var_function-call-6421004180030422518': 'file_storage/function-call-6421004180030422518.json', 'var_function-call-12647426590907445262': [{'name': 'Marie Canyon Green Streets', 'relevant_lines': ['anticipated to have a final design by March 2022. The project will be']}, {'name': 'advertised for construction bids shortly after this date.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'PCH Median Improvements Project', 'relevant_lines': ['project will have final approval by March 2022. The project will be']}, {'name': 'agreement will be sent to City Council in March.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022']}, {'name': 'to review', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'sending this project out to bid during the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'March 2022', 'relevant_lines': ['(cid:131) Begin Design: Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'beginning in April 2022.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': 'started and is anticipated to be completed by the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'assessment district will be created.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) Next public community meeting is scheduled for March 25th.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'within the City.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'construction bids.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'management services was approved by Council on March 14, 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids']}, {'name': 'will begin in conjunction with the PCH Median Improvement', 'relevant_lines': ['(cid:131) Complete Final Design: Spring 2022']}, {'name': 'scheduled for the April 11, 2022 Council meeting.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'relevant_lines': ['go to Council in April 2022 after the Funding Agreement is issued by']}, {'name': 'Metro.', 'relevant_lines': ['(cid:131) Begin Design: Late Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['Proposals are due in April 14, 2022.']}, {'name': 'damaged by the Woolsey Fire.', 'relevant_lines': ['anticipated that the final design will be complete by March 2022. The']}, {'name': 'beginning in Spring 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}]}

exec(code, env_args)
