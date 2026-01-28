code = """import json

with open(locals()['var_function-call-4161258242438240829'], 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Truncate at References
    # Case insensitive search for references
    # Look for "\nREFERENCES" or "\nReferences"
    # To be safe, find the last occurrence? Or the first on a line by itself?
    # Usually references are at the end.
    # Simple heuristic: Split by "REFERENCES" and take the first part.
    # But "references" word might appear in text.
    # Look for "REFERENCES" in upper case or "References" at start of line.
    
    body_text = text
    if "\nREFERENCES" in text:
        body_text = text.split("\nREFERENCES")[0]
    elif "\nReferences" in text:
        body_text = text.split("\nReferences")[0]
        
    # Detect Year (using original text or header)
    # The header is at the top.
    header = text[:1000]
    year = None
    if "2016" in header or "'16" in header or "Copyright 2016" in text[:3000]:
        year = 2016
    elif "2015" in header or "'15" in header:
        year = 2015
    elif "2019" in header:
        year = 2019
        
    # Check Domain in body_text
    if "physical activity" in body_text.lower():
        is_pa = True
    else:
        is_pa = False
        
    if year == 2016 and is_pa:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-18065361926361048824': 'file_storage/function-call-18065361926361048824.json', 'var_function-call-1502338921683613399': 'file_storage/function-call-1502338921683613399.json', 'var_function-call-4041748401913796717': [], 'var_function-call-2901872464972295904': [], 'var_function-call-12598558614972453544': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'], 'var_function-call-5379995669479938539': [], 'var_function-call-3504084481303803347': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-964086390390166412': {'2015': 1, '2019': 4}, 'var_function-call-15929576778750581044': 5, 'var_function-call-4161258242438240829': 'file_storage/function-call-4161258242438240829.json', 'var_function-call-15116999913814572746': 'file_storage/function-call-15116999913814572746.json', 'var_function-call-13249832550195431330': ['Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space'], 'var_function-call-9342671946872190788': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}], 'var_function-call-17940423380245423671': 'veritt, Ian Smith and \n\nJames A. Landay. 2006. Design requirements for \ntechnologies that encourage physical activity. \nIn Proceedings of the SIGCHI conference on Human \nFactors in computing systems ('}

exec(code, env_args)
