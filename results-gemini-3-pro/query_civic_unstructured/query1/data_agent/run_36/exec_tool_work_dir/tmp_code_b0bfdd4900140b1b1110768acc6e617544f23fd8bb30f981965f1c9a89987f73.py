code = """import json

p1 = locals()["var_function-call-5247396609485473632"]
with open(p1, "r") as f:
    fd = json.load(f)

res = []
for i in fd:
    if "civic center water" in i["Project_Name"].lower():
        res.append(i)
        
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json', 'var_function-call-9077877662949363263': ['malibu canyon road traffic study', 'civic center stormwater diversion structure', 'pch median improvements project', 'westward beach road drainage improvements project', 'latigo canyon road retaining wall repair project', 'malibu bluffs park south walkway repairs', 'pch at trancas canyon road right turn lane', 'outdoor warning signs', 'permanent skate park', 'storm drain master plan'], 'var_function-call-15990990681837136322': [], 'var_function-call-17594359016080085678': [{'Project_Name': 'Clover Heights Storm Drain', 'Amount': '53000'}], 'var_function-call-8434699775002976394': [{'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 343, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 327, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 317, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 371, 'context': ['', '', '', '', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}], 'var_function-call-3536160269563716772': ['Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}

exec(code, env_args)
