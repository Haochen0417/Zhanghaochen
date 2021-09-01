package piano;
import processing.core.PApplet;
import processing.core.PImage;
public class Banner{
    private int x;
    private int y;
    private PImage image;
    public Banner(int x,int y,PImage image){
        this.x=x;
        this.y=y;
        this.image=image;
    }
    public void tick(){
    }
    public void draw(PApplet app){
        app.image(this.image,this.x,this.y);
    }
}