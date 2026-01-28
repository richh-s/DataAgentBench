code = """import json
import re

# Load the paper documents data
paper_docs_path = locals().get('var_functions.query_db:10')
if paper_docs_path:
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = []

print(f"Number of papers loaded: {len(paper_docs)}")

# Function to extract year from text using multiple patterns
def extract_year(text):
    # Pattern 1: Look for venue year format like "CHI 2016"
    patterns = [
        r"CHI\s+(20\d{2})",
        r"Ubicomp\s+(20\d{2})",
        r"Ubicomp\s+'(\d{2})",  # Ubicomp '16
        r"CSCW\s+(20\d{2})",
        r"CSCW\s+'(\d{2})",
        r"DIS\s+(20\d{2})",
        r"PervasiveHealth\s+(20\d{2})",
        r"WWW\s+(20\d{2})",
        r"IUI\s+(20\d{2})",
        r"OzCHI\s+(20\d{2})",
        r"TEI\s+(20\d{2})",
        r"AH\s+(20\d{2})",
        r"Proceedings\s+of\s+the\s+(20\d{2})",
        r"\b(20{2}[0-9])\b",
        r"\b(2016)\b"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            year = matches[0]
            # Handle 2-digit years
            if len(year) == 2:
                year = "20" + year
            try:
                year_int = int(year)
                if 2010 <= year_int <= 2025:
                    return year_int
            except:
                continue
    
    return None

# Function to extract paper information
def extract_paper_info(doc):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    text = doc.get('text', '')
    year = extract_year(text)
    
    # Check for physical activity domain
    physical_activity_keywords = [
        'physical activity', 'fitness', 'exercise', 'workout', 'steps', 
        'walking', 'running', 'activity tracking', 'fitness tracking'
    ]
    
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    domain = 'physical activity' if is_physical_activity else None
    
    return {
        'title': title,
        'year': year,
        'domain': domain
    }

# Extract information from all papers
papers_info = []
for doc in paper_docs:
    info = extract_paper_info(doc)
    if info['title']:  # Only add papers with titles
        papers_info.append(info)

print(f"Extracted info for {len(papers_info)} papers")

# Filter for 2016 papers in physical activity domain
papers_2016_physical = [
    p for p in papers_info 
    if p['year'] == 2016 and p['domain'] == 'physical activity'
]

print(f"Found {len(papers_2016_physical)} papers from 2016 in physical activity domain")

for idx, paper in enumerate(papers_2016_physical[:10]):  # Print first 10
    print(f"{idx+1}. Title: {paper['title']}, Year: {paper['year']}, Domain: {paper['domain']}")

result = {
    "total_papers": len(papers_info),
    "papers_2016_physical": len(papers_2016_physical),
    "sample_papers": papers_2016_physical[:10]
}

print("----BEGIN PRINT FORMAT----")
print("__RESULT__:")
print(json.dumps(result))
print("----END PRINT FORMAT----")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
