code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-10742515175370138791'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-10742515175370139220'], 'r') as f:
    funding_data = json.load(f)

# 1. Process Funding Data to get Base Names
base_name_map = {} # Base_Name -> list of amounts

for record in funding_data:
    raw_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Remove (...) suffixes
    base_name = re.sub(r'\s*\(.*?\)\s*$', '', raw_name).strip()
    
    if base_name not in base_name_map:
        base_name_map[base_name] = []
    base_name_map[base_name].append(amount)

# 2. Combine text from all docs
full_text = "\n".join([d['text'] for d in docs])

# 3. Search for Base Names in text and validate
total_funding = 0
matched_projects = []

for base_name in base_name_map.keys():
    # Find the project section in the text
    # We look for the name followed by newlines and potentially "(cid:190)" or other indicators
    # To be robust, we find the name, and take the text until the next known base name or a reasonable limit.
    
    # Simple finding:
    # We'll look for the name on a line by itself or close to it.
    # Regex: \n\s*base_name\s*\n
    pattern = re.compile(re.escape(base_name), re.IGNORECASE)
    
    # Find all occurrences
    matches = list(pattern.finditer(full_text))
    
    is_park_project = False
    is_completed_2022 = False
    
    # Check if "park" is in the name
    if "park" in base_name.lower():
        is_park_project = True
    
    for match in matches:
        start_idx = match.end()
        # Extract a chunk of text after the name (e.g., 2000 chars)
        chunk = full_text[start_idx:start_idx+2000]
        
        # Stop chunk at next project header if possible? 
        # Hard to determine next header. 2000 chars is usually enough for a summary.
        # But we should stop at the start of another base name if it's closer.
        # Optimization: Just process the chunk.
        
        # Check topic in text if not already found
        if not is_park_project:
            # Check for "park" in the first few lines of the chunk? 
            # Or "topic" keywords. 
            # Let's search entire chunk.
            if "park" in chunk.lower():
                is_park_project = True
        
        # Check completion status
        # We need "Complete Construction" or "Construction was completed" associated with 2022
        
        # Regex for completion
        # Patterns based on preview:
        # "Complete Construction: [Season/Month] 2022"
        # "Construction was completed [Month] 2022"
        # "Notice of completion filed [Month] 2022" -> Completion likely 2021 or 2022. 
        # If Notice is Jan 2023, completion was Nov 2022.
        
        chunk_lower = chunk.lower()
        
        # Check for 2022 completion
        # 1. "complete construction: ... 2022"
        # 2. "construction was completed ... 2022"
        
        # We also need to ensure we don't pick up "Summer 2023"
        
        # Let's extract completion sentences
        completion_sentences = re.findall(r"(?:complete construction|construction was completed)[^.\n]*", chunk_lower)
        
        for sent in completion_sentences:
            if "2022" in sent:
                is_completed_2022 = True
                break
        
        if is_completed_2022:
            break
            
    # If matches criteria
    if is_park_project and is_completed_2022:
        project_total = sum(base_name_map[base_name])
        total_funding += project_total
        matched_projects.append({
            "name": base_name,
            "amount": project_total
        })

print("__RESULT__:")
print(json.dumps(matched_projects))"""

env_args = {'var_function-call-10742515175370138791': 'file_storage/function-call-10742515175370138791.json', 'var_function-call-10742515175370139220': 'file_storage/function-call-10742515175370139220.json', 'var_function-call-18198930664493974192': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City '}

exec(code, env_args)
