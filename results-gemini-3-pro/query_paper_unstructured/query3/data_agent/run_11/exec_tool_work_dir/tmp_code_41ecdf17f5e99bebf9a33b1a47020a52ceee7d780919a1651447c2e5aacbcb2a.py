code = """import json
import re

papers_path = locals()['var_function-call-15031094012965990615']
with open(papers_path, 'r') as f:
    papers = json.load(f)

filtered_papers = []

print("__RESULT__:")
print("Papers published after 2016:")

for p in papers:
    text = p['text']
    title = p['filename'].replace('.txt', '')
    
    # Extract year: search for 20xx in the first 1000 characters
    # Usually year is in the conference header
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    year = 0
    if years:
        # Take the first year found, or the one that seems most like a publication year (often repeated or near conference name)
        # But simply taking the first one is a good heuristic for headers like "CHI '19, May 4-9, 2019..."
        year = int(years[0])
    
    if year > 2016:
        # Check for empirical keywords in the whole text? 
        # Or check if "contribution" field is extractable?
        # Let's print the title and whether "empirical" is in the text
        is_empirical = "empirical" in text.lower()
        print(f"Title: {title}, Year: {year}, Has 'empirical': {is_empirical}")
        
        # Let's also check for "Contribution" section
        if "contribution" in text.lower()[:2000]:
             print(f"  (Contains 'contribution' in first 2000 chars)")

        filtered_papers.append({"title": title, "year": year})

print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-8030909776315158463': ['paper_docs'], 'var_function-call-8030909776315156092': ['Citations', 'sqlite_sequence'], 'var_function-call-4351617937578896443': 'file_storage/function-call-4351617937578896443.json', 'var_function-call-2229391005563320550': 'file_storage/function-call-2229391005563320550.json', 'var_function-call-17004659255608822319': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their lived informatics experiences. We develop a \nmodel characterizing tracker processes of deciding to track \nand selecting a tool, elaborate on tool usage during collection, \nintegration,  and  reflection  as  components  of  tracking  and \nacting,  and  discuss  the  lapsing  and  potential  resuming  of \ntracking.  We  use  our  model  to  surface  underexplored \nchallenges  in  lived  informatics,  thus  identifying  future \ndirections for personal informatics design and research.  \n\nAuthor Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  Personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  or  tracking ", 'var_function-call-3120155277340519594': "e. Forbes. \nhttp://www.forbes.com/sites/parmyolson/2014/06/19/ \nwearable-tech-health-insurance/. \n\n741\n\n \n \n\x0cUBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\n30.  Page, X. and Kobsa, A. Navigating the Social Terrain \nwith Google Latitude. iConference 2010, 174-178. \n\n31.  Powers, W.T. Behavior: The Control of Perception. \n\nBenchmark Publications, 2005. \n\n32.  Prochaska, J.O. and Velcier, W.F. The Transtheoretical \n\nModel of Health Behavior Change. American Journal \nof Health Promotion 12, 1 (1997), 38-48. \n\n33.  Rahman, T., Adams, A.T., Zhang, M., Cherry, E., \n\nZhou, B., Peng, H., and Choudhury, T. BodyBeat\u2009: A \nMobile System for Sensing Non-Speech Body Sounds. \nMobiSys 2014, 2-13. \n\n34.  Rooksby, J., Rost, M., Morrison, A., and Chalmers, M. \nPersonal Tracking as Lived Informatics. CHI 2014, \n1163-1172. \n\n35.  Schoenebeck, S.Y. Giving up Twitter for Lent: How \nand Why We Take Breaks from Social Media. \nCHI 2014, 773-782. \n\n36.  Schön, D.A. The Reflective Practitioner. Basic Books, \n\n1983. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c", 'var_function-call-15031094012965990615': 'file_storage/function-call-15031094012965990615.json', 'var_function-call-15031094012965993894': 'file_storage/function-call-15031094012965993894.json'}

exec(code, env_args)
