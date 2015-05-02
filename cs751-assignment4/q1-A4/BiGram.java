package uniGram_BiGram_TriGram;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class BiGram {
 public static void main(String[] args) throws Exception, IOException {
		 
		 File folder = new File("C:\\Users\\hkuna\\workspace\\Assignment4_Q1\\src\\uniGram_BiGram_TriGram\\");
		 File[] listOfFiles = folder.listFiles();
		 
		 
	       // String fileInput = "C:\\Users\\hkuna\\workspace\\Assignment4_Q1\\src\\uniGram_BiGram_TriGram\\textfromhtml11015";
		 for(int k =0 ; k<listOfFiles.length; k++)
		 {
			 String fileInput = listOfFiles[k].toString();
			 BufferedReader br = new BufferedReader(new FileReader(fileInput));
		    
		     String line = null;
		  
		     if(!(listOfFiles[k].getName().endsWith(".java"))){
		        BufferedWriter bw = new BufferedWriter(new FileWriter(fileInput+"biGram.txt"));
		        int i =0;
		        int j = 0;
		        while((line=br.readLine())!= null)
		         {
		          try{
		              String [] tokens = line.split("\\s+");
		          for (i=0;i<tokens.length-1;i++)
		          {
		              j=j+1;
		              bw.write(tokens[i]+" "+tokens[i+1]+"\r\n");
		              System.out.println(tokens[i]+" "+tokens[i+1]);
		          }
		          
		          //i= i+1;
		          //System.out.println("The value of i is " + i + " URL:" + url);
		          //System.out.println(DefaultExtractor.INSTANCE.getText(url));          
		}catch (Exception ex)
		{
		System.out.println(ex);
		}

		}
		System.out.println(j);
		bw.close();
		br.close();
		} 
		 }
        
}
}



