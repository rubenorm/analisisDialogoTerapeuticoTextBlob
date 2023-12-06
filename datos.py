import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download NLTK resources (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def getSentimentNLTK(text):
    return sia.polarity_scores(text)["compound"]
   
def getSentimentBlob(text):
    return TextBlob(text).sentiment.polarity


fgloria = open("Gloria.txt", "r")
fsylvia = open("Sylvia.txt", "r")
fsylvia2 = open("Sylvia2.txt", "r")
fkathy = open("Kathy.txt", "r")
fdione = open("Dione.txt", "r")
fdione2 = open("Dione2.txt", "r")


gloria = []
sylvia = []
sylvia2 = []
kathy = []
dione = []
dione2 = []


for x in fgloria:
    aux = x.split(" ", 1)
    gloria.append(dict(persona = aux[0][:1], numero = aux[0][1:], indice = aux[0], dialogo = aux[1], valornltk = getSentimentNLTK(aux[1]), valorblob = getSentimentBlob(aux[1])))

for x in fsylvia:
    aux = x.split(" ", 2)
    sylvia.append(dict(persona = aux[0], numero = aux[1][:-1], indice = aux[0]+aux[1], dialogo = aux[2], valornltk = getSentimentNLTK(aux[2]), valorblob = getSentimentBlob(aux[2])))

for x in fsylvia2:
    aux = x.split(" ", 1)
    sylvia2.append(dict(persona = aux[0][:1], numero = aux[0][1:-1], indice = aux[0], dialogo = aux[1], valornltk = getSentimentNLTK(aux[1]), valorblob = getSentimentBlob(aux[1])))

for x in fkathy:
    aux = x.split(" ", 1)
    kathy.append(dict(persona = aux[0][:1], numero = aux[0][1:-1], indice = aux[0], dialogo = aux[1], valornltk = getSentimentNLTK(aux[1]), valorblob = getSentimentBlob(aux[1])))

for x in fdione:
    aux = x.split(" ", 2)
    dione.append(dict(persona = aux[0], numero = aux[1][:-1], indice = aux[0]+aux[1], dialogo = aux[2], valornltk = getSentimentNLTK(aux[2]), valorblob = getSentimentBlob(aux[2])))

for x in fdione2:
    aux = x.split(" ", 1)
    dione2.append(dict(persona = aux[0][:1], numero = aux[0][1:-1], indice = aux[0], dialogo = aux[1], valornltk = getSentimentNLTK(aux[1]), valorblob = getSentimentBlob(aux[1])))

#print(sylvia)

class Session:
    def __init__(self, nombre, dialogos):
        self.nombre =  nombre
        self.xCliente = []
        self.yClienteNLTK = []
        self.yClienteBlob = []
        self.xTerapeuta = []
        self.yTerapeutaNLTK = []
        self.yTerapeutaBlob = []
        self.x = []
        self.yNLTK = []
        self.yBlob = []
        for dialogo in dialogos:
            #print(dialogo["numero"])
            if (nombre == "Sylvia" or nombre == "Sylvia2"): 
                if (dialogo["persona"] == "S"):
                    #x.append(num)
                    self.xCliente.append(int(dialogo["numero"]))
                    self.yClienteNLTK.append(dialogo["valornltk"])
                    self.yClienteBlob.append(dialogo["valorblob"])
                else:
                    #x2.append(num)
                    self.xTerapeuta.append(int(dialogo["numero"]))
                    self.yTerapeutaNLTK.append(dialogo["valornltk"])
                    self.yTerapeutaBlob.append(dialogo["valorblob"])
            else:  
                if (dialogo["persona"] == "C"):
                    #x.append(num)
                    self.xCliente.append(int(dialogo["numero"]))
                    self.yClienteNLTK.append(dialogo["valornltk"])
                    self.yClienteBlob.append(dialogo["valorblob"])
                else:
                    #x2.append(num)
                    self.xTerapeuta.append(int(dialogo["numero"]))
                    self.yTerapeutaNLTK.append(dialogo["valornltk"])
                    self.yTerapeutaBlob.append(dialogo["valorblob"])

sesionGloria = Session("Gloria", gloria)
sesionSylvia = Session("Sylvia", sylvia)
sesionSylvia2 = Session("Sylvia2", sylvia2)
sesionKathy = Session("Kathy", kathy)
sesionDione = Session("Dione", dione)
sesionDione2 = Session("Dione2", dione2)


