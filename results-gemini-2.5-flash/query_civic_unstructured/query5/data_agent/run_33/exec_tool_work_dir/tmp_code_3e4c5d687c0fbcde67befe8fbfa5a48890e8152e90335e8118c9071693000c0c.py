code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-12198994683327414611'], 'r') as f:
    funding_project_names_raw = json.load(f)

funding_project_names = [item['Project_Name'] for item in funding_project_names_raw]

disaster_projects_2022 = set() # Use a set to store unique project names

for doc in civic_docs:
    text = doc['text']
    
    for project_name in funding_project_names:
        # Look for the project name in the document
        if project_name in text:
            # Define a search window around the project name to find 'Disaster Recovery Projects' and '2022'
            # This avoids parsing the entire document with complex state machines for sections
            
            # Find all occurrences of the project name
            for match in re.finditer(re.escape(project_name), text):
                start_idx = max(0, match.start() - 500) # Look back 500 characters
                end_idx = min(len(text), match.end() + 500) # Look forward 500 characters
                
                context = text[start_idx:end_idx]
                
                # Check for 'Disaster Recovery Projects' and a 2022 date within the context
                if "Disaster Recovery Projects" in context:
                    # Now check more specifically for 2022 within a schedule context
                    # This regex looks for 2022 near common schedule keywords
                    if re.search(r'2022.*?(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|st:|Date prepared:|Complete Design|Start Date)', context, re.IGNORECASE | re.DOTALL) or \
                       re.search(r'(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|st:|Date prepared:|Complete Design|Start Date).*?2022', context, re.IGNORECASE | re.DOTALL):
                        disaster_projects_2022.add(project_name)
                        break # Move to the next project_name once found in this document

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'var_function-call-6360808465177343412': 'file_storage/function-call-6360808465177343412.json', 'var_function-call-11720092496161089352': 'file_storage/function-call-11720092496161089352.json', 'var_function-call-12198994683327414611': 'file_storage/function-call-12198994683327414611.json'}

exec(code, env_args)
