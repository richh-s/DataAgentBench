code = """import json
import re

# Read the MongoDB results file
result_path = var_functions.query_db:0
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Function to extract paper metadata
def extract_paper_metadata(paper):
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    text_preview = text[:2000]
    
    # Look for 4-digit years
    year_match = re.search(r"(20\d{2})[^a-zA-Z0-9]", text_preview)
    if year_match:
        found_year = int(year_match.group(1))
        if 2010 <= found_year <= 2020:
            year = found_year
    
    # Extract venues
    text_lower = text[:1500].lower()
    venues = ["chi", "ubicomp", "cscw", "dis", "pervasivehealth", "www", "iui", "ozchi", "tei", "ah"]
    found_venues = [venue.upper() for venue in venues if venue in text_lower]
    
    # Extract sources
    sources = ["acm", "ieee", "pubmed"]
    found_sources = [source.upper() for source in sources if source in text_lower]
    
    # Extract domains
    text_lower_full = text.lower()
    domains = ["food", "physical activity", "sleep", "mental", "finances", 
               "productivity", "screen time", "social interactions", 
               "location", "chronic", "diabetes", "health_behavior"]
    found_domains = [domain for domain in domains if domain in text_lower_full]
    
    return {
        '_id': paper['_id'],
        'title': title,
        'year': year,
        'venue': found_venues if found_venues else None,
        'source': found_sources if found_sources else None,
        'domains': found_domains if found_domains else None
    }

# Extract metadata for all papers
paper_metadata = [extract_paper_metadata(paper) for paper in papers]

# Filter papers from 2016 with physical activity domain
papers_2016_physical_activity = []
for paper in paper_metadata:
    if paper['year'] == 2016 and paper['domains']:
        # Check if physical activity is in any domain
        for domain in paper['domains']:
            if 'physical activity' in domain:
                papers_2016_physical_activity.append(paper)
                break

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")

# Print the titles for debugging
for paper in papers_2016_physical_activity:
    print(f"- {paper['title']} (Year: {paper['year']}, Domains: {paper['domains']})")

# Return the filtered papers
print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
