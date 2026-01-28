code = """import json
import re

# Load citations
with open(locals()['var_function-call-4239113770536719479'], 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2195288999403441372'], 'r') as f:
    papers = json.load(f)

paper_map = {p['filename']: p['text'] for p in papers}

results = []

for citation in citations[:20]:
    title = citation['title']
    filename = title + ".txt"
    venue = "Unknown"
    snippet = ""
    if filename in paper_map:
        text = paper_map[filename]
        snippet = text[:100].replace("\n", " ")
        
        # Detection
        header = text[:5000]
        if re.search(r'Human Factors in Computing Systems', header, re.IGNORECASE):
            venue = "CHI (Human Factors)"
        elif re.search(r'\bCHI\b', header):
             venue = "CHI (regex)"
        elif "UBICOMP" in header.upper():
            venue = "UbiComp"
        elif "CSCW" in header.upper():
            venue = "CSCW"
        elif "DIS '" in header.upper() or "DIS 20" in header.upper():
            venue = "DIS"
            
    results.append({"title": title, "venue": venue, "snippet": snippet})

# Also find which one was identified as CHI before
chi_found = []
for citation in citations:
    title = citation['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        header = text[:2000]
        if re.search(r'Human Factors in Computing Systems', header, re.IGNORECASE) or re.search(r'\bCHI\b', header):
             chi_found.append(title)

print("__RESULT__:")
print(json.dumps({"sample_results": results, "chi_found_list": chi_found}))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json', 'var_function-call-5140237096160835583': 'file_storage/function-call-5140237096160835583.json', 'var_function-call-13183044506038404940': 'file_storage/function-call-13183044506038404940.json', 'var_function-call-17837509656361549464': 'file_storage/function-call-17837509656361549464.json', 'var_function-call-11481915050006868588': {'total_citations': 0, 'missing_count': 184}, 'var_function-call-2195288999403441372': 'file_storage/function-call-2195288999403441372.json', 'var_function-call-8471152419459222340': {'total_citations': 16, 'chi_papers_count': 1}, 'var_function-call-13216662641955124697': [{'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'header': 'Sundroid: Solar Radiation Awareness with Smartphones∗\n\nThomas Fahrni, Michael Kuhn, Philipp Sommer, Roger Wattenhofer, and Samuel Welten\nComputer Engineering and Networks Laboratory\nETH Zurich, Switzerland\nﬁrstname.lastname@tik.ee.ethz.ch\n\nABSTRACT\nWhile the sun is important for our health, overexpo'}, {'title': 'Why We Use and Abandon Smart Devices', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nWhy We Use and Abandon Smart Devices \n\nAmanda Lazar \nUniversity of Washington \nalaz@uw.edu \n\nChristian Koehler \nCarnegie Mellon University \nckoehler@andrew.cmu.edu \n\nTheresa Jean Tanenbaum \nUniversity of California, Irvine \nttanen@uci.edu \n\nDavid H. N"}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'header': '\n\nOne Step Forward, Two Steps Back: The Key to \nWearables in the Field is the App \n\nBliss Altenhoff, Haley Vaigneur and Kelly Caine \nDepartment of Psychology, Department of Industrial Engineering, School of Computing \nClemson University \nClemson, United States \n{blissw, hvagine, caine} @clemson.edu '}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'header': 'I’ll Be Back: On the Multiple Lives of Users\nof a Mobile Activity Tracking Application\n\nZhiyuan Lin\nStanford University\nzylin@cs.stanford.edu\n\nTim Althoff\nStanford University\nalthoff@cs.stanford.edu\n\nJure Leskovec\nStanford University\njure@cs.stanford.edu\n\nABSTRACT\nMobile health applications that tra'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}]}

exec(code, env_args)
