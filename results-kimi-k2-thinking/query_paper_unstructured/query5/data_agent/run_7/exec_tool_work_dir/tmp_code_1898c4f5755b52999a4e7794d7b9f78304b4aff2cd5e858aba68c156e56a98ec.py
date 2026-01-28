code = """import json
import re

# Load the citations data
citations_file_path = locals()['var_functions.query_db:12']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print(f"Total citations in 2020: {len(citations_data)}")
print(f"Sample citations: {citations_data[:3]}")

# Load the papers data
papers_file_path = locals()['var_functions.query_db:14']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

print(f"\nTotal papers with 'CHI' in text: {len(papers_data)}")

# Let's examine a paper that definitely looks like CHI to understand the pattern
if papers_data:
    print("\nAnalyzing paper structure...")
    for paper in papers_data[:5]:
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        # Look for venue patterns
        chi_patterns = [
            r"CHI\s*'?\d{2}",
            r"CHI\s*Conference",
            r"Proceedings of.*CHI",
            r"CHI\s*'\d{2}",
            r"CHI\s*201[0-9]",
            r"CHI\s*202[0-9]"
        ]
        
        venue_found = False
        for pattern in chi_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                print(f"\nTitle: {title}")
                print(f"Found CHI pattern: {pattern}")
                # Show context
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    start = max(0, match.start() - 100)
                    end = min(len(text), match.end() + 100)
                    print(f"Context: ...{text[start:end]}...")
                venue_found = True
                break
        
        if not venue_found:
            # Look for other venue indicators
            other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
            for venue in other_venues:
                if re.search(venue, text, re.IGNORECASE):
                    print(f"\nTitle: {title}")
                    print(f"Found other venue: {venue}")
                    break

print('__RESULT__:')
print(json.dumps({"status": "analysis_complete"}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'status': 'ready_to_query_mongodb', 'citation_count': 188}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'status': 'papers_loaded', 'count': 99}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
