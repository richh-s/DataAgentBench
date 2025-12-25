code = """import json
import re

file_path = locals()['var_function-call-3852726166998737923']
with open(file_path, 'r') as f:
    articles = json.load(f)

tech_pattern = r"\b(science|technology|tech|computer|software|hardware|internet|web|online|digital|phone|mobile|wireless|gadget|device|robot|space|nasa|astronomy|biology|physics|chemistry|research|study|lab|scientist|microsoft|apple|google|intel|ibm|hp|dell|gameboy|nintendo|sony|console|video game|hacker|virus|security|broadband|satellite|engine|motor|battery|energy|solar|nuclear|stem cell|genetics|medical|disease|health|diabetes|cancer|browser|server|linux|windows|mac|ipod|mp3|dvd|chip|semiconductor|telecom|nanotech|biotech|innovation|telescope|mars|moon|rocket|astronaut|discovery|experiment|silicon|cyber|spam|blog|network|program|code|app|gps|search|yahoo|amazon|facebook|twitter|youtube|skype|wifi|bluetooth|firefox|shuttle|orbit|launch|probe|capsule|gene|genome|clone|vodafone|verizon|nokia|motorola|samsung|blackberry|itunes|paypal|ebay|email)\b"
business_pattern = r"\b(business|economy|market|stock|share|trade|finance|bank|money|currency|tax|profit|revenue|loss|company|firm|industry|ceo|deal|merger|acquisition|price|sales|oil|invest|wall street|nasdaq|dividend|bond|ipo|budget|gdp|recession|job|strike|retail|fed|loan|debt|bankruptcy|earnings)\b"
sports_pattern = r"\b(sport|game|match|cup|league|team|player|coach|win|lose|score|victory|defeat|football|soccer|basketball|baseball|tennis|golf|cricket|rugby|hockey|racing|f1|olympic|champion|stadium|nfl|nba|mlb|nhl|fifa|goal|medal|world cup|super bowl|season|roster|liverpool|schumacher|gerrard)\b"
world_pattern = r"\b(world|country|government|president|minister|parliament|law|war|military|police|attack|bomb|peace|un|eu|crisis|election|vote|candidate|party|troops|kill|death|iraq|iran|china|russia|usa|uk|israel|palestine)\b"

tech_count = 0
total = len(articles)
tech_list = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    s_tech = len(re.findall(tech_pattern, text))
    s_business = len(re.findall(business_pattern, text))
    s_sports = len(re.findall(sports_pattern, text))
    s_world = len(re.findall(world_pattern, text))
    
    # Classification
    cat = "Other"
    scores = {'Tech': s_tech, 'Business': s_business, 'Sports': s_sports, 'World': s_world}
    max_score = max(scores.values())
    
    if max_score > 0:
        candidates = [k for k, v in scores.items() if v == max_score]
        if len(candidates) == 1:
            cat = candidates[0]
        else:
            # Tie breaking
            if 'Tech' in candidates:
                if 'Business' in candidates:
                    # Prefer Business if financial terms
                    if re.search(r"\b(profit|revenue|loss|stock|market|merger)\b", text):
                        cat = 'Business'
                    else:
                        cat = 'Tech'
                elif 'Sports' in candidates:
                    # Prefer Sports if sports terms
                    if re.search(r"\b(nba|nfl|f1|racing|cup|league|team|win|game)\b", text):
                        cat = 'Sports'
                    else:
                        cat = 'Tech'
                elif 'World' in candidates:
                    # Prefer World if war/politics
                    if re.search(r"\b(war|president|minister|iraq|bomb)\b", text):
                        # Exception for Science in Iraq
                        if "science" in text or "research" in text:
                            cat = 'Tech'
                        else:
                            cat = 'World'
                    else:
                        cat = 'Tech'
                else:
                    cat = 'Tech'
            else:
                cat = candidates[0]
    
    if cat == 'Tech':
        tech_count += 1
        tech_list.append(art['title'])

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "tech_count": tech_count,
    "tech_list": tech_list
}))"""

env_args = {'var_function-call-1939965024232050517': [{'author_id': '218'}], 'var_function-call-15785083742190214670': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1096118954770325202': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-13750603828789518820': [{'_id': '6944ab0566db455b35c33c29', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ab0566db455b35c343da', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ab0566db455b35c34685', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ab0566db455b35c34714', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ab0566db455b35c348e4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-14990188966118478174': {'total': 5, 'tech_count': 3, 'tech_list': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award']}, 'var_function-call-3087470294558324779': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-3852726166998737923': 'file_storage/function-call-3852726166998737923.json', 'var_function-call-9830523105875136141': {'total': 111, 'tech_count': 20, 'tech_list': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Microsoft settles with UK phone maker', 'Liverpool prepares for life without Gerrard', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'FCC Approves Merger, Wireless Giant Created', 'Revealed: why the fear factor runs with the pack', "Cherkasky says Marsh may settle Spitzer's lawsuit within a month", "Blunkett denies visa 'fast-track'", 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', 'Paypal and Apple iTunes link-up', 'Bush Ordering Better Ocean Oversight (AP)', 'Schumacher in uncharted territory', 'Log on to be a satellite spy']}, 'var_function-call-1727543197329096109': {'total': 111, 'tech_count': 16, 'tech_list': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Revealed: why the fear factor runs with the pack', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', 'NBA Wrap: McGrady Leads Rockets to Stunning Win', 'Paypal and Apple iTunes link-up', 'Schumacher in uncharted territory', 'Log on to be a satellite spy'], 'unknown_list': []}, 'var_function-call-15716421149111189476': {'total': 111, 'tech_count': 48, 'tech_list': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'Somalians sworn in', 'Muenzer races for gold', 'Israelis to Expand West Bank Settlements', 'WTO Rejects U.S. Appeal on Canadian Wheat', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'Giants gain on Dodgers', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Charging Els moves to the top', 'Finance Leaders Urge Vigilance on Terror (Reuters)', 'German food retailer Spar sells 50-pct stake in Netto discount to ITM (AFP)', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Man remanded over Danielle murder', 'Two Soldiers Die After Crash in Iraq', "'Treasure hunt' for bandit's loot", 'Citigroup Says SEC May Take Action Against Jones (Update6)', 'Burma army intelligence  #39;purged #39;', 'Brazilian GP Race Report: Montoya claims first win of 2004', 'Clinton jumps into campaign, as missing explosives force Bush on defensive (AFP)', 'FCC Approves Merger, Wireless Giant Created', 'Satellite write-downs widen DirecTV #39;s loss', 'Israel to free Egyptian students: Cairo media', 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'Revealed: why the fear factor runs with the pack', "Cherkasky says Marsh may settle Spitzer's lawsuit within a month", 'Call Service with a Sneer (Reuters)', "Blunkett denies visa 'fast-track'", 'Death toll rises to 63 in Shaanxi coalmine explosion', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "'Tis the season to be greeted with silliness", "EBay Adds 'Want It Now' Feature (Reuters)", 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Bush Ordering Better Ocean Oversight (AP)', 'Peace delegation leaves Najaf empty-handed as fighting continues', 'Karzai deputy escapes a roadside bombing', 'Hendrick Motorsports', 'Log on to be a satellite spy']}}

exec(code, env_args)
