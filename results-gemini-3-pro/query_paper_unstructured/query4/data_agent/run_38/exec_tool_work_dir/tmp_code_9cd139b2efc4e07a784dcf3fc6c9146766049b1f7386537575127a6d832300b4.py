code = """import json

with open(locals()['var_function-call-4534989108856043984'], 'r') as f:
    paper_docs = json.load(f)

matches = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if 'physical activity' in text.lower():
        # Find year indicators
        year_hit = "Unknown"
        if "2016" in text:
            year_hit = "Found 2016"
            # Extract snippet around 2016
            idx = text.find("2016")
            snippet = text[max(0, idx-50):min(len(text), idx+50)].replace(chr(10), " ")
            year_hit += f": ...{snippet}..."
        elif "2015" in text:
            year_hit = "Found 2015"
        
        matches.append({"title": filename, "year_check": year_hit})

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-8115990490355926110': 'file_storage/function-call-8115990490355926110.json', 'var_function-call-15132226113380290757': 'file_storage/function-call-15132226113380290757.json', 'var_function-call-4534989108856043984': 'file_storage/function-call-4534989108856043984.json', 'var_function-call-280795814972665149': 'file_storage/function-call-280795814972665149.json', 'var_function-call-6662066494306016302': [], 'var_function-call-3983899214788075315': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics   Daniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2  1Computer Science & Engineering, 2Human Centered Design & Engineering  DUB Group, University of Washington  {depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Human Computer Interaction Institute, 2School of Design  Carnegie Mellon University, Pittsburgh, PA 15213  ianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu   ABSTRACT  People  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Animated Movies for Self-reﬂection Veronica Crista LaBelle MIT Cambridge, MA, USA vlabelle@mit.edu Rosalind W. Picard MIT Media Lab Cambridge, MA, USA picard@media.mit.edu  Emily Christen Yue Harvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  conditi'}]}

exec(code, env_args)
