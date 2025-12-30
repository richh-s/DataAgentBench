code = """import json
import re

# Load the paper docs
file_path = locals()['var_function-call-1738558855187005080']
with open(file_path, 'r') as f:
    papers = json.load(f)

extracted_data = []

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # 1. Extract Year
    # Look for Copyright year first
    copyright_match = re.search(r'Copyright\s+(?:©\s+)?(20\d{2})', text[:3000], re.IGNORECASE)
    venue_match = re.search(r"'\d{2}", text[:500]) # e.g. '15
    
    year = None
    if copyright_match:
        year = int(copyright_match.group(1))
    else:
        # Try to find any 20xx in the first 500 chars
        years = re.findall(r'20\d{2}', text[:1000])
        if years:
            # Pick the most common or just the first reasonable one?
            # Usually the first one is the conference date
            year = int(years[0])
        elif venue_match:
            # e.g. '15 -> 2015
            y = int(venue_match.group(0)[1:])
            year = 2000 + y

    # 2. Extract Contribution (check for 'empirical')
    is_empirical = 'empirical' in text.lower()
    
    extracted_data.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

print("__RESULT__:")
print(json.dumps(extracted_data))"""

env_args = {'var_function-call-9660472287118385372': ['paper_docs'], 'var_function-call-9660472287118386283': ['Citations', 'sqlite_sequence'], 'var_function-call-3569571174056930094': 'file_storage/function-call-3569571174056930094.json', 'var_function-call-4984347876536047178': "e. Forbes. \nhttp://www.forbes.com/sites/parmyolson/2014/06/19/ \nwearable-tech-health-insurance/. \n\n741\n\n \n \n\x0cUBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\n30.  Page, X. and Kobsa, A. Navigating the Social Terrain \nwith Google Latitude. iConference 2010, 174-178. \n\n31.  Powers, W.T. Behavior: The Control of Perception. \n\nBenchmark Publications, 2005. \n\n32.  Prochaska, J.O. and Velcier, W.F. The Transtheoretical \n\nModel of Health Behavior Change. American Journal \nof Health Promotion 12, 1 (1997), 38-48. \n\n33.  Rahman, T., Adams, A.T., Zhang, M., Cherry, E., \n\nZhou, B., Peng, H., and Choudhury, T. BodyBeat\u2009: A \nMobile System for Sensing Non-Speech Body Sounds. \nMobiSys 2014, 2-13. \n\n34.  Rooksby, J., Rost, M., Morrison, A., and Chalmers, M. \nPersonal Tracking as Lived Informatics. CHI 2014, \n1163-1172. \n\n35.  Schoenebeck, S.Y. Giving up Twitter for Lent: How \nand Why We Take Breaks from Social Media. \nCHI 2014, 773-782. \n\n36.  Schön, D.A. The Reflective Practitioner. Basic Books, \n\n1983. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c", 'var_function-call-1738558855187005080': 'file_storage/function-call-1738558855187005080.json', 'var_function-call-6817887731850724700': 5}

exec(code, env_args)
