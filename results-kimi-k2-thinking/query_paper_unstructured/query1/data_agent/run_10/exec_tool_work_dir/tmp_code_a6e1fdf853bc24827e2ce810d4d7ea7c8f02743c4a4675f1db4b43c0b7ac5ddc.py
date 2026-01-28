code = """import json

# Get paper_info from previous step
paper_info = locals()['var_functions.execute_python:10']['paper_info']

# Get the citations data file from the previous query
citations_file = locals()['var_functions.query_db:14']

# Load citations data
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print(f'Total citation records: {len(citations_data)}')

# Create a set of food domain paper titles for quick lookup
food_titles = set()
for paper in paper_info:
    if 'food' in paper['domains']:
        food_titles.add(paper['title'])

print(f'Food domain papers found: {len(food_titles)}')
print(f'Food domain paper titles: {list(food_titles)}')

# Filter citations for food domain papers and sum citation counts
total_citations = 0
food_citations = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    if citation_title in food_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        food_citations.append({
            'title': citation_title,
            'citation_year': citation.get('citation_year'),
            'citation_count': count
        })

print(f'Total food domain citations: {total_citations}')
print(f'Food citations records: {len(food_citations)}')

# Sort by citation count to see distribution
food_citations_sorted = sorted(food_citations, key=lambda x: x['citation_count'], reverse=True)
print('Top food citation records:')
for rec in food_citations_sorted[:10]:
    print(f"  {rec}")

result = {
    'food_titles': len(food_titles),
    'food_citation_records': len(food_citations),
    'total_citation_count': total_citations,
    'details': food_citations_sorted
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_papers': 5, 'food_papers_count': 3, 'paper_info': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['food', 'physical activity', 'mental', 'finances', 'social interactions', 'location', 'chronic', 'health_behavior']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['food', 'physical activity', 'sleep', 'finances', 'productivity', 'location', 'diabetes']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['physical activity', 'sleep', 'mental', 'social interactions']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'domains': ['food', 'physical activity', 'mental', 'productivity', 'social interactions', 'location', 'chronic']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'domains': ['physical activity', 'sleep', 'mental', 'location', 'chronic']}]}, 'var_functions.query_db:12': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
