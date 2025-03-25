import nltk
import re
import string
# nltk.download()

# Util Methods
def saveEmailAttachement(email_text, attachment_text, filePath):
    file_path = "./data/emails/"+filePath
    file = open(file_path, 'w', encoding='UTF-8')
    file.write(email_text+" " + attachment_text)
    file.close()


#pre-processing
stop_words = set(nltk.corpus.stopwords.words("english"))
spetial_chars = set(string.printable) - set(string.ascii_letters) - set(" ")
escaped_chars = [re.escape(c) for c in spetial_chars]
regex = re.compile(f"({'|'.join(escaped_chars)})")
stemmer = nltk.stem.porter.PorterStemmer()
url_regex = re.compile("(?P<url>https?://[^\s]+)")

def preprocess_text(text):
    # capitalization
    text = str(text)
    text = text.lower()

    # remove urls
    text = re.sub(url_regex," ",text)
    
    # tokenization
    text = nltk.word_tokenize(text, language='english')
        
    # stop words removal
    text = [word for word in text if word not in stop_words]
    
    # noise removal
    text = [word for word in text if word.isalpha()]
    
    # stemming
    text = [stemmer.stem(word) for word in text]
    
    return ' '.join(text)