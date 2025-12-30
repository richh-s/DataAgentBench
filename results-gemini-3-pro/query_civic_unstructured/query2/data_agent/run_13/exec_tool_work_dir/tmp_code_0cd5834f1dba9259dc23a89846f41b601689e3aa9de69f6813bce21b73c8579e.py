code = """import json

civic_path = locals()['var_function-call-18353548758763023349']
civic_docs = json.load(open(civic_path))
newline = chr(10)
full_text = newline.join([doc['text'] for doc in civic_docs])

found = False
context = ""
if "Legacy Park" in full_text:
    found = True
    start = full_text.find("Legacy Park")
    context = full_text[start:start+500]

print("__RESULT__:")
print(json.dumps({"found": found, "context": context}))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json', 'var_function-call-17154176344544213090': {'total_funding': 214000, 'matched_projects': [{'name': 'Marie Canyon Green Streets', 'amount': '50000', 'extracted_name': 'Marie Canyon Green Streets'}, {'name': 'Birdview Avenue Improvements', 'amount': '79000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'amount': '85000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}], 'extracted_park_projects': ['Marie Canyon Green Streets', 'Metro.', 'Birdview Avenue Improvements (CalOES Project)', '(cid:190) Updates: Project is currently under construction']}, 'var_function-call-6018647821410521570': {'total_funding': 21000, 'matched_projects': [{'name': 'Bluffs Park Shade Structure', 'amount': '21000', 'extracted_name': 'Bluffs Park Shade Structure'}], 'extracted_park_projects': ['Bluffs Park Shade Structure']}, 'var_function-call-5450632830697920529': 'file_storage/function-call-5450632830697920529.json'}

exec(code, env_args)
