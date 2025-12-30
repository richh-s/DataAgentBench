code = """import json
import re

file_path = locals()['var_function-call-332077821725117771']
with open(file_path, 'r') as f:
    docs = json.load(f)

titles_2016 = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    
    # Check first 5000 chars for metadata
    header_text = text[:5000]
    
    is_2016 = False
    
    # Patterns
    # 1. Copyright 2016
    if re.search(r"Copyright\s*(©|\(c\)|@)?\s*2016", header_text, re.IGNORECASE):
        is_2016 = True
    # 2. Conference/Venue 2016
    # Matches "CHI 2016", "CHI '16", "UbiComp 2016", "UbiComp '16", etc.
    # Note: \b ensures we don't match "20160"
    elif re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH|UIST|MobileHCI)\s*['\u2019]?16\b", header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH|UIST|MobileHCI).*?2016", header_text, re.IGNORECASE):
        is_2016 = True
    
    # Exclude if it explicitly says another year in copyright or conference (to avoid false positives)
    # e.g. "Copyright 2018"
    if re.search(r"Copyright\s*(©|\(c\)|@)?\s*(2015|2017|2018|2019|2014)", header_text, re.IGNORECASE):
        # If we found a 2016 match but also a clear 2018 match, it's likely 2018.
        # But maybe the 2016 was a reference?
        # If "Copyright 2018" exists, it's 2018.
        is_2016 = False
    
    if is_2016:
        # Check domain "physical activity"
        if "physical activity" in text.lower():
            title = filename.replace('.txt', '')
            titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-13901959142060692971': 'file_storage/function-call-13901959142060692971.json', 'var_function-call-1843899810838592799': 'file_storage/function-call-1843899810838592799.json', 'var_function-call-332077821725117771': 'file_storage/function-call-332077821725117771.json', 'var_function-call-14032909272112886475': [], 'var_function-call-2674259236540270834': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e'}}

exec(code, env_args)
