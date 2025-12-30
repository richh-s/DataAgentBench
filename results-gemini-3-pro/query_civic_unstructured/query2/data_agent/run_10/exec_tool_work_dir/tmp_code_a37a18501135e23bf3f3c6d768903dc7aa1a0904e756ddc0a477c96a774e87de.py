code = """import json
import re

# Load data
with open(locals()['var_function-call-10742515175370138791'], 'r') as f:
    docs = json.load(f)
with open(locals()['var_function-call-10742515175370139220'], 'r') as f:
    funding_data = json.load(f)

# 1. Identify Park Candidates from Funding Data
park_keywords = ["park", "playground", "recreation", "skate", "bench", "arbor"] # Added bench/arbor for Legacy Park
park_candidates = {}

for record in funding_data:
    raw_name = record['Project_Name']
    # Check keyword in name
    if any(k in raw_name.lower() for k in park_keywords):
        base_name = raw_name.split('(')[0].strip()
        if base_name not in park_candidates:
            park_candidates[base_name] = []
        park_candidates[base_name].append(int(record['Amount']))

# 2. Check Status in Text
full_text = "\n".join([d['text'] for d in docs])
# We keep newlines to handle line-based parsing

confirmed_projects = []

for base_name in park_candidates.keys():
    # Find base_name in text
    # Regex to find name as a header (roughly)
    # or just find the string
    
    # We want to see the status lines.
    # Let's find the name and print the next 500 chars
    
    pattern = re.escape(base_name)
    matches = list(re.finditer(pattern, full_text, re.IGNORECASE))
    
    for match in matches:
        start = match.end()
        chunk = full_text[start:start+1000] # 1000 chars context
        
        # Look for completion
        # Patterns:
        # "Construction was completed,? [Month] [Year]"
        # "Complete Construction: [Season] [Year]"
        
        # We extract lines containing "completed" or "complete construction"
        relevant_lines = []
        lines = chunk.split('\n')
        for line in lines:
            line_lower = line.lower()
            if "construction" in line_lower and ("completed" in line_lower or "complete" in line_lower):
                relevant_lines.append(line.strip())
            if "notice of completion" in line_lower:
                relevant_lines.append(line.strip())
        
        # Analyze relevant lines for 2022
        is_2022 = False
        for line in relevant_lines:
            # Check if 2022 is in the line
            if "2022" in line:
                # Exclude if it says "Start: 2022" (but we filtered for construction complete)
                # Exclude if it says "2023" (e.g. "2022-2023")
                # But "November 2022" is good.
                # "Summer 2023" -> Has 2023.
                
                # Logic: If 2023 is present, likely not completed in 2022 (unless it says "Started 2022, Finished 2023")
                # If "Completed ... 2022", it's good.
                if "2023" not in line:
                    is_2022 = True
                else:
                    # Check if 2022 is the completion year
                    # e.g. "Complete Construction: Summer 2023" -> No
                    # "Construction completed 2022. Notice 2023." -> Yes.
                    if "construction was completed" in line.lower() and "2022" in line:
                         is_2022 = True
                    elif "complete construction" in line.lower() and "2022" in line:
                         # e.g. "Complete Construction: 2022"
                         is_2022 = True
        
        if is_2022:
            # Add to list
            # Verify manually via print
            confirmed_projects.append({
                "name": base_name,
                "amount": sum(park_candidates[base_name]),
                "snippet": relevant_lines
            })
            break # Found match for this project

print("__RESULT__:")
print(json.dumps(confirmed_projects))"""

env_args = {'var_function-call-10742515175370138791': 'file_storage/function-call-10742515175370138791.json', 'var_function-call-10742515175370139220': 'file_storage/function-call-10742515175370139220.json', 'var_function-call-18198930664493974192': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City ', 'var_function-call-12067474679721807017': {'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Bluffs Park South Walkway', 'amount': 91000}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'amount': 81000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 81000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}, {'name': 'Trancas Canyon Park Playground', 'amount': 24000}], 'total_funding': 493000}}

exec(code, env_args)
