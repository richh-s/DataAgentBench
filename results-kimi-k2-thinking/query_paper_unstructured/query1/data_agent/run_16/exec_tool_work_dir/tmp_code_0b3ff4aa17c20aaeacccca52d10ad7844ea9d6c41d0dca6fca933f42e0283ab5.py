code = """import json
import re

# Load the full data
paper_docs_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:12']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(papers_citations_path, 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(paper_docs)}")
print(f"Total citation records: {len(citations)}")

# More comprehensive food domain detection
food_related_papers = []
keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary']

for doc in paper_docs:
    text_lower = doc['text'].lower()
    doc_filename = doc['filename'].lower()
    
    # Check if any food-related keyword appears
    has_food_keyword = any(keyword in text_lower or keyword in doc_filename for keyword in keywords)
    
    if has_food_keyword:
        title = doc['filename'].replace('.txt', '')
        
        # Try to extract year from text
        year_match = re.search(r'\b(200[0-9]|201[0-9]|202[0-9])\b', doc['text'])
        year = int(year_match.group(0)) if year_match else None
        
        # Try to extract venue
        venue_match = re.search(r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\b', doc['text'])
        venue = venue_match.group(0) if venue_match else ''
        
        food_related_papers.append({
            'title': title,
            'filename': doc['filename'],
            'year': year,
            'venue': venue
        })

print(f"Found {len(food_related_papers)} food-related papers")
print("Sample food papers:", food_related_papers[:10])

# Create citation map for faster lookup
citation_map = {c['title'].lower().strip(): int(c['total_citations']) for c in citations}

# Match food papers with citations
total_citations = 0
matched_papers = []

for paper in food_related_papers:
    paper_title = paper['title'].lower().strip()
    
    # Try direct match
    if paper_title in citation_map:
        citations_count = citation_map[paper_title]
        matched_papers.append({
            'title': paper['title'],
            'citations': citations_count,
            'year': paper['year'],
            'venue': paper['venue']
        })
        total_citations += citations_count
        continue
    
    # Try partial matching
    for cit_title, cit_count in citation_map.items():
        if (paper_title in cit_title or cit_title in paper_title or 
            paper_title.replace(':', '') in cit_title or 
            cit_title.replace(':', '') in paper_title):
            matched_papers.append({
                'title': paper['title'],
                'citations': cit_count,
                'year': paper['year'],
                'venue': paper['venue']
            })
            total_citations += cit_count
            break

print(f"Matched {len(matched_papers)} papers with citations")
print(f"Total citations for food domain: {total_citations}")
print("Top cited papers:", sorted(matched_papers, key=lambda x: x['citations'], reverse=True)[:10])

result = {
    'total_citation_count': total_citations,
    'matched_papers': len(matched_papers),
    'food_papers_found': len(food_related_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'paper_info': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'venue': '', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'venue': '', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'venue': '', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}], 'food_papers_with_citations': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citations': 220}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 266}], 'total_citation_count': 876}}

exec(code, env_args)
