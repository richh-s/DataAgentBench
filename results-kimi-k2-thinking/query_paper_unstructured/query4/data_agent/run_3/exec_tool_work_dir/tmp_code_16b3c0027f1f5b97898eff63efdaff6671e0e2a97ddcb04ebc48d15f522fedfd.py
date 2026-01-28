code = """import json

# Access the file path from the storage
file_path = var_functions.query_db:5

# Read and parse the JSON file
with open(file_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers mentioning '2016'")

# Extract paper titles and check for domains
physical_activity_papers = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    
    # Check if it's from 2016 and in physical activity domain
    if '2016' in text and 'physical activity' in text:
        physical_activity_papers.append({
            'title': title,
            'filename': filename
        })

print(f"Found {len(physical_activity_papers)} papers that mention both 2016 and physical activity")

if physical_activity_papers:
    print("Sample papers:")
    for paper in physical_activity_papers[:5]:
        print(f"  - {paper['title']}")

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({
    "total_2016_papers": len(papers),
    "physical_activity_papers": len(physical_activity_papers),
    "sample_papers": physical_activity_papers[:3]
}, indent=2))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
