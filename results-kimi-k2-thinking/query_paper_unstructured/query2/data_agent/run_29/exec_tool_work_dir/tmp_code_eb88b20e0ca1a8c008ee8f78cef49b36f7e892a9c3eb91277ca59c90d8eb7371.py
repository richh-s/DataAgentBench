code = """import json
import re

# Read the 2018 citations data
citations_2018 = locals()['var_functions.query_db:5']
if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

# Read the paper documents data
paper_docs = locals()['var_functions.query_db:2']
if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

print(f"Loaded {len(citations_2018)} citations from 2018")
print(f"Loaded {len(paper_docs)} paper documents")

# Create a dictionary mapping paper titles to citation counts for 2018
citation_dict = {}
for cit in citations_2018:
    title = cit['title'].strip()
    citation_dict[title] = int(cit['citation_count'])

print(f"Created citation dictionary with {len(citation_dict)} entries")

# Analyze paper documents to find ACM papers with 2018 citations
acm_papers_with_citations = []
total_acm_citations = 0
count_acm_papers = 0

for doc in paper_docs:
    # Get paper title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    # Check if this paper has citations in 2018
    if title in citation_dict:
        text = doc.get('text', '')
        
        # Check if it's an ACM paper by looking for ACM references
        # Look for ACM in the text, typically in copyright notices, conference headers, etc.
        if 'ACM' in text or 'acm' in text or 'Association for Computing Machinery' in text:
            # Additional validation - look for specific ACM patterns
            # Common patterns: "ACM " followed by year, "ACM Copyright", conference with ACM
            acm_patterns = [
                r'ACM\s+\d{4}',  # ACM year
                r'ACM\s+Copyright',  # ACM Copyright
                r'Proceedings.*?ACM',  # Proceedings with ACM
                r'ACM\s+Press',  # ACM Press
                r'ACM\s+Trans',  # ACM Transactions
                r'ACM\s+SIG',  # ACM SIG
                r'ISBN.*?ACM',  # ISBN with ACM
                r'DOI.*?10\.1145',  # ACM DOI prefix
                r'UbiComp.*?ACM',  # UbiComp with ACM
                r'CHI.*?ACM'  # CHI with ACM
            ]
            
            is_acm = False
            for pattern in acm_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    is_acm = True
                    break
            
            if is_acm:
                citation_count = citation_dict[title]
                acm_papers_with_citations.append({
                    'title': title,
                    'citation_count': citation_count,
                    'citation_year': 2018
                })
                total_acm_citations += citation_count
                count_acm_papers += 1

print(f"Found {count_acm_papers} ACM papers with 2018 citations")
print(f"Total citations for ACM papers: {total_acm_citations}")

if count_acm_papers > 0:
    average_citations = total_acm_citations / count_acm_papers
    print(f"Average citation count: {average_citations:.2f}")
    
    # Show some examples
    print("\nSample ACM papers with 2018 citations:")
    for i, paper in enumerate(acm_papers_with_citations[:5]):
        print(f"  {i+1}. {paper['title'][:60]}... - {paper['citation_count']} citations")
    
    __RESULT__:
    result = {
        "average_citation_count": round(average_citations, 2),
        "total_acm_papers": count_acm_papers,
        "total_citations": total_acm_citations
    }
    print(json.dumps(result))
else:
    __RESULT__:
    result = {
        "average_citation_count": 0,
        "total_acm_papers": 0,
        "total_citations": 0,
        "message": "No ACM papers found with 2018 citations"
    }
    print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
