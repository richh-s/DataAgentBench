code = """import json

# Read the MongoDB query result
with open('/tmp/tmp_result_2.json', 'r') as f:
    papers = json.load(f)

# Let's see how many papers we have and inspect a few
print(f"Total papers: {len(papers)}")
print("\nFirst 3 papers:")
for i, paper in enumerate(papers[:3]):
    print(f"Paper {i+1}:")
    print(f"  Filename: {paper['filename']}")
    print(f"  Text snippet: {paper['text'][:200]}...")
    print()

# Let's check if we can identify domains in the text
# Based on the hint, common domains include: "food", "physical activity", "sleep", "mental", etc.

# Let's search for domain mentions in the text
food_papers = []
for paper in papers:
    text = paper['text'].lower()
    # Check if 'food' appears in the text
    if ' food ' in text or '\nfood\n' in text or ',food' in text or 'food,' in text:
        food_papers.append(paper)

print(f"\nPotential food papers found: {len(food_papers)}")
for i, paper in enumerate(food_papers[:5]):
    print(f"  {i+1}. {paper['filename']}")

# Pass data to next step
result = {
    'total_papers': len(papers),
    'food_papers_count': len(food_papers),
    'food_papers': food_papers[:10]  # Sample for inspection
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
