fr=['Je', 'intelligent','suis', 'bonjour', 'type']
en=['I', 'smart','am', 'hello', 'taper']
i=0
# txt = "Je suis intelligent"
print('Taper votre message à traduire : ')
txt = input()
y=len(en)
while i<y: #for j in fr :
    txt = txt.replace(fr[i], en[i])
    i+=1

print('translated :',txt)
