def hw1(input,output):
 file=open(input,'r').readlines()
 out=open(output,'w')
 alphabet = "abcdefghijklmnopqrstuvwxyz"
 for line in file:
  a=0
  for char in alphabet:
   if char not in line:
    a=1   
  if a==0:
   out.write("true\n")
  else:
   out.write("false\n")
