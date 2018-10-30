import hashlib
import json


text = 'More efficient attacks are possible by employing cryptanalysis to specific hash functions. When a \
collision attack is discovered and is found to be faster than a birthday attack, a hash function is often \
denounced as "broken". The NIST hash function competition was largely induced by published collision \
attacks against two very commonly used hash functions, MD5 and SHA-1. The collision attacks against \
MD5 have improved so much that, as of 2007, it takes just a few seconds on a regular computer. Hash \
collisions created this way are usually constant length and largely unstructured, so cannot directly be \
applied to attack widespread document formats or protocols.'

hashed = hashlib.md5(text.encode()).hexdigest()

synonyms = {
'More': ['also','extra','further','higher','new','other','major','spare'], 
'efficient': ['able','active','adequate','capable','competent','decisive','dynamic','economical', 'energetic','potent','powerful','productive','profitable','skilled','skillful','tough',],
'are': [], 
'possible': ['achievable','available','conceivable','desirable','feasible','imaginable','potential','probable','viable', ],
'by': [], 
'employing': ['apply','engage','exploit','handle','occupy','operate','spend','use','utilize',], 
'cryptanalysis': [], 
'to': [], 
'specific': ['clear-cut','definite','definitive','different','distinct','exact','explicit','individual','limited','peculiar','precise','special','specialized','unambiguous','unequivocal','unique',], 
'hash': [], 
'functions.': [], 
'When': [], 
'a': [], 
'collision': [], 
'attack': ['aggression','barrage','charge','incursion','intervention','intrusion','invasion','offensive','onslaught','outbreak',], 
'is': [], 
'discovered': ['detected','disclosed','exposed','identified','invented',], 
'and': [], 
'found': ['begin','construct','create','erect','establish','form','initiate','launch','organize','plant','raise','settle','start',], 
'be': [], 
'faster': [], 
'than': [], 
'birthday': [], 
'function': [], 
'often': [], 
'denounced': ['accuse','blame','boycott','brand','castigate','censure','criticize','decry','excoriate','prosecute','rebuke','revile','scold','threaten','vilify',], 
'as': [], '"broken".':[], 
'The': [], 
'NIST': [], 
'competition': ['championship','clash','event','fight','game','match','meeting','race','rivalry','sport','struggle','tournament','trial',],
'was': [], 
'largely': ['broadly','chiefly','generally','mostly','predominantly','principally','widely',], 
'induced': [], 
'published': [], 
'against': [], 
'two': [], 
'very': [], 
'commonly': ['frequently','generally','more often than not','ordinarily','regularly',],
'used': [], 
'functions': [], 
'MD5': [], 
'SHA-1.': [], 
'have': [], 
'improved': ['enhanced','revised','upgraded',], 
'so': [], 
'much': [], 
'that': [], 
'of': [], 
'2007': [], 
'it': [], 
'takes': [], 
'just': [], 
'few': [], 
'seconds': [], 
'on': [], 
'regular': [], 
'computer.': [], 
'Hash': [], 
'collisions': [], 
'created': [], 
'this': [], 
'way': [], 
'usually': ['commonly','consistently','customarily','frequently','generally','mostly','normally','occasionally','ordinarily','regularly','routinely','sometimes',], 
'constant': [], 
'length': [], 
'unstructured': ['disorganized','unregulated',], 
'cannot': [], 
'directly': [], 
'applied': [], 
'widespread': [], 
'document': [], 
'formats': [], 
'or': [], 
'protocols.': []}

def testValue(text, text_arr, syn, index, hashed):
    if index == len(text_arr):
        return
    
    # keep current word
    testValue(text, text_arr, syn, index+1, hashed)
    # go throuh all replacements and do them
    for rep in syn.get(text_arr[index], []):
        new_text = text.replace(text_arr[index], rep)
        new_hash = hashlib.md5(new_text.encode()).hexdigest()
        if(new_hash==hashed):
            print('text with the same hash value is:\n', new_text)
            print('it also has the hash value of: \n', new_hash)
            print('original hash value is: \n', hashed)
            quit()
        testValue(new_text, text_arr, syn, index+1, hashed)


print('hash value =', hashed)
testValue(text, text.split(), synonyms, 0, hashed)