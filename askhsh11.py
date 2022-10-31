import os
#Ανοίγω το αρχείο κειμένου
fin=open("a.txt","r")
text=fin.read()
fin.close()
#Βάζω όλα τα στοιχεία σε μία λίστα αφού αφαιρέσω όλα τα κενά
text=os.linesep.join([s.strip() for s in text.splitlines() if s])
text=" ".join([s.strip() for s in text.split(" ") if s])
#Αφαιρώ όλα τα σημεία στίξης
points=[".", ",", "'", "?", ";"]
for p in points:
	text=text.replace(p,"")
#Κόβω σε λέξεις
words=text.split()
pairs=[]
#Ψάχνω τα ζευγάρια λέξεων με μήκος ίσο με 20 και τα αφαιρώ από τη λίστα
for w1 in words:
    for w2 in words:
        if w1 in pairs or w2 in pairs:
            continue
        if w1 != w2 and len(w1) + len(w2) == 20:
            print(w1, w2)
            pairs.append(w1)
            pairs.append(w2)
            break
#Εμφανίζω τη λίστα των λέξεων χωρίς τα ζευγάρια
print(list(set(words)-set(pairs)))







































