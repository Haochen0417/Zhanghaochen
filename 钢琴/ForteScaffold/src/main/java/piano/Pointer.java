package piano;
import processing.core.PApplet;
import processing.core.PImage;
public class Pointer{
    private int x;
    private int y;
    private int xVel;
    private int xr;
    private PImage image;
    public Pointer(int x,int y,int xVel,PImage image){
        this.x=x;
        this.y=y;
        this.xr=x;
        this.xVel=xVel;
        this.image=image;
    }
    public void tick(){
        if (this.x<=525){
            this.x += this.xVel;
        }


    }
    public void draw(PApplet app){
        app.image(this.image,this.x,this.y);
    }
    public void reset(){
        this.x=this.xr;
    }
}