code = """import json
import re

# Load the paper documents data
paper_docs_path = locals().get('var_functions.query_db:2')
if paper_docs_path:
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = []

print(f"Number of papers loaded: {len(paper_docs)}")

# Show a sample
if paper_docs:
    sample = paper_docs[0]
    print(f"Sample paper:")
    print(f"Filename: {sample['filename']}")
    print(f"Text preview: {sample['text'][:500]}")

# Function to extract title, year, and domain from paper documents
def extract_paper_info(doc):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    text = doc.get('text', '')
    
    # Extract year - look for 4-digit years around 2010-2025
    year_patterns = [
        r'\b(20(?:1[0-9]|2[0-5]))\b',  # 2010-2025
        r'\b(?:19|20)\d{2}\b'  # any 1900s or 2000s
    ]
    
    year = None
    for pattern in year_patterns:
        years = re.findall(pattern, text)
        if years:
            # Try to find 2016 specifically first
            if '2016' in years:
                year = 2016
                break
            # Otherwise take the most common year or the first one
            year_counts = {}
            for y in years:
                y_int = int(y)
                if 2010 <= y_int <= 2025:  # reasonable publication years
                    year_counts[y_int] = year_counts.get(y_int, 0) + 1
            
            if year_counts:
                year = max(year_counts.items(), key=lambda x: x[1])[0]
                break
    
    # Check for physical activity domain
    domain_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'steps', 'walking', 'running']
    domain = None
    text_lower = text.lower()
    
    for keyword in domain_keywords:
        if keyword in text_lower:
            domain = 'physical activity'
            break
    
    return {
        'title': title,
        'year': year,
        'domain': domain
    }

# Test extraction on a few papers
print("\nExtracting info from first 5 papers:")
for i, doc in enumerate(paper_docs[:5]):
    info = extract_paper_info(doc)
    print(f"Paper {i+1}: {info}")

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({"message": "Data loaded and extraction function created", "sample_count": len(paper_docs)}))
----END PRINT FORMAT----"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
