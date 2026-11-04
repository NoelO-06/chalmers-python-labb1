import sys #läsa argument från terminalen
import urllib.request #för att hämta data
from wordfreq import tokenize, printTopMost, countWords

def main():
    stopwords_files = open(sys.argv[1], encoding="utf-8")
    '''
    sys.argv hämtar argument 1, då när vi ex skall söka igenom en fil kör vi ett kommando i
    terminalen så skriver vi olika "argument" eller info och detta är ett sätt att plocka ut 
    indivuduella argument
    '''

    stopwords_list = []
    for line in stopwords_files:
        stopwords_list.append(line.strip())
    stopwords_files.close()
    #appendar de olika stopporden till en lokal lista

    if sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://"): 
        #checkar om webbadress
        
        response = urllib.request.urlopen(sys.argv[2])
        #kopplar upp mot webbadress och hämtar data
        
        lines = response.read().decode("utf8").splitlines() 
        #read= hämtar data i råformat, 
        # decode("utf8") = omvandlar till vanlig textsträng, med å,ä,ö, 
        # Splitlines = delar upp strängen vid varje radbrytning till en lista av rader
        
        words = tokenize(lines)

    else:
        lines = open(sys.argv[2], encoding="utf-8")
        words = tokenize(lines.readlines()) 
        #gör också om varje rad fast för en fil, till en lista

        lines.close()#stänger så filen inte är fortsatt öppen i datorns minne

    n = int(sys.argv[3]) 
    #tredje argumen som tar hur många ord vi skall ha i toplista


    frequency_dictionary = countWords(words, stopwords_list)

    printTopMost(frequency_dictionary, n)

    
main()

