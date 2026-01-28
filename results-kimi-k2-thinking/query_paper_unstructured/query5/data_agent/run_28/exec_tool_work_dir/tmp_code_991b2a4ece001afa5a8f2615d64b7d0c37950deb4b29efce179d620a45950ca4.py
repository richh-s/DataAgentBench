code = """import json

# The storage variables contain file paths
citations_file_path = var_functions.query_db:0
papers_file_path = var_functions.query_db:6

# Load the actual data from the files
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary to store paper info by title
paper_info = {}
for paper in paper_docs:
    if 'filename' in paper:
        title = paper['filename'].replace('.txt', '')
        # Extract years from the text - look for patterns like CHI '15 or 2015
        match = None
        if 'text' in paper:
            # Look for year patterns
            year_patterns = [
                r"CHI\s*['’]\s*(\d{2})",
                r"CHI\s*(\d{4})",
                r"\b(19|20)\d{2}\b"
            ]
            for pattern in year_patterns:
                matches = re.findall(pattern, paper['text'])
                if matches:
                    # Get first match
                    year_match = matches[0]
                    if isinstance(year_match, tuple):
                        year_match = year_match[0]
                    if len(year_match) == 2:  # Two digit year like '15
                        if year_match.startswith('9'):
                            match = '199' + year_match[1]
                        elif year_match.startswith('0'):
                            match = '200' + year_match[1]
                        else:
                            match = '20' + year_match
                    elif len(year_match) == 4:
                        match = year_match
                    if match and 1900 <= int(match) <= 2030:
                        break
        
        publication_year = int(match) if match else None
        paper_info[title] = {
            'venue': 'CHI' if 'CHI' in paper.get('text', '') or 'chi' in paper.get('filename', '').lower() else None,
            'year': publication_year,
            'text': paper.get('text', '')
        }

# Find total citation counts for CHI papers cited in 2020
chi_paper_citations = []
total_citations = 0

for citation in citations_2020:
    title = citation['title']
    if title in paper_info:
        paper = paper_info[title]
        if paper['venue'] == 'CHI':
            count = int(citation['citation_count'])
            chi_paper_citations.append({
                'title': title,
                'citation_count': count,
                'publication_year': paper['year']
            })
            total_citations += count

print('__RESULT__:')
print(json.dumps({
    'total_chi_papers': len(chi_paper_citations),
    'total_citation_count': total_citations,
    'chi_papers': chi_paper_citations
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:30': {'citations_type': "<class 'str'>", 'citations_preview': 'file_storage/functions.query_db:0.json', 'papers_type': "<class 'str'>", 'papers_preview': 'file_storage/functions.query_db:6.json'}}

exec(code, env_args)
