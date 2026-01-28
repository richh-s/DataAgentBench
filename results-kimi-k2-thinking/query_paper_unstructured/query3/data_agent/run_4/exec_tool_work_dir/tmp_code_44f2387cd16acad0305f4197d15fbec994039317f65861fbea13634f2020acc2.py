code = """import json
import re

# Load the MongoDB data
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    papers = json.load(f)

# Function to extract paper information from text
def extract_paper_info(paper):
    text = paper['text']
    filename = paper['filename']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like 'YYYY' or ''YY
    year_match = re.search(r"(UbiComp\s*'\s*(\d{2})|CHI\s*'\s*(\d{2})|DIS\s*'\s*(\d{2})|CSCW\s*'\s*(\d{2})|(\d{4}))", text)
    year = None
    if year_match:
        # Take the first non-None group
        for group in year_match.groups():
            if group:
                # Convert 2-digit year to 4-digit
                if len(group) == 2:
                    if int(group) > 50:  # Assuming 1950s-1999
                        year = int("19" + group)
                    else:  # Assuming 2000s-2049
                        year = int("20" + group)
                elif len(group) == 4:
                    year = int(group)
                break
    
    # Extract venue from common patterns
    venue = None
    venue_match = re.search(r"(UbiComp|CHI|DIS|CSCW|PervasiveHealth|WWW|IUI|OzCHI|TEE|AH)\s*'", text)
    if venue_match:
        venue = venue_match.group(1)
    
    # Extract contribution type - look for keywords
    contribution = ""
    text_lower = text.lower()
    if "empirical" in text_lower:
        contribution = "empirical"
    elif "artifact" in text_lower:
        contribution = "artifact"
    elif "theoretical" in text_lower or "theory" in text_lower:
        contribution = "theoretical"
    elif "survey" in text_lower:
        contribution = "survey"
    elif "methodological" in text_lower or "methodology" in text_lower:
        contribution = "methodological"
    
    return {
        'title': title,
        'year': year,
        'venue': venue,
        'contribution': contribution
    }

# Extract info from all papers
paper_info_list = []
for paper in papers:
    info = extract_paper_info(paper)
    paper_info_list.append(info)

# Filter for empirical papers after 2016
filtered_papers = [
    p for p in paper_info_list 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

preview = {
    'total_papers': len(paper_info_list),
    'empirical_papers_after_2016': len(filtered_papers),
    'sample_extracted': paper_info_list[:3],
    'sample_filtered': filtered_papers[:3] if filtered_papers else []
}

print('__RESULT__:')
print(json.dumps(preview))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'total_papers': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
