code = """import json
import re

with open(locals()['var_function-call-9752705045220679725'], 'r') as f:
    docs = json.load(f)

debug_info = []

venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
venue_pattern = r"(" + "|".join(venues) + r").{0,10}'(\d{2})"

for doc in docs[:5]:
    text = doc['text']
    header_text = text[:3000]
    
    # Year Extraction
    matches_year = re.findall(r'20\d{2}', header_text)
    
    # Venue Year Extraction (e.g. Ubicomp '15)
    matches_venue_year = re.findall(venue_pattern, header_text, re.IGNORECASE)
    
    # Contribution "Empirical" check
    has_empirical = 'empirical' in text.lower()
    
    # Check for "Contribution" context
    contrib_idx = text.lower().find('contribution')
    contrib_context = ""
    if contrib_idx != -1:
        contrib_context = text[contrib_idx:contrib_idx+100]
        
    debug_info.append({
        "title": doc['filename'],
        "all_years_found": matches_year,
        "venue_years_found": matches_venue_year,
        "has_empirical": has_empirical,
        "contrib_context": contrib_context
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17324318872041737699': 'file_storage/function-call-17324318872041737699.json', 'var_function-call-7414201362251444319': 'file_storage/function-call-7414201362251444319.json', 'var_function-call-9752705045220679725': 'file_storage/function-call-9752705045220679725.json', 'var_function-call-1938541816739605350': [], 'var_function-call-14592760295992219980': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'source': 'None', 'is_empirical': False, 'first_50_chars': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'source': 'Copyright', 'is_empirical': False, 'first_50_chars': 'A Stage-Based Model of Personal Informatics System'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'source': 'None', 'is_empirical': True, 'first_50_chars': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpe'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'source': 'None', 'is_empirical': True, 'first_50_chars': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'source': 'None', 'is_empirical': False, 'first_50_chars': 'ArmSleeve: a Patient Monitoring System to Support '}]}

exec(code, env_args)
