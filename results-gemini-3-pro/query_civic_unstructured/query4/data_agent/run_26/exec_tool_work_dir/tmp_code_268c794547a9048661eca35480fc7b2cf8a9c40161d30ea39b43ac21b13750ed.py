code = """import json
import re

path_docs = locals()['var_function-call-3486162399230155614']
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_funding = locals()['var_function-call-6421004180030422518']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

base_names = set()
for row in funding_data:
    name = row['Project_Name']
    base = re.sub(r'\s*\(.*?\)$', '', name)
    base_names.add(base)

found_events = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split(chr(10))
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if line_clean in base_names:
            context_lines = lines[i+1:i+51]
            
            schedule_active = False
            for l in context_lines:
                l_clean = l.strip()
                l_lower = l_clean.lower()
                
                # Detect start of schedule section
                if "project schedule" in l_lower or "estimated schedule" in l_lower:
                    schedule_active = True
                    continue # Skip the header itself
                
                # Use heuristics to detect end of section? (e.g. empty lines or new headers)
                # For now, just process lines.
                
                if schedule_active:
                    # Check for date
                    is_spring_2022 = False
                    if "2022" in l_lower:
                        if "spring" in l_lower or "march" in l_lower or "april" in l_lower or "may" in l_lower:
                            is_spring_2022 = True
                    
                    if is_spring_2022:
                        event_type = None
                        if "begin construction" in l_lower or "start construction" in l_lower:
                            event_type = "construction_start"
                        elif "advertise" in l_lower:
                            event_type = "advertise"
                        elif "begin design" in l_lower:
                            event_type = "design_start"
                        elif "complete" in l_lower:
                             # Exclude completion
                             pass
                        
                        if event_type:
                            found_events.append({
                                "project": line_clean,
                                "event": event_type,
                                "line": l_clean
                            })
                
                # Stop if we hit another project header (heuristic)
                if l_clean.startswith("(cid:190)") and "Updates:" in lines[lines.index(l)+1 if lines.index(l)+1 < len(lines) else lines.index(l)]:
                     # This check is hard because we are iterating context lines which are strings
                     pass

# Deduplicate found events
# Logic: If a project has "construction_start" in Spring 2022, count it.
# If it has "advertise" in Spring 2022 but NO "construction_start" info or construction is later?
# "Advertise" is a start. I'll count it.

final_projects = set()
for item in found_events:
    final_projects.add(item['project'])

print('__RESULT__:')
print(json.dumps(list(final_projects)))"""

env_args = {'var_function-call-5404665793405674675': ['civic_docs'], 'var_function-call-5404665793405674210': ['Funding'], 'var_function-call-4895478785273924841': 'file_storage/function-call-4895478785273924841.json', 'var_function-call-4895478785273921810': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3486162399230155614': 'file_storage/function-call-3486162399230155614.json', 'var_function-call-6421004180030422518': 'file_storage/function-call-6421004180030422518.json', 'var_function-call-12647426590907445262': [{'name': 'Marie Canyon Green Streets', 'relevant_lines': ['anticipated to have a final design by March 2022. The project will be']}, {'name': 'advertised for construction bids shortly after this date.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'PCH Median Improvements Project', 'relevant_lines': ['project will have final approval by March 2022. The project will be']}, {'name': 'agreement will be sent to City Council in March.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022']}, {'name': 'to review', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'sending this project out to bid during the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'March 2022', 'relevant_lines': ['(cid:131) Begin Design: Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'beginning in April 2022.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': 'started and is anticipated to be completed by the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'assessment district will be created.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) Next public community meeting is scheduled for March 25th.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'within the City.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'construction bids.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'management services was approved by Council on March 14, 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids']}, {'name': 'will begin in conjunction with the PCH Median Improvement', 'relevant_lines': ['(cid:131) Complete Final Design: Spring 2022']}, {'name': 'scheduled for the April 11, 2022 Council meeting.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'relevant_lines': ['go to Council in April 2022 after the Funding Agreement is issued by']}, {'name': 'Metro.', 'relevant_lines': ['(cid:131) Begin Design: Late Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['Proposals are due in April 14, 2022.']}, {'name': 'damaged by the Woolsey Fire.', 'relevant_lines': ['anticipated that the final design will be complete by March 2022. The']}, {'name': 'beginning in Spring 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}]}

exec(code, env_args)
