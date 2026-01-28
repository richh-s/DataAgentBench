code = """import json
import re

papers_path = locals()['var_function-call-10894468654798374866']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

count_recent = 0
recent_papers = []

empirical_keywords = ["empirical", "user study", "participants", "interview", "survey", "field study", "experiment", "quantitative", "qualitative", "mixed methods"]

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    header_text = text[:2000]
    years = re.findall(r"20[1-2]\d", header_text)
    
    pub_year = 0
    if years:
        valid_years = [int(y) for y in years if 2010 <= int(y) <= 2025]
        if valid_years:
            pub_year = valid_years[0]
            
    if pub_year > 2016:
        count_recent += 1
        is_empirical = False
        content_to_check = text[:15000].lower()
        for kw in empirical_keywords:
            if kw in content_to_check:
                is_empirical = True
                break
        recent_papers.append({"title": filename, "year": pub_year, "is_empirical": is_empirical})

print(f"Papers > 2016: {count_recent}")
print(f"Details: {recent_papers}")

print("__RESULT__:")
print(json.dumps("Verification Complete"))"""

env_args = {'var_function-call-5623558947517056704': 'file_storage/function-call-5623558947517056704.json', 'var_function-call-4507795440507618758': 'file_storage/function-call-4507795440507618758.json', 'var_function-call-10894468654798374866': 'file_storage/function-call-10894468654798374866.json', 'var_function-call-7275202975009130922': [], 'var_function-call-8227419315527480326': 'Debug Complete', 'var_function-call-4398658037254991230': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': ['2015'], 'is_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'is_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'is_empirical': False}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': ['2019', '2019', '2019', '2019'], 'is_empirical': False}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_found': [], 'is_empirical': False}], 'var_function-call-6427018599709865135': 'Analysis Complete', 'var_function-call-13902414228898295954': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 266}]}

exec(code, env_args)
