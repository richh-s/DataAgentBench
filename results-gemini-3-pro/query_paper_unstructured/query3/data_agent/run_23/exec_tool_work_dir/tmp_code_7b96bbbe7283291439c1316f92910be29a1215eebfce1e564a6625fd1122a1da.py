code = """import json
import re

file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

valid_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Search in first 5000 chars
    chunk = text[:5000]
    
    # Look for specific patterns first
    # Copyright 20xx
    copyright_years = re.findall(r'Copyright \d{0,4} ?(?:ACM|IEEE)? ?(20\d{2})', chunk, re.IGNORECASE)
    
    # Conference patterns: CHI 2018, Ubicomp 2019, etc.
    conf_years = re.findall(r'(?:CHI|UbiComp|CSCW|DIS|IUI|ISWC) \'?(\d{2,4})', chunk, re.IGNORECASE)
    
    # Just years
    all_years = re.findall(r'\b(20\d{2})\b', chunk)
    
    # Logic:
    # If copyright year found, use it.
    # Else if conf year found, use it (fix 2-digit years).
    # Else use max of all years (risky).
    
    pub_year = 0
    
    if copyright_years:
        pub_year = int(copyright_years[0])
    elif conf_years:
        y = int(conf_years[0])
        if y < 100: y += 2000
        pub_year = y
    else:
        # Filter all_years to be reasonable (e.g. not 2099)
        # And maybe take the one that appears in a date line?
        # "September 2018"
        # Let's take the max year < 2026 found in the chunk.
        valid_ys = [int(y) for y in all_years if 2000 <= int(y) <= 2025]
        if valid_ys:
            pub_year = max(valid_ys) # Risky, might catch a reference
    
    debug_info.append({"title": title, "pub_year": pub_year})
    
    if pub_year > 2016:
        valid_titles.append(title)

print("__RESULT__:")
print(json.dumps(valid_titles))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json', 'var_function-call-7940884221126680243': [], 'var_function-call-10237573905537353095': {'count': 5, 'first_paper_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'first_filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}}

exec(code, env_args)
