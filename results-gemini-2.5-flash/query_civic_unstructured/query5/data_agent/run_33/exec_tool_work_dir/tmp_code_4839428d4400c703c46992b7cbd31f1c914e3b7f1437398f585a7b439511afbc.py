code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-11720092496161089352'], 'r') as f:
    funding_project_names_raw = json.load(f)

funding_project_names = [item['Project_Name'] for item in funding_project_names_raw]

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Iterate through known project names and search for them in the document
    for project_name in funding_project_names:
        # Look for the project name and then check its context for 'Disaster Recovery Projects' and '2022'
        # We need to consider that the project type and date information might not be on the same line
        
        # Find all occurrences of the project name in the text
        for match in re.finditer(re.escape(project_name), text):
            start_index = match.start()
            end_index = match.end()
            
            # Define a window around the project name to search for relevant keywords
            # Look before and after the project name for context
            context_start = max(0, start_index - 500) # Look back 500 characters
            context_end = min(len(text), end_index + 500) # Look forward 500 characters
            
            context = text[context_start:context_end]
            
            if "Disaster Recovery Projects" in context and "2022" in context:
                # Further refine the search for 2022 within the schedule context of the project
                # Look for '2022' specifically in lines indicating schedule or start dates near the project name
                
                # Find the relevant section around the project name
                project_section_match = re.search(r'(?s)([A-Z][A-Za-z0-9&, -]+\s*(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?).*?)(?=(?:[A-Z][A-Za-z0-9&, -]+\s*(?:Project|Improvements|Study|Plan)|Capital Improvement Projects|Disaster Recovery Projects)|$)', text[context_start:context_end])
                
                if project_section_match:
                    project_section_text = project_section_match.group(0)
                    
                    # Look for 2022 in schedule/start date related keywords within this section
                    if re.search(r'2022.*?(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|st:|Date prepared:|Complete Design|Start Date)', project_section_text, re.IGNORECASE):
                        disaster_projects_2022.append(project_name)
                        break # Move to the next project name once found in a document

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'var_function-call-6360808465177343412': 'file_storage/function-call-6360808465177343412.json', 'var_function-call-11720092496161089352': 'file_storage/function-call-11720092496161089352.json'}

exec(code, env_args)
