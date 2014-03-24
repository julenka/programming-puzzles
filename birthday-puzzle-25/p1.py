original = u'''рфззн ишкервфн огдшф! нщгэку ецутен ашму нуфкы щдв ещвфн! ьщые зущзду цшдд сщтпкфегдфеу нщгб фтв ьфлу ощлуы фищге рщц нщг сфт куте сфкы фе дщцук кфеуыб иге ерукуэы ыщьуерштп ьгср ьщку шьзщкефте ерфе нщг туув ещ лтщцю

ерукуэы ф цфк щтб рфы иуут ащк сутегкшуыб иге ьщые зущзду фку щидшмшщгы ещ шеы учшыеутсую ф ыудусе ауц штвшмшвгфды фку срщыут ещ иу фпутеы шт ершы цфк щтсу ерун куфср ецутен ашмую ерун фку ыудусеув ащк ерушк штеуддшпутсуб куыщгксуагдтуыыб еутфсшенб фтв ыекутпер ща цшддю шэму иуут щиыукмштп нщг сфкуагддн ащк еру зфые еркуу фтв ф рфда нуфкыб фтв шэь зкщгв ещ ыфн ерфе нщгэку щту ща еру ещз сфтвшвфеуы ащк еру туче ифеср ща кускгшеыю

ещ иу фссузеувб рщцумукб нщгэдд рфму ещ зфыы ф ыукшуы ща еуыеыю ша нщгэку куфвштп ершы ьуыыфпуб нщгэму фдкуфвн зфыыув еру ашкые щтуб иге еру щерукы цщтэе иу ыщ уфыню

ша нщг афшдб ерут ершы цшдд рфму огые иуут ф ышьзду ишкервфн згяяду акщь вфмшвб фтв нщгэдд пщ ифсл ещ дшмштп нщгк тщкьфд дшаую ша нщг зфыыб ф туц цщкдв цшдд иу щзутув гз ещ нщгб фтв цуэдд ашпре еру ифв пгны ещпуерукю

нщгк ашкые сщву цщкв шы цфдлукю ерфе ы фдд шэь фддщцув ещ ыфн ащк тщцю пщщв дгсл!

вфмшв'''
key = {}

def translate(original, key):
    result = ""
    for c in original:
        if c in key:
            result += key[c]
        else:
            result += c
    return result

def extend_table(existing_key, from_str, to_str):
    for (f,t) in zip(from_str, to_str):
        existing_key[f] = t

def extend_print(from_str, to_str):
    extend_table(key, from_str, to_str)
    print translate(original, key)

# Work on it...
# solution!
solution = u'''happy birthday julia! you're twenty five years old today! most people will congratulate you, and make jokes about how you can rent cars at lower rates, but there's something much more important that you need to know:

there's a war on, has been for centuries, but most people are oblivious to its existence: a select few individuals are chosen to be agents in this war once they reach twenty five: they are selected for their intelligence, resourcefulness, tenacity, and strength of will: i've been observing you carefully for the past three and a half years, and i'm proud to say that you're one of the top candidates for the next batch of recruits:

to be accepted, however, you'll have to pass a series of tests: if you're reading this message, you've already passed the first one, but the others won't be so easy:

if you fail, then this will have just been a simple birthday puzzle from david, and you'll go back to living your normal life: if you pass, a new world will be opened up to you, and we'll fight the bad guys together:

your first code word is walker: that s all i'm allowed to say for now: good luck!

david'''

code = "walker"