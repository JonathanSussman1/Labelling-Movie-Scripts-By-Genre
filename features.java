package NLP_FINAL;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
//This program is gonna collect the data that I'm gonna put into the GMM, input is a directory that is called along with the file
//
//Program runs through directory and calculates features. Program assumes genres are going to be listed in line one as numbers, separated by spaces. We can work out a table for what number corresponds to what genre later
public class features {
    static ArrayList[] genres = new ArrayList[11]; //support about 11 genres so far (we can tweak)
    static ArrayList<Integer> genreHelper = new ArrayList<Integer>();
    public static void main(String[] args) throws IOException// Call this with path to directory
    {
        File f = new File(args[0]);
        if (!f.isDirectory()) // Input validation/debugging
        {
            System.out.println("Not a directory");
            System.exit(0);
        }
        File[] accessDirectory = f.listFiles(); // array of files

        for (int i = 1; i < accessDirectory.length; i++) // the i=1 is Mac-Specific (maybe linux too) (skips over the hidden .dsstore file that's in every directory and was causing a bunch of issues)
        {
            byte [] fileConverter = Files.readAllBytes(accessDirectory[i].toPath()); 
            String fileText = new String(fileConverter,StandardCharsets.UTF_8); //Turns file into String
            int genrelocation = fileText.indexOf("#$"); //two characters to put after genres so program knows where they're listed
            String genres = fileText.substring(0, genrelocation); //kinda messy, but String.split isn't working for some reason so this is what we're going with
            String [] listOfGenres = genres.split(" "); // 3 genres max, planning on using imdb as the gold standard for genres to compare output to
            for(int s = 0; s<listOfGenres.length; s++)
            {
                genreHelper.add(Integer.parseInt(listOfGenres[s]));
            }
            //this part of the program's gonna do all of the heavy lifting, remember to use substring to skip over the #$ sequence that separates genre from actual script text
            //I'll add regexes and other shit here to capture data for simpler features (ratio of adjectives to nouns)
            //we can also call methods directly on the string for more complex features (tfidf) if easier
            
            
            
            //create datapoint object from data here (variable will be referred to as datum) 
           
            /*
            for(int j = 0; j<genreHelper.size();j++)
            {
                genres[genreHelper.get(j)].add(datum)
            }
            */

            

          
            


        }




        //program will convert arraylist to matrices here (or whatever format scikit uses)



    }
    
}
