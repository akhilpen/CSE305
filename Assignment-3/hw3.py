toBind={}
def push(line):
 alphabetList = "abcdefghijklmnopqrstuvwxyz"
 if '"' in line:
  stack.push(line[0:len(line)-1])
 elif line[0] in alphabetList:
  if line[0:len(line)-1] not in toBind:
   toBind[line[0:len(line)-1]] = 'empty'
  stack.push(line[0:len(line)-1])
 elif line[0] == '-':
   if line[1] == '0':
    stack.push(0)
   elif line[1].isdigit():
    a1=float(line[1:])
    b1=int(a1)
    if a1%b1==0:
     stack.push(-b1)
    else:
     stack.push(":error:")
   else:
    stack.push(":error:")
 else:
    if line[0] == '0':
     stack.push(0)
    else:
     a=float(line)
     b=int(a)
     if a%b==0:
      stack.push(b)
     else:
      stack.push(":error:")

def let():
 stack.push("z")
def end():
 i = stack.size()
 a = stack.pop()
 while(i>0):
  i=i-1
  b = stack.pop()
  if b=="z":
   stack.push(a)
   break 

def add():
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
    
def sub():
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

def mul():
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

def div():
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

def rem():
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

def neg():
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


def dobind():
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
  
def swap():
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
 


def pop():
 if stack.isEmpty():
  stack.push(":error:")
 else:
  stack.pop()


def true():
 stack.push(":true:")

def false():
 stack.push(":false:")

def error():
 stack.push(":error:")


def doand():
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
def door():
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
 
def donot():
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

def doequal():
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

def doless():
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

 
def doif():
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
             
  def push(self, item):
    return self.items.append(item)

  def size(self):
    return len(self.items)
  def pop(self):
    return self.items.pop()

    
stack = Stack()
letstack = Stack()
def hw3(input,output):
 file=open(input,'r').readlines()
 out=open(output,'w')

 for line in file:
  if "mul" in line:
   mul()
  if "let" in line:
   toBind["z"] = 'empty'
   letstack.push("let")
  if "sub" in line:
   sub() 
  if "div" in line:
   div()    
  if "rem" in line:
   rem() 
  if "neg" in line:
   neg() 
  if "swap" in line:
   swap()     
  if "add" in line:
   add()
  if "not" in line:
   donot()
  if "let" in line:
   let()
  if "end" in line:
   end()
  if ":true:" in line:
   true()
  if ":false:" in line:
   false()
  if "bind" in line:
   dobind()
  if "pop" in line:
   pop()
  if "or" in line:
   door()
  if "if" in line:
   doif()
  if "and" in line:
   doand()
  if "equal" in line:
   doequal()
  if "lessThan" in line:
   doless()
  if "quit" in line:
   while(str(stack.isEmpty())== "False"):
    a=str(stack.pop())
    if a[0] == '"':
     a=a[1:len(a)-1]
    out.write(a)
    out.write("\n")
  if "push" in line:
   a=line[5:]
   push(a)
hw3("input.txt","output.txt")
