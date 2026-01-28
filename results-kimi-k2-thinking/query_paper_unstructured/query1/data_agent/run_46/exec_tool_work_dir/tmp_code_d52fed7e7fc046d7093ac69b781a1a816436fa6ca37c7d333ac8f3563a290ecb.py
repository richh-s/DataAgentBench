code = """import json
import re

# Get the documents from the storage variable
# The result from query_db is stored in var_functions.query_db:2
result_path = var_functions.query_db_2  # Using underscore instead of colon

# Read the JSON file
with open(result_path, 'r') as f:
    documents = json.load(f)

print('Total documents: ' + str(len(documents)))

# Function to extract domains from paper text
def extract_domains(text):
    """Extract domains from paper text. Look for common patterns."""
    text_lower = text.lower()
    domains = []
    
    # Common domain patterns found in academic papers
    domain_keywords = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health_behavior', 'weight', 'exercise',
        'stress', 'mood', 'wellbeing', 'health', 'fitness'
    ]
    
    # Look for explicit domain mentions (often in format: domain [citation])
    for keyword in domain_keywords:
        # Pattern: keyword followed by [ (citation) or , or : 
        pattern = r'\b' + re.escape(keyword) + r'\s*[,\[]'
        if re.search(pattern, text_lower):
            domains.append(keyword)
    
    # Also check if keyword appears frequently in the text
    for keyword in domain_keywords:
        count = text_lower.count(keyword)
        if count >= 5 and keyword not in domains:
            domains.append(keyword)
    
    return domains

# Process documents and find food papers
food_papers = []
all_paper_info = []

for doc in documents:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    domains = extract_domains(text)
    
    if 'food' in domains:
        food_papers.append({
            'title': title,
            'filename': filename,
            'domains': domains
        })
    
    all_paper_info.append({
        'title': title,
        'domains': domains
    })

print('Found ' + str(len(food_papers)) + ' food domain papers')

# Show some examples
for i in range(min(5, len(food_papers))):
    paper = food_papers[i]
    print(str(i+1) + '. ' + paper['title'] + ' (domains: ' + str(paper['domains']) + ')')

# Get titles for querying citations
food_titles = [paper['title'] for paper in food_papers]

result = {
    "food_papers_count": len(food_papers),
    "food_titles": food_titles,
    "sample_papers": food_papers[:5]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
