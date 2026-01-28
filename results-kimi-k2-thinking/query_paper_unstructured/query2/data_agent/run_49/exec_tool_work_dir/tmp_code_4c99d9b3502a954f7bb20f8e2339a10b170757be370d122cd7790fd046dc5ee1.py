code = """import json
import re

# Load data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

# Extract actual titles from paper text content
titles_from_papers = []
for paper in papers_data:
    text = paper.get('text', '')
    lines = text.split('\n')
    title_found = False
    
    for line in lines[:30]:  # Check first 30 lines
        line = line.strip()
        # Skip empty lines and common header/footer lines
        if not line or 'Permission' in line or 'Author Keywords' in line or 'ABSTRACT' in line:
            continue
            
        # Look for title patterns: uppercase, mixed case with proper capitalization, 
        # often followed by author names or newline
        if len(line) > 15 and not line.startswith('http'):
            # Check if it looks like a title (has words, reasonable length, not just numbers/symbols)
            word_count = len(line.split())
            if word_count > 3 and word_count < 20:
                # Extract potential title (lines before author names or emails)
                if '@' not in line and 'University' not in line and 'Copyright' not in line:
                    titles_from_papers.append(line)
                    title_found = True
                    break
    
    if not title_found:
        # Fallback to filename if no title found in text
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '')
        titles_from_papers.append(title)

print('Extracted titles from papers:')
for i, title in enumerate(titles_from_papers):
    print('  {}: {}'.format(i, title))

# Now try to match with citations
citation_titles = [c['title'].strip().lower() for c in citations_data]

acm_citations = []
matched_count = 0

for i, paper_title in enumerate(titles_from_papers):
    paper_title_normalized = paper_title.strip().lower()
    paper = papers_data[i]
    
    # Check if this paper title matches any citation
    for citation_title in citation_titles:
        if paper_title_normalized == citation_title or citation_title in paper_title_normalized or paper_title_normalized in citation_title:
            matched_count += 1
            
            # Check if this is an ACM paper
            text = paper.get('text', '').lower()
            if 'acm' in text:
                # Find the citation count for this paper
                for citation in citations_data:
                    if citation['title'].strip().lower() == citation_title:
                        acm_citations.append(int(citation['citation_count']))
                        break
            break

print('Matched papers to citations: {}'.format(matched_count))
print('ACM papers identified: {}'.format(len(acm_citations)))

if len(acm_citations) > 0:
    avg = sum(acm_citations) / len(acm_citations)
    print('Average citations for ACM papers: {}'.format(avg))
    result_value = avg
else:
    result_value = 0

result = {
    'acm_papers_count': len(acm_citations),
    'average_citations': result_value,
    'total_citations_2018': len(citations_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}, 'var_functions.execute_python:24': {'total_citations': 158, 'total_papers': 5, 'papers_dict_size': 5, 'sample_citation_title': 'expense control: a gamified, semi-automated, crowd-based approach for receipt capturing', 'sample_match_found': False}}

exec(code, env_args)
