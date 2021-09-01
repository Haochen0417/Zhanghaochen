package ghost;

import processing.core.PApplet;
import processing.core.PImage;
import processing.core.PApplet;
import processing.core.PImage;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.io.FileWriter;
import java.lang.Object;
public class Ambusher{

     private int x;
     private int y;
     private int xVel;
     private int yVel;
     private int xr;
     private int yr;
     private int d;
     private PImage image;
     private PImage ambusherpic;
     private PImage frightened;
     public boolean die;

    public Ambusher(int x,int y,int xVel,int yVel,PImage image,PImage ambusherpic,PImage frightened){
        this.x=x;
        this.y=y;
        this.xVel=xVel;
        this.yVel=yVel;
        this.xr=x;
        this.yr=y;
        this.image=image;
        d=0;
        this.ambusherpic=ambusherpic;
        this.frightened=frightened;
        die=true;
    }
    public void tickxu(){
        this.x += this.xVel;
    }
    public void tickxd(){
        this.x -= this.xVel;
    }
    public void tickyu(){
        this.y += this.yVel;
    }
    public void tickyd(){
        this.y -= this.yVel;
    }
    public void setnimage(){
        image=ambusherpic;
    }
    public void setfimage(){
        image=frightened;
    }
    public void draw(PApplet app){
        app.image(this.image,this.x,this.y);
    }
    public void reset(){
        this.x=this.xr;
        this.y=this.yr;
        d=0;
        die=true;
        setnimage();
    }
    public int getx(){
        return x;
    }
    public int gety(){
        return y;
    }
    public void setx(int a){
        x=a;
    }
    public void sety(int a){
        y=a;
    }
    public boolean canselect(ArrayList<String> maparray){ // can ghost change direction now?
        if(x%16==0&&y%16==0){
            if(d==0){
                return true;
            }else if(d==37){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")){
                    return true;
                }else if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")){
                    return true;
                }else if(!maparray.get(y/16).substring(x/16-1,x/16).equals("0")&&!maparray.get(y/16).substring(x/16-1,x/16).equals("7")&&!maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(d==39){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                    return true;
                }else if(!maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")&&!maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")&&!maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(d==38){
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                    return true;
                }else if(!maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")&&!maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")&&!maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(d==40){
                if(!maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")&&!maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")&&!maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                    return true;
                }else if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }
            return false;
        }else{
            return false;
        }

    }
    public boolean haveisselect(ArrayList<String> maparray,int ed ,int x1,int y1){ // have how many choice
        if(x1%16==0&&y1%16==0){
            if(ed==0){
                return true;
            }else if(ed==37){
                if(maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("0")||maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("7")||maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("0")||maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("7")||maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(!maparray.get(y1/16).substring(x1/16-1,x1/16).equals("0")&&!maparray.get(y1/16).substring(x1/16-1,x1/16).equals("7")&&!maparray.get(y1/16).substring(x1/16-1,x1/16).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(ed==39){
                if(maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("0")||maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("7")||maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("0")||maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("7")||maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(!maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("0")&&!maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("7")&&!maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(ed==38){
                if(maparray.get(y1/16).substring(x1/16-1,x1/16).equals("0")||maparray.get(y1/16).substring(x1/16-1,x1/16).equals("7")||maparray.get(y1/16).substring(x1/16-1,x1/16).equals("8")){
                    return true;
                }else if(!maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("0")&&!maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("7")&&!maparray.get(y1/16-1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("0")||maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("7")||maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }else if(ed==40){
                if(!maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("0")&&!maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("7")&&!maparray.get(y1/16+1).substring(x1/16,x1/16+1).equals("8")){
                    return true;
                }else if(maparray.get(y1/16).substring(x1/16-1,x1/16).equals("0")||maparray.get(y1/16).substring(x1/16-1,x1/16).equals("7")||maparray.get(y1/16).substring(x1/16-1,x1/16).equals("8")){
                    return true;
                }else if(maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("0")||maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("7")||maparray.get(y1/16).substring(x1/16+1,x1/16+2).equals("8")){
                    return true;
                }else{
                    return false;
                }
            }
            return false;
        }else{
            return false;
        }
    }
    public int select(ArrayList<String> maparray){ // scatter mode turn where is better
        int[][] numarray = new int[4][2];
        int[] shortarray = new int[4];
        int x1=x;
        int y1=y;
        numarray[0][0]=100000;
        numarray[0][1]=100000;
        numarray[1][0]=100000;
        numarray[1][1]=100000;
        numarray[2][0]=100000;
        numarray[2][1]=100000;
        numarray[3][0]=100000;
        numarray[3][1]=100000;
        if(canselect(maparray)){
            if(d==0){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }

                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }

                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }

                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }

                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==37){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==38){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==39){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){

                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
            }else if(d==40){
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){

                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }

            int i=0;
            for (int[] na : numarray){
                if(na[0]==100000&&na[1]==100000){

                    shortarray[i]=100000;
                }else{
                    shortarray[i]=(na[0]/16-27)*(na[0]/16-27)+(na[1]/16-3)*(na[1]/16-3);
                }
                i+=1;
            }
            i=0;
            int ii=0;
            int c=100000;
            for (int n : shortarray){
                if(n<c){
                    c=n;
                    ii=i;
                }
                i+=1;
            }

            return ii;
        }else{
            return 4;
        }
    }
    public int cselect(ArrayList<String> maparray,Player player,int ddd){ // chaser mode turn where is better
        int[][] numarray = new int[4][2];
        int[] shortarray = new int[4];
        numarray[0][0]=100000;
        numarray[0][1]=100000;
        numarray[1][0]=100000;
        numarray[1][1]=100000;
        numarray[2][0]=100000;
        numarray[2][1]=100000;
        numarray[3][0]=100000;
        numarray[3][1]=100000;

        int x1=x;
        int y1=y;
        if(canselect(maparray)){
            if(d==0){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }

                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }

                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }

                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }

                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==37){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==38){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==39){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){

                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
            }else if(d==40){
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){

                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }
            int i=0;
            for (int[] na : numarray){

                if(na[0]==100000&&na[1]==100000){
                    shortarray[i]=100000;
                }else{
                    if(ddd==37){
                        shortarray[i]=(na[0]/16-player.getx()/16+4)*(na[0]/16-player.getx()/16+4)+(na[1]/16-player.gety()/16)*(na[1]/16-player.gety()/16);
                    }else if(ddd==38){
                        shortarray[i]=(na[0]/16-player.getx()/16)*(na[0]/16-player.getx()/16)+(na[1]/16-player.gety()/16+4)*(na[1]/16-player.gety()/16+4);
                    }else if(ddd==39){
                        shortarray[i]=(na[0]/16-player.getx()/16-4)*(na[0]/16-player.getx()/16-4)+(na[1]/16-player.gety()/16)*(na[1]/16-player.gety()/16);
                    }else if(ddd==40){
                        shortarray[i]=(na[0]/16-player.getx()/16)*(na[0]/16-player.getx()/16)+(na[1]/16-player.gety()/16-4)*(na[1]/16-player.gety()/16-4);
                    }

                }
                i+=1;
            }

            i=0;
            int ii=0;
            int c=100000;
            for (int n : shortarray){

                if(n<c){
                    c=n;
                    ii=i;
                }
                i+=1;
            }
            return ii;
        }else{
            return 4;
        }
    }

    public int ff(ArrayList<String> maparray,Player player){ // frighten move
        int[][] numarray = new int[4][2];
        int[] shortarray = new int[4];
        numarray[0][0]=100000;
        numarray[0][1]=100000;
        numarray[1][0]=100000;
        numarray[1][1]=100000;
        numarray[2][0]=100000;
        numarray[2][1]=100000;
        numarray[3][0]=100000;
        numarray[3][1]=100000;

        int x1=x;
        int y1=y;
        if(canselect(maparray)){
            if(d==0){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }

                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }

                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }

                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }

                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==37){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==38){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){
                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }else if(d==39){
                if(maparray.get(y/16-1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")){
                    while(!haveisselect(maparray,38,x1,y1-16)){
                        y1-=16;
                    }
                    numarray[0][0]=x1;
                    numarray[0][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){

                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;

                }
            }else if(d==40){
                if(maparray.get(y/16+1).substring(x/16,x/16+1).equals("0")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8")){
                     while(!haveisselect(maparray,40,x1,y1+16)){
                        y1+=16;
                    }
                    numarray[2][0]=x1;
                    numarray[2][1]=y1;
                    y1=y;
                }
                if(maparray.get(y/16).substring(x/16+1,x/16+2).equals("0")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")){
                     while(!haveisselect(maparray,39,x1+16,y1)){
                        x1+=16;
                    }
                    numarray[1][0]=x1;
                    numarray[1][1]=y1;
                    x1=x;
                }
                if(maparray.get(y/16).substring(x/16-1,x/16).equals("0")||maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8")){

                     while(!haveisselect(maparray,37,x1-16,y1)){
                        x1-=16;
                    }
                    numarray[3][0]=x1;
                    numarray[3][1]=y1;
                    x1=x;
                }
            }
            int i=0;
            int num=0;
            num=(int)(37+Math.random()*(4-1+1));
            while(i==0){
                if(num==37&& numarray[3][0]==100000&&numarray[3][1]==100000){
                    num=(int)(37+Math.random()*(4-1+1));
                }else if(num==38&& numarray[0][0]==100000&&numarray[0][1]==100000){
                    num=(int)(37+Math.random()*(4-1+1));
                }else if(num==39&& numarray[1][0]==100000&&numarray[1][1]==100000){
                    num=(int)(37+Math.random()*(4-1+1));
                }else if(num==40&& numarray[2][0]==100000&&numarray[2][1]==100000){
                    num=(int)(37+Math.random()*(4-1+1));
                }else{
                    i=1;
                }
            }
            return num;
        }else{
            return 0;
        }
    }





    public void move(Player player,int scatter, int chase, int t,ArrayList<String> maparray,int ddd){ // ghost move

        if(t%(60*scatter+60*chase)<=60*scatter){
            if(select(maparray)==0){
                d=38;
                this.tickyd();
            }else if(select(maparray)==1){
                d=39;
                this.tickxu();
            }else if(select(maparray)==2){
                d=40;
                this.tickyu();
            }else if(select(maparray)==3){
                d=37;
                this.tickxd();
            }else if(select(maparray)==4){
                if(d==38){
                    this.tickyd();
                }else if(d==39){
                    this.tickxu();
                }else if(d==40){
                    this.tickyu();
                }else if(d==37){
                    this.tickxd();
                }
            }
        }else{
            if(cselect(maparray,player,ddd)==0){
                d=38;
                this.tickyd();
            }else if(cselect(maparray,player,ddd)==1){
                d=39;
                this.tickxu();
            }else if(cselect(maparray,player,ddd)==2){
                d=40;
                this.tickyu();
            }else if(cselect(maparray,player,ddd)==3){
                d=37;
                this.tickxd();
            }else if(cselect(maparray,player,ddd)==4){
                if(d==38){
                    this.tickyd();
                }else if(d==39){
                    this.tickxu();
                }else if(d==40){
                    this.tickyu();
                }else if(d==37){
                    this.tickxd();
                }
            }
        }

    }
    public void f(Player player,ArrayList<String> maparray){ // ghost frighten move
        if(ff(maparray,player)==38){
            d=38;
            this.tickyd();
        }else if(ff(maparray,player)==39){
            d=39;
            this.tickxu();
        }else if(ff(maparray,player)==40){
            d=40;
            this.tickyu();
        }else if(ff(maparray,player)==37){
            d=37;
            this.tickxd();
        }else if(ff(maparray,player)==0){
            if(d==38){
                this.tickyd();
            }else if(d==39){
                this.tickxu();
            }else if(d==40){
                this.tickyu();
            }else if(d==37){
                this.tickxd();
            }
        }
    }

}