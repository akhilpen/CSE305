import java.io.*;
import java.util.*;



public class hw3 {
   public  static int  maxSize = 20;
  public static  String[]  stackArray = new String[maxSize];
  public static int  top = -1;
   public static int  size = -1;
   public static void push(String j) {
      stackArray[++top] = j;
      size=top;
   }

public static boolean CheckString(String str) {
    for (char c : str.toCharArray()) {
        if (!Character.isDigit(c))
            return false;
    }
    return true;
} 

   public static String pop() {
     size = top--;
      return stackArray[size];
   }
   public static boolean peek() {
   String str=stackArray[top];
   if(str.charAt(0)=='"'||str.equals(":true:")||str.equals(":unit:")||str.equals(":false:")||str.equals(":error:"))
   {return false;}
   else
   return true;
      
   }
   public static boolean isEmpty() {
      return (top == -1);
   }
   public static boolean isFull() {
    return (top == maxSize - 1);
   }
   
public static boolean testTrue(String temp){
if (temp == ":true:" ){
return true;}
else{return false;}
}

public static String testNum(boolean temp){
if (temp == true) {
return ":true:";}
else{return ":false:";}
}

 
    public static void hw3(String inFile,String outFile) {
Boolean temp;
NavigableMap<String,String> dict = new TreeMap<String, String>();    
 String line = null;
 try {
 FileReader fileReader = new FileReader(inFile);
FileWriter file=new FileWriter(outFile);
BufferedWriter bw=new BufferedWriter(file);
  BufferedReader br =new BufferedReader(fileReader);
   String a,b,atemp;
     int a1,b1;
     boolean a2,b2,c2;
     float af,bf;
     
      while((line = br.readLine()) != null) {

if (line.contains("and")){
String c;
               if(isEmpty())
               {
                   push(":error:");
               }
               
               else
               {
                     a=pop();
                    if (dict.containsKey(a)){
                      a = dict.get(a);} 
                     
                      if(isEmpty())
               {   push(a);
                   push(":error:");
               }
               
               else{
               b=pop();
               if (dict.containsKey(b)){
                      b = dict.get(b);}
               if ((a==":true:" || a==":false:") && (b==":true:" || b==":false:")){
               a2 = testTrue(a);
               b2=testTrue(b);
               c2=a2&b2;
               c=testNum(c2);
               push(c);
               }
               else{
               push(b);
               push(a);
               push(":error:");
               
               }
               
               }
                     
                }
}

if (line.contains("bind")){
  if(isEmpty())
               {
                   push(":error:");
               }
               else{
               a=pop();
               if(isEmpty()||a==":error:")
               {   push(a);
                   push(":error:");
               }
               else{
               b=pop();
               if (dict.containsKey(b)){
               if (dict.containsKey(a)&&dict.get(a)=="empty"){
               push(b);
               push(a);
               push(":error:");
               }
             else if (dict.containsKey(a)&&dict.get(a)!="empty"){
              dict.put(b,dict.get(a));
               push(":unit:"); 
              } 
               else{
               dict.put(b,a);
               push(":unit:");
               }
               }
               else{
               push(b);
               push(a);
               push(":error:");
               }
               }}}
if (line.contains("let")){
push("z");

}
if (line.contains("end")){
a=pop();
for(int i =size;i>-1;i--)
{
 //a=pop();
 b = pop();
 if(b=="z"){push(a);break;}}
}
if (line.contains("equal")){
  if(isEmpty())
               {
                   push(":error:");
               }
               else{
               a=pop();
if (dict.containsKey(a)){
                      a = dict.get(a);} 
               if(isEmpty())
               {   push(a);
                   push(":error:");
               }
               else{
               b=pop();
               if (dict.containsKey(b)){
                      b = dict.get(b);}
               if((CheckString(a)||CheckString(a.substring(1))) && (CheckString(b)||CheckString(b.substring(1)))){
               if(a.charAt(0)=='-'){a1=0-Integer.parseInt(a.substring(1));} else{a1=Integer.parseInt(a);}
               if(b.charAt(0)=='-'){b1=0-Integer.parseInt(b.substring(1));}else{b1=Integer.parseInt(b);}
               if(a1 == b1){push(":true:");}else{push(":false:");}
               }
               else{push(b);push(a);push(":error:");}
               }}}

if (line.contains("lessThan")){
  if(isEmpty())
               {
                   push(":error:");
               }
               else{
               a=pop();
           if (dict.containsKey(a)){
                      a = dict.get(a);} 
               if(isEmpty())
               {   push(a);
                   push(":error:");
               }
               else{
               b=pop();
               if (dict.containsKey(b)){
                      b = dict.get(b);}
               if((CheckString(a)||CheckString(a.substring(1))) && (CheckString(b)||CheckString(b.substring(1)))){
               if(a.charAt(0)=='-'){a1=0-Integer.parseInt(a.substring(1));} else{a1=Integer.parseInt(a);}
               if(b.charAt(0)=='-'){b1=0-Integer.parseInt(b.substring(1));}else{b1=Integer.parseInt(b);}
               if(a1 > b1){push(":true:");}else{push(":false:");}
               }
               else{push(b);push(a);push(":error:");}
               }}}
 
if (line.contains("or")){
String c;
               if(isEmpty())
               {
                   push(":error:");
               }
               
               else
               {
                     a=pop();
                if (dict.containsKey(a)){
                      a = dict.get(a);}      
                      if(isEmpty())
               {   push(a);
                   push(":error:");
               }
               
               else{
               b=pop();
if (dict.containsKey(b)){
                      b = dict.get(b);}              
 if ((a==":true:" || a==":false:") && (b==":true:" || b==":false:")){
               a2 = testTrue(a);
               b2=testTrue(b);
               c2=a2|b2;
               c=testNum(c2);
               push(c);
               }
               else{
               push(b);
               push(a);
               push(":error:");
               
               }
               
               }
                     
                }
}

if (line.contains("if")){
String c; 
 if(isEmpty())
               {
                   push(":error:");
               }
            else{
            a=pop();
            if(isEmpty())
               {   push(a);
                   push(":error:");
               }    
               else{
              b=pop();
              if(isEmpty())
               {   push(b);push(a);
                   push(":error:");
               }    
               else{
            c=pop();
                    if (dict.containsKey(c)){ 
                      c = dict.get(c);} 
                      if(c==":true:"){push(a);}
                      else if (c==":false:"){push(b);}
                      else {push(":error:");}
            }}}}
            

if (line.contains("not")){
String c;
               if(isEmpty())
               {
                   push(":error:");
               }
               
               else
               {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);} 
               if (a==":true:" || a==":false:"){
               a2 = testTrue(a);
               c2= !a2;
               c=testNum(c2);
               push(c);
               }
               else{
               push(a);
               push(":error:");
               
               }
               
               }
                     
                } 
  
                
          if (line.contains("push")){

                 a=line.substring(5,line.length());
                 if(a.charAt(0)=='"'){
                 atemp=a.substring(0,a.length());
                 push(atemp);
                 }
                 else if(a.substring(0,1).matches("[a-z]+")){
                if(dict.containsKey(a)){push(a);}
                else{
                 dict.put(a,"empty");
                 push(a);
                 }}
    else if(a.charAt(0) == '-'){
        atemp=a.substring(1);
   if(a.charAt(1) == '0'){
    push("0");}
else{
   if(atemp.matches("[0-9]+")){
    bf =Float.parseFloat(atemp);
                 a1=Integer.parseInt(atemp);
                if(bf%a1==0)
                {push(a);}
                else
                {push(":error:");}} else{push(":error:");}}}
else{
if(a.charAt(0) == '0'){
    push("0");}
else{
              if(a.matches("[0-9]+")){
                 bf =Float.parseFloat(a);
                 a1=Integer.parseInt(a);
                if(bf%a1==0)
                {push(a);}
                else
                {push(":error:");}
                } else{push(":error:");}} }}
 

    if (line.contains("add")){

               if(isEmpty())
               {
                   push(":error:");
               }
               else
               {
                 if(peek())
                 {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                     a1=Integer.parseInt(a);}
                     if(isEmpty())
                     {
                         push(a);
                         push(":error:");
                     }
                     else
                     {
                         if(peek())
                         {
                         b=pop();
                  if (dict.containsKey(b)){
                      b = dict.get(b);}
                        if(b.substring(0,1)=="-"){b1 =0-(Integer.parseInt(b.substring(1)));}
                      else{ b1=Integer.parseInt(b);}
                  push(Integer.toString(b1+a1));
                     }
                         else
                         {
                             push(a);
                             push(":error:");
                         }
                 }}
                   else
                   {
                       push(":error:");
                   }
                }
               }
            
                
       if (line.contains("sub")){

               if(isEmpty())
               {
                   push(":error:");
               }
               else
               {
                 if(peek())
                 {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                     a1=Integer.parseInt(a);}
                     if(isEmpty())
                     {
                         push(a);
                         push(":error:");
                     }
                     else
                     {
                         if(peek())
                         {
                         b=pop();
                  if (dict.containsKey(b)){
                      b = dict.get(b);}
                        if(b.substring(0,1)=="-"){b1 =0-(Integer.parseInt(b.substring(1)));}
                      else{ b1=Integer.parseInt(b);}
                  push(Integer.toString(b1-a1));
                     }
                         else
                         {
                             push(a);
                             push(":error:");
                         }
                 }}
                   else
                   {
                       push(":error:");
                   }
                }
               }   
                
         if (line.contains("mul")){

               if(isEmpty())
               {
                   push(":error:");
               }
               else
               {
                 if(peek())
                 {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                     a1=Integer.parseInt(a);}
                     if(isEmpty())
                     {
                         push(a);
                         push(":error:");
                     }
                     else
                     {
                         if(peek())
                         {
                         b=pop();
                  if (dict.containsKey(b)){
                      b = dict.get(b);}
                        if(b.substring(0,1)=="-"){b1 =0-(Integer.parseInt(b.substring(1)));}
                      else{ b1=Integer.parseInt(b);}
                  push(Integer.toString(b1*a1));
                     }
                         else
                         {
                             push(a);
                             push(":error:");
                         }
                 }}
                   else
                   {
                       push(":error:");
                   }
                }
               }
 
                
         if (line.contains("div")){

               if(isEmpty())
               {
                   push(":error:");
               }
               else
               {
                 if(peek())
                 {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                     a1=Integer.parseInt(a);}
                     if(isEmpty())
                     {
                         push(a);
                         push(":error:");
                     }
                     else
                     {
                         if(peek())
                         {
                         b=pop();
                  if (dict.containsKey(b)){
                      b = dict.get(b);}
                        if(b.substring(0,1)=="-"){b1 =0-(Integer.parseInt(b.substring(1)));}
                      else{ b1=Integer.parseInt(b);}
                  push(Integer.toString(b1/a1));
                     }
                         else
                         {
                             push(a);
                             push(":error:");
                         }
                 }}
                   else
                   {
                       push(":error:");
                   }
                }
               }
 
                
         if (line.contains("rem")){

               if(isEmpty())
               {
                   push(":error:");
               }
               else
               {
                 if(peek())
                 {
                     a=pop();
                     if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                     a1=Integer.parseInt(a);}
                     if(isEmpty())
                     {
                         push(a);
                         push(":error:");
                     }
                     else
                     {
                         if(peek())
                         {
                         b=pop();
                  if (dict.containsKey(b)){
                      b = dict.get(b);}
                        if(b.substring(0,1)=="-"){b1 =0-(Integer.parseInt(b.substring(1)));}
                      else{ b1=Integer.parseInt(b);}
                  push(Integer.toString(b1%a1));
                     }
                         else
                         {
                             push(a);
                             push(":error:");
                         }
                 }}
                   else
                   {
                       push(":error:");
                   }
                }
               } 
                
if (line.contains("neg")){
                if(isEmpty())
                {push(":error:");}
               else
               {
                if(peek())
                { a=pop();
                  if (dict.containsKey(a)){
                      a = dict.get(a);}
                      if(a.substring(0,1)=="-"){a1 =0-(Integer.parseInt(a.substring(1)));}
                      else{
                   a1=Integer.parseInt(a);}
                  push(Integer.toString(-a1));
                  }
                 else
                 {push(":error:");}
                }}
          
if(line.contains("swap"))
          {
              if(!isEmpty())
              {
                  a=pop();
                  if(!isEmpty())
                  {
                      b=pop();
                      push(a);
                      push(b);
                  }
                  else
                  {
                      push(a);
                      push(":error:");
                  }
              }
              else
              {
                  push(":error:");
              }
          }
          
                
                if (line.contains(":true:")){push(":true:");}
                
                if (line.contains(":false:")){push(":false:");}
                
                if (line.contains("pop")){
                if(isEmpty()){push(":error:");}
                else{pop();}
                }
          
          if (line.contains("quit"))
          {
              while(!isEmpty())
              {  a=pop();
                if(a.charAt(0) == '"'){a=a.substring(1,a.length()-1);}
                  bw.write(a);
                  bw.write("\n");
              }
          }
          
      }
     
     
     
     
     
     
    bw.close();
     br.close();
    
        }
        
 catch(FileNotFoundException ex) {
            System.out.println(
                "Unable to open file '"
              );
        }
 catch(NullPointerException ex) {
            System.out.println(
                "Unable to open file '"
              );
        }
        catch(IOException ex) {
            System.out.println(
                "Error reading file '"
                );
        }
    }
}
