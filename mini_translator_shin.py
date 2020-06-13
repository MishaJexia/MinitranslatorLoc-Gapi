from googletrans import Translator
translator=Translator()

print('traduit vers fr ou en?')
froren=input()
print('Taper votre message à traduire : ')

txt = input()
if(froren.casefold()=='en'.casefold()) :#casefold to use capital or letter on lowercase
    result = translator.translate(txt, src='fr', dest='en')
    print('translated :')
    print(result.text)
else :
    result = translator.translate(txt, src='en', dest='fr')
    print('traduit :')
    print(result.text)