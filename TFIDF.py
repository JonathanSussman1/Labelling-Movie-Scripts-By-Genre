import string, math, sys
from operator import itemgetter
import nltk, re, pprint
from nltk import word_tokenize
import numpy as np
from random import sample
from preprocessing import PreprocessingObj

closed_class_stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or']

queries=[]
abstracts=[]
numscripts = 5
numgenrescripts = 50

print("Generating corpus of scripts and genre scripts...")
preprocessor = PreprocessingObj(n_scripts_to_add=40, n_scripts_to_randomly_remove=20, n_genre_scripts_to_add=17, n_genre_scripts_to_randomly_remove=1)


print("computing all scripts TFIDF...")
finalQueries={}
queryNum=0
for i in preprocessor.allscripts[:10]:
   for j in i:
      if j==i[0]:
         finalQueries[i[0]]=[]
         continue
      elif (j[1]!=" " and j[1]!=''):
         newcollection = word_tokenize(j[1])
         filteredcollection  = [word for word in newcollection if word.lower() not in closed_class_stop_words and word not in string.punctuation]
         for k in filteredcollection:
            if (k.lower() not in closed_class_stop_words and k not in string.punctuation) and (not any(k in subquery for subquery in finalQueries[i[0]])):
               wordTFIDF=[k,0,0,0]
               numDocsContainingWord=0
               tf=0
               for l in range(len(preprocessor.allscripts)):
                  purescripts = preprocessor.allscripts[l]
                  purescripts = purescripts[1:]
                  indoc=False
                  # if any(k.lower in map(str.lower,word_tokenize(line[1])) for line in purescripts):
                  #    numDocsContainingWord+=1
                  for freq_line in purescripts:
                     if freq_line[1]:
                        if freq_line[1]!="" and freq_line[1]!=" ":
                           for n in word_tokenize(freq_line[1]):
                              if n.lower()==k.lower():
                                 tf+=1
                                 indoc=True
                  if indoc==True:
                     numDocsContainingWord+=1
               wordTFIDF[1] = numDocsContainingWord
               if (wordTFIDF[1]>1):
                  wordTFIDF[2] =  float(math.log(len(preprocessor.allscripts)/numDocsContainingWord,wordTFIDF[1]))
               else:
                  if (numDocsContainingWord==0):
                     wordTFIDF[2] = float(math.log(sys.float_info.max))
                  else:
                     wordTFIDF[2] =  float(math.log(len(preprocessor.allscripts)/numDocsContainingWord))
               wordTFIDF[3] = wordTFIDF[1] * wordTFIDF[2]
               finalQueries[i[0]].append(wordTFIDF)
   print(finalQueries[i[0]])

print("computing genre scripts TFIDF...")
numDocsContainingWord=0
finalAbstracts={}
for genre in preprocessor.genrescripts:
   finalAbstracts[genre]=[]
   for script in preprocessor.genrescripts[genre]:
      for line in script:
         if line == script[0]:
            continue
         elif (line[1]!=" " and line[1]!=''):
            newcollection = word_tokenize(line[1])
            filteredcollection  = [word for word in newcollection if word.lower() not in closed_class_stop_words and word not in string.punctuation]
            for l in filteredcollection:
               if (l.lower() not in closed_class_stop_words and l not in string.punctuation) and (not any(l in subquery for subquery in finalAbstracts[genre])):
                  wordTFIDF=[l,0,0,0]
                  numDocsContainingWord=0
                  tf=0
                  for freq_genre in (preprocessor.genrescripts):
                     indoc=False
                     for freq_script in preprocessor.genrescripts[freq_genre]:
                        for freq_line in freq_script[1:]:
                           if freq_line[1]!='' and freq_line[1]!=" ":
                              for o in word_tokenize(freq_line[1]):
                                 if o.lower()==l.lower():
                                    tf+=1
                                    indoc=True
                        # if any(l.lower() in map(str.lower,freq_line[1]) for freq_line in freq_script[1:])
                        #    indoc=True
                     if indoc==True:
                        numDocsContainingWord+=1
                     # for freq_line in freq_script[1:] in freq_script in preprocessor.genrescripts[freq_genre]:                    
                  wordTFIDF[1] = tf
                  if (wordTFIDF[1]>1):
                     wordTFIDF[2] =  float(math.log(len(preprocessor.genrescripts)/numDocsContainingWord,wordTFIDF[1]))
                  else:
                     if (numDocsContainingWord==0):
                        wordTFIDF[2] =  float(math.log(sys.float_info.max))
                     else:
                        wordTFIDF[2] =  float(math.log(len(preprocessor.genrescripts)/numDocsContainingWord))
                  wordTFIDF[3] = wordTFIDF[1] * wordTFIDF[2]
                  finalAbstracts[genre].append(wordTFIDF)
   print(finalAbstracts[genre])

print("writing to text file")
linesWritten=0
qnum=-1
numvals=0
f= open("testoutput2.txt","w+")
for q in finalQueries:
   qnum+=1
   cosineSims=[]
   for a in finalAbstracts:
      c=0.0
      asum=0.0
      qsum=0
      qinfo = finalQueries[q]
      ainfo = finalAbstracts[a]
      for i in range(len(qinfo)):
         qtfidf = qinfo[i]
         qsum+=(qtfidf[3])**2
         for d in range(len(ainfo)):
            if (((ainfo[d])[0])==qtfidf[0]):
               c+= float(((ainfo[d])[3])*qtfidf[3])
               break
         else:
            c+= 0.0

      ainfo = finalAbstracts[a]
      for i in range(len(ainfo)):
         atfidf = ainfo[i]
         asum+=(atfidf[3])**2
      numvals+=1
      if (asum!=0 and qsum!=0):
         c = c / float(((asum)*(qsum))**0.5)
         if c!=0:
            cosineSims.append([q,a,c])
         else:
            cosineSims.append([q,a,0])
      else:
         cosineSims.append([q,a,0])
      
   cosineSims = sorted(cosineSims, key=itemgetter(2), reverse = True)
   for l in cosineSims:
      f.write(str(l[0]) + " " + str(l[1]) + " " + str(l[2]) + "\n")
      linesWritten+=1

f.close()