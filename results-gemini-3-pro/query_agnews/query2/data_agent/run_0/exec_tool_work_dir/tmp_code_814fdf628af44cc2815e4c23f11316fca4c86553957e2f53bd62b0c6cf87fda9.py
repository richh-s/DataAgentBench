code = """import json
import re

file_path = locals()['var_function-call-7338206399480502302']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Weighted Keywords
# Format: "word": weight
# Categories: ST, Sports, Business, World

# Shared ambiguous words need context or low weight
# I'll define separate dictionaries and merge logic

st_weights = {
    'science': 5, 'technology': 5, 'tech': 4, 'computer': 4, 'software': 4, 'hardware': 4,
    'internet': 4, 'web': 3, 'online': 2, 'digital': 3, 'mobile': 3, 'wireless': 3,
    'broadband': 3, 'network': 3, 'satellite': 4, 'space': 4, 'nasa': 5, 'astronomy': 5,
    'galaxy': 4, 'planet': 4, 'mars': 4, 'robot': 4, 'ai': 4, 'gadget': 3, 'device': 2,
    'chip': 3, 'processor': 3, 'microsoft': 5, 'google': 5, 'apple': 3, 'ibm': 4,
    'intel': 4, 'linux': 4, 'windows': 3, 'mac': 2, 'video game': 5, 'gaming': 4,
    'nintendo': 5, 'sony': 3, 'xbox': 5, 'gameboy': 5, 'hacker': 4, 'virus': 3,
    'cyber': 4, 'data': 2, 'server': 4, 'cloud': 3, 'code': 2, 'app': 3, 'browser': 3,
    'search engine': 4, 'email': 3, 'spam': 3, 'blog': 3, 'facebook': 5, 'twitter': 5,
    'amazon': 3, 'yahoo': 4, 'physics': 5, 'biology': 5, 'chemistry': 5, 'genetics': 5,
    'medical': 3, 'research': 3, 'lab': 3, 'scientist': 4, 'engineer': 3, 'innovation': 2,
    'ipod': 5, 'gps': 4, 'telescope': 4, 'shuttle': 4, 'probe': 4, 'orbit': 3, 'moon': 2,
    'study': 1, 'university': 1, 'experiment': 3, 'drug': 2, 'cancer': 3, 'disease': 2,
    'fda': 2, 'health': 2, 'patient': 1, 'doctor': 1
}

sports_weights = {
    'sport': 5, 'football': 5, 'soccer': 5, 'basketball': 5, 'baseball': 5, 'tennis': 5,
    'golf': 5, 'hockey': 5, 'olympic': 5, 'championship': 4, 'tournament': 4, 'league': 4,
    'cup': 3, 'medal': 4, 'player': 2, 'coach': 3, 'team': 2, 'athlete': 3, 'stadium': 3,
    'match': 2, 'score': 2, 'win': 1, 'loss': 1, 'nfl': 5, 'nba': 5, 'mlb': 5, 'nhl': 5,
    'fifa': 5, 'nascar': 5, 'f1': 5, 'racing': 3, 'cricket': 5, 'rugby': 5, 'game': 1,
    'quarterback': 5, 'receiver': 3, 'pitcher': 4, 'homerun': 5, 'touchdown': 5,
    'gold': 2, 'silver': 2, 'bronze': 2, 'broncos': 5, 'bowl': 3, 'cornerback': 4,
    'pro bowl': 5, 'red sox': 5, 'yankees': 5, 'united': 1, 'real madrid': 5,
    'arsenal': 5, 'chelsea': 5, 'liverpool': 5, 'manchester': 4, 'club': 2,
    'season': 2, 'injury': 2, 'standings': 3, 'playoff': 4, 'final': 2
}

business_weights = {
    'business': 5, 'economy': 5, 'market': 4, 'stock': 5, 'trade': 4, 'company': 3,
    'profit': 4, 'loss': 2, 'bank': 4, 'finance': 5, 'dollar': 3, 'euro': 3, 'currency': 4,
    'oil': 4, 'gas': 3, 'energy': 3, 'price': 2, 'corp': 3, 'inc': 2, 'investment': 4,
    'investor': 4, 'share': 3, 'revenue': 4, 'sales': 2, 'deal': 2, 'merger': 4,
    'acquisition': 4, 'ceo': 4, 'cfo': 4, 'executive': 3, 'industry': 2, 'manufacturing': 3,
    'retail': 3, 'inflation': 5, 'fed': 4, 'rates': 3, 'wall street': 5, 'dow jones': 5,
    'nasdaq': 5, 'deficit': 4, 'budget': 3, 'spending': 2, 'consumer': 2, 'jobs': 3,
    'unemployment': 4, 'hiring': 2, 'earnings': 4, 'forecast': 2, 'quarter': 2
}

world_weights = {
    'world': 3, 'war': 5, 'peace': 4, 'politics': 5, 'president': 4, 'minister': 4,
    'government': 4, 'country': 2, 'nation': 2, 'iraq': 5, 'iran': 5, 'china': 4,
    'usa': 2, 'uk': 2, 'eu': 4, 'un': 5, 'treaty': 4, 'election': 5, 'vote': 3,
    'military': 4, 'army': 3, 'police': 3, 'attack': 3, 'bomb': 4, 'terrorism': 5,
    'disaster': 3, 'quake': 4, 'tsunami': 5, 'hurricane': 4, 'storm': 3, 'flood': 3,
    'kill': 2, 'die': 1, 'dead': 1, 'hostage': 5, 'baghdad': 5, 'kabul': 5, 'gaza': 5,
    'israel': 5, 'palestine': 5, 'nuclear': 4, 'prime minister': 5, 'parliament': 4,
    'official': 1, 'protest': 3, 'court': 2, 'law': 2, 'legal': 2, 'judge': 2,
    'senator': 4, 'congress': 4, 'bush': 3, 'kerry': 3, 'blair': 3, 'sharon': 3
}

all_cats = {
    "Science/Technology": st_weights,
    "Sports": sports_weights,
    "Business": business_weights,
    "World": world_weights
}

def categorize(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in all_cats}
    
    # Calculate weighted scores
    for cat, weights in all_cats.items():
        for kw, weight in weights.items():
            if len(kw) <= 3:
                # word boundary for short words
                if re.search(r'\b' + re.escape(kw) + r'\b', text):
                    scores[cat] += weight
            else:
                if kw in text:
                    scores[cat] += weight
                    
    # Adjustments
    if "game" in text:
        if scores["Science/Technology"] > 0:
            scores["Science/Technology"] += 2 # likely video game
        if scores["Sports"] > 0:
            scores["Sports"] += 1
            
    # "Competition" with "Science"
    if "science" in text and "competition" in text:
        scores["Science/Technology"] += 5
        
    # "Win" is ambiguous, but if "Science" is present, boost ST
    if "win" in text and "science" in text:
        scores["Science/Technology"] += 2

    # Tie breaking
    # If Business and ST are close, check for "Tech Company" names in Business context
    # But names like Microsoft are in ST weights.
    
    if sum(scores.values()) == 0:
        return "Unknown"
        
    return max(scores, key=scores.get)

st_count = 0
total = 0
results = []

for article in articles:
    total += 1
    cat = categorize(article.get('title', ''), article.get('description', ''))
    
    # Correction logic for specific known patterns if still failing?
    # "Students Win $100,000 in National Team Science Competition"
    # st_weights: science(5), team(1? no team is in sports), win(1? no win is in sports).
    # sports: win(1), team(2). 
    # Logic above: if science and competition -> +5 ST.
    
    is_st = (cat == "Science/Technology")
    if is_st:
        st_count += 1
        
    results.append({
        "title": article.get('title'),
        "category": cat,
        "is_st": is_st,
        "scores": "..." # omitting to save space
    })

fraction = st_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "st_count": st_count,
    "total": total,
    "fraction": fraction,
    "sample_st": [r['title'] for r in results if r['is_st']][:10],
    "sample_other": [r['title'] + " (" + r['category'] + ")" for r in results if not r['is_st']][:10]
}))"""

env_args = {'var_function-call-15392532606870454627': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-13831368158755182800': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'title': 1, 'description': 1}}, 'var_function-call-16257297644781231984': [{'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-281867425968629856': {'st_count': 2, 'total': 5, 'fraction': 0.4, 'sample_classifications': [['GameBoy mini-games win prize', 'ST'], ['Bailey Tries WR', 'Unknown'], ['Students Win \\$100,000 in National Team Science Competition', 'World'], ['Energy from waves  teenager wins science award', 'ST'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-7973401665590639291': {'count': 5, 'type': "<class 'list'>"}, 'var_function-call-8494642040961561930': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'title': 1, 'description': 1}, 'limit': 1000}, 'var_function-call-7338206399480502302': 'file_storage/function-call-7338206399480502302.json', 'var_function-call-16109598322301367296': {'st_count': 20, 'total': 111, 'fraction': 0.18018018018018017, 'sample_st': ['GameBoy mini-games win prize', 'Energy from waves  teenager wins science award', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars'], 'sample_other': ['Bailey Tries WR (Unknown)', 'Students Win \\$100,000 in National Team Science Competition (World)', 'China #39;s appetite boosts BHP (Business)', 'Leading Indicators, Jobless Claims Dip (AP) (World)', 'Even in win, nasty vibes (World)']}}

exec(code, env_args)
