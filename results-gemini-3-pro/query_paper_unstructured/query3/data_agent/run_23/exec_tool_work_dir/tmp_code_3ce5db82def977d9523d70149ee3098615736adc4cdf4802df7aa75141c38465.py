code = """import json
import re

file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

valid_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    chunk = text[:5000]
    
    # Regex: Copyright followed by optional chars and year
    # pattern: Copyright.*(20\d\d)
    # We use simple pattern to avoid escaping hell
    # finding 'Copyright ... 2018'
    
    # simple search for year
    # Look for "Copyright 20xx"
    # In python string: "Copyright \\d{0,4} ?(?:ACM|IEEE)? ?(20\\d{2})"
    # In JSON: "Copyright \\\\d{0,4} ?(?:ACM|IEEE)? ?(20\\\\d{2})"
    
    # Let's try to just find all years and use heuristics without complex regex if possible
    # Or just use the regex with correct escaping.
    
    # Pattern: \b(20\d{2})\b
    # Python: r'\\b(20\\d{2})\\b'
    
    years_strs = re.findall(r'\b(20\d{2})\b', chunk)
    years = [int(y) for y in years_strs if 2000 <= int(y) <= 2025]
    
    pub_year = 0
    if years:
        # Heuristic: if "2018" is in years, and max is 2018, likely 2018.
        # But if we have 2015 and 2018, likely 2018 (pub year) vs 2015 (reference).
        pub_year = max(years)
        
    if pub_year > 2016:
        valid_titles.append(title)

print("__RESULT__:")
print(json.dumps(valid_titles))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json', 'var_function-call-7940884221126680243': [], 'var_function-call-10237573905537353095': {'count': 5, 'first_paper_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'first_filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}}

exec(code, env_args)
