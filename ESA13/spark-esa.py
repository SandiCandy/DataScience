import re
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("shakespeare.txt")
    
    #out = lines.map(lambda l: [re.sub('<<.*?>>', " ", x) for x in lines])
    #print(lines)

    ############## CLEANING *******
    # 1. Clean information and copyright information ***/

    # 1a: Remove the Header (alles vor Beginn des ersten Werks manuell geloescht)
    # 1b: Remove Copyright Information (--> toRemove)
    toRemove = "<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>"

    # 1c: Remove all punctuation marks (".", ",", ":", "!", "?", ";", ...) ("brow," to "brow") 
    # 1d: Change everything to lower case (start of new sentence) ---> Problem: Some words (names and I) are normally not lower case
    # 1f: Theoretisch muessten noch die Titel der Werke entfernt werden (wird hier vernachlaessigt)
    wordRdd = lines.flatMap(lambda line : line
                        .replace(toRemove, '')
                        .lower()
                        .replace(',','')
                        .replace('.','')
                        .replace(';','')
                        .replace(':','')
                        .replace('?','')
                        .replace('!','')
                        .replace(')','')
                        .replace('(','')
                        .split(" "))

     #Loeschen aller leeren "Worte"
    wordsRdd = wordRdd.filter(lambda x: x != "")

    wordPairRdd = wordsRdd.map(lambda word : (word, 1))
    wordCounts = wordPairRdd.reduceByKey(lambda x, y: x + y)

    sortedWords = wordCounts.sortBy(lambda wordCount: wordCount[1], ascending=False)

    sortedWords.filter(lambda line: len(line) in line)

    #for word, count in sortedWords.collect():
    i = 1
    for word, count in sortedWords.takeOrdered(25, key = lambda x: -x[1]):
        print("{} {}: {}".format(i, word, count))
        i += 1


    ##### LÖSUNG
    # Siehe Screenshot 
    # have mit 5873x    
        

    ##### Zusaetzliche Anmerkung
    # - Verkuerzte Worte wie "I'll" = I will, "that`s"="that is" werden als eigenstaendige Woerter gesehen
    # - Prinzipiell kann man noch Stopwoerter (haeufig auftretente und meist irrelevante Woerter zur Erfassung des Inhalts) herausfiltern - war hier allerdings nicht gefordert
    # - Weiterhin ist es sinnvoll Anfuehrungszeichen zu filtern also 'Beispiel --> Beispiel), dabei ist zu beachten, dass ' auch im Wort vorkommen kann (I'll)
    # - Aehnliches gilt fuer - (z.B. Beispiel- --> Beispiel). Aber auch - kann mitten im Wort vorkommen (z.B. wild-fowl)
    