#!/usr/bin/python3

import copy

class dictinfo() :

  ''' show dict info  '''
  def __init__(self , dictin) :
    self.mdict = dictin
    self.keylist = []
    self.key =  []
    self.depth = []

    self.outv = ''

    self.dictparsermain(self.mdict)

  def refresh(self ,  data) :
    ''' refresh data  '''
    self.mdict = copy.deepcopy(data)
    self.key =  []
    self.depth = []
    self.keylist = []
    self.dictparsermain(self.mdict)

  def showkey(self) :
    ''' show all key combination '''
    return self.keylist

  def haskey(self , klist) :
    ''' confirm key is existed '''
    if  klist in self.keylist :
      return True 
    else :
      return False

  def getvalue(self , klist) :
    '''get value '''
    if self.haskey(klist) :
      klist.reverse()
      self.loopgetv(self.mdict , klist)
      return self.outv
    else  :
      return None

  def loopgetv(self , data  , klist)  :
    if klist != [] :
      key = klist[-1]
      klist.pop()
      self.loopgetv(data[key] ,  klist)
    else :
      self.outv = data

  def dictparsermain(self  , data ) :

    self.depth.append(len(data.keys()))
    for k in data :
      self.key.append(k)
      if isinstance(data[k] , dict) :
        self.dictparsermain(data[k])
      else :
        stack = copy.deepcopy(self.key)
        self.keylist.append(stack)
        while True :
          if self.depth == [] :
            break
          if self.depth[-1] == 1 :
            self.key.pop()
            self.depth.pop()
          else :
            self.depth[-1]  = self.depth[-1] - 1 
            self.key.pop()
            break
            
    


''' modify dicct '''

def dictmerge(dict1 , dict2) :
  '''
  merge dict
  '''
  for k in dict2  :
    if k not in  dict1 :
      dict1[k] = copy.deepcopy(dict2[k])
    else :
      if isinstance(dict1[k] , dict) :
        dictmerge(dict1[k] , dict2[k])
      else :
        dict1[k] = copy.deepcopy(dict2[k])
      
def setvalue(dictin  , keylist , value) :
  if len(keylist) == 0 :
    return
  k = keylist[0]
  if len(keylist) == 1 :
    dictin[k] = copy.deepcopy(value)
  else :
    if keylist[0] in dictin :
      keylist.pop(0)
      setvalue(dictin[k] , keylist ,value)
    else :
      dictin[k] = {}
      keylist.pop(0)
      setvalue(dictin[k] , keylist ,value)
  


'''  test   '''
d1 = { 'a':{'cb':'4' ,
            'ab':{'abc':{'abcd':'1'}} ,
            'bb':{'bbc':{'bbcd':'2'} ,
                  'cbc':{'cbcd':'3'}}}}

print(d1)
md1 = dictinfo(d1)
print(md1.showkey())
d2  = { 'aa':{'cb':'4' ,
             'ab':{'abc':{'abcd':'1'}} ,
             'bb':{'bbc':{'bbcd':'2'} ,
                   'cbc':{'cbcd':'3'}}}}
md1.refresh(d2)
print(md1.showkey())
print(md1.getvalue(['aa' , 'ab' , 'abc' , 'abcd']))
a = {'a':{'b':2}}
b = {'a':{'c':2}}
dictmerge(a,b)
print(a)
setvalue(a , ['a','b'] , 22)
print(a)
