code = """import json

# Load both datasets
file_path_papers = locals()['var_functions.execute_python:6']
file_path_citations = locals()['var_functions.query_db:14']

papers_data = None
citations_data = None

# Load papers data (2016 physical activity papers data)
with open(file_path_papers, 'r') as f:
    papers_data = json.load(f)

# Load citations data
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

# Create a mapping of title to total citations
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = int(item['total_citations'])

# The physical activity papers from 2016
pa_papers = papers_data['titles']

# Match citations and prepare results
results = []
for title in pa_papers:
    citation_count = citation_map.get(title, 0)
    results.append({
        'title': title,
        'total_citations': citation_count
    })

# Sort by citation count (descending)
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Prepare final output
output = {
    'physical_activity_papers_2016': results_sorted,
    'summary': {
        'total_papers': len(results_sorted),
        'total_citations': sum([r['total_citations'] for r in results_sorted])
    }
}

# Print in required format
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'num_2016_pa_papers': 13, 'titles': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'Personal Tracking of Screen Time on Digital Devices', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity'], 'all_2016_titles': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'Personal Tracking of Screen Time on Digital Devices', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity']}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
