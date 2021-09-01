package ghost;
import processing.core.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;
import java.lang.*;
import java.lang.Object;
public class App extends PApplet {
    public static final int WIDTH = 448;
    public static final int HEIGHT = 576;
    private Player player;
    private Chaser chaser;
    private Ambusher ambusher;
    private Ignorant ignorant;
    private Whim whim;
    private File myObj;
    private Manager mm;
    private int x;
    private int xw;
    private int t;
    private int d; // player direction now
    private int ed; // expected direction now
    private int live; // waka live
    private int ft;  // frightened times
    private PFont font;
    private ArrayList<String> maparray; // put the map in the maparray
    public App() {
        x=0;
        t=0;
        d=0;
        int xw=0; // record the time when win or end
        ft=0;
        maparray=new ArrayList<String>();
    }
    public void setup() {
        frameRate (60);
        font=createFont("src/main/resources/PressStart2P-Regular.tff",50);
        mm = new Manager(); // manager is build the game
        maparray=mm.readjson(); // get the map
        live=mm.livestime();
        this.player=new Player(16*mm.getx(),16*mm.gety(),mm.speedstime(),mm.speedstime(),this.loadImage("src/main/resources/playerClosed.png"),this.loadImage("src/main/resources/downLeft.png"),this.loadImage("src/main/resources/downRight.png"),this.loadImage("src/main/resources/fruit.png"),this.loadImage("src/main/resources/vertical.png"),this.loadImage("src/main/resources/upRight.png"),this.loadImage("src/main/resources/upLeft.png"),this.loadImage("src/main/resources/chaser.png"),this.loadImage("src/main/resources/horizontal.png"),this.loadImage("src/main/resources/playerClosed.png"),this.loadImage("src/main/resources/playerUp.png"),this.loadImage("src/main/resources/playerLeft.png"),this.loadImage("src/main/resources/playerDown.png"),this.loadImage("src/main/resources/playerRight.png"),this.loadImage("src/main/resources/superfruit.png"));
        this.chaser=new Chaser(16*mm.getcx(),16*mm.getcy(),mm.speedstime(),mm.speedstime(),this.loadImage("src/main/resources/chaser.png"),this.loadImage("src/main/resources/chaser.png"),this.loadImage("src/main/resources/frightened.png"));
        this.ambusher=new Ambusher(16*mm.getax(),16*mm.getay(),mm.speedstime(),mm.speedstime(),this.loadImage("src/main/resources/ambusher.png"),this.loadImage("src/main/resources/ambusher.png"),this.loadImage("src/main/resources/frightened.png"));
        this.ignorant=new Ignorant(16*mm.getix(),16*mm.getiy(),mm.speedstime(),mm.speedstime(),this.loadImage("src/main/resources/ignorant.png"),this.loadImage("src/main/resources/ignorant.png"),this.loadImage("src/main/resources/frightened.png"));
        this.whim=new Whim(16*mm.getwx(),16*mm.getwy(),mm.speedstime(),mm.speedstime(),this.loadImage("src/main/resources/whim.png"),this.loadImage("src/main/resources/whim.png"),this.loadImage("src/main/resources/frightened.png"));
        maparray=mm.mapclean(player, ambusher, chaser, ignorant, whim,maparray);
    }
    public void settings() {size(WIDTH, HEIGHT);}
    public void draw() {
        background(0,0,0);
        if(live!=0 && !mm.calculate(maparray)){
            int ii=0;
            while(ii<maparray.size()){
                int i=0;
                String data=maparray.get(ii); // data is the each line of the map
                while(i<data.length()){
                    if(data.substring(i,i+1).equals("0")){
                    }else if(data.substring(i,i+1).equals("1")){this.image(this.player.horizontal,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("2")){this.image(this.player.vertical,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("3")){this.image(this.player.upleft,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("4")){this.image(this.player.upright,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("5")){this.image(this.player.downleft,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("6")){this.image(this.player.downright,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("7")){this.image(this.player.fruit,16*i,16*ii);
                    }else if(data.substring(i,i+1).equals("8")){this.image(this.player.superfruit,16*i,16*ii);
                    }i++;
                }ii++;}
            d=this.player.direct(ed,d,maparray); // reset the direction
            this.player.move(d,maparray);
            this.player.playerchange(x,d); // change the direction image
            this.player.draw(this);
            ft=mm.f(this.player,maparray,ft); // if waka each fruit frighten time will change
            if(ft>0){mm.gfmove( ambusher, chaser, ignorant, whim, maparray, x , d, player);}
            else{mm.gmove( ambusher, chaser, ignorant, whim, maparray, x , d, player);}
            if(chaser.die){this.chaser.draw(this);}
            if(ambusher.die){this.ambusher.draw(this);}
            if(ignorant.die){this.ignorant.draw(this);}
            if(whim.die){this.whim.draw(this);}
            x++;
            mm.touch(this.player,maparray);
            if(ft>0){mm.touchfghost(player, ambusher, chaser, ignorant, whim);}
            else{if(mm.touchghost(player, ambusher, chaser, ignorant, whim)){d=0;x=0;ed=0;live-=1;ft=0;}}
            ft-=1;
            int nn =0;
            while(nn<live){this.image(this.loadImage("src/main/resources/playerRight.png"),24*nn,544);nn+=1;}
        }else if(live!=0 && mm.calculate(maparray)){textFont(font); text("YOU WIN",120,256);xw++;
                if(xw==600){mm.resett(player, ambusher, chaser, ignorant, whim);maparray.clear();maparray=mm.readjson();mm.mapclean(player,ambusher,chaser,ignorant,whim,maparray);x=0;ed=0;live=mm.livestime();xw=0;d=0;ft=0;}
        }else{this.image(this.loadImage("src/main/resources/gameover - Copy.png"),170,256);
            x++;
            if(x==600){maparray.clear();maparray=mm.readjson();mm.mapclean(player,ambusher,chaser,ignorant,whim,maparray);x=0;ed=0;live=mm.livestime();ft=0;}}}
    public void keyPressed() {this.ed=keyCode;}
    public static void main(String[] args) {PApplet.main("ghost.App");}
}
