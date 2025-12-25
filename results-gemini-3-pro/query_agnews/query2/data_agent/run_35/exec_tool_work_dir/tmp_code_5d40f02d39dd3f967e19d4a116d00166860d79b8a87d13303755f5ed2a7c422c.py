code = """import json

articles = locals()['var_function-call-5412345516838293038']

tech_keywords = [
    'technology', 'science', 'computer', 'internet', 'software', 'space', 'nasa', 'robot', 'mobile', 'web', 'digital', 'tech', 
    'virus', 'hacker', 'network', 'online', 'data', 'cyber', 'apple', 'google', 'microsoft', 'intel', 'wireless', 'satellite', 
    'mars', 'moon', 'galaxy', 'universe', 'stem cell', 'clone', 'gene', 'dna', 'research', 'scientist', 'astronomer', 'launch', 
    'orbit', 'solar', 'gadget', 'chip', 'broadband', 'linux', 'windows', 'browser', 'server', 'bluetooth', 'wifi', 'gps', 'app', 
    'code', 'program', 'blog', 'email', 'spam', 'security', 'firefox', 'explorer', 'ipod', 'mp3', 'dvd', 'camera', 'nintendo', 
    'sony', 'playstation', 'xbox', 'wii', 'physics', 'chemistry', 'biology', 'math', 'ibm', 'yahoo', 'dell', 'hp', 'telecom',
    'gameboy', 'spam', 'spyware', 'phishing', 'malware', 'browser', 'search engine'
]

sports_keywords = [
    'sport', 'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf', 'cup', 'league', 'team', 'coach', 
    'player', 'athlete', 'olympics', 'medal', 'championship', 'stadium', 'race', 'racing', 'f1', 'nascar', 'cricket', 'rugby',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'tour de france', 'wimbledon', 'super bowl'
]

business_keywords = [
    'business', 'market', 'stock', 'profit', 'revenue', 'loss', 'economy', 'trade', 'bank', 'finance', 'invest', 'merger', 
    'acquisition', 'share', 'dollar', 'euro', 'yen', 'oil', 'gas', 'price', 'ceo', 'cfo', 'manager', 'company', 'corp', 'inc',
    'wall street', 'dow jones', 'nasdaq', 'imf', 'wto'
]

world_keywords = [
    'world', 'war', 'peace', 'election', 'president', 'minister', 'government', 'country', 'city', 'state', 'court', 'law', 
    'police', 'crime', 'attack', 'bomb', 'disaster', 'hurricane', 'earthquake', 'flood', 'tornado', 'tsunami', 'un', 'iraq', 
    'iran', 'china', 'usa', 'uk', 'europe', 'asia', 'africa', 'israel', 'palestine', 'russia', 'syria', 'korea', 'nuclear'
]

def classify(title, desc):
    text = (title + " " + desc).lower()
    
    # Check for "game" ambiguity
    if 'game' in text:
        # Check for tech-specific game terms
        if any(k in text for k in ['video', 'console', 'nintendo', 'sony', 'xbox', 'ps2', 'ps3', 'gameboy', 'computer', 'software', 'arcade', 'mobile', 'electronic']):
            return 'Science/Technology'
        # Check for sports-specific game terms
        if any(k in text for k in sports_keywords):
            return 'Sports'
        # Fallback to general tech keywords if no sports keywords found
    
    score_tech = sum(1 for k in tech_keywords if k in text)
    score_sports = sum(1 for k in sports_keywords if k in text)
    score_business = sum(1 for k in business_keywords if k in text)
    score_world = sum(1 for k in world_keywords if k in text)
    
    scores = {'Science/Technology': score_tech, 'Sports': score_sports, 'Business': score_business, 'World': score_world}
    
    # Get the category with max score
    best_cat = max(scores, key=scores.get)
    
    if scores[best_cat] == 0:
        return 'Unclassified'
    
    return best_cat

count_tech = 0
total = 0
tech_articles = []
others = []

for a in articles:
    cat = classify(a['title'], a['description'])
    total += 1
    if cat == 'Science/Technology':
        count_tech += 1
        tech_articles.append(a['title'])
    else:
        others.append((a['title'], cat))

result = {
    "total": total,
    "count_tech": count_tech,
    "tech_titles": tech_articles[:10], # sample
    "other_titles_sample": others[:10] # sample
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4111685012841103611': [{'author_id': '218'}], 'var_function-call-5496456177737444367': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-4223469945802372589': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-5412345516838293038': [{'_id': '6944af6493068f61aa899c32', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944af6493068f61aa89a3e3', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944af6493068f61aa89a68e', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944af6493068f61aa89a71d', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944af6493068f61aa89a8ed', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-4122209881831467705': ['GameBoy mini-games win prize ||| A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.', "Bailey Tries WR ||| Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday.", 'Students Win \\$100,000 in National Team Science Competition ||| Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.', 'Energy from waves  teenager wins science award ||| A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.', 'China #39;s appetite boosts BHP ||| BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. ']}

exec(code, env_args)
