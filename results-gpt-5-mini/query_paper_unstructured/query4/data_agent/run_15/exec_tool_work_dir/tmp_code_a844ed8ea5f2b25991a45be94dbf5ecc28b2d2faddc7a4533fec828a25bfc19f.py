code = """import json
# Load the previous python result from storage
with open(var_call_Mg0DhyZ8Yl6EfH8SYYYG3Nzz, 'r', encoding='utf-8') as f:
    res = json.load(f)

# For clarity, produce a simple mapping of title -> total_citations
out = {r['title']: r['total_citations'] for r in res}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wQdnI6hks6T5yZhIQVRwTx5I': ['paper_docs'], 'var_call_4boCUXjDl1lUc9qc07KOWzez': ['Citations', 'sqlite_sequence'], 'var_call_aZURe3TkzDmxJKgkobkFzbj7': 'file_storage/call_aZURe3TkzDmxJKgkobkFzbj7.json', 'var_call_HbYVb9be9FWKtOodjttq4c7I': 'file_storage/call_HbYVb9be9FWKtOodjttq4c7I.json', 'var_call_Mg0DhyZ8Yl6EfH8SYYYG3Nzz': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': 264}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': 259}, {'title': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'total_citations': 55}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': 362}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'total_citations': 449}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': 133}, {'title': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'total_citations': 139}, {'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'total_citations': 271}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': 335}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': 404}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': 191}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': 278}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citations': 72}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'total_citations': 143}]}

exec(code, env_args)
