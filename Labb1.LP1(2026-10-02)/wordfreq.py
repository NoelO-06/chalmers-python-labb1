def tokenize(documents):
    
    resultat = []   #ny lista som vi stegvis lägger till det färdiga resultatet i
    
    for document in documents:  #loopar igenom rad för rad
        ord_lista = document.split()
    
    
        for orden in ord_lista:     #går igenom orden var för sig.
            orden=orden.lower()
            nu = ""
            
            
            for tecken in orden:    
                if tecken.isalpha():   #kollar om tecknet är en bokstav
                    if nu != "" and not nu[0].isalpha():
                        resultat.append(nu)
                        nu = ""
                    nu += tecken
                        
                        
                elif tecken.isdigit():   #kollar om tecknet är en siffra
                    if nu != "" and not nu[0].isdigit():
                        resultat.append(nu)
                        nu = ""
                    nu += tecken

                elif tecken.isspace():
                    if nu != "":
                        resultat.append(nu) #checkar så att ordet vi kikar på inte är ett mellanslag
                        nu=""

                else:
                    if nu != "":
                        resultat.append(nu)
                        nu = ""
                    resultat.append(tecken)
            if nu != "":
                resultat.append(nu)
    return (resultat)



def countWords(words, stopwords):
    frequencies = {}

    for word in words:

        if word in stopwords:
            pass

        else:
            if word not in frequencies:
                
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    return frequencies
    



def printTopMost(frequencies_dictionary, n):
    sorterad = sorted(frequencies_dictionary.items(), key = lambda x: -x[1])
    #.items gör om dictionaryn till en tuple av paren, dvs nyckeln och sen värdet
    #key säger vad soreted ska sortera efter
    if n <= 0:
        return


    if n > len(sorterad): # Om n är större än antalet ord som finns sätter n = listans längd
        n=len(sorterad) 

    for i in range(n):
        ord, nummer = sorterad[i]

        print(ord.ljust(20) + str(nummer).rjust(5))
