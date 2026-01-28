code = """import json
import re

# Load the MongoDB data
mongo_file_path = var_functions.query_db_8
with open(mongo_file_path, 'r') as f:
    papers_raw = json.load(f)

print(f"Total papers in collection: {len(papers_raw)}")

# Extract paper information
papers = []
for doc in papers_raw:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract venue and year from the beginning of the text
    # Look for patterns like: CHI 'YY or CHI YYYY or CHI Conference
    venue = 'Unknown'
    year = None
    
    # Search in first 500 characters for venue/year info
    header_text = text[:500]
    
    # Look for CHI venue patterns
    chi_patterns = [
        r"CHI\s*'\s*(\d{2})",  # CHI '15
        r"CHI\s+(\d{4})",      # CHI 2015
        r"CHI\s+Conference",
        r"Proceedings of the.*CHI",
        r"ACM.*CHI.*Conference"
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header_text, re.IGNORECASE):
            is_chi = True
            venue = "CHI"
            break
    
    # Extract year if found
    year_match = re.search(r"(\d{4})|'(\d{2})", header_text[:200])
    if year_match:
        year_str = year_match.group()
        if year_str.startswith("'"):
            # Handle '15 -> 2015
            year = int('20' + year_str[1:])
        else:
            year = int(year_str)
    
    if is_chi:
        papers.append({
            'title': title,
            'venue': venue,
            'year': year,
            'filename': filename
        })

# Filter papers that look like CHI papers
chi_papers = []
for paper in papers:
    text_lower = text.lower()
    if 'chi' in text_lower and ('conference' in text_lower or 'proceedings' in text_lower):
        chi_papers.append(paper)

# Get unique papers by title (some may have duplicates)
unique_chi_papers = {}
for paper in chi_papers:
    if paper['title'] not in unique_chi_papers:
        unique_chi_papers[paper['title']] = paper

chi_papers_unique = list(unique_chi_papers.values())

print(f"CHI papers found: {len(chi_papers_unique)}")
print("\nSample CHI papers:")
for p in chi_papers_unique[:10]:
    print(f"- {p['title']} ({p['year']})")

# Save CHI papers to examine later
chi_papers_data = json.dumps(chi_papers_unique, ensure_ascii=False, indent=2)
print('__RESULT__:')
print(chi_papers_data)"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:2': [{'total_2020_citations': '188'}], 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
