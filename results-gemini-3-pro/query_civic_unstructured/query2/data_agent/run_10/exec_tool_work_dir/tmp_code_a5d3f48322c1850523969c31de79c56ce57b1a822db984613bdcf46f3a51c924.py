code = """import json
import re

# Load data
with open(locals()['var_function-call-10742515175370138791'], 'r') as f:
    docs = json.load(f)
with open(locals()['var_function-call-10742515175370139220'], 'r') as f:
    funding_data = json.load(f)

# Map Base Name -> Amount
base_name_map = {}
for record in funding_data:
    raw_name = record['Project_Name']
    amount = int(record['Amount'])
    # Split by '(' to remove suffix
    base_name = raw_name.split('(')[0].strip()
    if base_name not in base_name_map:
        base_name_map[base_name] = []
    base_name_map[base_name].append(amount)

# Combine text
full_text = " ".join([d['text'] for d in docs])
full_text_lower = full_text.lower()

matched_projects = []
total_funding = 0

base_names = list(base_name_map.keys())

for base_name in base_names:
    # Check if base_name is in text
    if base_name.lower() in full_text_lower:
        
        # Check if it is park related
        is_park = False
        if "park" in base_name.lower():
            is_park = True
        
        # We need to find the specific section for this project to check context (park) and completion date
        # Search for the name in text
        # We assume the name is followed by project details
        # We take a chunk of 2000 chars after the name
        
        # Find all occurrences
        start_index = 0
        while True:
            idx = full_text_lower.find(base_name.lower(), start_index)
            if idx == -1:
                break
            
            chunk = full_text_lower[idx:idx+2000]
            
            # Check for park in chunk if not in name
            if not is_park:
                # Check for "park" surrounded by non-alphanumeric (simple boundary check)
                # Or just simple check " park "
                if " park " in chunk or "park." in chunk or "park," in chunk:
                    is_park = True
            
            # Check completion 2022
            # Look for "construction was completed" or "complete construction" and "2022"
            is_complete_2022 = False
            
            # Check strict phrases first
            if "construction was completed" in chunk or "complete construction" in chunk or "notice of completion" in chunk:
                # Find the sentence or line
                # Let's verify if 2022 is near the completion phrase
                # We can split chunk by newlines? The full_text uses " " join, so newlines are gone?
                # Ah! I used " ".join(). So newlines are replaced by spaces.
                # So I can't split by line.
                # I should look for proximity.
                # Say within 100 chars.
                
                # Regex for "completed ... 2022"
                # raw string for regex
                if re.search(r'(construction was completed|complete construction|notice of completion).{0,100}2022', chunk):
                    is_complete_2022 = True
            
            if is_park and is_complete_2022:
                # Found a valid match
                proj_sum = sum(base_name_map[base_name])
                # avoid double counting if multiple occurrences found for same project
                # check if base_name already in matched_projects
                already_added = False
                for p in matched_projects:
                    if p['name'] == base_name:
                        already_added = True
                        break
                if not already_added:
                    matched_projects.append({"name": base_name, "amount": proj_sum})
                    total_funding += proj_sum
                break # Move to next base_name
            
            start_index = idx + 1

print("__RESULT__:")
print(json.dumps({"projects": matched_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-10742515175370138791': 'file_storage/function-call-10742515175370138791.json', 'var_function-call-10742515175370139220': 'file_storage/function-call-10742515175370139220.json', 'var_function-call-18198930664493974192': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City '}

exec(code, env_args)
