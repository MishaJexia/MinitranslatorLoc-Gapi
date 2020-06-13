fr=['Je', 'intelligent','suis']
en=['I', 'smart','am']
i=0
txt = "Je suis intelligent"
y=len(en)
while i<y: #for j in fr :
    txt = txt.replace(fr[i], en[i])
    i+=1

print('translated :',txt)
