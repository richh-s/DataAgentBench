code = """import json

# Check available storage variables
storage_vars = {k: v for k, v in globals().items() if k.startswith('var_')}

print("Available storage variables:")
for var_name in sorted(storage_vars.keys()):
    var_value = storage_vars[var_name]
    if isinstance(var_value, str) and len(var_value) < 300:
        print("  " + var_name + ": " + var_value)
    else:
        print("  " + var_name + ": " + type(var_value).__name__)

# Find the file paths
food_papers_path = None
citations_path = None

for var_name, var_value in storage_vars.items():
    if 'query_db:20' in var_name:  # Food papers query result
        food_papers_path = var_value
    elif 'query_db:8' in var_name:  # Citations query result
        citations_path = var_value

print("\nFood papers path: " + str(food_papers_path))
print("Citations path: " + str(citations_path))

# Load and process data
with open(food_papers_path, 'r') as f:
    food_papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print("\nLoaded " + str(len(food_papers)) + " food domain papers")
print("Loaded " + str(len(citations)) + " citation records")

# Extract paper titles
food_titles = []
for paper in food_papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    food_titles.append(title)

food_titles_set = set(food_titles)
print("Sample food titles: " + str(list(food_titles_set)[:3]))

# Sum citations for food papers
total_citations = 0
for citation in citations:
    cit_title = citation['title']
    if cit_title in food_titles_set:
        cit_count = int(citation['total_citations'])
        total_citations += cit_count

print("\nTotal citations for food domain: " + str(total_citations))

# Print final result
print("__RESULT__:")
print(str(total_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
