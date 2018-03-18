import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def word_feats(words):
	return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print ('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))



classifier = NaiveBayesClassifier.train(trainfeats)
print ('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
##classifier.show_most_informative_features()
tt={'love': False, 'deal': False, 'tired': False, 'feel': False, 'is': True, 'am': False, 'an': False, 'sandwich': False, 'ca': False, 'best': True, '!': True, 'what': False, 'i': True, '.': False, 'amazing': False, 'horrible': False, 'sworn': False, 'awesome': False, 'do': False, 'good': False, 'very': False, 'boss': False, 'beers': False, 'not': False, 'with': False, 'he': False, 'enemy': False, 'about': False, 'like': False, 'restaurant': False, 'this': True, 'of': False, 'work': False, "n't": False, 'these': False, 'stuff': False, 'place': False, 'my': False, 'view': False}
input_text="I like it."
dict_input_text={'i':False,'like':False,'it':False}
print (classifier.classify(dict_input_text))
