code = """import json

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers retrieved: {len(papers)}")

# Let's examine the first paper to understand the structure
if papers:
    print("\nFirst paper structure:")
    print(f"Filename: {papers[0]['filename']}")
    print(f"ID: {papers[0]['_id']}")
    print(f"Text preview: {papers[0]['text'][:500]}...")

# Now let's filter for papers from 2016 in the 'physical activity' domain
# We need to check if the text contains both "2016" and "physical activity"
# But we also need to be more precise - "2016" could appear anywhere
# Let's look for publication year patterns and domain indicators

physical_activity_2016 = []
for paper in papers:
    text = paper['text'].lower()
    filename = paper['filename']
    
    # Check if it's likely from 2016
    # Look for copyright year, publication year, or venue year
    has_2016 = False
    if '2016' in paper['text']:
        # Look for patterns that indicate publication year
        year_patterns = [
            'copyright 2016',
            'published in 2016',
            'proc. 2016',
            'proceedings 2016',
            'chi 2016',
            'ubicomp 2016',
            'cscw 2016',
            'dis 2016',
            'pervasivehealth 2016',
            'www 2016',
            'iui 2016',
            'ozchi 2016',
            'tei 2016',
            'ah 2016'
        ]
        
        text_lower = paper['text'].lower()
        for pattern in year_patterns:
            if pattern in text_lower:
                has_2016 = True
                break
    
    # Check if it belongs to physical activity domain
    # Look for domain indicators
    domain_indicators = [
        'physical activity',
        'exercise',
        'fitness',
        'activity tracking',
        'activity monitor'
    ]
    
    has_physical_activity = False
    text_lower = paper['text'].lower()
    for indicator in domain_indicators:
        if indicator in text_lower:
            has_physical_activity = True
            break
    
    if has_2016 and has_physical_activity:
        physical_activity_2016.append({
            'filename': filename,
            'title': filename.replace('.txt', ''),
            '_id': paper['_id']
        })

print(f"\nPapers from 2016 in physical activity domain: {len(physical_activity_2016)}")
for paper in physical_activity_2016[:10]:  # Show first 10
    print(f"- {paper['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
