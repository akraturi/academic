import collections
import time

spBoxKey=[3,5,2,7,4,10,1,9,8,6]
cmpBox=[6,3,7,4,8,5,10,9]
ip=[2,6,3,1,4,8,5,7]
fp=[4,1,3,5,7,2,8,6]
expBox=[4,1,2,3,2,3,4,1]
spBox=[2,4,3,1]
sbox1=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
sbox2=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def splitList(l):
    half=len(l)//2;
    return l[:half],l[half:]

def applysBox(l,s):
    result=list(bin(s[int(''.join(l[0:2]),2)][int(''.join(l[2:4]),2)])[2:])
    return formatResult(result,len(l)//2)

def leftShift(l,n):
    d=collections.deque(l)
    d.rotate(-n)
    return list(d)

def applyPermutation(inp,permutation):
     inp=[inp[i-1] for i in permutation]
     return inp; 

def performXOR(l1,l2):
    l=list(bin(int(''.join(l1),2)^int(''.join(l2),2))[2:])
    length= max(len(l1),len(l2));
    return formatResult(l,length)

def performEncryption(inp,k1,k2):
    l1,l2=splitList(inp)
    temp=performXOR(l1,performFunction(l2,k1))
    l1=l2;
    l2=temp;
    temp=performXOR(l1,performFunction(l2,k2))
    return applyPermutation(temp+l2,fp);

def formatResult(l,length):
      while len(l)<length:
          l=['0']+l  
      return l;

def performFunction(l,k):
    result=applyPermutation(l,expBox)
    length=len(result)
    result=performXOR(result,k)
    l1,l2=splitList(result)
    l1=applysBox(l1,sbox1)
    l2=applysBox(l2,sbox2)
    return applyPermutation(l1+l2,spBox)
     
def generateKeys(key):
    key=applyPermutation(key,spBoxKey)
    l1,l2=splitList(key)
    l1=leftShift(l1,1)
    l2=leftShift(l2,1)
    k1=applyPermutation(l1+l2,cmpBox)
    k2=applyPermutation(leftShift(l1,2)+leftShift(l2,2),cmpBox)
    return k1,k2;
    
#def isInputValid(inp,key):
#    if len(inp) != 8 
#       return False
#    if len(key) != 10:
#       return False
#    if(!isBinary(inp)||!isBinary(key)):
#       return False
#    return True            

#def isBinary(l):
#    return all(i in ('0','1') for i in l)

         
print("\t::Simplied Data Encryption standard::")
time.sleep(0.4)

inp=list(input("Enter 8 bit binary plain text:\n"))
key=list(input("Enter the 10 bit binary key for encryption:\n"))

inp=applyPermutation(inp,ip)
k1,k2=generateKeys(key)
print("\tData is being incrypted...")
time.sleep(0.4)
result=performEncryption(inp,k1,k2)
print("Cipher text:"+''.join(result))



