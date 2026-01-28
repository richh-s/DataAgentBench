code = """import json
import re

# Read the MongoDB query results from file
result_path = var_functions.query_db:22
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers mentioning physical activity: {len(papers)}")

# Function to extract year from text
def extract_year(text):
    # Common venue patterns with years
    patterns = [
        r'\b(2016)\b',
        r'CHI\s*[\'"]?\s*\b(2016)\b',
        r'UbiComp\s*[\'"]?\s*\b(2016)\b',
        r'CSCW\s*[\'"]?\s*\b(2016)\b',
        r'DIS\s*[\'"]?\s*\b(2016)\b',
        r'PervasiveHealth\s*[\'"]?\s*\b(2016)\b',
        r'WWW\s*[\'"]?\s*\b(2016)\b',
        r'IUI\s*[\'"]?\s*\b(2016)\b'
    ]
    
    text_upper = text.upper()
    for pattern in patterns:
        match = re.search(pattern, text_upper)
        if match:
            # Try to get year from different capture groups
            for group_num in range(1, 3):
                try:
                    year_str = match.group(group_num)
                    if year_str:
                        return int(year_str)
                except:
                    pass
    return None

# Filter papers from 2016 that are in physical activity domain
papers_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    year = extract_year(text)
    
    # Check if from 2016
    if year == 2016:
        # Count physical activity mentions
        physical_activity_count = len(re.findall(r'physical activity', text, re.IGNORECASE))
        
        # Also check for related domain keywords
        domain_indicators = ['fitness', 'exercise', 'sedentary', 'active living']
        domain_score = physical_activity_count
        
        for indicator in domain_indicators:
            domain_score += len(re.findall(r'\\b' + indicator + r'\\b', text, re.IGNORECASE))
        
        if domain_score > 0:
            papers_2016.append({
                'title': title,
                'filename': filename,
                'year': year,
                'domain_score': domain_score
            })

print(f"Found {len(papers_2016)} papers from 2016 in physical activity domain")

# Print details
for paper in sorted(papers_2016, key=lambda x: x['title']):
    print(f"  Title: {paper['title']}")
    print(f"  Domain Score: {paper['domain_score']}")
    print()

# Return the filtered papers
result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
