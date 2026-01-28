code = """import json
import re

# Load citation data from file
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load paper documents from file
papers_file = locals()['var_functions.query_db:2']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print('Total citations in 2020: ' + str(len(citations_data)))
print('Total paper documents: ' + str(len(papers_data)))

# Create a dictionary mapping paper titles to citation counts for 2020
citation_dict = {}
for item in citations_data:
    title = item['title'].lower().strip()
    count = int(item['citation_count'])
    citation_dict[title] = count

# Extract venue information from paper documents
def extract_venue_from_text(text):
    text_upper = text.upper()
    
    # Check for CHI specifically
    if re.search(r'CHI\s*[\'\d]', text_upper):
        return 'CHI'
    
    # Check other venues
    if re.search(r'UBICOMP|UBI COMP', text_upper):
        return 'Ubicomp'
    if 'CSCW' in text_upper:
        return 'CSCW'
    if 'DIS' in text_upper and re.search(r'DIS\s*[\'\d]', text_upper):
        return 'DIS'
    if 'PERVASIVEHEALTH' in text_upper:
        return 'PervasiveHealth'
    if 'WWW' in text_upper and re.search(r'WWW\s*\d', text_upper):
        return 'WWW'
    if 'IUI' in text_upper and re.search(r'IUI\s*\d', text_upper):
        return 'IUI'
    if 'OZCHI' in text_upper:
        return 'OzCHI'
    if 'TEI' in text_upper and re.search(r'TEI\s*\d', text_upper):
        return 'TEI'
    if 'AH' in text_upper and re.search(r'AH\s*\d', text_upper):
        return 'AH'
    
    return None

# Process papers and extract CHI papers with citations
chi_papers = []
venue_counts = {}

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '').strip()
    
    # Extract venue
    venue = extract_venue_from_text(text)
    
    if venue:
        venue_counts[venue] = venue_counts.get(venue, 0) + 1
        
        # Check if this is a CHI paper and if it has citations in 2020
        if venue == 'CHI':
            title_key = title.lower()
            if title_key in citation_dict:
                chi_papers.append({
                    'title': title,
                    'citation_count': citation_dict[title_key]
                })

# Calculate total citations for CHI papers
total_chi_citations = sum(p['citation_count'] for p in chi_papers)

result = {
    'total_chi_citations_2020': total_chi_citations,
    'num_chi_papers_with_citations': len(chi_papers),
    'total_citations_2020': len(citations_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
