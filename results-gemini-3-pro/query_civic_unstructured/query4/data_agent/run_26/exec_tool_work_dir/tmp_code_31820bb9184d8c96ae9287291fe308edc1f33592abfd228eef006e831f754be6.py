code = """import json

path_funding = locals()['var_function-call-6421004180030422518']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

# The result from previous step
started_projects = locals()['var_function-call-10771641254414666451']
# Note: previous result is a JSON string or list? 
# The tool output says "The result is: [...]" which is a list.
# But in python `locals()['...']` gives the value. If it was printed as JSON string, it might be a string.
# But `execute_python` returns the *printed* string?
# Wait, "The result is stored under key...". The tool output says "The result is: ...".
# Usually, if I use `print(json.dumps(...))`, the result captured is the string.
# So I need to parse it.

try:
    if isinstance(started_projects, str):
        started_projects = json.loads(started_projects)
except:
    pass # already list

total_funding = 0
project_funding_details = {}

for sp in started_projects:
    # Find all funding records that start with this name
    # Be careful with partial matches e.g. "Park" matches "Park A" and "Park B"
    # But these are full names from the funding table (minus suffix).
    # So we match: Funding_Name.startswith(sp)
    
    # Also, we should ensure that we don't double count if we have "Project A" and "Project A Phase 2" in `started_projects`.
    # But `started_projects` comes from `Funding` base names.
    # If `Funding` has `Project A` and `Project A Phase 2` as distinct base names, they are distinct.
    
    p_total = 0
    for row in funding_data:
        fname = row['Project_Name']
        if fname.startswith(sp):
             # check if it's a valid suffix match or exact match
             # e.g. "Project A" matches "Project A" and "Project A (FEMA)"
             # But "Project A" should not match "Project A Extended" unless "Project A" is the prefix.
             # Given the suffixes are usually in parens, startswith is usually safe.
             
             # Double check: if `sp` is "Test", and fname is "Test 2", `startswith` is True.
             # We should checking if the remainder is empty or starts with " ("?
             remainder = fname[len(sp):]
             if remainder == "" or remainder.startswith(" ("):
                 p_total += int(row['Amount'])
    
    project_funding_details[sp] = p_total
    total_funding += p_total

count = len(started_projects)

print('__RESULT__:')
print(json.dumps({"count": count, "total_funding": total_funding, "details": project_funding_details}))"""

env_args = {'var_function-call-5404665793405674675': ['civic_docs'], 'var_function-call-5404665793405674210': ['Funding'], 'var_function-call-4895478785273924841': 'file_storage/function-call-4895478785273924841.json', 'var_function-call-4895478785273921810': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3486162399230155614': 'file_storage/function-call-3486162399230155614.json', 'var_function-call-6421004180030422518': 'file_storage/function-call-6421004180030422518.json', 'var_function-call-12647426590907445262': [{'name': 'Marie Canyon Green Streets', 'relevant_lines': ['anticipated to have a final design by March 2022. The project will be']}, {'name': 'advertised for construction bids shortly after this date.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'PCH Median Improvements Project', 'relevant_lines': ['project will have final approval by March 2022. The project will be']}, {'name': 'agreement will be sent to City Council in March.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022']}, {'name': 'to review', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'sending this project out to bid during the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'March 2022', 'relevant_lines': ['(cid:131) Begin Design: Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'beginning in April 2022.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': 'started and is anticipated to be completed by the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'assessment district will be created.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) Next public community meeting is scheduled for March 25th.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'within the City.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'construction bids.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'management services was approved by Council on March 14, 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids']}, {'name': 'will begin in conjunction with the PCH Median Improvement', 'relevant_lines': ['(cid:131) Complete Final Design: Spring 2022']}, {'name': 'scheduled for the April 11, 2022 Council meeting.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'relevant_lines': ['go to Council in April 2022 after the Funding Agreement is issued by']}, {'name': 'Metro.', 'relevant_lines': ['(cid:131) Begin Design: Late Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['Proposals are due in April 14, 2022.']}, {'name': 'damaged by the Woolsey Fire.', 'relevant_lines': ['anticipated that the final design will be complete by March 2022. The']}, {'name': 'beginning in Spring 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}], 'var_function-call-10771641254414666451': ['Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Malibu Park Drainage Improvements', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Way Improvements', 'PCH Median Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'PCH Signal Synchronization System Improvements Project', 'Permanent Skate Park', 'Bluffs Park Shade Structure', 'Marie Canyon Green Streets', '2021 Annual Street Maintenance']}

exec(code, env_args)
