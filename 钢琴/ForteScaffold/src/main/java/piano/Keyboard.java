package piano;
import processing.core.PApplet;
import processing.core.PImage;
public class Keyboard{
    private int x;
    private int y;
    private PImage image;
    public Keyboard(int x,int y,PImage image){
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