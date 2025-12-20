code = """import json
import re

file_path = locals()['var_function-call-14645694745949228888']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords (same as before but we'll use them carefully)
sci_tech_keywords = [
    'science', 'technology', 'tech', 'computer', 'internet', 'web', 'software', 'hardware', 
    'chip', 'processor', 'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'windows', 
    'browser', 'server', 'network', 'wireless', 'mobile', 'phone', 'cellphone', 'telecom', 
    'satellite', 'space', 'nasa', 'astronaut', 'mars', 'orbit', 'astronomy', 'physics', 
    'chemistry', 'biology', 'genetics', 'genome', 'medical', 'research', 'study', 'lab', 
    'scientist', 'researcher', 'robot', 'gadget', 'device', 'electronic', 'digital', 'online', 
    'virtual', 'cyber', 'hacker', 'virus', 'spam', 'security', 'encryption', 'game', 'gaming', 
    'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'console', 'video game', 'ipod', 'mp3', 
    'dvd', 'camera', 'pixel', 'blog', 'search engine', 'yahoo', 'amazon', 'facebook', 
    'myspace', 'youtube', 'email', 'mail', 'firefox', 'explorer', 'opera', 'netscape', 'voip',
    'skype', 'broadband', 'wifi', 'bluetooth', 'gps', 'nanotech', 'stem cell', 'cloning',
    'solar', 'energy', 'battery', 'fuel cell', 'shuttle', 'telescope', 'hubble', 'supercomputer',
    'ibm', 'dell', 'hp', 'compaq', 'palm', 'pda', 'blackberry', 'algorithm', 'program', 'code'
]

# Business strong indicators
business_strong = [
    'profit', 'loss', 'revenue', 'earnings', 'quarter', 'stock', 'share', 'market', 'wall street',
    'acquisition', 'merger', 'buyout', 'acquire', 'bought', 'sold', 'bank', 'economy', 'fed', 
    'rates', 'inflation', 'trade', 'deal', 'billion', 'million' # billion/million often business
]

# Sports strong indicators
sports_strong = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'nfl', 
    'nba', 'mlb', 'nhl', 'olympic', 'medal', 'tournament', 'championship', 'world cup', 
    'super bowl', 'match', 'score', 'win', 'lose', 'defeat', 'victory', 'team', 'player', 
    'coach', 'athlete', 'stadium', 'red sox', 'yankees', 'broncos', 'cowboys'
]

def classify_final(title, desc):
    text = (title + " " + desc).lower()
    
    # Check Business Strong First
    # If title has Profit, Loss, Stocks, etc. -> Business
    # Unless it's "Profit from your new PC" (unlikely in news titles)
    
    bus_score = 0
    for kw in business_strong:
        if kw in text:
            bus_score += 1
            
    # Check Sports Strong
    sport_score = 0
    for kw in sports_strong:
        if kw in text:
            if kw == 'win' or kw == 'lose' or kw == 'score':
                # Ambiguous
                pass
            else:
                sport_score += 1
    
    # Check ST
    st_score = 0
    for kw in sci_tech_keywords:
        if kw in text:
            # Avoid substring matches for short words
            if len(kw) <= 4:
                # Use word boundary check roughly
                if re.search(r'\b' + re.escape(kw) + r'\b', text):
                    st_score += 1
            else:
                st_score += 1
    
    # Refine "game"
    if 'game' in text:
        if any(x in text for x in ['video', 'console', 'nintendo', 'xbox', 'ps2', 'tech']):
            st_score += 5
        elif any(x in text for x in ['football', 'baseball', 'sport', 'coach', 'team']):
            sport_score += 5
    
    # Decision Logic
    # 1. If financial news (bus_score high) -> Business, even if tech company
    if bus_score >= 2 and bus_score >= st_score:
        return 'Business'
    if bus_score > 0 and 'profit' in title.lower():
        return 'Business'
    if bus_score > 0 and 'stock' in title.lower():
        return 'Business'
    
    # 2. If Sports
    if sport_score > st_score and sport_score > 0:
        return 'Sports'
        
    # 3. If ST
    if st_score > 0:
        # Check if it's a study/discovery vs just a mention
        return 'Science/Technology'
        
    return 'World' # or Other

st_count = 0
st_list = []
all_cats = []

for art in articles:
    cat = classify_final(art['title'], art['description'])
    all_cats.append(cat)
    if cat == 'Science/Technology':
        st_count += 1
        st_list.append(art['title'])

print("__RESULT__:")
print(json.dumps({
    "count": st_count,
    "total": len(articles),
    "fraction": st_count / len(articles),
    "titles": st_list
}))"""

env_args = {'var_function-call-7921738261678552472': [{'author_id': '218'}], 'var_function-call-15988986839234050151': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3807883415123841385': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-12359104834319763328': [{'_id': '694495f9bcd2c7e4a7fdf919', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '694495f9bcd2c7e4a7fe00ca', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '694495f9bcd2c7e4a7fe0375', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '694495f9bcd2c7e4a7fe0404', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '694495f9bcd2c7e4a7fe05d4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-13061389522128022440': {'total': 5, 'st_count': 3, 'sample': [['GameBoy mini-games win prize', 'ST'], ['Bailey Tries WR', 'World'], ['Students Win \\$100,000 in National Team Science Competition', 'ST'], ['Energy from waves  teenager wins science award', 'ST'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-14645694745949228888': 'file_storage/function-call-14645694745949228888.json', 'var_function-call-9364624269194835292': {'total': 111, 'st_count': 18, 'st_fraction': 0.16216216216216217, 'st_titles_sample': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'Satellite write-downs widen DirecTV #39;s loss', 'Revealed: why the fear factor runs with the pack', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Ford #39;s Scheele to Retire as President on Feb. 1 (Update2)', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy'], 'all_cats': ['Sports', 'Sports', 'Science/Technology', 'Science/Technology', 'Business', 'World', 'Sports', 'World', 'World', 'World', 'Sports', 'World', 'Business', 'World', 'World', 'World', 'Business', 'Business', 'World', 'World', 'Science/Technology', 'Business', 'Science/Technology', 'Science/Technology', 'Sports', 'Business', 'Sports', 'World', 'World', 'World', 'Sports', 'Science/Technology', 'Business', 'Business', 'Business', 'Sports', 'Sports', 'Sports', 'World', 'Science/Technology', 'Science/Technology', 'Sports', 'World', 'Business', 'Sports', 'World', 'Sports', 'Business', 'Business', 'Sports', 'World', 'World', 'Science/Technology', 'World', 'World', 'Business', 'World', 'World', 'Sports', 'Sports', 'World', 'Business', 'Business', 'Sports', 'Science/Technology', 'Sports', 'Business', 'Business', 'World', 'Business', 'World', 'Business', 'World', 'World', 'Business', 'Science/Technology', 'World', 'World', 'World', 'Business', 'Sports', 'World', 'World', 'Sports', 'World', 'World', 'Sports', 'World', 'Sports', 'World', 'Science/Technology', 'Science/Technology', 'Sports', 'Business', 'Science/Technology', 'Business', 'Science/Technology', 'Sports', 'Science/Technology', 'World', 'Science/Technology', 'World', 'Sports', 'World', 'Sports', 'World', 'Business', 'World', 'World', 'Science/Technology', 'Business']}, 'var_function-call-13297967277760975901': [{'title': 'Texas Instruments Posts Higher 3Q Profits (AP)', 'desc': 'AP - Third quarter profits at Texas Instruments Inc. grew by  #36;116 million from a year ago due to rising demand for its chips used in high-end mobile phones and digital light processing systems for big-screen televisions.'}, {'title': 'Satellite write-downs widen DirecTV #39;s loss', 'desc': 'DirecTV Group, the largest satellite television programmer, said its loss widened considerably in the third quarter because of a one-time charge to pay for new satellites.'}, {'title': 'Revealed: why the fear factor runs with the pack', 'desc': 'THE rapid spread of fear that can cause crush injuries and serious accidents in crowds could be provoked by an innate reaction to body language, a provocative new study has found.'}, {'title': 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'desc': 'BEIJING -- China #39;s biggest computer maker said it has acquired a majority stake in IBM #39;s personal computer business for \\$1.75 billion dollars in one of the biggest Chinese overseas acquisitions ever.'}, {'title': 'Ford #39;s Scheele to Retire as President on Feb. 1 (Update2)', 'desc': 'Ford Motor Co. President Nick Scheele, who postponed his retirement three years ago after being called to the US to help stop losses, will retire Feb. 1. He turns 61 next month.'}]}

exec(code, env_args)
