
# coding: utf-8

# In[1]:


class GetKey():
    def __init__(self,arraynum):
        self.key=''
        if self.readkeybook()==-1:
            self.key+="Open keybook Error! Please retry!"
        if len(arraynum)!=16:
            key+="arr length Error! Please retry!"
        for i in arraynum:
            self.key+=self.keybook[i]
    def readkeybook(self):
        a=-1
        try:
            f=open("Seck.xjgcb","r")
            a=1
        except:
            a=-1
            return a
        self.keybook=f.read()
        f.close()
        return a

