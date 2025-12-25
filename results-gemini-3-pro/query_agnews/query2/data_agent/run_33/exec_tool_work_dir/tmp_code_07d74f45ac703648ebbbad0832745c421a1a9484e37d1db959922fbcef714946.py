code = """import json
import re

file_path = locals()['var_function-call-12538038109257007794']
with open(file_path, 'r') as f:
    articles = json.load(f)

categories = {
    'Sci/Tech': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'gadget', 'device', 'space', 'nasa', 'astronomy', 'biology', 'genetics', 'genome', 'medical', 'health', 'disease', 'virus', 'cancer', 'treatment', 'drug', 'physics', 'chemistry', 'energy', 'power', 'solar', 'nuclear', 'innovation', 'research', 'study', 'scientist', 'researcher', 'engineer', 'robot', 'ai', 'artificial intelligence', 'data', 'cyber', 'security', 'network', 'telecom', 'wireless', 'broadband', 'satellite', 'game', 'gaming', 'console', 'nintendo', 'sony', 'microsoft', 'intel', 'amd', 'google', 'apple', 'linux', 'windows', 'browser', 'server', 'chip', 'processor', 'memory', 'storage', 'cloud', 'app', 'application', 'update', 'patch', 'version', 'release', 'beta', 'review', 'preview', 'test', 'ibm', 'oracle', 'cisco', 'yahoo', 'amazon', 'facebook', 'ebay', 'videogame', 'video game', 'xbox', 'playstation', 'wii', 'ipod', 'iphone', 'ipad', 'smartphone', 'tablet', 'laptop', 'desktop', 'monitor', 'screen', 'display', 'camera', 'lens', 'sensor', 'biotech', 'nanotech', 'stem cell', 'cloning', 'mission', 'launch', 'orbit', 'mars', 'moon', 'planet', 'galaxy', 'star', 'telescope', 'shuttle', 'station', 'astronaut', 'cosmonaut', 'physicist', 'chemist', 'biologist', 'geologist', 'mathematician', 'laboratory', 'lab', 'experiment', 'theory', 'discovery', 'invention', 'patent', 'copyright', 'piracy', 'hacker', 'spam', 'phishing', 'malware', 'spyware', 'trojan', 'worm', 'virus', 'firewall', 'encryption', 'password', 'login', 'account', 'user', 'interface', 'gui', 'api', 'sdk', 'ide', 'code', 'programming', 'language', 'script', 'database', 'sql', 'nosql', 'server', 'client', 'network', 'protocol', 'http', 'ftp', 'smtp', 'tcp', 'ip', 'dns', 'url', 'link', 'hyperlink', 'browser', 'search engine', 'email', 'e-mail', 'chat', 'im', 'messenger', 'voip', 'skype', 'blog', 'forum', 'wiki', 'social media', 'tweet', 'twitter', 'facebook', 'linkedin', 'myspace', 'youtube', 'video', 'audio', 'music', 'mp3', 'format', 'file', 'download', 'upload', 'stream', 'streaming'
    ],
    'Sports': [
        'sport', 'sports', 'game', 'match', 'team', 'player', 'coach', 'win', 'won', 'loss', 'lost', 'score', 'league', 'season', 'championship', 'champion', 'tournament', 'cup', 'olympic', 'olympics', 'medal', 'gold', 'silver', 'bronze', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'racing', 'race', 'driver', 'athlete', 'stadium', 'arena', 'field', 'court', 'track', 'gym', 'training', 'practice', 'roster', 'trade', 'draft', 'contract', 'salary', 'agent', 'referee', 'umpire', 'official', 'foul', 'penalty', 'offside', 'goal', 'touchdown', 'homerun', 'strike', 'ball', 'bat', 'club', 'racket', 'net', 'basket', 'puck', 'helmet', 'jersey', 'uniform', 'fan', 'spectator', 'ticket', 'broadcast', 'espn', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'ncaa', 'wimbledon', 'us open', 'french open', 'australian open', 'masters', 'pga', 'lpga', 'nascar', 'f1', 'formula 1', 'grand prix', 'tour de france', 'world cup', 'super bowl', 'world series', 'stanley cup', 'playoff', 'final', 'semifinal', 'quarterfinal', 'round', 'heat', 'lap', 'marathon', 'sprint', 'relay', 'swim', 'swimming', 'diving', 'gymnastics', 'skiing', 'skating', 'boxing', 'wrestling', 'mma', 'ufc', 'cricket', 'rugby'
    ],
    'Business': [
        'business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'trading', 'profit', 'revenue', 'earnings', 'loss', 'sale', 'sales', 'company', 'corporation', 'corp', 'inc', 'ltd', 'bank', 'banking', 'finance', 'financial', 'investment', 'investor', 'currency', 'dollar', 'euro', 'yen', 'pound', 'oil', 'gas', 'price', 'cost', 'inflation', 'deflation', 'interest', 'rate', 'fed', 'federal reserve', 'treasury', 'bond', 'debt', 'loan', 'credit', 'mortgage', 'tax', 'budget', 'deficit', 'surplus', 'gdp', 'job', 'employment', 'unemployment', 'hiring', 'layoff', 'strike', 'union', 'merger', 'acquisition', 'deal', 'contract', 'ceo', 'cfo', 'executive', 'manager', 'management', 'board', 'chairman', 'director', 'shareholder', 'dividend', 'wall street', 'dow', 'dow jones', 'nasdaq', 's&p', 'nyse', 'exchange', 'commodity', 'future', 'option', 'derivative', 'hedge fund', 'private equity', 'venture capital', 'startup', 'ipo', 'bankruptcy', 'insolvency', 'liquidation', 'audit', 'accounting', 'regulation', 'antitrust', 'monopoly', 'cartel', 'opec', 'wto', 'imf', 'world bank'
    ],
    'World': [
        'world', 'international', 'nation', 'country', 'state', 'government', 'politic', 'politics', 'politician', 'president', 'minister', 'prime minister', 'chancellor', 'king', 'queen', 'prince', 'princess', 'parliament', 'congress', 'senate', 'representative', 'diplomat', 'diplomacy', 'ambassador', 'embassy', 'treaty', 'agreement', 'summit', 'conference', 'war', 'conflict', 'battle', 'fighting', 'military', 'army', 'navy', 'air force', 'marine', 'soldier', 'troop', 'weapon', 'gun', 'bomb', 'blast', 'explosion', 'attack', 'terrorism', 'terrorist', 'rebel', 'insurgent', 'guerrilla', 'militia', 'coup', 'revolution', 'protest', 'demonstration', 'rally', 'strike', 'riot', 'police', 'crime', 'criminal', 'arrest', 'prison', 'jail', 'court', 'judge', 'jury', 'verdict', 'sentence', 'execution', 'law', 'legal', 'right', 'human rights', 'refugee', 'immigrant', 'immigration', 'border', 'security', 'intelligence', 'cia', 'fbi', 'un', 'united nations', 'eu', 'european union', 'nato', 'asean', 'au', 'african union', 'election', 'vote', 'voter', 'ballot', 'campaign', 'candidate', 'party', 'democrat', 'republican', 'conservative', 'liberal', 'socialist', 'communist', 'fascist', 'dictator', 'tyrant', 'regime', 'sanction', 'embargo', 'peace', 'ceasefire', 'truce', 'negotiation', 'talk', 'meeting', 'visit', 'tour', 'disaster', 'catastrophe', 'tragedy', 'accident', 'crash', 'collision', 'fire', 'flood', 'storm', 'hurricane', 'typhoon', 'cyclone', 'tornado', 'earthquake', 'tsunami', 'volcano', 'eruption', 'drought', 'famine', 'epidemic', 'pandemic', 'outbreak', 'flu', 'influenza', 'aids', 'hiv', 'malaria', 'cholera', 'ebola', 'zika', 'covid', 'coronavirus', 'vaccine', 'vaccination'
    ]
}

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    
    # Simple word matching
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, keywords in categories.items():
            if word in keywords:
                scores[cat] += 1
    
    # Specific adjustments
    # "game" is in both Sports and Tech. If "video" or "console" or "nintendo" etc appears, weight Tech higher.
    if 'game' in words:
        tech_indicators = ['video', 'console', 'nintendo', 'sony', 'microsoft', 'xbox', 'playstation', 'wii', 'boy', 'computer', 'software', 'app']
        if any(w in words for w in tech_indicators):
            scores['Sci/Tech'] += 2 # Boost Tech
        # Else assume sports or check for sports terms
    
    # If tie, default to World? Or random?
    # Get max score
    max_score = max(scores.values())
    if max_score == 0:
        return "Unknown"
    
    # Get cats with max score
    best_cats = [cat for cat, score in scores.items() if score == max_score]
    
    # Tie breaking logic
    if len(best_cats) > 1:
        # Priority: World > Sports > Business > Sci/Tech?
        # Or based on dataset distribution.
        # Let's try to prioritize specific over general.
        # Tech is specific.
        if 'Sci/Tech' in best_cats:
            return 'Sci/Tech'
        if 'Sports' in best_cats:
            return 'Sports'
        if 'Business' in best_cats:
            return 'Business'
        return best_cats[0]
    
    return best_cats[0]

results = []
count_tech = 0
for article in articles:
    cat = classify(article['title'], article['description'])
    results.append({'title': article['title'], 'cat': cat})
    if cat == 'Sci/Tech':
        count_tech += 1

print("__RESULT__:")
print(json.dumps({'total': len(articles), 'tech_count': count_tech, 'samples': results[:10]}))"""

env_args = {'var_function-call-7824498463487359527': [{'author_id': '218'}], 'var_function-call-12299435220607160936': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1259592477097744164': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-1246676392852871560': [{'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-17050363897638211259': 5, 'var_function-call-11640760222079090320': [{'_id': '6944ad769b77b04b15165539', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ad779b77b04b15165cea', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ad779b77b04b15165f95', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ad779b77b04b15166024', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ad779b77b04b151661f4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12538038109257007794': 'file_storage/function-call-12538038109257007794.json'}

exec(code, env_args)
