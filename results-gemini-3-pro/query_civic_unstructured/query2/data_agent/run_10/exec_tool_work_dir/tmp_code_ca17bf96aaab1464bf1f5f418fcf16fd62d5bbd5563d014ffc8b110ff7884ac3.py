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
    # Regex: remove (suffix)
    # Use raw string for regex pattern
    base_name = re.sub(r'\s*\(.*?\)\s*$', '', raw_name).strip()
    if base_name not in base_name_map:
        base_name_map[base_name] = []
    base_name_map[base_name].append(amount)

full_text = "\n".join([d['text'] for d in docs])

matched_projects = []
total_funding = 0

# Get list of base names
base_names = list(base_name_map.keys())

for base_name in base_names:
    # Find base_name in text
    safe_name = re.escape(base_name)
    # Search for name
    matches = list(re.finditer(safe_name, full_text, re.IGNORECASE))
    
    is_park = False
    is_complete_2022 = False
    
    # Check name for "park" (whole word check or just substring? Park is usually a substring like "Trancas Canyon Park")
    if "park" in base_name.lower():
        is_park = True
        
    for match in matches:
        start = match.end()
        # Look ahead 2000 chars
        chunk = full_text[start:start+2000].lower()
        
        # Check topic in text
        if not is_park:
            # Check for "park" as whole word to avoid "parking"
            if re.search(r'\bpark\b', chunk):
                is_park = True
                
        # Check completion
        lines = chunk.split('\n')
        for line in lines[:30]: # Check first 30 lines
            # Check for completion keywords
            if ("construction" in line and ("completed" in line or "complete" in line)) or \
               ("notice of completion" in line):
                if "2022" in line:
                    is_complete_2022 = True
    
    if is_park and is_complete_2022:
        proj_sum = sum(base_name_map[base_name])
        # Check if already added? No, we iterate base_names which are unique.
        total_funding += proj_sum
        matched_projects.append({"name": base_name, "amount": proj_sum})

print("__RESULT__:")
print(json.dumps({"projects": matched_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-10742515175370138791': 'file_storage/function-call-10742515175370138791.json', 'var_function-call-10742515175370139220': 'file_storage/function-call-10742515175370139220.json', 'var_function-call-18198930664493974192': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City '}

exec(code, env_args)
