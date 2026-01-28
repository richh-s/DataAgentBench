code = """import json
import re

# Read the MongoDB results file
result_path = var_functions.query_db:0
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Function to extract paper metadata from text
class PaperInfoExtractor:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        
    def get_title(self):
        """Extract title from filename (without .txt extension)"""
        return self.filename.replace('.txt', '')
    
    def get_year(self):
        """Extract year from text (look for 4-digit years)"""
        # Common patterns for years in academic papers
        # Look for patterns like: 2015, '15, 15 but validate they're likely publication years
        text = self.text[:2000]  # Look in the first part of the text
        
        # Pattern 1: Full year with conference/journal
        year_match = re.search(r"(20\d{2})[^a-zA-Z0-9]", text)
        if year_match:
            year = int(year_match.group(1))
            if 2010 <= year <= 2020:  # Reasonable range for HCI papers
                return year
        
        # Pattern 2: 'YY format
        short_year_match = re.search(r"['"]([0-9]{2})[^a-zA-Z0-9]", text)
        if short_year_match:
            short_year = int(short_year_match.group(1))
            # Convert to full year
            if short_year >= 10 and short_year <= 20:
                return 2000 + short_year
        
        # Pattern 3: Just the year at the beginning
        lines = text.split('\n')
        for line in lines[:10]:
            year_search = re.search(r"20\d{2}", line)
            if year_search:
                year = int(year_search.group())
                if 2010 <= year <= 2020:
                    return year
        
        return None
    
    def get_venue(self):
        """Extract venue from text"""
        text = self.text[:1500].lower()
        venues = ["chi", "ubicomp", "cscw", "dis", "pervasivehealth", 
                  "www", "iui", "ozchi", "tei", "ah"]
        found_venues = []
        for venue in venues:
            if venue in text:
                found_venues.append(venue.upper())
        return found_venues if found_venues else None
    
    def get_source(self):
        """Extract source from text"""
        text = self.text[:1500].lower()
        sources = ["acm", "ieee", "pubmed"]
        found_sources = []
        for source in sources:
            if source in text:
                found_sources.append(source.upper())
        return found_sources if found_sources else None
    
    def get_domains(self):
        """Extract domains from text"""
        text = self.text.lower()
        domains = ["food", "physical activity", "sleep", "mental", "finances", 
                   "productivity", "screen time", "social interactions", 
                   "location", "chronic", "diabetes", "health_behavior"]
        found_domains = []
        for domain in domains:
            if domain in text:
                found_domains.append(domain)
        return found_domains if found_domains else None

# Extract metadata for all papers
paper_metadata = []
for paper in papers:
    extractor = PaperInfoExtractor(paper['filename'], paper['text'])
    metadata = {
        '_id': paper['_id'],
        'title': extractor.get_title(),
        'year': extractor.get_year(),
        'venue': extractor.get_venue(),
        'source': extractor.get_source(),
        'domains': extractor.get_domains()
    }
    paper_metadata.append(metadata)

# Filter papers from 2016 in physical activity domain
papers_2016_physical_activity = []
for paper in paper_metadata:
    if paper['year'] == 2016 and paper['domains']:
        if any('physical activity' in domain for domain in paper['domains']):
            papers_2016_physical_activity.append(paper)

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")

# Print the titles for verification
for paper in papers_2016_physical_activity:
    print(f"- {paper['title']} (Year: {paper['year']}, Domains: {paper['domains']})")

# Return the filtered papers for the next step
print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
