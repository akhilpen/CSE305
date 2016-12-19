import java.io.*;



public class hw2 {
    public  static int  maxSize = 15;
   public  static String[]  stackArray = new String[maxSize];
   public static int  top = -1;
   public static void push(String j) {
      stackArray[++top] = j;
   }
   public static String pop() {
      return stackArray[top--];
   }
   public static boolean peek() {
   String str=stackArray[top];
   if(str.equals(":true:")||str.equals(":false:")||str.equals(":error:"))
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
   
 
    public static void hw2(String inFile,String outFile) {
Boolean temp;
      
 String line = null;
 try {
 FileReader fileReader = new FileReader(inFile);
FileWriter file=new FileWriter(outFile);
BufferedWriter bw=new BufferedWriter(file);
  BufferedReader br =new BufferedReader(fileReader);
   String a,b;
     int a1,b1;
     float af,bf;
     
      while((line = br.readLine()) != null) {
                
                if (line.contains("push")){
String getNum = line.substring(5);
		if (getNum.charAt(0) == '-'){
			if (getNum.substring(1).equals("0")){
				push("0");
			}
			else if (getNum.substring(1).matches("[0-9]+")){
				stack.add(0, getNum);
			}
			else{
				stack.add(0, ":error:");
			}
		}
		else if (getNum.matches("[0-9]+")){
			stack.add(0, getNum);
		}
        else if (getNum.charAt(0) == '"'){
			stack.add(0,getNum.substring(1,(getNum.length()-1)));
		}
		else{
			stack.add(0, ":error:");
		}
		return stack;


                 a=line.substring(5,line.length());
                 bf =Float.parseFloat(a);
                 a1=Integer.parseInt(a);
                if(bf%a1==0)
                {push(a);}
                else
                {push(":error:");}
                }
          
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
                     a1=Integer.parseInt(a);
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
                         b1=Integer.parseInt(b);
                  push(Integer.toString(a1+b1));
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
                     a1=Integer.parseInt(a);
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
                         b1=Integer.parseInt(b);
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
                     a1=Integer.parseInt(a);
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
                         b1=Integer.parseInt(b);
                  push(Integer.toString(a1*b1));
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
                     a1=Integer.parseInt(a);
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
                         b1=Integer.parseInt(b);
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
                     a1=Integer.parseInt(a);
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
                         b1=Integer.parseInt(b);
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
                   a1=Integer.parseInt(a);
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
          
          if (line.contains(":error:")){push(":error:");}
                
                if (line.contains(":true:")){push(":true:");}
                
                if (line.contains(":false:")){push(":false:");}
                
                if (line.contains("pop")){
                if(isEmpty()){push(":error:");}
                else{pop();}
                }
          
          if (line.contains("quit"))
          {
              while(!isEmpty())
              {
                  bw.write(pop());
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
        catch(IOException ex) {
            System.out.println(
                "Error reading file '"
                );
        }
    }
}
