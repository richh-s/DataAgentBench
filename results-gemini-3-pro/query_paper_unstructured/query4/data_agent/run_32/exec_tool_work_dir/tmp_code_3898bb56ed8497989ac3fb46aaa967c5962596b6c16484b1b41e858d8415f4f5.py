code = """import json

paper_docs_path = locals()['var_function-call-14925158578354177648']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

snippets = []
for doc in paper_docs:
    snippets.append(f"--- {doc['filename']} ---\n{doc['text'][:500]}\n")

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-1637384971147103697': ['paper_docs'], 'var_function-call-1637384971147100208': ['Citations', 'sqlite_sequence'], 'var_function-call-12832305372190774842': 'file_storage/function-call-12832305372190774842.json', 'var_function-call-8891803198092466496': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-15218699156222790202': 5, 'var_function-call-14925158578354177648': 'file_storage/function-call-14925158578354177648.json', 'var_function-call-15838681542065948214': 'file_storage/function-call-15838681542065948214.json', 'var_function-call-1830984539435977228': [], 'var_function-call-4415673637431539251': [{'title': 'A Lived Informatics Model of Personal Informatics', 'years_found': [2015], 'has_physical_activity': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'years_found': [], 'has_physical_activity': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years_found': [], 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years_found': [], 'has_physical_activity': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'years_found': [], 'has_physical_activity': False}]}

exec(code, env_args)
