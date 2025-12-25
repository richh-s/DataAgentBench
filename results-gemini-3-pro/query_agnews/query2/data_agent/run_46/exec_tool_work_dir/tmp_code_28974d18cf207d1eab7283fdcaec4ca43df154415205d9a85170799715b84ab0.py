code = """import json
import re
import os

data_key = 'var_function-call-4427803853797445487'
data_val = locals()[data_key]

if isinstance(data_val, str) and os.path.exists(data_val):
    with open(data_val, 'r') as f:
        articles = json.load(f)
else:
    articles = []

# Keywords configuration
strong_scitech = {
    'science', 'technology', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'cyber', 'digital', 
    'virus', 'hacker', 'space', 'nasa', 'astronomy', 'mars', 'moon', 'orbit', 'galaxy', 'biology', 'physics', 
    'chemistry', 'genetics', 'dna', 'research', 'lab', 'scientist', 'robot', 'ai', 'artificial intelligence', 
    'gameboy', 'nintendo', 'xbox', 'playstation', 'wii', 'console', 'video game', 'google', 'microsoft', 'apple', 
    'intel', 'linux', 'browser', 'wireless', 'mobile', 'smartphone', 'semiconductor', 'chip'
}
weak_scitech = {
    'tech', 'game', 'device', 'gadget', 'network', 'data', 'code', 'app', 'innovation', 'study', 'monitor', 'screen'
}

strong_sports = {
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'racing', 'f1', 'nascar', 'olympic', 
    'medal', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'quarterback', 'cornerback', 'receiver', 'touchdown', 'homerun', 
    'wicket', 'stadium', 'athlete', 'sprint', 'cycling', 'marathon'
}
weak_sports = {
    'sport', 'game', 'match', 'team', 'coach', 'player', 'win', 'loss', 'score', 'goal', 'race', 'cup', 'league', 
    'champion', 'season', 'club'
}

strong_business = {
    'economy', 'market', 'stock', 'share', 'trade', 'finance', 'invest', 'profit', 'revenue', 'merger', 'acquisition', 
    'corp', 'ceo', 'inflation', 'tax', 'fed', 'wall street', 'dow', 'nasdaq', 'nyse'
}
weak_business = {
    'business', 'money', 'bank', 'loss', 'sale', 'price', 'cost', 'deal', 'company', 'industry', 'oil', 'dollar', 'euro'
}

strong_world = {
    'politics', 'government', 'president', 'minister', 'election', 'parliament', 'congress', 'war', 'military', 'army', 
    'terror', 'bomb', 'suicide', 'iraq', 'iran', 'nuclear', 'un', 'united nations', 'treaty', 'afghanistan', 'palestinian', 'israeli'
}
weak_world = {
    'world', 'official', 'vote', 'poll', 'peace', 'attack', 'kill', 'dead', 'disaster', 'storm', 'police', 'crime', 'law', 
    'court', 'country', 'china', 'usa', 'uk', 'eu'
}

def classify(text):
    # Tokenize: simple split by non-alphanumeric
    tokens = set(re.findall(r'[a-z0-9]+', text.lower()))
    
    scores = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}
    
    # Function to check keywords
    def check_keywords(tokens, kw_set, weight):
        score = 0
        for kw in kw_set:
            if ' ' in kw: # Multi-word
                if kw in text.lower():
                    score += weight
            else:
                if kw in tokens:
                    score += weight
        return score

    scores['Science/Technology'] += check_keywords(tokens, strong_scitech, 5)
    scores['Science/Technology'] += check_keywords(tokens, weak_scitech, 1)
    
    scores['Sports'] += check_keywords(tokens, strong_sports, 5)
    scores['Sports'] += check_keywords(tokens, weak_sports, 1)
    
    scores['Business'] += check_keywords(tokens, strong_business, 5)
    scores['Business'] += check_keywords(tokens, weak_business, 1)
    
    scores['World'] += check_keywords(tokens, strong_world, 5)
    scores['World'] += check_keywords(tokens, weak_world, 1)
    
    # Adjustments
    # Tech companies with financial terms -> Business
    if any(kw in tokens for kw in ['apple', 'google', 'microsoft', 'intel', 'ibm']):
        if any(kw in tokens for kw in ['profit', 'revenue', 'stock', 'share', 'market']):
            scores['Business'] += 5
            
    # "Game" disambiguation
    if 'game' in tokens:
        # Check context again if needed, but weights might handle it.
        # "video game" (5 in SciTech)
        # "football game" (football 5, game 1 -> Sports 6).
        pass

    if max(scores.values()) == 0:
        return 'World' # Default
        
    return max(scores, key=scores.get)

scitech_count = 0
total = len(articles)
debug_list = []

for art in articles:
    text = (art.get('title', '') + ' ' + art.get('description', '')).replace('quot;', '"').replace('#39;', "'")
    cat = classify(text)
    if cat == 'Science/Technology':
        scitech_count += 1
        debug_list.append(art.get('title'))

fraction = scitech_count / total if total > 0 else 0

result = {
    "total": total,
    "scitech_count": scitech_count,
    "fraction": fraction,
    "scitech_titles_sample": debug_list[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13537257212664467500': [{'author_id': '218'}], 'var_function-call-5795812948484354417': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15291064105337959156': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-18392777885130959803': [{'_id': '6944bd03ccbbae8c297964fc', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bd03ccbbae8c29796cad', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bd03ccbbae8c29796f58', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bd03ccbbae8c29796fe7', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bd03ccbbae8c297971b7', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12258251932423174369': {'total': 5, 'scitech_count': 2, 'fraction': 0.4, 'example_scitech': ['Bailey Tries WR', 'Energy from waves  teenager wins science award']}, 'var_function-call-4427803853797445487': 'file_storage/function-call-4427803853797445487.json', 'var_function-call-2648101618528656708': {'total': 111, 'scitech_count': 0, 'fraction': 0.0, 'titles': []}, 'var_function-call-12232096866090601877': [{'title': 'GameBoy mini-games win prize', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Science/Technology': [], 'Sports': [], 'Business': [], 'World': []}}, {'title': 'Bailey Tries WR', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Science/Technology': [], 'Sports': [], 'Business': [], 'World': []}}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Science/Technology': [], 'Sports': [], 'Business': [], 'World': []}}, {'title': 'Energy from waves  teenager wins science award', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Science/Technology': [], 'Sports': [], 'Business': [], 'World': []}}, {'title': 'China #39;s appetite boosts BHP', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Science/Technology': [], 'Sports': [], 'Business': [], 'World': []}}], 'var_function-call-8855328180272719622': {'_id': '6944bd03ccbbae8c297964fc', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}}

exec(code, env_args)
