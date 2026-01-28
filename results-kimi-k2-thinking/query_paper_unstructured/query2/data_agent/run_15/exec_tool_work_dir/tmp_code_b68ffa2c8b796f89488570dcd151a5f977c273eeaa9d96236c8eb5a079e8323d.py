code = """import json
import re

# Load citations data for 2018
citations_file_path = locals()['var_functions.query_db:9']
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents
papers_file_path = locals()['var_functions.query_db:5']
with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded', len(citations_2018), 'citations for 2018')
print('Loaded', len(paper_docs), 'paper documents')

# Create a helper function to normalize titles
def normalize_title(title):
    return re.sub(r'\s+', ' ', title.strip().lower())

# Extract metadata from paper documents
paper_metadata = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '').strip()
    normalized_title = normalize_title(title)
    
    text = doc.get('text', '')
    
    # Check if ACM paper
    is_acm = bool(re.search(r'ACM|acm\.org|ACM Classification', text))
    
    # Extract year - look for patterns like 2015, 2016, etc.
    year = None
    year_matches = re.findall(r'\b(20[01]\d)\b', text)
    if year_matches:
        year = int(min(year_matches))  # Use the earliest year found
    
    # Extract venue
    venue = None
    venue_match = re.search(r"(UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['’]?\s*\d{2}", text, re.IGNORECASE)
    if venue_match:
        venue = venue_match.group(1).upper()
    
    paper_metadata[normalized_title] = {
        'original_title': title,
        'is_acm': is_acm,
        'year': year,
        'venue': venue
    }

# Match citations with papers and filter for ACM papers published by 2018
acm_citation_counts = []
matched_details = []

for citation in citations_2018:
    citation_title = citation.get('title', '')
    normalized_citation_title = normalize_title(citation_title)
    citation_count = int(citation.get('citation_count', 0))
    
    if normalized_citation_title in paper_metadata:
        paper = paper_metadata[normalized_citation_title]
        if paper['is_acm'] and paper['year'] and paper['year'] <= 2018:
            acm_citation_counts.append(citation_count)
            matched_details.append({
                'title': citation_title,
                'citations_2018': citation_count,
                'paper_year': paper['year'],
                'venue': paper['venue']
            })

# Calculate average
avg_citations = 0
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)

result = {
    'total_citations_checked': len(citations_2018),
    'matched_acm_papers': len(acm_citation_counts),
    'avg_citations_2018': round(avg_citations, 2),
    'total_citations_for_avg': sum(acm_citation_counts),
    'matched_papers': matched_details
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'citations_2018_count': 158, 'paper_docs_count': 5}, 'var_functions.execute_python:14': {'total_citations_2018': 158, 'matched_papers': 0, 'unmatched_papers': 156, 'acm_papers_2018': 0, 'acm_papers_sample': []}, 'var_functions.execute_python:16': {'citation_titles_2018': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'total_citations_2018': 158}, 'var_functions.execute_python:18': [{'index': 0, 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'index': 1, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'index': 2, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'index': 3, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'index': 4, 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:20': {'a lived informatics model of personal informatics': {'original_title': 'A Lived Informatics Model of Personal Informatics', 'is_acm': True, 'year': None, 'venue': 'Ubicomp'}, 'a stage-based model of personal informatics systems': {'original_title': 'A Stage-based Model of Personal Informatics Systems', 'is_acm': True, 'year': None, 'venue': 'Ubicomp'}, 'a trip to the moon: personalized animated movies for self-reflection': {'original_title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_acm': True, 'year': None, 'venue': 'Ubicomp'}, 'a wee bit more interaction: designing and evaluating an overactive bladder app': {'original_title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_acm': True, 'year': None, 'venue': 'Ubicomp'}, 'armsleeve: a patient monitoring system to support occupational therapists in stroke rehabilitation': {'original_title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'is_acm': True, 'year': None, 'venue': 'Ubicomp'}}, 'var_functions.execute_python:24': 'debug done', 'var_functions.execute_python:26': 'debug done', 'var_functions.execute_python:28': 'debug inspection complete'}

exec(code, env_args)
