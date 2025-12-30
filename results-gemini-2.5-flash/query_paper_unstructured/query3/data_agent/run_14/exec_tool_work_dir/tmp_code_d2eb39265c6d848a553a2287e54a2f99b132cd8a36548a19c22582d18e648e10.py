code = """import pandas as pd
import json
import re

# Load paper documents data
file_path_paper_docs = locals()['var_function-call-12891957927342614811']
with open(file_path_paper_docs, 'r') as f:
    paper_docs = json.load(f)

debug_years_data = []
# Process a sample of documents for debugging (e.g., first 100)
for doc in paper_docs[:100]: 
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    potential_years = []

    # Attempt to find 4-digit year in the first 2000 characters
    for match in re.finditer(r'\b(19|20)\d{2}\b', text[:2000]):
        current_year = int(match.group(0))
        if 1950 <= current_year <= 2024:  # Plausible year range
            potential_years.append(current_year)
    
    # If no 4-digit year, try to find 'YY format in the first 2000 characters
    if not potential_years:
        for match in re.finditer(r"'(\d{2})", text[:2000]):
            two_digit_year = int(match.group(1))
            # Heuristic for 2-digit to 4-digit year conversion
            if 0 <= two_digit_year <= 24: # e.g., '22 -> 2022
                potential_years.append(2000 + two_digit_year)
            elif 50 <= two_digit_year <= 99: # e.g., '98 -> 1998
                potential_years.append(1900 + two_digit_year)
    
    if potential_years:
        year = min(potential_years)

    debug_years_data.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(debug_years_data))"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json', 'var_function-call-2589591416908310925': [], 'var_function-call-13239531528128313526': [], 'var_function-call-835119119760637705': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-16986230209680427031': [], 'var_function-call-16617323784436067599': [], 'var_function-call-14351219517084226270': [], 'var_function-call-320867719890547711': [], 'var_function-call-17243782874587110711': [], 'var_function-call-10202973670430014698': [], 'var_function-call-15414146859521326470': 'file_storage/function-call-15414146859521326470.json', 'var_function-call-9425818148868776550': [], 'var_function-call-12608294071483797543': 'file_storage/function-call-12608294071483797543.json', 'var_function-call-6914328032805360955': [], 'var_function-call-8891258027671418511': [], 'var_function-call-7099604938380591321': [], 'var_function-call-12891957927342614811': 'file_storage/function-call-12891957927342614811.json', 'var_function-call-14820484231919104682': [], 'var_function-call-10820505087453654198': [{'title': 'A Lived Informatics Model of Personal Informatics', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'found_year': None, 'has_empirical_contribution': False}], 'var_function-call-9399836260284748412': [], 'var_function-call-14437775131078797157': [], 'var_function-call-8252736776323072349': [], 'var_function-call-17061380091064174368': []}

exec(code, env_args)
