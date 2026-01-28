code = """import json
import re

# Load all papers from MongoDB
papers_file = locals()['var_functions.query_db:10']
papers = []
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load all citations from SQLite
citations_file = locals()['var_functions.query_db:5']
citations = []
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract domain information from papers
paper_domains = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '').lower()
    
    # Check if this is a food domain paper
    # Look for direct mention of food or related terms
    food_indicators = ['food', 'diet', 'nutrition', 'eating']
    is_food_paper = any(indicator in text for indicator in food_indicators)
    
    # Also extract other domains for completeness
    domains = []
    domain_keywords = ['food', 'physical activity', 'sleep', 'mental', 'finances', 
                      'productivity', 'screen time', 'social', 'location', 'health']
    for keyword in domain_keywords:
        if keyword in text:
            domains.append(keyword)
    
    if title:
        paper_domains[title] = {
            'is_food': is_food_paper,
            'domains': list(set(domains))
        }

# Create comprehensive paper title index for matching
# Include variations and case-insensitive versions
food_paper_titles = []
title_mappings = {}

for title, info in paper_domains.items():
    if info['is_food']:
        food_paper_titles.append(title)
        title_mappings[title.lower()] = title
        title_mappings[title] = title

# Find citations for food papers
food_citations_sum = 0
matched_citation_records = []
unmatched_food_papers = set(food_paper_titles)

for citation in citations:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    citation_year = citation.get('citation_year')
    
    # Try exact match and case-insensitive match
    if citation_title in food_paper_titles:
        matched_title = citation_title
    elif citation_title.lower() in title_mappings:
        matched_title = title_mappings[citation_title.lower()]
    else:
        continue
    
    # Found a match for a food paper
    if matched_title in unmatched_food_papers:
        unmatched_food_papers.remove(matched_title)
    
    food_citations_sum += citation_count
    matched_citation_records.append({
        'title': citation_title,
        'citation_count': citation_count,
        'citation_year': citation_year
    })

# Also check if there are more papers in MongoDB
print('__RESULT__:')
print(json.dumps({
    "food_papers_found": food_paper_titles,
    "food_papers_count": len(food_paper_titles),
    "total_food_citations": food_citations_sum,
    "citation_records_matched": len(matched_citation_records),
    "unmatched_food_papers": list(unmatched_food_papers),
    "sample_matched_records": matched_citation_records[:5] if matched_citation_records else []
}))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_papers': 5, 'total_citations': 1405}, 'var_functions.execute_python:14': {'total_papers_loaded': 5, 'papers_with_titles': 5, 'food_papers_found': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'food_papers_count': 3}, 'var_functions.execute_python:16': {'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'total_food_citations': 876, 'citation_records_found': 17}, 'var_functions.execute_python:18': {'paper_analysis': {'A Lived Informatics Model of Personal Informatics': {'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['social interactions', 'screen time', 'health_behavior', 'food'], 'venue': None, 'year': None}, 'A Stage-based Model of Personal Informatics Systems': {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['social interactions', 'screen time', 'health_behavior', 'food'], 'venue': None, 'year': None}, 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['social interactions', 'screen time', 'health_behavior', 'food'], 'venue': None, 'year': None}, 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'domains': ['social interactions', 'screen time', 'health_behavior'], 'venue': None, 'year': None}, 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation': {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'domains': ['social interactions', 'screen time', 'health_behavior', 'food'], 'venue': None, 'year': None}}, 'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
