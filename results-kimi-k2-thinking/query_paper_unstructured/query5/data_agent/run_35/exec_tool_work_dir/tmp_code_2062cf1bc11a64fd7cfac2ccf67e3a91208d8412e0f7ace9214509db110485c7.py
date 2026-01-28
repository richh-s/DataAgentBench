code = """import json
import re

# Load the citation data for 2020
citations_file = '/tmp/result_functions.query_db:0.json'
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper documents
paper_docs_file = '/tmp/result_functions.query_db:2.json'
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary mapping paper titles to their venue and year
# Extract title from filename and search for CHI in the text
chi_papers = []
venue_pattern = r"'\d{2}\s*,?\s*CHI\s*'\d{2}|CHI\s*'\d{2}|'\d{2}\s*,?\s*CHI"  # Common CHI patterns

doc_pattern = r"[A-Z][A-Za-z\s]+:\s+[A-Z][A-Za-z\s]+\s+'\d{2}\s*,?\s*CHI\s*|Proceedings of the .*CHI.*\d{4}|CHI \d{4}|ACM SIGCHI.*\d{4}|Conference on Human Factors in Computing Systems.*\d{4}"

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for CHI venue patterns in text
    chi_indicators = []
    chi_indicators.extend(re.findall(venue_pattern, text))
    chi_indicators.extend(re.findall(r"Proceedings of the SIGCHI", text))
    chi_indicators.extend(re.findall(r"Proceedings of the \d{4} CHI", text))
    chi_indicators.extend(re.findall(r"Proceedings of the ACM Conference on Human Factors", text))
    chi_indicators.extend(re.findall(r"Human Factors in Computing Systems", text))
    
    # More flexible CHI detection
    if (re.search(r"CHI[^a-zA-Z]*[' ]?\d{2,4}", text) or 
        re.search(r"Proceedings of the .*CHI", text, re.IGNORECASE) or
        re.search(r"SIGCHI", text) or
        re.search(r"Human Factors in Computing Systems", text)):
        chi_indicators.append("CHI")
    
    if chi_indicators or "CHI" in text:
        # Extract year from text
        year_match = re.search(r"CHI\s*'?\s*(\d{2,4})|'\s*CHI\s*(\d{2,4})|CHI\s+(\d{4})|Ubicomp '15.*(\d{4})|(\d{4})\s*CHI", text)
        year = None
        if year_match:
            year_str = next(g for g in year_match.groups() if g)
            if len(year_str) == 2:
                year = int("20" + year_str if int(year_str) < 50 else "19" + year_str)
            else:
                year = int(year_str)
        
        chi_papers.append({
            'title': title,
            'venue': 'CHI',
            'year': year,
            'indicators': chi_indicators
        })

# Create a dictionary of CHI papers for easy lookup
chi_papers_dict = {paper['title']: paper for paper in chi_papers}

# Find matching citations
chi_citations_2020 = []
for citation in citations_2020:
    title = citation['title']
    if title in chi_papers_dict:
        chi_citations_2020.append({
            'title': title,
            'citation_count': int(citation['citation_count']),
            'venue': 'CHI',
            'year': chi_papers_dict[title]['year']
        })

# Calculate total citation count
total_citations = sum(paper['citation_count'] for paper in chi_citations_2020)

result = {
    'chi_citations_2020': chi_citations_2020,
    'total_citation_count': total_citations,
    'chi_papers_count': len(chi_papers),
    'matched_chi_papers': len(chi_citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
