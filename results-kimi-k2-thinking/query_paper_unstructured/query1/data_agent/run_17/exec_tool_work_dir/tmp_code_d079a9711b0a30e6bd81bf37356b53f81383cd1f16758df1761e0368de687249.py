code = """import json

# Load citations data
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Find all论文 titles that are clearly food-related from the citations database
food_titles_in_citations = []

for record in citations_data:
    title = record['title'].lower()
    # Check if title contains food-related keywords
    food_keywords_in_title = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary', 'nutrition tracking']
    
    for keyword in food_keywords_in_title:
        if keyword in title:
            food_titles_in_citations.append(record['title'])
            break

print(f"Found {len(food_titles_in_citations)} food-related papers in citations database:")
for i, title in enumerate(sorted(set(food_titles_in_citations)), 1):
    print(f"{i}. {title}")

# Group by title and sum citations
food_title_citations = {}
for record in citations_data:
    title = record['title']
    if title in food_titles_in_citations:
        citations = int(record['total_citations'])
        if title not in food_title_citations:
            food_title_citations[title] = 0
        food_title_citations[title] = citations  # Use the total_citations from the grouped query

print(f"\nTotal food papers: {len(food_title_citations)}")

# Calculate total citations
total_citations = sum(food_title_citations.values())

result = {
    'food_papers_count': len(food_title_citations),
    'total_citation_count': total_citations,
    'food_papers_and_citations': food_title_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'food_papers_count': 5, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_food_papers': 5, 'food_papers_with_citations': 5, 'total_citation_count': 1593, 'food_citation_details': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 452}]}, 'var_functions.execute_python:16': {'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'count': 4}}

exec(code, env_args)
