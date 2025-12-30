code = """import json

# Load citations
with open(locals()['var_function-call-15646429060027290344'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "limit": 300  # Set a limit higher than 188 to be safe
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-173807103424142885': ['Citations', 'sqlite_sequence'], 'var_function-call-173807103424140732': ['paper_docs'], 'var_function-call-173807103424142675': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-173807103424140522': 'file_storage/function-call-173807103424140522.json', 'var_function-call-17670429279864850901': [{'COUNT(*)': '188'}], 'var_function-call-5884279522157261639': 'file_storage/function-call-5884279522157261639.json', 'var_function-call-15646429060027290344': 'file_storage/function-call-15646429060027290344.json', 'var_function-call-6914183761872541415': 'file_storage/function-call-6914183761872541415.json', 'var_function-call-14650497424767224127': 0, 'var_function-call-12560711107649030866': {'num_citations': 188, 'num_papers': 5, 'num_intersection': 4, 'sample_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Stage-based Model of Personal Informatics Systems', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_citation_titles': ['Why We Use and Abandon Smart Devices', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care', 'Predicting About-to-Eat Moments for Just-in-Time Eating Intervention', 'A Family Health App: Engaging Children to Manage Wellness of Adults']}}

exec(code, env_args)
