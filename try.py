from nltk.corpus import wordnet as wn
from itertools import chain

input_word = raw_input(&quot;Enter word to get hyponyms and hypernyms: &quot;)

for i,j in enumerate(wn.synsets('dog')):
print &quot;Meaning&quot;,i, &quot;NLTK ID:&quot;, j.name()
print &quot;Hypernyms:&quot;, &quot;, &quot;.join(list(chain(*[l.lemma_names() for l in j.hypernyms()])))
print &quot;Hyponyms:&quot;, &quot;, &quot;.join(list(chain(*[l.lemma_names() for l in j.hyponyms()])))
wn.synsets('sushi')[0].definition()


(0, '0.073*"sushi" + 0.057*"roll" + 0.036*"hibachi" + 0.019*"primanti" + 0.014*"fish" + 0.012*"chef" + 0.011*"rice" + 0.010*"tuna" + 0.007*"japanes" + 0.007*"salmon"')
(1, '0.011*"sauc" + 0.011*"meatbal" + 0.009*"menu" + 0.009*"restaur" + 0.009*"salad" + 0.009*"order" + 0.008*"good" + 0.008*"dinner" + 0.007*"dish" + 0.007*"also"')
(2, '0.013*"coffe" + 0.010*"like" + 0.009*"ice" + 0.009*"flavor" + 0.009*"store" + 0.008*"it" + 0.008*"cream" + 0.008*"shop" + 0.008*"chocol" + 0.007*"one"')
(3, '0.122*"pizza" + 0.032*"wing" + 0.017*"deliveri" + 0.017*"order" + 0.014*"crust" + 0.013*"hoagi" + 0.012*"vegan" + 0.012*"sauc" + 0.011*"pie" + 0.010*"chees"')
(4, '0.025*"bar" + 0.023*"beer" + 0.015*"place" + 0.013*"drink" + 0.011*"it" + 0.011*"good" + 0.010*"great" + 0.009*"night" + 0.008*"select" + 0.008*"like"')
(5, '0.023*"sandwich" + 0.019*"fri" + 0.014*"chees" + 0.012*"like" + 0.011*"good" + 0.011*"it" + 0.009*"order" + 0.008*"burger" + 0.007*"bread" + 0.007*"get"')
(6, '0.031*"place" + 0.029*"food" + 0.026*"great" + 0.024*"good" + 0.020*"it" + 0.013*"go" + 0.013*"servic" + 0.012*"alway" + 0.012*"love" + 0.012*"friend"')
(7, '0.015*"order" + 0.013*"food" + 0.012*"time" + 0.010*"u" + 0.009*"get" + 0.009*"would" + 0.009*"one" + 0.009*"place" + 0.009*"go" + 0.008*"wait"')
(8, '0.013*"hotel" + 0.009*"ethiopian" + 0.009*"stay" + 0.008*"club" + 0.007*"tana" + 0.007*"room" + 0.006*"pittsburgh" + 0.006*"inn" + 0.006*"play" + 0.005*"burgatori"')
(9, '0.032*"taco" + 0.022*"chicken" + 0.015*"flavor" + 0.013*"rice" + 0.011*"mexican" + 0.011*"pork" + 0.010*"restaur" + 0.010*"smoke" + 0.010*"food" + 0.009*"good"')


a = [str(lemma.name()) for lemma in wn.synset('gyro.n.01').lemmas()]
item = wn.synset('red.n.01')
item.hypernyms()
