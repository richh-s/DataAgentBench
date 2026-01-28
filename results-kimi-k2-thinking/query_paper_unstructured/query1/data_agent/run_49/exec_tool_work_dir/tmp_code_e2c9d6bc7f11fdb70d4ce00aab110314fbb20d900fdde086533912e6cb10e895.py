code = """# Load the MongoDB data from the file
import json

# Read the file path from storage
file_path = 'var_functions.query_db:12'

# Read and parse the JSON data
with open(file_path, 'r') as f:
    papers_data = json.load(f)

print('Number of papers loaded:', len(papers_data))

# Extract paper information with domains
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this is a food domain paper
    # Look for food keyword in the text (case-insensitive)
    is_food = 'food' in text.lower()
    
    if is_food:
        papers_info.append({
            'title': title,
            'filename': filename
        })

print('Number of food domain papers found:', len(papers_info))

# Show a few examples
for i, paper in enumerate(papers_info[:5]):
    print(str(i+1) + '. ' + paper['title'])

# Store the food paper titles for later use
food_titles = [p['title'] for p in papers_info]
print('\nTotal food papers to check for citations:', len(food_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
