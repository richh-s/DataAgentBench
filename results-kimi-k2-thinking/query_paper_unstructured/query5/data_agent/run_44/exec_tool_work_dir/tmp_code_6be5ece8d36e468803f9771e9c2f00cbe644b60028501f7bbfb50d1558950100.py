code = """import json
import re

# Load citation data from file
citations_file = var_functions.query_db:0
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load paper documents from file
papers_file = var_functions.query_db:2
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total citations in 2020: {len(citations_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Create a dictionary mapping paper titles to citation counts for 2020
citation_dict = {item['title'].lower().strip(): int(item['citation_count']) for item in citations_data}

# Extract venue information from paper documents
def extract_venue_from_text(text):
    """Extract venue from paper text"""
    # Look for patterns like CHI, Ubicomp, CSCW, etc. in the text
    # Common patterns: venue name followed by year
    patterns = [
        r'CHI\s*\'\d{2}',
        r'CHI\s*\d{4}',
        r'Ubicomp\s*\'?\d{2}',
        r'UbiComp\s*\'\d{2}',
        r'CSCW\s*\'?\d{2}',
        r'DIS\s*\'\d{2}',
        r'PervasiveHealth\s*\d{4}',
        r'WWW\s*\d{4}',
        r'IUI\s*\d{4}',
        r'OzCHI\s*\d{4}',
        r'TEI\s*\d{4}',
        r'AH\s*\d{4}'
    ]
    
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

# Process papers and extract venues
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
                    'citation_count': citation_dict[title_key],
                    'venue': venue
                })

print(f"\nPapers by venue:")
for venue, count in sorted(venue_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {venue}: {count}")

print(f"\nCHI papers with 2020 citations: {len(chi_papers)}")

# Calculate total citations for CHI papers
total_chi_citations = sum(paper['citation_count'] for paper in chi_papers)

print(f"Total citation counts for CHI papers in 2020: {total_chi_citations}")

# Show some examples
print("\nTop CHI papers by 2020 citations:")
chi_papers_sorted = sorted(chi_papers, key=lambda x: x['citation_count'], reverse=True)
for i, paper in enumerate(chi_papers_sorted[:10], 1):
    print(f"  {i}. {paper['citation_count']} citations: {paper['title']}")

# Also show CHI papers that weren't found in citations
chi_papers_all = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '').strip()
    venue = extract_venue_from_text(text)
    
    if venue == 'CHI':
        title_key = title.lower()
        citation_count = citation_dict.get(title_key, 0)
        chi_papers_all.append({
            'title': title,
            'citation_count': citation_count,
            'has_citations': title_key in citation_dict
        })

print(f"\nTotal CHI papers found: {len(chi_papers_all)}")
chi_papers_with_citations = [p for p in chi_papers_all if p['has_citations']]
print(f"CHI papers with 2020 citations: {len(chi_papers_with_citations)}")
print(f"CHI papers without 2020 citations: {len(chi_papers_all) - len(chi_papers_with_citations)}")

total_citations_all_chi = sum(p['citation_count'] for p in chi_papers_all)
print(f"Total citations for ALL CHI papers (including those with 0 citations): {total_citations_all_chi}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
