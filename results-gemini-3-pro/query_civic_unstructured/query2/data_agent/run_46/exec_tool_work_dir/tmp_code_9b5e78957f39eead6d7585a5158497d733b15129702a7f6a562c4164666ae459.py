code = """import json
import re

# Load data
with open(locals()['var_function-call-14713834321312381364'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-14713834321312381855'], 'r') as f:
    civic_docs = json.load(f)
full_text = " ".join([doc.get('text', '') for doc in civic_docs])

# Find all potential park projects and check if completed in 2022
matches = []

for p in funding_data:
    name = p['Project_Name']
    # expanded keywords
    if any(k in name.lower() for k in ['park', 'beach', 'creek', 'trail', 'walkway', 'recreation', 'playground']):
        # check status in text
        starts = [m.start() for m in re.finditer(re.escape(name), full_text)]
        for start in starts:
            chunk = full_text[start:start+1000].lower()
            if "completed" in chunk and "2022" in chunk:
                 # verify it's not "design completed"
                 if re.search(r"construction\s+was\s+completed", chunk) or re.search(r"project\s+was\s+completed", chunk) or "notice of completion" in chunk:
                     matches.append(p)
                     break

print("__RESULT__:")
print(json.dumps([m['Project_Name'] for m in matches]))"""

env_args = {'var_function-call-14713834321312381364': 'file_storage/function-call-14713834321312381364.json', 'var_function-call-14713834321312381855': 'file_storage/function-call-14713834321312381855.json', 'var_function-call-14503968957198369253': {'matched_projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}, 'var_function-call-17804470175278883708': 'file_storage/function-call-17804470175278883708.json', 'var_function-call-9609312173957712810': {'Bluffs Park Shade Structure': {'amount': '21000', 'status_found': 'Completed 2022 (Maybe)', 'snippet': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Cou'}, 'Legacy Park Benches and Arbors Renovation': {'amount': '41000', 'status_found': 'No'}, 'Legacy Park Paver Repair Project': {'amount': '69000', 'status_found': 'No'}, 'Malibu Bluffs Park Roof Replacement Project': {'amount': '44000', 'status_found': 'No'}, 'Point Dume Walkway Repairs': {'amount': '59000', 'status_found': 'Completed 2022 (Maybe)', 'snippet': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was i'}, 'Trancas Canyon Park Planting and Irrigation Repairs': {'amount': '78000', 'status_found': 'No'}, 'Trancas Canyon Park Playground': {'amount': '24000', 'status_found': 'No'}}}

exec(code, env_args)
