code = """import json
import re

p2 = locals()["var_function-call-633765740054289148"]
with open(p2, "r") as f:
    dl = json.load(f)

# Find latest document
def get_date(filename):
    # expect format ...MMDDYYYY...
    match = re.search(r'(\d{8})', filename)
    if match:
        d = match.group(1)
        # return YYYYMMDD for sorting
        return d[4:] + d[:2] + d[2:4]
    return "00000000"

latest_doc = None
latest_date = "00000000"

for d in dl:
    date_str = get_date(d["filename"])
    if date_str > latest_date:
        latest_date = date_str
        latest_doc = d

print("__RESULT__:")
print(json.dumps({"filename": latest_doc["filename"], "date": latest_date}))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json', 'var_function-call-9077877662949363263': ['malibu canyon road traffic study', 'civic center stormwater diversion structure', 'pch median improvements project', 'westward beach road drainage improvements project', 'latigo canyon road retaining wall repair project', 'malibu bluffs park south walkway repairs', 'pch at trancas canyon road right turn lane', 'outdoor warning signs', 'permanent skate park', 'storm drain master plan'], 'var_function-call-15990990681837136322': [], 'var_function-call-17594359016080085678': [{'Project_Name': 'Clover Heights Storm Drain', 'Amount': '53000'}], 'var_function-call-8434699775002976394': [{'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 343, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 327, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 317, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 371, 'context': ['', '', '', '', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}], 'var_function-call-3536160269563716772': ['Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)'], 'var_function-call-9370289276184492999': [], 'var_function-call-10845941831033251560': ['Found in section: Construction, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Design, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Design, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Construction, Line: Civic Center Stormwater Diversion Structure']}

exec(code, env_args)
