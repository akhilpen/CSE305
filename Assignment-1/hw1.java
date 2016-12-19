import java.io.*;

public class hw1 {
 public static boolean isPangram(String test){
        for (char a = 'a'; a <= 'z'; a++)
            if ((test.indexOf(a) < 0) && (test.indexOf((char)(a + 32)) < 0))
                return false;
        return true;
    }
    public static void hw1(String inFile,String outFile) {
Boolean temp; 
 String line = null;
 try {
 FileReader fileReader = 
                new FileReader(inFile);
FileWriter file=new FileWriter(outFile);
BufferedWriter bw=new BufferedWriter(file);
  BufferedReader bufferedReader = 
                new BufferedReader(fileReader);
     while((line = bufferedReader.readLine()) != null) {
temp=isPangram(line);
           if(temp){
bw.write("true\n");}
else{
bw.write("false\n");
} } 
bufferedReader.close();
bw.close();         
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
