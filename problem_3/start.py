from data_dict import synonyms
from itertools import product


#create a list of all synonyms of a word
def get_synonyms(key):
    if type(key) is not str:
        raise TypeError("Only Strings are acceptable")
    words =set()
    l_synonyms = synonyms.copy()
    subkey =""
    #if the key exists
    while key in l_synonyms:
        #check if the value is a tuple
        if type(l_synonyms[key]) != tuple:
            oldkey=key
            key = l_synonyms[key]
            words.add(key)
            l_synonyms.pop(oldkey)
        else:
            for subkey in l_synonyms[key]:
                if  subkey in l_synonyms:
                    words.add(subkey)
                    words.add(l_synonyms[subkey])
                    oldkey=subkey
                    subkey = l_synonyms[subkey]
                    l_synonyms.pop(oldkey)
                else:
                    words.add(subkey)
           
            oldkey=key
            key = l_synonyms[key]
            l_synonyms.pop(oldkey)
    
    #print(words)
    return list(words)

#create variations of given sentence
#Assumption input string is in a format 'xx : xx'
#This will keep the second part of the string fixed
def get_variations(sentence):
    if type(sentence) is not str:
        raise TypeError("Only Strings are acceptable")
    parts =sentence.split(":")
    if len(parts)<2:
        raise ValueError("Strings should be in two parts separated by ':' ")
    result=[]
    synonym_list =[]

    text_parts = parts[0].split()
    #get  synonyms of all the words
    for word in text_parts:
        synonym_list.append(get_synonyms(word))

    #create a product of all the synonyms of each word
    for x in product(*synonym_list):
        result.append(" ".join(x) + ": " + parts[1].strip())
    return result
    

def main():
    #input 1
    text = "ph #: +91-9848012345"
    variations =  get_variations(text)    
    print(variations)  
    for variation in variations:
        print(variation)

    #input 2
    text = "NH #: 44"
    variations =  get_variations(text)   
    print(variations)  
   
    for variation in variations:
        print(variation)




if __name__ == '__main__':
    main()