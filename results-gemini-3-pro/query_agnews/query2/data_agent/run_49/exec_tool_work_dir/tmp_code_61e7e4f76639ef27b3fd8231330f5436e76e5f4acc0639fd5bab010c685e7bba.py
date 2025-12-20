code = """import json
import string

# Load articles
file_path = locals()['var_function-call-13320926440093840629']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Strong Keywords
strong_sports = {
    "league", "championship", "olympics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "world cup", "super bowl", 
    "wimbledon", "nascar", "f1", "rugby", "cricket", "medals", "athlete", "tournament", "coach", "touchdown", 
    "quarterback", "goalkeeper", "striker", "midfielder", "defenseman", "pitcher", "batter"
}

strong_business = {
    "stock", "market", "revenue", "profit", "loss", "merger", "acquisition", "dow", "nasdaq", "wall street", 
    "economy", "financial", "shareholder", "dividend", "earnings", "quarterly", "buyout", "takeover", "ipo", 
    "inflation", "recession", "fed", "treasury", "bank", "investor", "currency", "exchange", "sales"
}

strong_sci_tech = {
    "science", "nasa", "space", "internet", "software", "hardware", "virus", "hacker", "robot", "biology", 
    "physics", "astronomy", "chemistry", "genetic", "stem cell", "cloning", "dna", "genome", "laboratory", 
    "scientist", "researcher", "browser", "spam", "spyware", "malware", "biotech", "nanotech", "gameboy", 
    "nintendo", "sony", "xbox", "console", "videogame", "broadband", "wireless", "mobile phone", "satellite", 
    "microsoft", "google", "apple", "linux", "windows", "intel", "ibm", "computing", "digital", "tech"
}

# Weak Keywords (for fallback)
weak_sports = {"game", "match", "team", "player", "score", "win", "lose", "sport", "play", "club"}
weak_business = {"business", "company", "firm", "deal", "contract", "price", "cost", "money", "pay"}
weak_sci_tech = {"web", "net", "app", "device", "system", "program", "code", "file", "link", "online", "computer", "phone"}
weak_world = {"world", "war", "peace", "government", "president", "country", "law", "police", "attack", "election"}

def clean_text(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return text.split()

def classify(article):
    text_str = (article.get('title', '') + ' ' + article.get('description', ''))
    words = clean_text(text_str)
    
    # Check strong keywords
    s_strong = sum(1 for w in words if w in strong_sports)
    b_strong = sum(1 for w in words if w in strong_business)
    st_strong = sum(1 for w in words if w in strong_sci_tech)
    
    # Priority: Sports > Business > Sci/Tech
    # But we need to compare counts.
    
    # If "Space Probe Fails" -> st_strong=1 ("space"). s_strong=0. b_strong=0. -> Sci/Tech.
    # If "Chinese Firm To Buy IBM's PC Business" -> b_strong=0? ("business" is weak? No, let's check).
    # "business" is in weak_business. "buy" is weak.
    # "IBM" is strong_sci_tech.
    # So it might be Sci/Tech?
    # I should add "business" to strong_business? No, "business" is too generic.
    # "acquisition" is strong. "buy" is weak.
    # In the title: "Chinese Firm To Buy IBM's PC Business For $1.75 Billion".
    # "billion" -> should be strong business?
    
    # Let's adjust strong_business.
    
    if "billion" in words or "million" in words:
        b_strong += 1
    if "deal" in words:
        b_strong += 0.5
        
    # Scores
    scores = {
        "Sports": s_strong * 2,
        "Business": b_strong * 2,
        "Science/Technology": st_strong * 2
    }
    
    # Fallback to weak keywords if all zero
    if all(v == 0 for v in scores.values()):
        s_weak = sum(1 for w in words if w in weak_sports)
        b_weak = sum(1 for w in words if w in weak_business)
        st_weak = sum(1 for w in words if w in weak_sci_tech)
        w_weak = sum(1 for w in words if w in weak_world)
        
        scores["Sports"] += s_weak
        scores["Business"] += b_weak
        scores["Science/Technology"] += st_weak
        scores["World"] = w_weak # World only competes in weak phase
        
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "World"
        
    return best

sci_tech_titles = []
for a in articles:
    cat = classify(a)
    if cat == "Science/Technology":
        sci_tech_titles.append(a['title'])

result = {
    "count": len(sci_tech_titles),
    "total": len(articles),
    "titles": sci_tech_titles,
    "fraction": len(sci_tech_titles) / len(articles) if len(articles) > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17731222421355545554': [{'author_id': '218'}], 'var_function-call-10772589579831415629': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1499085717710810079': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-2672201808982955812': [{'_id': '6944bfacff70ed2d3ca442b9', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bfacff70ed2d3ca44a6a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bfacff70ed2d3ca44d15', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bfacff70ed2d3ca44da4', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bfacff70ed2d3ca44f74', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-14450440653002166621': {'total': 5, 'sci_tech_count': 2, 'sci_tech_titles': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award'], 'other_examples': [['GameBoy mini-games win prize', 'Sports'], ['Bailey Tries WR', 'Business'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-13320926440093840629': 'file_storage/function-call-13320926440093840629.json', 'var_function-call-16312177675477890472': {'count': 0, 'total': 111, 'titles': []}, 'var_function-call-3612848950533246018': [{'title': 'GameBoy mini-games win prize', 'text': 'gameboy mini-games win prize a set of gameboy micro-games is named as the most innovative game of the year at a festival in scotland.', 'words': [], 's_score': 0}, {'title': 'Bailey Tries WR', 'text': "bailey tries wr pro bowl cornerback champ bailey practiced with the offense at wide reciever during the denver broncos' practice on tuesday.", 'words': [], 's_score': 0}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'text': 'students win \\$100,000 in national team science competition lucie guo, motivated by the death of her grandfather in china before she was born, spent two summers doing research in a duke university laboratory.', 'words': [], 's_score': 0}, {'title': 'Energy from waves  teenager wins science award', 'text': 'energy from waves  teenager wins science award a teenager from the san diego, california area has won the siemens westinghouse competition in math, science and technology for his  quot;gyro-gen, quot; a machine that produces electricity from ocean waves.', 'words': [], 's_score': 0}, {'title': 'China #39;s appetite boosts BHP', 'text': 'china #39;s appetite boosts bhp bhp billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. ', 'words': [], 's_score': 0}], 'var_function-call-6982956827147498695': {'count': 25, 'total': 111, 'titles': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Liverpool prepares for life without Gerrard', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'FCC Approves Merger, Wireless Giant Created', 'Satellite write-downs widen DirecTV #39;s loss', 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'Revealed: why the fear factor runs with the pack', 'Rams not in Pack #39;s league', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "EBay Adds 'Want It Now' Feature (Reuters)", 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy'], 'fraction': 0.22522522522522523}}

exec(code, env_args)
