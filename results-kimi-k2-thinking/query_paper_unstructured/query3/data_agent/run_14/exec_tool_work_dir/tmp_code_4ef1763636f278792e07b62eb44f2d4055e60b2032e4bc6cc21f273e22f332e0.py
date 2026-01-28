code = """import json
import re

# Load all paper documents
papers_file_path = locals()['var_functions.query_db:16']
if isinstance(papers_file_path, str):
    with open(papers_file_path, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_file_path

# Load all citations
citations_file_path = locals()['var_functions.query_db:10']
if isinstance(citations_file_path, str):
    with open(citations_file_path, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_file_path

# Function to extract paper metadata
paper_metadata = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year (common pattern in HCI papers: venue + year at the beginning)
    year = None
    # Look for patterns like "Ubicomp '15", "CHI 2017", "2015", etc.
    year_patterns = [
        r"(?:\b|')((?:19|20)\d{2})(?:\b|'|\s|-|\))",  # 2015, '15, 2017), etc.
        r"(?:UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s*['\s]((?:1[5-9]|20)\d{2})"
    ]
    
    # Search in the first 3000 characters where the venue/year typically appears
    text_start = text[:3000]
    for pattern in year_patterns:
        year_match = re.search(pattern, text_start, re.IGNORECASE)
        if year_match:
            year_str = year_match.group(1)
            if len(year_str) == 2:
                year = 2000 + int(year_str) if int(year_str) < 50 else 1900 + int(year_str)
            else:
                year = int(year_str)
            if 2000 <= year <= 2030:  # Reasonable HCI paper year range
                break
    
    # If no year found or year is too early, try to extract from the full text
    if not year or year < 2000:
        all_years = re.findall(r'\b(20\d{2})\b', text)
        if all_years:
            years = [int(y) for y in all_years if 2000 <= int(y) <= 2025]
            if years:
                # Take the most common year (likely publication year)
                year_counts = {}
                for y in years:
                    year_counts[y] = year_counts.get(y, 0) + 1
                year = max(year_counts.items(), key=lambda x: x[1])[0]
    
    # Default year if not found
    if not year:
        year = 1900
    
    # Identify contribution types
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical contribution (various indicators)
    empirical_keywords = [
        'empirical', 'study', 'experiment', 'user study', 'field study', 
        'case study', 'interview', 'survey', 'data collection', 
        'we conducted', 'we studied', 'we interviewed', 'we surveyed'
    ]
    if any(keyword in text_lower for keyword in empirical_keywords):
        contribution.append('empirical')
    
    # Check for other contributions (not needed for this query but keeping for completeness)
    if len(contribution) == 0:  # Only mark as unknown if no empirical evidence
        contribution = ['unknown']
    else:
        contribution = contribution
        
    paper_metadata.append({
        'title': title,
        'year': year,
        'contribution': ','.join(contribution)
    })

# Filter papers: empirical contribution AND year > 2016
empirical_papers_after_2016 = [
    paper for paper in paper_metadata 
    if 'empirical' in paper['contribution'] and paper['year'] > 2016
]

# Create a dictionary for easy lookup by title
empirical_papers_dict = {paper['title']: paper for paper in empirical_papers_after_2016}

# Process citations and sum them by title
citation_counts = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    # Check if this title is in our empirical papers list
    if title in empirical_papers_dict:
        citation_counts[title] = citation_counts.get(title, 0) + count

# Prepare final results
results = []
for title, total_citations in citation_counts.items():
    results.append({
        'title': title,
        'total_citations': total_citations
    })

# Sort by citations (descending)
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    "empirical_papers_found": len(empirical_papers_after_2016),
    "papers_with_citations": len(results),
    "results": results
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_papers': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'papers_processed': 5, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 1900, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 1900, 'contribution': 'empirical,artifact,survey,methodological'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 1900, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical,theoretical,artifact,survey,methodological'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 1900, 'contribution': 'empirical,artifact'}], 'citations_count': 1405}}

exec(code, env_args)
