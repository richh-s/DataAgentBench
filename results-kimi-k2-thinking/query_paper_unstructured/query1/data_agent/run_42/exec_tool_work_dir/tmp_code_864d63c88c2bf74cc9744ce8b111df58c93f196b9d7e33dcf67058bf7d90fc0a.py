code = """import json
import re

# Load the citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load the paper documents
papers_path = locals()['var_functions.query_db:0']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Get all unique paper titles from citations
citation_papers = {}
for citation in citations:
    title = citation['title']
    if title not in citation_papers:
        citation_papers[title] = []
    citation_papers[title].append(citation)

print('Unique papers with citations: ' + str(len(citation_papers)))

# Find food domain papers by examining content more carefully
food_domain_papers = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    
    # Only process papers that have citation records
    if title not in citation_papers:
        continue
    
    text_lower = text.lower()
    
    # More sophisticated approach: look for explicit domain indicators
    # Check if paper focuses on food/eating as a primary topic
    
    # Indicators that this is actually a food domain paper:
    food_indicators = []
    
    # 1. Title contains food-related terms
    title_lower = title.lower()
    if any(term in title_lower for term in ['food', 'diet', 'eating', 'nutrition']):
        food_indicators.append('title_food_term')
    
    # 2. Abstract/intro mentions food as the studied domain
    # Look for phrases that indicate food is the primary domain
    food_phrases = [
        r'study.*food',
        r'food.*track',
        r'food.*journal',
        r'food.*intake',
        r'eat.*habit',
        r'diet.*track',
        r'weight.*loss',
        r'weight.*management'
    ]
    
    for phrase in food_phrases:
        if re.search(phrase, text_lower):
            food_indicators.append('food_phrase')
            break
    
    # 3. Count food-related term frequency
    food_terms = ['food', 'eating', 'diet', 'dietary', 'nutrition', 'calorie', 'meal']
    food_term_count = sum(text_lower.count(term) for term in food_terms)
    
    if food_term_count >= 5:  # If mentioned multiple times, likely food domain
        food_indicators.append('multiple_mentions')
    
    # Consider it a food paper if it has multiple indicators
    if len(food_indicators) >= 2 or (len(food_indicators) == 1 and food_term_count >= 10):
        food_domain_papers.append({
            'title': title,
            'indicators': food_indicators,
            'food_term_count': food_term_count
        })

print('\nFood domain papers found: ' + str(len(food_domain_papers)))
for paper in food_domain_papers:
    print('  ' + paper['title'] + ' - ' + str(paper['indicators']))

# Calculate total citations for food papers
food_paper_titles = [p['title'] for p in food_domain_papers]
food_citations_list = []
total_citation_count = 0

for title in food_paper_titles:
    for citation in citation_papers[title]:
        count = int(citation['citation_count'])
        food_citations_list.append(citation)
        total_citation_count += count

result = {
    'food_paper_count': len(food_paper_titles),
    'citation_record_count': len(food_citations_list),
    'total_citation_count': total_citation_count,
    'food_papers': food_domain_papers
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:12': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:14': {'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'count': 5, 'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keyword': 'food'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keyword': 'food'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keyword': 'eating'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keyword': 'food'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keyword': 'eating'}]}, 'var_functions.execute_python:16': {'food_citations': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}, {'id': '124', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2016'}, {'id': '125', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '9', 'citation_year': '2017'}, {'id': '126', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50', 'citation_year': '2018'}, {'id': '127', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '49', 'citation_year': '2019'}, {'id': '128', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2020'}, {'id': '129', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '60', 'citation_year': '2021'}, {'id': '130', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '68', 'citation_year': '2022'}, {'id': '147', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2019'}, {'id': '148', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98', 'citation_year': '2020'}, {'id': '149', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '23', 'citation_year': '2021'}, {'id': '150', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2022'}, {'id': '151', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '14', 'citation_year': '2023'}, {'id': '293', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '9', 'citation_year': '2017'}, {'id': '294', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '87', 'citation_year': '2018'}, {'id': '295', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '31', 'citation_year': '2019'}, {'id': '296', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '52', 'citation_year': '2020'}, {'id': '297', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '16', 'citation_year': '2021'}, {'id': '298', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '73', 'citation_year': '2022'}, {'id': '299', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '32', 'citation_year': '2023'}, {'id': '300', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '75', 'citation_year': '2024'}, {'id': '301', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '77', 'citation_year': '2025'}, {'id': '392', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '88', 'citation_year': '2011'}, {'id': '393', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '32', 'citation_year': '2012'}, {'id': '394', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '86', 'citation_year': '2013'}, {'id': '395', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '14', 'citation_year': '2014'}], 'total_citation_count': 1593, 'food_paper_count': 5, 'citation_record_count': 31}, 'var_functions.execute_python:22': {'food_paper_count': 0, 'citation_record_count': 0, 'total_citation_count': 0}}

exec(code, env_args)
