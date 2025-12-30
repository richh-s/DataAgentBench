code = """import json

# Load the result from the previous large query
with open(locals()['var_function-call-205188535857108763'], 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '').lower()
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    reason = None
    
    # 1. Title Check
    if 'food' in title.lower():
        reason = 'Title'
        
    # 2. Keywords Check
    if not reason:
        # Simple heuristic for keywords: Look for 'keywords' line and check context
        # Check first 5000 chars to avoid scanning references
        header = text[:5000]
        if 'keywords' in header:
            # Find the index of 'keywords'
            k_idx = header.find('keywords')
            # Look at the next 500 chars
            k_context = header[k_idx:k_idx+500]
            if 'food' in k_context:
                reason = 'Keywords'
    
    # 3. Abstract Check?
    # Usually Abstract is near the top.
    # If "food" is in the first 2000 chars, it's a strong signal?
    # But we saw "food" in introduction as citation.
    # Let's be strict first: Title or Keywords.
    
    if reason:
        food_papers.append({"title": title, "reason": reason})

print('__RESULT__:')
print(json.dumps(food_papers))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json', 'var_function-call-12574282544977898815': [], 'var_function-call-11433524787453468215': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-4825611475060270292': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-205188535857108763': 'file_storage/function-call-205188535857108763.json', 'var_function-call-2821502025567842666': [{'count(*)': '1405'}]}

exec(code, env_args)
