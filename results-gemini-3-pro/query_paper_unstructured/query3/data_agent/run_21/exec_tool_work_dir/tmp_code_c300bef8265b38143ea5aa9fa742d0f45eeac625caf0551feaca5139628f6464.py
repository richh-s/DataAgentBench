code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-8978544678357083899'], 'r') as f:
    papers = json.load(f)

def extract_year_robust(text):
    # Find all 4-digit numbers starting with 20
    matches = re.findall(r'(20\d{2})', text)
    # Filter reasonable range (e.g., 2010-2025)
    valid_years = [int(y) for y in matches if 2010 <= int(y) <= 2025]
    if not valid_years:
        return None
    # Heuristic: The publication year is often early in the text (header) or in copyright notice.
    # It is usually the *earliest* valid year mentioned? No, references might have earlier years.
    # It is usually the *latest* valid year mentioned? No, future work or citation of upcoming?
    # Actually, the copyright year is usually the publication year.
    # Look for "Copyright ... 20xx"
    # Or "CHI 20xx"
    
    # Let's try to find year in first 2000 chars.
    head = text[:2000]
    head_matches = re.findall(r'(20\d{2})', head)
    valid_head_years = [int(y) for y in head_matches if 2010 <= int(y) <= 2025]
    
    if valid_head_years:
        # Return the most common one in head? Or just the first one?
        # In "UBICOMP '15 ... 2015", 2015 appears.
        # In "Copyright 2015", 2015 appears.
        return valid_head_years[0]
    
    # If not in head, look for copyright in the end?
    # Or just return the most common year in the whole text?
    c = Counter(valid_years)
    return c.most_common(1)[0][0]

debug_info = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    year = extract_year_robust(p['text'])
    has_empirical = "empirical" in p['text'].lower()
    debug_info.append({"title": title, "year": year, "has_empirical": has_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15050569047067534700': 'file_storage/function-call-15050569047067534700.json', 'var_function-call-3142892684795704503': 'file_storage/function-call-3142892684795704503.json', 'var_function-call-8978544678357083899': 'file_storage/function-call-8978544678357083899.json', 'var_function-call-9130584372251179173': 'file_storage/function-call-9130584372251179173.json', 'var_function-call-5001071914055655965': [], 'var_function-call-15001692400345327096': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-684904427441614468': {'A Lived Informatics Model of Personal Informatics.txt': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}}

exec(code, env_args)
