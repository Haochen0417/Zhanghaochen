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
public class Player{
    private int x;
    private int y;
    private int xVel;
    private int yVel;
    private int xr;
    private int yr;
    private PImage image;

    public PImage downleft;
    public PImage downright;
    public PImage fruit;
    public PImage vertical;
    public PImage upright;
    public PImage upleft;
    public PImage ghost;
    public PImage horizontal;
    public PImage playerleft;
    public PImage playerclosed;
    public PImage playerup;
    public PImage playerdown;
    public PImage playerright;
    public PImage superfruit;
    public Player(int x,int y,int xVel,int yVel,PImage image,PImage downleft,PImage downright,PImage fruit,PImage vertical,PImage upright,PImage upleft,PImage ghost,PImage horizontal,PImage playerclosed,PImage playerup,PImage playerleft,PImage playerdown,PImage playerright,PImage superfruit){
        this.x=x;
        this.y=y;
        this.xVel=xVel;
        this.yVel=yVel;
        this.xr=x;
        this.yr=y;
        this.image=image;
        this.downleft= downleft;
        this.downright= downright;
        this.fruit= fruit;
        this.vertical= vertical;
        this.upright= upright;
        this.upleft= upleft;
        this.ghost= ghost;
        this.horizontal= horizontal;
        this.playerclosed= playerclosed;
        this.playerup= playerup;
        this.playerleft=playerleft;
        this.playerdown= playerdown;
        this.playerright=playerright;
        this.superfruit=superfruit;
    }
    public void tickxu(){ // move left
        this.x += this.xVel;
    }
    public void tickxd(){ // move right
        this.x -= this.xVel;
    }
    public void tickyu(){ // move up
        this.y += this.yVel;
    }
    public void tickyd(){ // move down
        this.y -= this.yVel;
    }
    public void setimage(PImage imagea){ // change the image
        image=imagea;
    }
    public void draw(PApplet app){
        app.image(this.image,this.x,this.y);
    }
    public void reset(){ // when game restart, waka will reset
        this.x=this.xr;
        this.y=this.yr;
        this.image=this.playerclosed;
    }
    public int getx(){
        return x;
    }
    public int gety(){
        return y;
    }









    public int direct(int ed,int d,ArrayList<String> maparray){ // change the direction
        if(d==38){
            if(ed==37 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16-1,x/16).equals("7") ||maparray.get(y/16).substring(x/16-1,x/16).equals("8")  || maparray.get(y/16).substring(x/16-1,x/16).equals("0"))){
                    d=37;
                }else if(x%16!=0 ){
                    d=37;
                }

            }else if(ed==39 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8")  || maparray.get(y/16).substring(x/16+1,x/16+2).equals("0"))){
                    d=39;
                }else if(x%16!=0 ){
                    d=39;
                }
            }else if(ed==40 && x%16==0){
                if(y%16==0 && (maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8") || maparray.get(y/16+1).substring(x/16,x/16+1).equals("0"))){
                    d=40;
                }else if(y%16!=0){
                    d=40;
                }
            }
        }else if(d==40){
            if(ed==37 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16-1,x/16).equals("7")||maparray.get(y/16).substring(x/16-1,x/16).equals("8") || maparray.get(y/16).substring(x/16-1,x/16).equals("0"))){
                    d=37;
                }else if(x%16!=0 ){
                    d=37;
                }
            }else if(ed==39 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")|| maparray.get(y/16).substring(x/16+1,x/16+2).equals("8") || maparray.get(y/16).substring(x/16+1,x/16+2).equals("0"))){
                    d=39;
                }else if(x%16!=0 ){
                    d=39;
                }
            }else if(ed==38 && x%16==0){
                if(y%16==0 && (maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("0"))){
                    d=38;
                }else if(y%16!=0){
                    d=38;
                }
            }
        }else if(d==37){
            if(ed==40 && x%16==0){
                if(y%16==0 && (maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8") || maparray.get(y/16+1).substring(x/16,x/16+1).equals("0"))){
                    d=40;
                }else if(y%16!=0){
                    d=40;
                }
            }else if(ed==39 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16+1,x/16+2).equals("7")||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8") || maparray.get(y/16).substring(x/16+1,x/16+2).equals("0"))){
                    d=39;
                }else if(x%16!=0 ){
                    d=39;
                }
            }else if(ed==38 && x%16==0){
                if(y%16==0 && (maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("0"))){
                    d=38;
                }else if(y%16!=0){
                    d=38;
                }
            }
        }else if(d==39){
            if(ed==40 && x%16==0){
                if(y%16==0 && (maparray.get(y/16+1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8") || maparray.get(y/16+1).substring(x/16,x/16+1).equals("0"))){
                    d=40;
                }else if(y%16!=0){
                    d=40;
                }
            }else if(ed==37 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16-1,x/16).equals("7") ||maparray.get(y/16).substring(x/16-1,x/16).equals("8") || maparray.get(y/16).substring(x/16-1,x/16).equals("0"))){
                    d=37;
                }else if(x%16!=0 ){
                    d=37;
                }
            }else if(ed==38 && x%16==0){
                if(y%16==0 && (maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("0"))){
                    d=38;
                }else if(y%16!=0){
                    d=38;
                }
            }
        }else if(d==0){
             if(ed==40 && x%16==0){
                if(y%16==0 && (maparray.get(y/16+1).substring(x/16,x/16+1).equals("7") || maparray.get(y/16+1).substring(x/16,x/16+1).equals("8") ||maparray.get(y/16+1).substring(x/16,x/16+1).equals("0"))){
                    d=40;
                }else if(y%16!=0){
                    d=40;
                }
            }else if(ed==37 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16-1,x/16).equals("7") || maparray.get(y/16).substring(x/16-1,x/16).equals("8") ||maparray.get(y/16).substring(x/16-1,x/16).equals("0"))){
                    d=37;
                }else if(x%16!=0 ){
                    d=37;
                }
            }else if(ed==38 && x%16==0){
                if(y%16==0 && (maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("0"))){
                    d=38;
                }else if(y%16!=0){
                    d=38;
                }
            }else if(ed==39 && y%16==0 ){
                if(x%16==0 && (maparray.get(y/16).substring(x/16+1,x/16+2).equals("7") ||maparray.get(y/16).substring(x/16+1,x/16+2).equals("8") || maparray.get(y/16).substring(x/16+1,x/16+2).equals("0"))){
                    d=39;
                }else if(x%16!=0 ){
                    d=39;
                }
            }
        }
        return d;
    }
    public void move(int d,ArrayList<String> maparray ){ // waka move
        if(d==37){
            if(x%16==0 && (maparray.get(y/16).substring(x/16-1,x/16).equals("7") ||maparray.get(y/16).substring(x/16-1,x/16).equals("8") || maparray.get(y/16).substring(x/16-1,x/16).equals("0"))){
                this.tickxd();
            }else if(x%16!=0 ){
                this.tickxd();
            }
        }else if(d==39){
            if(x%16==0 && (maparray.get(y/16).substring(x/16+1,x/16+2).equals("7") || maparray.get(y/16).substring(x/16+1,x/16+2).equals("8") || maparray.get(y/16).substring(x/16+1,x/16+2).equals("0"))){
                this.tickxu();
            }else if(x%16!=0 ){
                this.tickxu();
            }
        }else if(d==38){
            if(y%16==0 && (maparray.get(y/16-1).substring(x/16,x/16+1).equals("7")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("8")||maparray.get(y/16-1).substring(x/16,x/16+1).equals("0"))){
                this.tickyd();
            }else if(y%16!=0){
                this.tickyd();
            }
        }else if(d==40){
            if(x%16==0 && (maparray.get(y/16+1).substring(x/16,x/16+1).equals("7") ||maparray.get(y/16+1).substring(x/16,x/16+1).equals("8") || maparray.get(y/16+1).substring(x/16,x/16+1).equals("0"))){
                this.tickyu();
            }else if(x%16!=0 ){
                this.tickyu();
            }
        }
    }
    public void playerchange(int x,int d){ // waka change image
        if((x/8)%2==0){
            this.setimage(this.playerclosed);
        }else{
            if(d==37){
                this.setimage(this.playerleft);
            }else if(d==38){
                this.setimage(this.playerup);
            }else if(d==39){
                this.setimage(this.playerright);
            }else if(d==40){
                this.setimage(this.playerdown);
            }else{
                this.setimage(this.playerclosed);
            }
        }
    }

}