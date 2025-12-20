code = """import json
import re

file_path = locals()['var_function-call-7752384695117518704']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Regex patterns (compiled for speed if needed, but here simple strings)
keywords = {
    'Sports': [
        r'\bolympics?\b', r'\bfootball\b', r'\bsoccer\b', r'\bbasketball\b', r'\bbaseball\b', 
        r'\btennis\b', r'\bgolf\b', r'\bhockey\b', r'\bmedal\b', r'\bathlete\b', r'\bchampion\b', 
        r'\btournament\b', r'\bstadium\b', r'\bnba\b', r'\bnfl\b', r'\bmlb\b', r'\bfifa\b', 
        r'\buefa\b', r'\bwimbledon\b', r'\bathens\b', r'\bgold\b', r'\bsilver\b', r'\bbronze\b', 
        r'\bworld cup\b', r'\drugby\b', r'\bcricket\b', r'\bf1\b', r'\bracing\b', r'\bcoach\b', 
        r'\bsquad\b', r'\bmarathon\b', r'\bsprint\b', r'\bswimmer\b', r'\bgymnastics?\b',
        r'\bteam\b', r'\bgame\b', r'\bwin\b', r'\bscore\b', r'\bmatch\b', r'\bplayer\b', 
        r'\bcup\b', r'\bleague\b', r'\bclub\b', r'\bseason\b', r'\btitle\b', r'\bmanager\b',
        r'\broddick\b', r'\bfederer\b', r'\bphelps\b', r'\barmstrong\b', r'\btiger woods\b',
        r'\byankees\b', r'\bred sox\b', r'\blakers\b', r'\bears\b', r'\bcolts\b'
    ],
    'Business': [
        r'\bstock\b', r'\bprice\b', r'\bmarket\b', r'\beconomy\b', r'\boil\b', 
        r'\bcompany\b', r'\bcorp\b', r'\binc\b', r'\bprofit\b', r'\bloss\b', r'\bdollar\b', 
        r'\bbank\b', r'\btrade\b', r'\bsales\b', r'\brate\b', r'\bdeal\b', r'\bceo\b', 
        r'\bshare\b', r'\binvestor\b', r'\bwall street\b', r'\bnasdaq\b', r'\bdow\b', 
        r'\bearnings\b', r'\brevenue\b', r'\bgrowth\b', r'\binflation\b', r'\bfed\b',
        r'\bboeing\b', r'\bairbus\b', r'\bwal-mart\b'
    ],
    'Sci/Tech': [
        r'\bsoftware\b', r'\bhardware\b', r'\binternet\b', r'\bcomputer\b', r'\bmicrosoft\b', 
        r'\bgoogle\b', r'\bintel\b', r'\blinux\b', r'\bwindows\b', r'\bunix\b', r'\bvirus\b', 
        r'\btechnology\b', r'\bspace\b', r'\bnasa\b', r'\bapple\b', r'\bibm\b', r'\bweb\b', 
        r'\bonline\b', r'\bserver\b', r'\bdownload\b', r'\bipod\b', r'\bsearch engine\b',
        r'\bbrowser\b', r'\bsecurity\b', r'\bworm\b', r'\bpatch\b', r'\bgame boy\b', r'\bsony\b'
    ],
    'World': [
        r'\biraq\b', r'\bwar\b', r'\bpresident\b', r'\bminister\b', r'\bgovernment\b', 
        r'\bbomb\b', r'\battack\b', r'\bofficial\b', r'\bun\b', r'\bcountry\b', r'\bmilitary\b',
        r'\bpalestinian\b', r'\bisrael\b', r'\bbaghdad\b', r'\btroops\b', r'\bsecurity\b', 
        r'\bpeace\b', r'\belection\b', r'\bnuclear\b', r'\biran\b', r'\bkorea\b', r'\brussia\b', 
        r'\bputin\b', r'\bbush\b', r'\bkerry\b', r'\bvenezuela\b', r'\bsudan\b', r'\bdarfur\b'
    ]
}

sports_articles = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {}
    for cat, patterns in keywords.items():
        score = 0
        for p in patterns:
            if re.search(p, text):
                score += 1
        scores[cat] = score
    
    # Heuristic: Sports score must be highest (strictly greater than others)
    # Also score > 0
    if scores['Sports'] > 0:
        # Check if it's the strict max
        is_max = True
        for cat in scores:
            if cat != 'Sports' and scores[cat] >= scores['Sports']:
                is_max = False
                break
        
        if is_max:
             sports_articles.append(article)

# Sort by description length
sports_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

print('__RESULT__:')
print(json.dumps(sports_articles[:3]))"""

env_args = {'var_function-call-13104621924763589325': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6733588393098441366': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12515281274921194462': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-4082764859491298474': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7752384695117518704': 'file_storage/function-call-7752384695117518704.json', 'var_function-call-11819510026672765726': {'_id': '694480101a20f323c78a0569', 'article_id': '183', 'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}, 'var_function-call-12995565944568440432': [], 'var_function-call-3624804630817289697': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'pred': 'Sports', 'scores': {'World': 0, 'Business': 0, 'Sci/Tech': 0, 'Sports': 1}}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'pred': 'World', 'scores': {'World': 1, 'Business': 1, 'Sci/Tech': 1, 'Sports': 0}}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'pred': 'Business', 'scores': {'World': 0, 'Business': 5, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'pred': 'World', 'scores': {'World': 2, 'Business': 1, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'pred': 'Business', 'scores': {'World': 1, 'Business': 3, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'pred': 'Business', 'scores': {'World': 0, 'Business': 3, 'Sci/Tech': 1, 'Sports': 0}}, {'title': 'Money Funds Fell in Latest Week (AP)', 'pred': 'Business', 'scores': {'World': 1, 'Business': 2, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'pred': 'World', 'scores': {'World': 2, 'Business': 2, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Safety Net (Forbes.com)', 'pred': 'Unknown', 'scores': {'World': 0, 'Business': 0, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Wall St. Bears Claw Back Into the Black', 'pred': 'Sports', 'scores': {'World': 0, 'Business': 0, 'Sci/Tech': 0, 'Sports': 1}}, {'title': "Oil and Economy Cloud Stocks' Outlook", 'pred': 'Business', 'scores': {'World': 0, 'Business': 5, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'No Need for OPEC to Pump More-Iran Gov', 'pred': 'Business', 'scores': {'World': 1, 'Business': 3, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Non-OPEC Nations Should Up Output-Purnomo', 'pred': 'World', 'scores': {'World': 2, 'Business': 2, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Google IPO Auction Off to Rocky Start', 'pred': 'Sci/Tech', 'scores': {'World': 0, 'Business': 1, 'Sci/Tech': 2, 'Sports': 0}}, {'title': 'Dollar Falls Broadly on Record Trade Gap', 'pred': 'Business', 'scores': {'World': 1, 'Business': 3, 'Sci/Tech': 0, 'Sports': 1}}, {'title': 'Rescuing an Old Saver', 'pred': 'Unknown', 'scores': {'World': 0, 'Business': 0, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'Kids Rule for Back-to-School', 'pred': 'Business', 'scores': {'World': 0, 'Business': 1, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'In a Down Market, Head Toward Value Funds', 'pred': 'World', 'scores': {'World': 2, 'Business': 2, 'Sci/Tech': 0, 'Sports': 0}}, {'title': 'US trade deficit swells in June', 'pred': 'Business', 'scores': {'World': 1, 'Business': 2, 'Sci/Tech': 0, 'Sports': 0}}, {'title': "Shell 'could be target for Total'", 'pred': 'Business', 'scores': {'World': 0, 'Business': 1, 'Sci/Tech': 0, 'Sports': 0}}]}

exec(code, env_args)
