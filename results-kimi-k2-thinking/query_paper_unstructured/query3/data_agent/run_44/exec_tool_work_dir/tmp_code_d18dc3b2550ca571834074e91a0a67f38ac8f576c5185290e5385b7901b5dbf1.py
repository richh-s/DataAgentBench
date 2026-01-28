code = """import json

# Load citations to see all unique paper titles
citations_path = locals()['var_functions.query_db:5']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Get unique titles from citations
unique_titles = set()
for cite in citations:
    unique_titles.add(cite['title'])

# Count citations per title
citation_counts = {}
for cite in citations:
    title = cite['title']
    if title not in citation_counts:
        citation_counts[title] = 0
    citation_counts[title] += int(cite['citation_count'])

# Sort by citation count
top_cited = sorted(citation_counts.items(), key=lambda x: x[1], reverse=True)

# Show all unique titles
result = {
    'total_unique_titles': len(unique_titles),
    'total_citation_records': len(citations),
    'all_titles': list(unique_titles),
    'top_cited': top_cited[:20]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}, 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'filtered_results': [], 'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 'unknown', 'contribution': [], 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 'unknown', 'contribution': [], 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 'unknown', 'contribution': [], 'citations': 452}]}, 'var_functions.execute_python:28': [], 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:34': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year_found': 'venue_pattern', 'year': 2015, 'has_empirical': False, 'meets_criteria': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year_found': 'copyright', 'year': 2010, 'has_empirical': False, 'meets_criteria': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'meets_criteria': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_found': 'venue_pattern', 'year': 2014, 'has_empirical': True, 'meets_criteria': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_found': 'venue_pattern', 'year': 2011, 'has_empirical': False, 'meets_criteria': False}]}

exec(code, env_args)
