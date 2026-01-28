code = """import json

with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations = json.load(f)

titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "limit": 1000
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True, 'var_function-call-13779047879887923666': True, 'var_function-call-8236464070197401554': {'count': 5, 'avg': 67.8}, 'var_function-call-709801467346895870': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_function-call-17697871091250765431': '', 'var_function-call-15344622579435763101': {'total': 5, 'empty': 0}}

exec(code, env_args)
