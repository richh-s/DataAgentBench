code = """import json

# Read the full result from the file
file_path = 'a8a8c5d8-27b2-469d-8ac2-5de8a58cc8fa.json'
with open(file_path, 'r') as f:
    papers = json.load(f)

print("Total papers retrieved: " + str(len(papers)))

# Filter for papers from 2016 in the physical activity domain
physical_activity_2016 = []
for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Check if it belongs to physical activity domain and is from 2016
    text_lower = text.lower()
    
    # Domain check
    has_physical_activity = 'physical activity' in text_lower
    
    # Year check - look for 2016 specifically in publication contexts
    has_2016_publication = False
    year_patterns = ['copyright 2016', 'published in 2016', 'proc. 2016', 'proceedings 2016', 'chi 2016', 'ubicomp 2016', 'cscw 2016', 'dis 2016']
    for pattern in year_patterns:
        if pattern in text_lower:
            has_2016_publication = True
            break
    
    if has_physical_activity and has_2016_publication:
        physical_activity_2016.append({
            'filename': filename,
            'title': filename.replace('.txt', ''),
            '_id': paper['_id']
        })

print("Papers from 2016 in physical activity domain: " + str(len(physical_activity_2016)))
for paper in physical_activity_2016:
    print("- " + paper['title'])

# Store the filtered papers for later use
filtered_papers = physical_activity_2016
__RESULT__:
print(json.dumps(filtered_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
