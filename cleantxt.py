# Imports for set up
import nltk
from nltk.corpus import stopwords
import enchant
import re

# Reading the CSV file & setting stop words
data = open("fraud_email_.csv", 'r', encoding="utf8")
stop_words = nltk.corpus.stopwords.words('english')
url = ["http", "https"]

#Create a dictionary
dictionary = enchant.Dict("en_US")

# Parse through csv file and eliminate stop words
appendFile = open('cleantext.csv', 'w', encoding="utf8")
svmFile = open('svmtext.csv', 'w', encoding="utf8")

#Set up the csv attributes
sent = data.readline()
appendFile.write("ID,Text,Class,Percent Misspelled,Has URL,Fully Uppercase,Total Words\n")
svmFile.write("Class,Percent Misspelled,Has URL,Fully Uppercase,Total Words\n")

count = 0
string = sent[:len(sent)-2]

#Loop that outputs to the file as text, class
while True:
    URLFlag = 0
    misspelled = []
    appendFile.write(str(count) + ",")
    count = count + 1

    #Reroute variables to next line's values
    sent = data.readline()
    words = sent.split()
    string = words[:len(words)-1]
    nums = sent[len(sent)-2:]
    up = 0
    ress = []
    for sub in nums:
        ress.append(re.sub('\n', '', sub))
    
    #Loop to iterate and eliminate stop words
    for i in string:
        w = re.sub(r'[^\w\s]', ' ', i)
        #Add word to file if it is not a stop word
        if w not in stop_words:
            appendFile.write(w + " ")
            
        #Add misspelled words to the misspelled array
        if dictionary.check(w) == False:
            misspelled.append(w)

        #Check to see if there is any URL tags
        for i in url:
            if i in w:
                URLFlag = 1

        #Check % uppercase
        if w.isupper():
            up = up + 1

    missed = len(misspelled)
    total = len(words)
    
    if total > 0:
        miss = missed/total
        upper = up/total
    else:
        miss = 0
        up = 0

    if not words:
        break
    
    appendFile.write("," + ress[0] + "," + str(miss) + "," + str(URLFlag) + "," + str(upper) + "," + str(total) + "\n")
    svmFile.write(ress[0] + "," + str(miss) + "," + str(URLFlag) + "," + str(upper) + "," + str(total) + "\n")
       
#Close the file
appendFile.close()
svmFile.close()
data.close()
print("Files successfully cleaned.")


