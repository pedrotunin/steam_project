package extrairusuarios;

import java.util.*;
import java.io.*;
public class ExtrairUsuarios {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        Scanner buff = new Scanner(System.in);
        
        FileWriter arq = new FileWriter("d:\\arq.txt");
        PrintWriter gravarArq = new PrintWriter(arq);
        
        String s, a = "";
        String v[] = new String[1000];
        int cont = 0; 
        
        s = buff.next();
        
        boolean primeiro = false;
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '<'){
                i += 10; 
                continue;
            }
            if(a.length() < 17){
                
                a += s.charAt(i);
            }
            else{
                v[cont] = a;
                a = "";
                cont++;
            } 
        }
        for (String v1 : v)
            gravarArq.println(v1);
        
        arq.close();
        
    }
}
