code = """import json
import re

# Load all physical activity papers
papers_path = locals()['var_functions.query_db:14']
with open(papers_path, 'r') as f:
    physical_activity_papers = json.load(f)

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create citations dictionary
citations_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Debug: Let's look at a few papers to understand the format
print(f"Total physical activity papers: {len(physical_activity_papers)}")
print("\nFirst few papers:")
for i, paper in enumerate(physical_activity_papers[:3]):
    filename = paper['filename']
    text_preview = paper['text'][:500]
    title = filename.replace('.txt', '')
    has_citations = title in citations_dict
    print(f"\n{i+1}. Filename: {filename}")
    print(f"   Title: {title}")
    print(f"   Has citations: {has_citations}")
    if has_citations:
        print(f"   Citations: {citations_dict[title]}")
    print(f"   Text preview: {text_preview[:200]}")

# Now look for 2016 patterns more carefully
results = []
year_checks = []

for paper in physical_activity_papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Look for 2016 in various contexts
    year_2016_indicators = []
    
    # Pattern 1: Explicit 2016 with venue
    if re.search(r'\b2016\b.*?(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Proceedings|Conference)', text, re.IGNORECASE):
        year_2016_indicators.append("2016_with_venue")
    
    # Pattern 2: Venue with 2016
    if re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Proceedings|Conference).*?\b2016\b', text, re.IGNORECASE):
        year_2016_indicators.append("venue_with_2016")
    
    # Pattern 3: Copyright 2016
    if re.search(r'Copyright[^\n]*\b2016\b', text, re.IGNORECASE):
        year_2016_indicators.append("copyright_2016")
    
    # Pattern 4: Conference year format (e.g., CHI '16)
    if re.search(r'(CHI|Ubicomp|CSCW|DIS)\s*[\'’]\s*16\b', text, re.IGNORECASE):
        year_2016_indicators.append("conference_year_16")
    
    # Pattern 5: Any 2016 (for debugging)
    if re.search(r'\b2016\b', text):
        year_2016_indicators.append("any_2016")
    
    if year_2016_indicators and title in citations_dict:
        results.append({
            'title': title,
            'total_citations': citations_dict[title],
            'year_indicators': year_2016_indicators
        })
        year_checks.append({
            'title': title,
            'indicators': year_2016_indicators
        })

print(f"\n\nFound {len(results)} potential 2016 physical activity papers with citations")

# Show the indicators found
if year_checks:
    print("\nYear indicators found:")
    for item in year_checks:
        print(f"  {item['title']}: {item['indicators']}")

# Sort and output results
sorted_results = sorted(results, key=lambda x: x['total_citations'], reverse=True)
result_str = json.dumps(sorted_results[:20], indent=2)  # Top 20
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': []}

exec(code, env_args)
