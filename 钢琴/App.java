package piano;


import processing.core.PApplet;
import processing.core.PImage;
import java.util.ArrayList;
import javax.sound.midi.*;

public class App extends PApplet {
    private Keyboard keyboard;
    private Grid grid;
    private MiddleBanner middleBanner;
    private Banner banner;
    private ButtonBack buttonBack1;
    private ButtonBack buttonBack2;
    private Pointer pointer;
    private Play play;
    private Pause pause;
    private Stop stop;
    private Block block;
    private PImage bb;
    private int x;
    private ArrayList<Integer> intX;
    private ArrayList<Integer> intY;
    private int signal;
    private Synthesizer synthesizer;
    private MidiChannel channel;
    private int nmove;
    private int nmoveact;
    private ArrayList<Integer>  nmovel;
    private ArrayList<Integer>  note;




    public App() {
        // Initialise variables here
    }

    public void settings() {
        // Don't touch
        size(540, 335);

    }

    public void setup() {
        frameRate(60);
        // Load images here
        this.keyboard= new Keyboard(0,75,this.loadImage("src/main/resources/keyboard.png"));
        this.grid = new Grid (60,75,this.loadImage("src/main/resources/grid.png"));
        this.middleBanner = new MiddleBanner(0,0,this.loadImage("src/main/resources/middleBanner.png"));
        this.banner=new Banner(0,0,this.loadImage("src/main/resources/banner.png"));
        this.buttonBack1=new ButtonBack(5,5,this.loadImage("src/main/resources/buttonBack.png"));
        this.buttonBack2=new ButtonBack(50,5,this.loadImage("src/main/resources/buttonBack.png"));
        this.pointer=new Pointer(45,55,1,this.loadImage("src/main/resources/pointer.png"));
        this.play=new Play(5,5,this.loadImage("src/main/resources/play.png"));
        this.pause=new Pause(5,5,this.loadImage("src/main/resources/pause.png"));
        this.stop=new Stop(50,5,this.loadImage("src/main/resources/stop.png"));
        this.bb=this.loadImage("src/main/resources/block.png");
        x=0;
        this.intX=new ArrayList<Integer>();
        this.intY=new ArrayList<Integer>();
        signal=0;
        nmove=60;






    }

    public void draw() {
        // Draw your program here

        //tick
        if(x%2==1){

            this.keyboard.tick();
            this.pointer.tick();
            nmoveact=(nmove-60)/15*15+60;
            ArrayList<Integer> nmovel=new ArrayList<Integer>();
            ArrayList<Integer> note=new ArrayList<Integer>();
            for(int a=0; a<intX.size() ;a+=1){
                if(intX.get(a)==nmoveact&&nmoveact==nmove){
                    nmovel.add(a);
                }
            }
            for (int a:nmovel){
                int aa = 72-((intY.get(a)-75)/20);
                try{
                    Synthesizer synthesizer = MidiSystem.getSynthesizer();
                    synthesizer.open();
                    MidiChannel channel =  synthesizer.getChannels()[0];
                    channel.noteOn(aa,90);

                }catch(MidiUnavailableException e){
                    e.printStackTrace();
                }
            }
            nmove+=1;
        }
        //draw
        this.keyboard.draw(this);
        this.grid.draw(this);
        this.middleBanner.draw(this);
        this.banner.draw(this);
        this.buttonBack1.draw(this);
        this.buttonBack2.draw(this);
        this.pointer.draw(this);
        this.stop.draw(this);
        if(x%2==1){
            this.pause.draw(this);
        }else{
            this.play.draw(this);
        }
        for (int i =0;i<intX.size();i+=1){
            this.image(this.bb,intX.get(i),intY.get(i));
        }






    }
    public void mousePressed(){
        if((5<mouseX&&mouseX<45) && (5<mouseY&&mouseY<45)){
            x+=1; //play and pause
        }
        if(50<mouseX&&mouseX<90&&5<mouseY&&mouseY<45){
            x=0;
            pointer.reset();
            nmove=60;

        }
        if(60<mouseX&&mouseX<540&&mouseY>75&&mouseY<335){
            signal=0;
            ArrayList<Integer> sameplot = new ArrayList<Integer>();
            for (int a=0;a<intX.size();a+=1){
                if (intX.get(a)==(mouseX-60)/15*15+60){
                    sameplot.add(a);
                }
            }
            for (int a:sameplot){
                if (intY.get(a)==(mouseY-75)/20*20+75){
                    intX.remove(a);
                    intY.remove(a);
                    signal=1;
                }
            }
            if(signal==0){
                intX.add((mouseX-60)/15*15+60);
                intY.add((mouseY-75)/20*20+75);
            }else{
                signal=0;
            }
        }

    }

    public static void main(String[] args) {
        // Don't touch this
        PApplet.main("piano.App");
    }
}
