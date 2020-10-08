sent = str(input("Write your sentence, than I calculate :  "))
sent_dict = {}
looked = []
for i in sent:
    if i not in looked:
        sent_dict.update({i: sent.count(i)})
        looked.append(i)
    else:
        pass
print(sent_dict)
