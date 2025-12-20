code = """import json
import re

file_path = locals()['var_function-call-417301987294769020']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Categories
# Strong keywords get more points.
# Business: stock, market, wall st, dow jones, nasdaq, revenue, profit, earnings, quarter, share, investor, economy, fed, bank, trade, oil price, merger, acquisition, deal.
# Sci/Tech: science, technology, computer, software, internet, web, space, nasa, orbit, biology, physics, research, study, lab, robot, gadget, mobile, phone, wireless, network, microsoft, google, apple, intel, linux, virus, security, gameboy, nintendo, xbox, playstation, video game.
# Sports: sport, football, baseball, basketball, soccer, hockey, tennis, golf, olympic, medal, team, coach, player, game (if sports context), win (if sports context), score, cup, league, championship.
# World: world, war, iraq, iran, president, minister, government, election, police, attack, bomb, kill, blast, crash, storm, hurricane.

def get_category(title, description):
    text = (title + " " + description).lower()
    
    scores = {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}
    
    # Business
    bus_keywords = ['business', 'stock', 'market', 'wall st', 'dow', 'nasdaq', 'revenue', 'profit', 'earnings', 'quarter', 'share', 'investor', 'economy', 'fed', 'bank', 'trade', 'oil price', 'merger', 'acquisition', 'deal', 'corp', 'inc', 'company', 'prices']
    for kw in bus_keywords:
        if kw in text:
            scores['Business'] += 1
            
    # Sci/Tech
    tech_keywords = ['science', 'technology', 'tech', 'computer', 'software', 'internet', 'web', 'space', 'nasa', 'orbit', 'biology', 'physics', 'research', 'study', 'lab', 'robot', 'gadget', 'mobile', 'phone', 'wireless', 'network', 'microsoft', 'google', 'apple', 'intel', 'linux', 'virus', 'security', 'gameboy', 'nintendo', 'xbox', 'playstation', 'video game', 'telescope', 'astronomy', 'genetic', 'stem cell', 'medicine', 'health', 'disease']
    for kw in tech_keywords:
        if kw in text:
            scores['Sci/Tech'] += 1
            
    # Sports
    sports_keywords = ['sport', 'football', 'baseball', 'basketball', 'soccer', 'hockey', 'tennis', 'golf', 'olympic', 'medal', 'team', 'coach', 'player', 'game', 'win', 'score', 'cup', 'league', 'championship', 'racing', 'race', 'athlete', 'stadium']
    for kw in sports_keywords:
        if kw in text:
            # Context check for 'game' or 'win'
            if kw in ['game', 'win']:
                # These are weak if alone, but strong if with other sports terms.
                # Just count them, but maybe less weight?
                scores['Sports'] += 0.5
            else:
                scores['Sports'] += 1

    # World
    world_keywords = ['world', 'war', 'iraq', 'iran', 'president', 'minister', 'government', 'election', 'police', 'attack', 'bomb', 'blast', 'kill', 'dead', 'crash', 'storm', 'hurricane', 'disaster', 'protest', 'official', 'country', 'nation', 'palestin', 'israel', 'un', 'united nations']
    for kw in world_keywords:
        if kw in text:
            scores['World'] += 1
            
    # Corrections
    # "Intel lowers revenue" -> Business score (revenue, corp) vs Tech score (intel).
    # If Business score >= Tech score, Business.
    # "Space Probe Fails" -> Tech (space, nasa).
    # "GameBoy mini-games win prize" -> Tech (gameboy, game). Sports (game, win). 
    # gameboy is unique to tech.
    # game is shared.
    
    # Let's handle explicit Sci/Tech indicators that override others.
    if any(k in text for k in ['nasa', 'space', 'science', 'software', 'browser', 'internet', 'gameboy', 'nintendo', 'xbox', 'playstation']):
        scores['Sci/Tech'] += 2
        
    if any(k in text for k in ['olympic', 'nfl', 'nba', 'mlb', 'fifa']):
        scores['Sports'] += 2
        
    if any(k in text for k in ['dow', 'nasdaq', 'wall st', 'earnings']):
        scores['Business'] += 2

    # Return max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
        
    # Tie breaking
    # If Sci/Tech and Business tie, and it mentions a company, usually Business unless product launch.
    # "Intel lowers revenue": Business=1+2(earnings implied? no, revenue), Tech=1+?
    
    return best_cat

scitech_count = 0
total = 0
results = []
for a in articles:
    cat = get_category(a['title'], a['description'])
    if cat == 'Sci/Tech':
        scitech_count += 1
    total += 1
    # Store title and cat for debugging
    results.append((a['title'], cat))

fraction = scitech_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({"fraction": fraction, "scitech": scitech_count, "total": total, "examples": results[:20]}))"""

env_args = {'var_function-call-7444710123955650203': [{'author_id': '218'}], 'var_function-call-9301313333916833534': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3059483436393923606': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-14216560875484551006': [{'_id': '69449d2918eb6e0bd5dec050', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449d2918eb6e0bd5dec801', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449d2918eb6e0bd5decaac', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449d2918eb6e0bd5decb3b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449d2918eb6e0bd5decd0b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2113033153754808277': {'scitech_count': 0, 'total_count': 5, 'details': [{'title': 'GameBoy mini-games win prize', 'category': 'Unknown'}, {'title': 'Bailey Tries WR', 'category': 'Unknown'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Unknown'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Unknown'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Unknown'}]}, 'var_function-call-10746624833329780838': [], 'var_function-call-14792202653839301150': [{'_id': '69449d2918eb6e0bd5decf12', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-417301987294769020': 'file_storage/function-call-417301987294769020.json'}

exec(code, env_args)
