code = """import json

with open('var_function-call-396539203064907425', 'r') as f:
    funding_data = json.load(f)

with open('var_function-call-13579578021652581201', 'r') as f:
    docs = json.load(f)

funded_projects = {item['Project_Name'].strip() for item in funding_data}
design_capital_projects = set()

header = 'Capital Improvement Projects (Design)'
terminators = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
skip_prefixes = ['(cid:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:', 'Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Date prepared:', 'Meeting date:']

for doc in docs:
    text = doc.get('text', '')
    if not text: continue
    in_design = False
    for line in text.split(chr(10)):
        s = line.strip()
        if not s: continue
        if s == header:
            in_design = True
            continue
        if in_design:
            is_term = False
            for t in terminators:
                if t in s: is_term = True; break
            if is_term: in_design = False; continue
            should_skip = False
            for p in skip_prefixes:
                if s.startswith(p): should_skip = True; break
            if should_skip: continue
            if len(s) < 5: continue
            design_capital_projects.add(s)

matching = design_capital_projects.intersection(funded_projects)
print('__RESULT__:')
print(json.dumps(len(matching)))"""

env_args = {'var_function-call-396539203064907425': 'file_storage/function-call-396539203064907425.json', 'var_function-call-396539203064906594': 'file_storage/function-call-396539203064906594.json', 'var_function-call-13579578021652581201': 'file_storage/function-call-13579578021652581201.json'}

exec(code, env_args)
