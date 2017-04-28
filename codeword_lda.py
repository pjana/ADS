"""
Codeword LDA - injects positive and negative words to ensure sentiments in
topic modeling

@author - Prerana Jana
"""
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from stemming.porter2 import stem
import gensim
from gensim import corpora

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


"""
pre process and clean each review
"""
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    stemmed = " ".join(stem(word) for word in normalized.split())
    return stemmed


reviews = pd.read_pickle('rel_user_reviews.pkl') # (115841, 10)
reviews_text = reviews['text'].tolist()
reviews_clean = []

for j in range(10): #range(len(reviews_text)):
    if j % 2000 == 0:
        print(j)
    reviews_clean.append(clean((reviews_text[j])))


"""
read positive and negative words
"""
stem_p = []
stem_n = []

p_w = open('positive-words.txt','r')
pos_words = p_w.readlines()
positive_word = pd.DataFrame(pos_words)
positive_words = positive_word.iloc[:,0]
positive_words = positive_words.str.split('\n').str.get(0)
p = positive_words.tolist() # 2006
for i in range(len(p)):
    stem_p.append(stem(p[i]))
stem_p = list(set(stem_p)) # 1280



n_w = open('negative-words.txt','r', encoding = 'latin-1')
neg_words = n_w.readlines()
negative_word = pd.DataFrame(neg_words)
negative_words = negative_word.iloc[:,0]
negative_words = negative_words.str.split('\n').str.get(0)
n = negative_words.tolist() # 4781
stem_n = []
for j in range(len(n)):
    stem_n.append(stem(n[j]))
stem_n = list(set(stem_n)) # 2959


"""
injecting positive and negative codeword at every positive and negative word
"""
print('injecting codewords')
coded_clean_reviews = []
clean_reviews = []
for line in reviews_clean:
    clean_reviews.append(line.split())
    # line = 'this food is really good , it is simply good'
    indices = [i for i, x in enumerate(line.split()) if x in stem_p]
    inserted_line = line.split()
    for i in range(len(indices)):
        index = indices[i] + i + 1
        inserted_line.insert(index,'GOODREV2IEW')
    final_line = inserted_line
    indices = [i for i, x in enumerate(inserted_line) if x in stem_n]
    for i in range(len(indices)):
        index = indices[i] + i + 1
        final_line.insert(index,'BADREVIEW')
    coded_clean_reviews.append(final_line)
print(clean_reviews)
print(coded_clean_reviews)
"""
codeword lda implementation
"""
print('running codeword lda')
# Creating the term dictionary of our courpus, where every unique term is assigned an index.
corpus = clean_reviews
dictionary = corpora.Dictionary(corpus)
# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel
# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dictionary, passes=50)
for topic in ldamodel.print_topics():
    print(topic)

"""
clubbing the topics
"""
wn.synsets('sushi')[0].definition()
