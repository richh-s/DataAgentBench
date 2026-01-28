code = """import json

# Load citations
with open(locals()['var_function-call-4481896084510856696'], 'r') as f:
    citations = json.load(f)

citation_map = {c['title']: c['citation_count'] for c in citations}
cited_titles = set(citation_map.keys())

# Load papers
# Result from the last query_db call
with open(locals()['var_function-call-10157305147628051086'], 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers from DB.")

# Create map of title -> paper text
paper_map = {}
for p in papers:
    title = p['filename'].replace('.txt', '')
    paper_map[title] = p.get('text', '')

# Check matches
matched_titles = []
for title in cited_titles:
    if title in paper_map:
        matched_titles.append(title)
    else:
        # Debug missing?
        pass

print(f"Matched {len(matched_titles)} out of {len(cited_titles)} cited papers.")

# Filter by source ACM
acm_counts = []
for title in matched_titles:
    text = paper_map[title]
    header = text[:5000] # Check first 5000 chars
    
    # Heuristic for ACM source
    is_acm = False
    if "permissions@acm.org" in header:
        is_acm = True
    elif "Copyright" in header and "ACM" in header:
        is_acm = True
    elif "published by ACM" in header.lower():
        is_acm = True
    elif "ACM" in header and "IEEE" not in header:
        is_acm = True
        
    if is_acm:
        count = citation_map[title]
        acm_counts.append(int(count))

if acm_counts:
    avg = sum(acm_counts) / len(acm_counts)
else:
    avg = 0

print(f"Found {len(acm_counts)} ACM papers among cited papers.")
print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-4481896084510856696': 'file_storage/function-call-4481896084510856696.json', 'var_function-call-12106380733343301840': 'file_storage/function-call-12106380733343301840.json', 'var_function-call-13470949196896071643': {'count': 158, 'unique_titles': 158}, 'var_function-call-13653321032674723116': 'file_storage/function-call-13653321032674723116.json', 'var_function-call-7433450238174774024': 68.5, 'var_function-call-3551788599043845062': {'count': 5}, 'var_function-call-10796722554973325023': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-9449244658521359486': {'count': 5}, 'var_function-call-10157305147628051086': 'file_storage/function-call-10157305147628051086.json'}

exec(code, env_args)
