code = """import json

with open(locals()['var_function-call-4403390195297864469'], 'r') as f:
    docs = json.load(f)

doc = docs[0]
text = doc['text'].lower()

print("__RESULT__:")
print(json.dumps({
    "has_empirical": "empirical" in text,
    "has_survey": "survey" in text,
    "has_interview": "interview" in text,
    "has_study": "study" in text
}))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json'}

exec(code, env_args)
