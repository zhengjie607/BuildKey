
# coding: utf-8

# In[21]:


import datetime
from BuildKey import GetKey
from MyCryptoAMSlicer import PrpCrypt
arr1=[68002, 9786, 970, 453, 5, 789, 3426, 90876, 21, 4563, 2965, 432, 34, 845, 395, 434]
arr2=[976, 902, 238, 5432, 754, 70, 32, 72, 214, 9029, 341, 3453, 322, 6377, 222, 3075]
arr3=[ 432, 65, 7658, 261, 8276, 144, 11, 9804, 230, 643, 473, 2287, 432, 7978, 484, 353]
arr4=[21, 79, 6, 56, 200, 65, 102, 4, 655, 4444, 8098, 65323, 643, 1111, 378, 63]
arr_final=[658, 221, 23522, 4, 4346, 6, 7, 1459, 9, 10, 10011, 7910, 13, 312, 52789, 646]
def authorization(serialnumber,days1):
    if len(serialnumber.strip())!=39:
        return -1#序列号长度有误
    tmp_serialnumber=serialnumber.replace('-','')
    serialnumber1=tmp_serialnumber[0:8]
    serialnumber2=tmp_serialnumber[8:16]
    serialnumber3=tmp_serialnumber[16:24]
    serialnumber4=tmp_serialnumber[24:32]
    
    key1=GetKey(arr1).key
    key2=GetKey(arr2).key
    key3=GetKey(arr3).key
    key4=GetKey(arr4).key
    key_final=GetKey(arr_final).key
   
    enserialnumber1=PrpCrypt(key1).encrypt(serialnumber1)
    enserialnumber2=PrpCrypt(key2).encrypt(serialnumber2)
    enserialnumber3=PrpCrypt(key3).encrypt(serialnumber3)
    enserialnumber4=PrpCrypt(key4).encrypt(serialnumber4)
    
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    newyear=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).year
    newmonth=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).month
    newday=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).day
    
    beforeAes=str(enserialnumber3,encoding='utf-8')+str(newday)+str(enserialnumber2,encoding='utf-8')+str(enserialnumber4,encoding='utf-8')+str(newyear)[2:4]+tohex(newmonth)+str(enserialnumber1,encoding='utf-8')
    w=beforeAes.replace("\n","")
    print(key_final)
    return PrpCrypt(key_final).encrypt(w)
    
def authorization_days(days1):
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    newyear=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).year
    newmonth=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).month
    newday=(datetime.datetime(year,month,day)+datetime.timedelta(days=days1)).day
def tohex(be):
    tmp=""
    if be==10:
        tmp="A"
    elif be==11:
        tmp="B"
    elif be==12:
        tmp='C'
    else:
        tmp=str(be)
    return tmp
if __name__=='__main__':
    a=authorization("e4be-74e4-3029-0f40-fb40-9b13-f4e0-9ccf",290)
    print(a)


# In[ ]:


dir(datetime.datetime.now)

