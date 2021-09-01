package ghost;

import processing.core.PApplet;
import processing.core.PImage;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.lang.Object;
public class Manager{
    private File myObj;
    private ArrayList<String> maparray;
    private ArrayList<String> maparrayo;
    public Manager(){
        maparray=new ArrayList<String>();
        maparrayo=new ArrayList<String>();
    }
    public ArrayList<String> readjson(){ // read json file and output maparray
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
            try {
            Scanner myReader = new Scanner(myObj);

            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();

                if(data!=null){
                    maparray.add(data);
                }

            }
            myReader.close();
            return maparray;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return null;
    }
    public int getx(){ // get waka x
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("p")){
                        return i;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int gety(){ // get waka y
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("p")){
                        return ii;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }

    public int getcy(){ //get chaser y
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("c")){
                        return ii;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getcx(){ //get chaser x
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("c")){
                        return i;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getay(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("a")){
                        return ii;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getax(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("a")){
                        return i;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getiy(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("i")){
                        return ii;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getix(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("i")){
                        return i;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getwx(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("w")){
                        return i;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int getwy(){
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              String map = (String) jsonObject.get("map");
              myObj = new File(map);
              try {
            Scanner myReader = new Scanner(myObj);
            int ii=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data!=null){

                }
                int i=0;
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("w")){
                        return ii;
                    }
                    i++;
                }
                ii++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public ArrayList<String> touch(Player player, ArrayList<String> maparray){ // if touch fruit will change the maparray to delete fruit
        if(player.getx()%16==0 && player.gety()%16==0){
            if(maparray.get(player.gety()/16).substring(player.getx()/16,player.getx()/16+1).equals("7")||maparray.get(player.gety()/16).substring(player.getx()/16,player.getx()/16+1).equals("8")){
                maparray.set(player.gety()/16,maparray.get(player.gety()/16).substring(0,player.getx()/16)+"0"+maparray.get(player.gety()/16).substring(player.getx()/16+1));
            }
        }
        return maparray;
    }
    public boolean touchghost(Player player,Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim){ // when touch ghost reset
        if(player.getx()>=ambusher.getx()-1 && player.getx()<=ambusher.getx()+1 && player.gety()==ambusher.gety()){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()>=chaser.getx()-1 && player.getx()<=chaser.getx()+1 && player.gety()==chaser.gety()){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()>=ignorant.getx()-1 && player.getx()<=ignorant.getx()+1 && player.gety()==ignorant.gety()){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()>=whim.getx()-1 && player.getx()<=whim.getx()+1 && player.gety()==whim.gety()){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()==ambusher.getx() && player.gety()>=ambusher.gety()-1&& player.gety()<=ambusher.gety()+1){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()==chaser.getx() && player.gety()>=chaser.gety()-1&& player.gety()<=chaser.gety()+1){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()==ignorant.getx() && player.gety()>=ignorant.gety()-1&& player.gety()<=ignorant.gety()+1){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else if(player.getx()==whim.getx() && player.gety()>=whim.gety()-1&& player.gety()<=whim.gety()+1){
            player.reset();
            ambusher.reset();
            chaser.reset();
            ignorant.reset();
            whim.reset();
            return true;
        }else{
            return false;
        }
    }
    public void resett(Player player,Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim){
        player.reset();
        ambusher.reset();
        chaser.reset();
        ignorant.reset();
        whim.reset();
    }
    public ArrayList<String> mapclean(Player player,Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim,ArrayList<String> maparray){ // change waka or ghost number in map to 0
        maparray.set(this.gety(),maparray.get(player.gety()/16).substring(0,player.getx()/16)+"0"+maparray.get(player.gety()/16).substring(player.getx()/16+1));
        maparray.set(this.getcy(),maparray.get(chaser.gety()/16).substring(0,chaser.getx()/16)+"0"+maparray.get(chaser.gety()/16).substring(chaser.getx()/16+1));
        maparray.set(this.getay(),maparray.get(ambusher.gety()/16).substring(0,ambusher.getx()/16)+"0"+maparray.get(ambusher.gety()/16).substring(ambusher.getx()/16+1));
        maparray.set(this.getiy(),maparray.get(ignorant.gety()/16).substring(0,ignorant.getx()/16)+"0"+maparray.get(ignorant.gety()/16).substring(ignorant.getx()/16+1));
        maparray.set(this.getwy(),maparray.get(whim.gety()/16).substring(0,whim.getx()/16)+"0"+maparray.get(whim.gety()/16).substring(whim.getx()/16+1));
        return maparray;
    }
    public boolean calculate(ArrayList<String> maparray){
        int i = 0;
        for(String s: maparray){
            int ii = 0;
            while(ii<28){
                if(s.substring(ii,ii+1).equals("7")||s.substring(ii,ii+1).equals("8")){i+=1;}
                ii+=1;;
            }
        }
        if(i==0){return true;}
        else{return false;}
    }
    public void gmove(Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim,ArrayList<String> maparray,int x,  int d , Player player){ //ghost move
        if(chaser.die){
            chaser.setnimage();
            chaser.move(player,getscattertime().get(2), getscattertime().get(3), x,maparray);
        }
        if(ambusher.die){
            ambusher.setnimage();
            ambusher.move(player,getscattertime().get(0), getscattertime().get(1), x,maparray,d);
        }
        if(ignorant.die){
            ignorant.setnimage();
            ignorant.move(player,getscattertime().get(4), getscattertime().get(5), x,maparray,d);
        }
        if(whim.die){
            whim.setnimage();
            whim.move(player,getscattertime().get(6), getscattertime().get(7), x,maparray,d,chaser);
        }
    }
    public void gfmove(Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim,ArrayList<String> maparray,int x,  int d , Player player){// frighten ghost move
        if(chaser.die){
            chaser.setfimage();
            chaser.f(player,maparray);
        }


        if(ambusher.die){
            ambusher.setfimage();
            ambusher.f(player,maparray);
        }
        if(ignorant.die){
            ignorant.setfimage();
            ignorant.f(player,maparray);
        }

       if(whim.die){
            whim.setfimage();
            whim.f(player,maparray);
        }

    }
    public int f(Player player, ArrayList<String> maparray,int tt){ // identify eat superfruit
        if(player.getx()%16==0 && player.gety()%16==0){
            if(maparray.get(player.gety()/16).substring(player.getx()/16,player.getx()/16+1).equals("8")){
                return 600;
            }else{return tt;}
        }else{return tt;}
    }
    public void touchfghost(Player player,Ambusher ambusher,Chaser chaser,Ignorant ignorant,Whim whim){ //remove the frighten ghost
        if(player.getx()>=ambusher.getx()-1 && player.getx()<=ambusher.getx()+1 && player.gety()==ambusher.gety()){
            ambusher.die=false;
            ambusher.setx(0);
            ambusher.sety(0);
        }else if(player.getx()>=chaser.getx()-1 && player.getx()<=chaser.getx()+1 && player.gety()==chaser.gety()){
            chaser.die=false;
            chaser.setx(0);
            chaser.sety(0);
        }else if(player.getx()>=ignorant.getx()-1 && player.getx()<=ignorant.getx()+1 && player.gety()==ignorant.gety()){
            ignorant.die=false;
            ignorant.setx(0);
            ignorant.sety(0);
        }else if(player.getx()>=whim.getx()-1 && player.getx()<=whim.getx()+1 && player.gety()==whim.gety()){
            whim.die=false;
            whim.setx(0);
            whim.sety(0);
        }else if(player.getx()==ambusher.getx() && player.gety()>=ambusher.gety()-1&& player.gety()<=ambusher.gety()+1){
            ambusher.die=false;
            ambusher.setx(0);
            ambusher.sety(0);
        }else if(player.getx()==chaser.getx() && player.gety()>=chaser.gety()-1&& player.gety()<=chaser.gety()+1){
            chaser.die=false;
            chaser.setx(0);
            chaser.sety(0);
        }else if(player.getx()==ignorant.getx() && player.gety()>=ignorant.gety()-1&& player.gety()<=ignorant.gety()+1){
            ignorant.die=false;
            ignorant.setx(0);
            ignorant.sety(0);
        }else if(player.getx()==whim.getx() && player.gety()>=whim.gety()-1&& player.gety()<=whim.gety()+1){
            whim.die=false;
            whim.setx(0);
            whim.sety(0);
        }
    }
    public ArrayList<Integer> getscattertime(){ // read modelength
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              ArrayList<Long> map = (ArrayList<Long>) jsonObject.get("modeLengths");
              ArrayList<Integer> mapa = new ArrayList<Integer>();
              for(long a : map){
                  mapa.add((int) a);
              }
              return mapa;

        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return null;
    }
    public int livestime(){ //read live times
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              long map = (long) jsonObject.get("lives");
              int mapa = (int) map;
              return mapa;

        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }
    public int speedstime(){ // read speed
        JSONParser parser = new JSONParser();
        try {
              Object obj = parser.parse(new FileReader("config.json"));
              JSONObject jsonObject = (JSONObject) obj;
              long map = (long) jsonObject.get("speed");
              int mapa = (int) map;
              return mapa;

        } catch (FileNotFoundException e) {
              e.printStackTrace();
        } catch (IOException e) {
              e.printStackTrace();
        } catch (ParseException e) {
              e.printStackTrace();
        }
        return 0;
    }


}