code = """import json

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load paper documents
papers_path = locals()['var_functions.query_db:0']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f'Total papers: {len(papers)}')
print(f'Total citation records: {len(citations)}')

# Get unique paper titles from citations
citation_titles = set()
for citation in citations:
    citation_titles.add(citation['title'])

print(f'Unique papers in citations: {len(citation_titles)}')

# Search for food-related papers more comprehensively
import re

food_papers_detailed = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    
    # Skip if this paper doesn't have any citations (not in citation_titles)
    if title not in citation_titles:
        continue
    
    # Comprehensive food-related patterns
    food_patterns = [
        r'\bfood\b',
        r'\beating\b',
        r'\bdiet\b',
        r'\bdietary\b',
        r'\bnutrition\b',
        r'\bnutritional\b',
        r'\bcalorie\b',
        r'\bcalories\b',
        r'\bmeal\b',
        r'\bmeals\b',
        r'\brestaurant\b',
        r'\brestaurants\b',
        r'\beating habits\b',
        r'\bfood intake\b',
        r'\bdieting\b',
        r'\bweight loss\b',
        r'\bweight management\b',
        r'\bdiet app\b',
        r'\bfood tracking\b',
        r'\bmeal tracking\b'
    ]
    
    found_patterns = []
    for pattern in food_patterns:
        if re.search(pattern, text):
            # Get the actual matched term for reporting
            match = re.search(pattern, text)
            if match:
                found_patterns.append(match.group())
    
    if found_patterns:
        food_papers_detailed.append({
            'title': title,
            'found_terms': list(set(found_patterns)),  # Unique terms
            'term_count': len(set(found_patterns))
        })

print(f'\nFound {len(food_papers_detailed)} papers with food-related terms')

# Show the papers found
for paper in food_papers_detailed:
    print(f"\nPaper: {paper['title']}")
    print(f"  Food terms found: {', '.join(paper['found_terms'])}")

# Get citation counts for these food papers
food_paper_titles = [p['title'] for p in food_papers_detailed]
food_citations = []
total_citations = 0

for citation in citations:
    if citation['title'] in food_paper_titles:
        count = int(citation['citation_count'])
        food_citations.append({
            'title': citation['title'],
            'count': count,
            'year': citation['citation_year']
        })
        total_citations += count

print(f'\nTotal citation records for food papers: {len(food_citations)}')
print(f'Total citation count: {total_citations}')

# Show citation distribution
from collections import defaultdict
citations_by_paper = defaultdict(int)
for citation in food_citations:
    citations_by_paper[citation['title']] += citation['count']

print('\nCitations by paper:')
for title, count in citations_by_paper.items():
    print(f'  {title}: {count}')

result = {
    'food_paper_count': len(food_paper_titles),
    'citation_record_count': len(food_citations),
    'total_citation_count': total_citations,
    'citations_by_paper': dict(citations_by_paper),
    'food_papers': food_papers_detailed
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:12': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:14': {'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'count': 5, 'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keyword': 'food'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keyword': 'food'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keyword': 'eating'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keyword': 'food'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keyword': 'eating'}]}, 'var_functions.execute_python:16': {'food_citations': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}, {'id': '124', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2016'}, {'id': '125', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '9', 'citation_year': '2017'}, {'id': '126', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50', 'citation_year': '2018'}, {'id': '127', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '49', 'citation_year': '2019'}, {'id': '128', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2020'}, {'id': '129', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '60', 'citation_year': '2021'}, {'id': '130', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '68', 'citation_year': '2022'}, {'id': '147', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2019'}, {'id': '148', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98', 'citation_year': '2020'}, {'id': '149', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '23', 'citation_year': '2021'}, {'id': '150', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2022'}, {'id': '151', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '14', 'citation_year': '2023'}, {'id': '293', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '9', 'citation_year': '2017'}, {'id': '294', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '87', 'citation_year': '2018'}, {'id': '295', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '31', 'citation_year': '2019'}, {'id': '296', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '52', 'citation_year': '2020'}, {'id': '297', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '16', 'citation_year': '2021'}, {'id': '298', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '73', 'citation_year': '2022'}, {'id': '299', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '32', 'citation_year': '2023'}, {'id': '300', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '75', 'citation_year': '2024'}, {'id': '301', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '77', 'citation_year': '2025'}, {'id': '392', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '88', 'citation_year': '2011'}, {'id': '393', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '32', 'citation_year': '2012'}, {'id': '394', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '86', 'citation_year': '2013'}, {'id': '395', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '14', 'citation_year': '2014'}], 'total_citation_count': 1593, 'food_paper_count': 5, 'citation_record_count': 31}}

exec(code, env_args)
