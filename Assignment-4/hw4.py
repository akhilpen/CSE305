import sys
sys.setrecursionlimit(1000000)
tempfunarray = {}

Bind={}

length=0
line = 0

file=0





def push(a,stack,toBind,funarray,inoutarray,line,indicator):
 alphabetList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

 if indicator==1:
  for i in (funarray):

   if funarray.get(i)[0] == a[0:len(a)-1]:

    if (a[0:len(line)-1]) in toBind:
     stack.push(toBind[a[0:len(a)-1]])

     return line
 if a==":false:" or a == ":true:\n" or a == ":unit:":
  stack.push(a[0:len(a)-1])

 elif '"' in a:
  stack.push(a[0:len(a)-1])
 elif (a[0:len(a)-1]) in funarray:
  stack.push(a[0:len(a)-1])
 elif a[0] in alphabetList:

  if a[0:len(a)-1] not in toBind:
   toBind[a[0:len(a)-1]] = 'empty'
  stack.push(a[0:len(a)-1])

 elif a[0:len(a)-1]  in toBind :
  stack.push(a[0:len(a) - 1])




 elif a[0] == '-':
   if a[1] == '0':
    stack.push(0)
   elif a[1].isdigit():
    a1=float(a[1:])
    b1=int(a1)
    if a1%b1==0:
     stack.push(-b1)
    else:
     stack.push(":error:")
   else:
    stack.push(":error:")
 else:
    if a[0] == '0':
     stack.push(0)
    else:
     a=float(a)
     b=int(a)
     if a%b==0:
      stack.push(b)
     else:
      stack.push(":error:")
 return line


def add(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      c=a+b
      stack.push(c)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def sub(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      c=b-a
      stack.push(c)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def mul(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      c=b*a
      stack.push(c)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def div(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if a == 0:
     stack.push(a)
     stack.push(":error:")
   else:
    if isinstance(a,int):
     if stack.isEmpty():
      stack.push(a)
      stack.push(":error:")
     else:
      b=stack.pop()
      if (b in toBind) and (toBind[b]!='empty'):
       b=toBind[b]
      if isinstance(b,int):
       c=int(b/a)
       stack.push(c)
      else:
       stack.push(b)
       stack.push(a)
       stack.push(":error:")
    else:
     stack.push(a)
     stack.push(":error:")

def rem(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      c=b%a
      stack.push(c)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def neg(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    b=-a
    stack.push(b)
   else:
    stack.push(a)
    stack.push(":error:")


def dobind(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
  a = stack.pop()
  if (stack.isEmpty() or a== ":error:"):
   stack.push(a)
   stack.push(":error:")
  else:
   b = stack.pop()
   if b in toBind:
    if a in toBind:
     if toBind[a]== "empty":
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
     else:
      toBind[b]=toBind[a]
      stack.push(":unit:")
    else:
     toBind[b]=a
     stack.push(":unit:")
   else:
     stack.push(b)
     stack.push(a)
     stack.push(":error:")

def swap(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if stack.isEmpty():
    stack.push(a)
    stack.push(":error:")
   else:
    b=stack.pop()
    stack.push(a)
    stack.push(b)



def pop(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
  stack.pop()


def true(stack,toBind):
 stack.push(":true:")
 return line

def false(stack,toBind):
 stack.push(":false:")

def error(stack,toBind):
 stack.push(":error:")


def doand(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if (a == ':true:') or (a == ':false:') :
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if (b == ':true:') or (b == ':false:') :
      if a == ':true:' :
       a1 = 1
      else:
       a1 = 0
      if b == ':true:' :
       b1 = 1
      else:
       b1 = 0
      c=a1 and b1
      if c == 1 :
       c1 = ":true:"
      else:
       c1 = ":false:"

      stack.push(c1)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")
def door(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if (a == ':true:') or (a == ':false:') :
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if (b == ':true:') or (b == ':false:') :
      if a == ':true:' :
       a1 = 1
      else:
       a1 = 0
      if b == ':true:' :
       b1 = 1
      else:
       b1 = 0
      c=a1 or b1
      if c == 1 :
       c1 = ":true:"
      else:
       c1 = ":false:"

      stack.push(c1)
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def donot(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]

   if a == ':true:' or a == ':false:':
     if a == ':true:' :
       a1 = 1
     else:
       a1 = 0
     c = not a1
     if c == 1 :
       c1 = ":true:"
     else:
       c1 = ":false:"
     stack.push(c1)
   else:
    stack.push(a)
    stack.push(":error:")

def doequal(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      if a == b :
       stack.push(":true:")
      else:
       stack.push(":false:")
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")

def doless(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
   a=stack.pop()
   if (a in toBind) and (toBind[a]!='empty'):
    a=toBind[a]
   if isinstance(a,int):
    if stack.isEmpty():
     stack.push(a)
     stack.push(":error:")
    else:
     b=stack.pop()
     if (b in toBind) and (toBind[b]!='empty'):
      b=toBind[b]
     if isinstance(b,int):
      if b<a :
       stack.push(":true:")
      else:
       stack.push(":false:")
     else:
      stack.push(b)
      stack.push(a)
      stack.push(":error:")
   else:
    stack.push(a)
    stack.push(":error:")


def doif(stack,toBind):
 if stack.isEmpty():
  stack.push(":error:")
 else:
  a=stack.pop()
  if stack.isEmpty():
   stack.push(a)
   stack.push(":error:")
  else:
   b=stack.pop()
   if stack.isEmpty():
    stack.push(b)
    stack.push(a)
    stack.push(":error:")
   else:
    c=stack.pop()

    if (c in toBind) and (toBind[c]!='empty'):
      c=toBind[c]

    if c == ':true:' :
     stack.push(a)
    elif c == ':false:':
     stack.push(b)
    else:
     stack.push(":error:")

class Stack():

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def clear(self):
   while len(self.items)>0:
       self.items.pop()

  def push(self, item):
    return self.items.append(item)

  def peek(self):
   return self.items[-1]

  def size(self):
    return len(self.items)
  def pop(self):
    return self.items.pop()


letstack = Stack()

def hw4(input,output):

 line=0
 stack= Stack()
 toBind = {}
 file=open(input,'r').readlines()
 out=open(output,'w')

 funarray = {}
 inoutarray={}

 while line <len(file):
  line=checker(file,file[line],stack,toBind,funarray,inoutarray,line,0)
  line=line+1


 line=line-1



 if "quit" in file[line]:
  while (str(stack.isEmpty()) == "False"):
   a = str(stack.pop())
   if a[0] == '"':
    a = a[1:len(a) - 1]
   out.write(a)
   out.write("\n")

def dolet(file,loopline,stack,toBind,funarray,inoutarray,line):
 newstack = Stack()
 temparray = {}
 inoutaray={}
 tempbind={}
 line = line + 1

 while file[line] != "end\n":

   line=checker(file, file[line], newstack, tempbind, temparray,inoutarray,line,0)

   line=line+1


 if file[line]=="end\n":

  if str(newstack.isEmpty()) != "True":
   stack.push(str(newstack.pop()))
  tempbind.clear()

  return line




def doend(file,loopline,stack,tempbind,funarray,inoutarray,line):
 temp = stack.pop()
 stack.clear()

 tempbind.clear()

 stack.push(temp)
 funarray.clear()
 return line

def function(name,stack,toBind,funarray,inoutarray,line):


 i=1
 tempstack = Stack()
 temp=funarray.get(name)
 a=stack.pop()






 if (a) in toBind:
  a=toBind.get(a)
  if type(a) is int:
   temp[-1][temp[0]] = a

 else:
  temp[-1][temp[0]] = a



 while(funarray.get(name)[i]!= "funEnd"):
  if funarray.get(name)[i].startswith("push"):
   temp[i]=temp[i].replace(temp[0],str(a))
  i=i+1

 for size in range(len(temp[0:-2])):


  if "return" in temp[size]:
   b = tempstack.pop()

   stack.push(b)

   return line


  size= checker(funarray.get(name),temp[size],tempstack,temp[-1],funarray,inoutarray,size,1)




def inoutfunction(name,stack,toBind,funarray,inoutarray,line):

 i=1
 tempstack = Stack()
 temp=inoutarray.get(name)
 a=stack.pop()


 while(inoutarray.get(name)[i]!= "funEnd"):

  if inoutarray.get(name)[i].startswith("push"):
   temp[i]=temp[i].replace(temp[0],str(a))
  i=i+1



 for size in range(len(temp[0:-2])):
  if "return" in temp[size]:
   b = tempstack.pop()
   if a==b:
    stack.push(toBind[b])
   else:
    stack.push(b)

   return line

  size=checker(inoutarray.get(name),temp[size],tempstack,toBind,funarray,inoutarray,size,1)

 return line



def checker(file,loopline,stack,toBind,funarray,inoutarray,line,indicator):



  if file[line].startswith("fun "):
   stack.push(":unit:")
   temporary = []
   temp = ""
   vartemp = ""
   i = 3
   while (file[line][i + 1] != " "):
    temp = temp + file[line][i + 1]
    i = i + 1
   i = i + 1
   while (file[line][i + 1] != "\n"):
    vartemp = vartemp + loopline[i + 1]
    i = i + 1
   temporary.append(vartemp)
   line = line + 1
   while (file[line] != "funEnd\n"):
    temporary.append(file[line][0:len(file[line]) ])
    file[line] = ""
    line = line + 1
   temporary.append("funEnd")
   Bind=toBind
   temporary.append(Bind.copy())
   funarray[temp] = temporary


  if file[line].startswith("inOutFun "):
   stack.push(":unit:")
   temporary = []
   temp = ""

   vartemp = ""
   i = 8
   while (file[line][i + 1] != " "):
    temp = temp + file[line][i + 1]
    i = i + 1
   i = i + 1
   while (file[line][i + 1] != "\n"):
    vartemp = vartemp + loopline[i + 1]
    i = i + 1
   temporary.append(vartemp)
   line = line + 1
   while (file[line] != "funEnd\n"):
    temporary.append(file[line][0:len(file[line])])
    file[line] = ""
    line = line + 1
   temporary.append("funEnd")
   Bind = toBind
   temporary.append(Bind.copy())
   inoutarray[temp] = temporary

  if loopline == ("mul\n"):
   mul(stack,toBind)
  if loopline == ("let\n"):


   line= dolet(file,loopline,stack,toBind,funarray,inoutarray,line)


  if loopline == "end\n":

   return line

  if loopline == ("sub\n"):
   sub(stack,toBind)
  if "div\n" == loopline:
   div(stack,toBind)
  if "rem\n" == loopline:
   rem(stack,toBind)
  if "neg\n" == loopline:
   neg(stack,toBind)
  if "swap\n" == loopline:
   swap(stack,toBind)
  if "add\n" == loopline:
   add(stack,toBind)
  if "not\n" == loopline:
   donot(stack,toBind)
  if ":true:\n" == loopline:
   true(stack,toBind)
  if ":false:\n" == loopline:
   false(stack,toBind)
  if "bind\n" == loopline:
   dobind(stack,toBind)
  if "pop\n" == loopline:
   pop(stack,toBind)
  if "or\n" == loopline:
   door(stack,toBind)
  if "if\n" == loopline:
   doif(stack,toBind)
  if "and\n" == loopline:
   doand(stack,toBind)
  if "equal\n" == loopline:
   doequal(stack,toBind)
  if "call\n" == loopline:

   temp=stack.pop()


   if stack.peek() == ":error:":
    stack.push(temp)
    stack.push(":error:")
    return line

   if (temp) in funarray:

    line= function(temp,stack,toBind,funarray,inoutarray,line)


   elif (temp) in inoutarray:
    line=inoutfunction(temp,stack,toBind,funarray,inoutarray,line)
   else:
    stack.push(temp)
    stack.push(":error:")


  if "lessThan\n" == loopline:
   doless(stack,toBind)

  if "push" in loopline:

   a=loopline[5:]

   line =push(a,stack,toBind,funarray,inoutarray,line,indicator)
  return line


