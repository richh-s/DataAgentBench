code = """import json
import re

# Load the paper documents data
paper_docs_path = locals().get('var_functions.query_db:10')
if paper_docs_path:
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = []

# Function to extract year from text
def extract_year(text):
    # Look for venue year format
    patterns = [
        r"CHI\s+(20\d{2})",
        r"Ubicomp\s+(20\d{2})",
        r"Ubicomp\s+'(\d{2})",
        r"CSCW\s+(20\d{2})",
        r"CSCW\s+'(\d{2})",
        r"DIS\s+(20\d{2})",
        r"PervasiveHealth\s+(20\d{2})",
        r"WWW\s+(20\d{2})",
        r"IUI\s+(20\d{2})",
        r"OzCHI\s+(20\d{2})",
        r"TEI\s+(20\d{2})",
        r"AH\s+(20\d{2})",
        r"\b(2016)\b",
        r"\b(20[12]\d)\b"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            year = matches[0]
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

# Filter for 2016 papers in physical activity domain
papers_2016_physical = [
    p for p in papers_info 
    if p['year'] == 2016 and p['domain'] == 'physical activity'
]

# Save the filtered papers for later use
output = {
    "papers_2016_physical": papers_2016_physical
}

print("----BEGIN PRINT FORMAT----")
print("__RESULT__:")
print(json.dumps(output))
print("----END PRINT FORMAT----")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
