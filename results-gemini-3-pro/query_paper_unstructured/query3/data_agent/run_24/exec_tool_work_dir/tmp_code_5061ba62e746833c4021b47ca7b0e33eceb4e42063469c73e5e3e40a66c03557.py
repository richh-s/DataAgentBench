code = """import json
import re

citations_file_path = locals()['var_function-call-8765785804266823925']
papers_file_path = locals()['var_function-call-10316404265600385483']

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

keywords = ["empirical", "user study", "participants", "interview", "experiment", "field study"]

debug_info = []
for paper in papers_data[:15]:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    header_text = text[:500]
    
    # Year
    years = re.findall(r'20\d{2}', header_text)
    year = int(years[0]) if years else 0
    
    # Empirical
    # Check lowercase text for keywords
    text_lower = text.lower()
    found_keywords = [k for k in keywords if k in text_lower]
    is_empirical = len(found_keywords) > 0
    
    debug_info.append({
        "title": title,
        "year": year,
        "is_empirical": is_empirical,
        "found_keywords": found_keywords
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2080358657401428239': 'file_storage/function-call-2080358657401428239.json', 'var_function-call-4922993133298785860': ['paper_docs'], 'var_function-call-4922993133298782503': ['Citations', 'sqlite_sequence'], 'var_function-call-15480292294165083401': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10316404265600385483': 'file_storage/function-call-10316404265600385483.json', 'var_function-call-8350695654712224507': [{'count(*)': '1405'}], 'var_function-call-8765785804266825960': 'file_storage/function-call-8765785804266825960.json', 'var_function-call-8765785804266823925': 'file_storage/function-call-8765785804266823925.json', 'var_function-call-5730915488565907792': [], 'var_function-call-5254736183491458142': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}], 'var_function-call-15128375922083714200': {'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years_found': ['2015']}}

exec(code, env_args)
