code = """import json
import re
from datetime import datetime

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

# Parse docs
project_events = {} # Name -> list of {date: datetime, event: str, date_text: str}

for doc in civic_docs:
    filename = doc['filename']
    # Extract date
    m = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if m:
        doc_date = datetime(int(m.group(3)), int(m.group(1)), int(m.group(2)))
    else:
        continue # Should not happen based on previous list

    text = doc['text']
    lines = text.split(chr(10))
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if line_clean in base_names:
            # Found project
            # Scan context
            context_lines = lines[i+1:i+51]
            
            # Find start dates
            # We want to capture the date string associated with "Begin Construction", "Start", "Advertise"
            
            # Simple line scan
            for l in context_lines:
                l_lower = l.lower()
                
                # Check for year to filter noise
                # But sometimes "Spring" is without year? Usually "Spring 2022".
                if "202" not in l_lower: # 2021, 2022, 2023...
                    continue

                event = None
                if "begin construction" in l_lower or "construction start" in l_lower or "start construction" in l_lower:
                    event = "construction"
                elif "advertise" in l_lower:
                    event = "advertise"
                
                if event:
                    # Extract date string
                    # Heuristic: look for month/season + year
                    date_match = re.search(r'(spring|summer|fall|winter|january|february|march|april|may|june|july|august|september|october|november|december)\s*,?\s*202\d', l_lower)
                    if date_match:
                        date_str = date_match.group(0)
                        if line_clean not in project_events:
                            project_events[line_clean] = []
                        project_events[line_clean].append({
                            "doc_date": doc_date,
                            "event": event,
                            "date_text": date_str
                        })

# Analyze projects
final_started = []

for proj, events in project_events.items():
    # Sort events by doc_date desc
    events.sort(key=lambda x: x['doc_date'], reverse=True)
    
    # We prefer "construction" over "advertise"
    # But we want the LATEST info.
    # If the latest doc has "construction", use it.
    # If the latest doc has "advertise" but no "construction", use it.
    # If the latest doc has nothing, check previous.
    
    # Actually, we group by doc_date.
    # Get the latest doc that has info.
    if not events:
        continue
        
    latest_event_date = events[0]['doc_date']
    latest_events = [e for e in events if e['doc_date'] == latest_event_date]
    
    # Check if we have construction in latest
    const_events = [e for e in latest_events if e['event'] == "construction"]
    adv_events = [e for e in latest_events if e['event'] == "advertise"]
    
    target_event = None
    if const_events:
        target_event = const_events[0]
    elif adv_events:
        target_event = adv_events[0]
    
    # If no event in latest doc (e.g. maybe it just says "Completed" and we didn't capture it)
    # Our `events` list only contains Start/Advertise matches.
    # So `events[0]` IS the latest doc that mentions start/advertise.
    # This is exactly what we want: the latest prediction/record of start.
    
    if target_event:
        d_text = target_event['date_text']
        # Check if Spring 2022 (March, April, May)
        is_spring_2022 = False
        if "2022" in d_text:
            if "spring" in d_text or "march" in d_text or "april" in d_text or "may" in d_text:
                is_spring_2022 = True
        
        if is_spring_2022:
            final_started.append(proj)

# Sum funding
total_funding = 0
details = {}
for proj in final_started:
    p_sum = 0
    for row in funding_data:
        fname = row['Project_Name']
        if fname.startswith(proj):
             remainder = fname[len(proj):]
             if remainder == "" or remainder.startswith(" ("):
                 p_sum += int(row['Amount'])
    details[proj] = p_sum
    total_funding += p_sum

print('__RESULT__:')
print(json.dumps({"count": len(final_started), "total_funding": total_funding, "projects": final_started}))"""

env_args = {'var_function-call-5404665793405674675': ['civic_docs'], 'var_function-call-5404665793405674210': ['Funding'], 'var_function-call-4895478785273924841': 'file_storage/function-call-4895478785273924841.json', 'var_function-call-4895478785273921810': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3486162399230155614': 'file_storage/function-call-3486162399230155614.json', 'var_function-call-6421004180030422518': 'file_storage/function-call-6421004180030422518.json', 'var_function-call-12647426590907445262': [{'name': 'Marie Canyon Green Streets', 'relevant_lines': ['anticipated to have a final design by March 2022. The project will be']}, {'name': 'advertised for construction bids shortly after this date.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'PCH Median Improvements Project', 'relevant_lines': ['project will have final approval by March 2022. The project will be']}, {'name': 'agreement will be sent to City Council in March.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022']}, {'name': 'to review', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'sending this project out to bid during the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'March 2022', 'relevant_lines': ['(cid:131) Begin Design: Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'beginning in April 2022.', 'relevant_lines': ['(cid:131) Begin Construction: April 2022']}, {'name': 'started and is anticipated to be completed by the Spring of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'assessment district will be created.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) Next public community meeting is scheduled for March 25th.', 'relevant_lines': ['(cid:131) Begin Construction: March 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'that was damaged by the Woolsey Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'Fire.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'within the City.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'construction bids.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'management services was approved by Council on March 14, 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022']}, {'name': 'PCH Signal Synchronization System Improvements Project', 'relevant_lines': ['(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids']}, {'name': 'will begin in conjunction with the PCH Median Improvement', 'relevant_lines': ['(cid:131) Complete Final Design: Spring 2022']}, {'name': 'scheduled for the April 11, 2022 Council meeting.', 'relevant_lines': ['(cid:131) Begin Construction: Spring 2022']}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'relevant_lines': ['Commission will then review the project in Spring 2022 before final']}, {'name': 'review by the Council.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'relevant_lines': ['go to Council in April 2022 after the Funding Agreement is issued by']}, {'name': 'Metro.', 'relevant_lines': ['(cid:131) Begin Design: Late Spring 2022']}, {'name': 'is finalizing the bid documents.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022']}, {'name': 'timber with non-combustible materials.', 'relevant_lines': ['(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': '(cid:131) The project consultant has started the design of this project.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}, {'name': 'A kick-off meeting was held in late December.', 'relevant_lines': ['(cid:131) Completion Date: Spring 2022']}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'relevant_lines': ['Proposals are due in April 14, 2022.']}, {'name': 'damaged by the Woolsey Fire.', 'relevant_lines': ['anticipated that the final design will be complete by March 2022. The']}, {'name': 'beginning in Spring 2022.', 'relevant_lines': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'of 2022.', 'relevant_lines': ['(cid:131) Complete Design: Spring 2022']}], 'var_function-call-10771641254414666451': ['Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Malibu Park Drainage Improvements', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Way Improvements', 'PCH Median Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'PCH Signal Synchronization System Improvements Project', 'Permanent Skate Park', 'Bluffs Park Shade Structure', 'Marie Canyon Green Streets', '2021 Annual Street Maintenance'], 'var_function-call-9551949960399857960': {'count': 12, 'total_funding': 546000, 'details': {'Civic Center Stormwater Diversion Structure': 64000, 'Westward Beach Road Improvements Project': 29000, 'Malibu Park Drainage Improvements': 17000, 'PCH at Trancas Canyon Road Right Turn Lane': 90000, 'Civic Center Way Improvements': 37000, 'PCH Median Improvements Project': 56000, 'Civic Center Water Treatment Facility Phase 2': 45000, 'PCH Signal Synchronization System Improvements Project': 16000, 'Permanent Skate Park': 97000, 'Bluffs Park Shade Structure': 21000, 'Marie Canyon Green Streets': 50000, '2021 Annual Street Maintenance': 24000}}, 'var_function-call-3615368124065316708': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}

exec(code, env_args)
