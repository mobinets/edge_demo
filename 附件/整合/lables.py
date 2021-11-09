lableInfo=[]
with open('model/labels.txt','r') as f:
    lableInfo = f.read().strip().split("\n")