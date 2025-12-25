code = """import json

# Load the articles from the file
file_path = locals()['var_function-call-15997635584120329157']
with open(file_path, 'r') as f:
    articles_data = json.load(f)

# Keywords lists (same as before)
tech_keywords = [
    'science', 'technology', 'tech', 'computer', 'internet', 'web', 'software', 'hardware', 'chip', 'intel', 
    'microsoft', 'google', 'apple', 'linux', 'unix', 'windows', 'virus', 'hacker', 'security', 'firewall', 
    'spyware', 'spam', 'phishing', 'space', 'nasa', 'astronomy', 'universe', 'planet', 'mars', 'moon', 
    'solar', 'galaxy', 'star', 'telescope', 'shuttle', 'rocket', 'orbit', 'astronaut', 'biology', 'physics', 
    'chemistry', 'genetics', 'genome', 'dna', 'clone', 'stem cell', 'medical', 'medicine', 'research', 
    'laboratory', 'scientist', 'researcher', 'study', 'experiment', 'innovation', 'invention', 'patent', 
    'engine', 'fuel', 'battery', 'energy', 'power', 'nuclear', 'solar', 'wind', 'mobile', 'phone', 
    'cellphone', 'wireless', 'wifi', 'bluetooth', 'network', 'broadband', 'telecom', 'satellite', 'gps', 
    'robot', 'robotics', 'automation', 'gadget', 'device', 'electronic', 'digital', 'online', 'virtual', 
    'cyber', 'video game', 'videogame', 'gaming', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 
    'wii', 'gameboy', 'psp', 'ipod', 'mp3', 'itunes', 'browser', 'firefox', 'explorer', 'server', 'data',
    'system', 'app', 'application', 'user', 'interface', 'monitor', 'screen', 'display', 'disk', 'drive',
    'memory', 'processor', 'amd', 'nvidia', 'graphic', 'pixel', 'resolution', 'download', 'upload',
    'link', 'url', 'website', 'blog', 'post', 'email', 'chat', 'message', 'text', 'code', 'program',
    'developer', 'engineer', 'beta', 'version', 'update', 'patch', 'release', 'launch', 'announce',
    'feature', 'tool', 'service', 'platform', 'standard', 'format', 'protocol', 'network', 'connection',
    'supercomputer', 'nanotech', 'biotech', 'broadband', 'voip', 'semiconductor'
]

sports_keywords = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 
    'rugby', 'racing', 'f1', 'nascar', 'olympic', 'medal', 'athlete', 'player', 'team', 'coach', 
    'manager', 'cup', 'league', 'season', 'championship', 'tournament', 'game', 'match', 'score', 
    'win', 'lose', 'defeat', 'victory', 'draw', 'stadium', 'club', 'squad', 'roster', 'trade', 
    'draft', 'agent', 'contract', 'signing', 'transfer', 'goal', 'point', 'run', 'home run', 
    'touchdown', 'basket', 'shot', 'save', 'penalty', 'foul', 'referee', 'umpire', 'pitcher', 
    'quarterback', 'striker', 'defender', 'midfielder', 'goalkeeper', 'driver', 'rider', 'cyclist',
    'swimmer', 'runner', 'sprinter', 'marathon', 'race', 'lap', 'circuit', 'track', 'field', 
    'court', 'pitch', 'diamond', 'ring', 'arena', 'gym', 'training', 'practice', 'injury', 'hurt', 
    'sideline', 'bench', 'start', 'finish', 'record', 'ranking', 'standing', 'playoff', 'final', 
    'semi-final', 'quarter-final', 'heat', 'round', 'bout', 'fight', 'boxer', 'wrestler',
    'giants', 'dodgers', 'broncos', 'red sox', 'yankees', 'lakers', 'knicks', 'bulls', 'celtics'
]

business_keywords = [
    'business', 'company', 'corp', 'corporation', 'inc', 'incorporated', 'ltd', 'limited', 'stock', 
    'market', 'share', 'wall street', 'dow', 'jones', 'nasdaq', 'nyse', 's&p', 'investor', 'investment', 
    'earnings', 'profit', 'revenue', 'loss', 'income', 'sales', 'retail', 'store', 'shop', 'chain', 
    'brand', 'product', 'goods', 'service', 'customer', 'consumer', 'spending', 'demand', 'supply', 
    'trade', 'economy', 'economic', 'bank', 'banking', 'finance', 'financial', 'loan', 'credit', 
    'debt', 'bond', 'rate', 'interest', 'currency', 'dollar', 'euro', 'yen', 'pound', 'exchange', 
    'deal', 'merger', 'acquisition', 'takeover', 'buyout', 'bid', 'offer', 'ceo', 'cfo', 'coo', 
    'executive', 'manager', 'director', 'board', 'shareholder', 'dividend', 'industry', 'sector', 
    'manufacturing', 'factory', 'plant', 'production', 'output', 'price', 'cost', 'expense', 'budget', 
    'forecast', 'outlook', 'growth', 'recession', 'depression', 'inflation', 'deflation', 'tax', 
    'tariff', 'subsidy', 'regulation', 'antitrust', 'monopoly', 'competition', 'competitor', 'rival', 
    'partner', 'partnership', 'joint venture', 'bankruptcy', 'insolvency', 'restructuring', 'layoff', 
    'job', 'employment', 'unemployment', 'hiring', 'wage', 'salary', 'strike', 'union', 'negotiation'
]

# Simple scoring
def classify(text):
    text = text.lower()
    scores = {'tech': 0, 'sports': 0, 'business': 0}
    
    for word in tech_keywords:
        if word in text:
            scores['tech'] += 1
            
    for word in sports_keywords:
        if word in text:
            # Handle "game" ambiguity
            if word == 'game':
                if any(x in text for x in ['video', 'console', 'boy', 'cube', 'station', 'box', 'computer']):
                    scores['tech'] += 1
                else:
                    scores['sports'] += 1
            else:
                scores['sports'] += 1
                
    for word in business_keywords:
        if word in text:
            scores['business'] += 1
            
    # Heuristics for overlapping terms
    if 'oil' in text and 'price' in text: scores['business'] += 2
    if 'profit' in text or 'earnings' in text: scores['business'] += 2
    if 'cup' in text or 'league' in text: scores['sports'] += 2
    if 'research' in text or 'study' in text: scores['tech'] += 1
    if 'space' in text and 'nasa' in text: scores['tech'] += 2
    
    # Return category with max score
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return 'world' # Default
    
    # Tie breaking (heuristic)
    # If tie between Tech and Business, and mention of "stock" or "revenue", prefer Business.
    # If tie between Tech and Sports, unlikely, but check keywords.
    if scores['tech'] == scores['business'] and scores['tech'] > 0:
         if any(x in text for x in ['stock', 'revenue', 'profit', 'market']):
             return 'business'
         else:
             return 'tech'
             
    return max_cat

sci_tech_count = 0
total_count = len(articles_data)
# To debug, I'll store the titles of tech articles
tech_titles = []

for article in articles_data:
    content = article['title'] + " " + article['description']
    category = classify(content)
    if category == 'tech':
        sci_tech_count += 1
        tech_titles.append(article['title'])

fraction = sci_tech_count / total_count if total_count > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "sci_tech_count": sci_tech_count, 
    "total_count": total_count, 
    "fraction": fraction,
    "tech_titles_preview": tech_titles[:5]
}))"""

env_args = {'var_function-call-2251101591535773672': [{'author_id': '218'}], 'var_function-call-2515055789371333606': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-12715464307461799012': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-5902508147498761044': [{'_id': '694494035f0c25acd79a6f0c', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '694494045f0c25acd79a76bd', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '694494045f0c25acd79a7968', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '694494045f0c25acd79a79f7', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '694494045f0c25acd79a7bc7', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-11420655887465550102': {'sci_tech_count': 3, 'total_count': 5, 'fraction': 0.6, 'examples': [['GameBoy mini-games win prize', 'tech'], ['Students Win \\$100,000 in National Team Science Competition', 'tech'], ['Energy from waves  teenager wins science award', 'tech']]}, 'var_function-call-16168324659342571363': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-15997635584120329157': 'file_storage/function-call-15997635584120329157.json'}

exec(code, env_args)
