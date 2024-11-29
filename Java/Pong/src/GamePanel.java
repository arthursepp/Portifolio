import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class GamePanel extends JPanel implements Runnable {

    //Largura da janela:
    static final int GAME_WIDTH = 1000;

    //Altura da janela:
    static final int GAME_HEIGHT = (int)(GAME_WIDTH * (0.5555));
    static final Dimension SCREEN_SIZE = new Dimension(GAME_WIDTH, GAME_HEIGHT);

    //Tamanho da bola:
    static final int BALL_DIAMETER = 20;

    //Largura do jogador:
    static final int PADDLE_WIDTH = 25;

    //Altura do jogador:
    static final int PADDLE_HEIGHT = 100;
    Thread gameThread;
    Image image;
    Graphics graphics;
    Random random;
    Paddle paddle1;
    Paddle paddle2;
    Ball ball;
    Score score;

    GamePanel(){

        newPaddles();
        newBall();
        score = new Score(GAME_WIDTH, GAME_HEIGHT);
        this.setFocusable(true);
        this.addKeyListener(new AL());
        this.setPreferredSize(SCREEN_SIZE);

        gameThread = new Thread(this);
        gameThread.start();

    }

    public void newBall(){
        random = new Random();
        ball = new Ball((GAME_WIDTH / 2) - (BALL_DIAMETER/2), random.nextInt(GAME_HEIGHT - BALL_DIAMETER), BALL_DIAMETER, BALL_DIAMETER);
    }

    public void newPaddles(){

        paddle1 = new Paddle(0, (GAME_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT, 1);
        paddle2 = new Paddle(GAME_WIDTH - PADDLE_WIDTH, (GAME_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT, 2);

    }

    public void paint(Graphics g){

        image = createImage(getWidth(), getHeight());
        graphics = image.getGraphics();
        draw(graphics);
        g.drawImage(image, 0,0,this);
    }

    public void draw(Graphics g){

        paddle1.draw(g);
        paddle2.draw(g);
        ball.draw(g);
        score.draw(g);
    }

    public void move(){

        paddle1.move();
        paddle2.move();
        ball.move();

    }
    public void checkCollision(){

        //Impede que a bola saia pelo topo ou por baixo da janela.
        if (ball.y <= 0) {
            ball.setYDirection(-ball.yVelocity);
        }
        if (ball.y >= GAME_HEIGHT - BALL_DIAMETER) {
            ball.setYDirection(-ball.yVelocity);
        }

        //Rebate a bola nas barras
        if (ball.intersects(paddle1)) {
            ball.xVelocity = Math.abs(ball.xVelocity);
            ball.xVelocity++; //OPCIONAL: aumenta a velocidade da bola quando ela
            //bater em uma das barras.

            if (ball.yVelocity > 0)
                ball.yVelocity++; //OPCIONAL: aumenta a velocidade da bola quando ela
                //bater em uma das paredes (cima e baixo).
            else
                ball.yVelocity--;
            ball.setXDirection(ball.xVelocity);
            ball.setYDirection(ball.yVelocity);

        }

        if (ball.intersects(paddle2)) {
            ball.xVelocity = Math.abs(ball.xVelocity);
            ball.xVelocity++; //OPCIONAL: aumenta a velocidade da bola quando ela
            //bater em uma das barras.

            if (ball.yVelocity > 0)
                ball.yVelocity++; //OPCIONAL: aumenta a velocidade da bola quando ela
                //bater em uma das paredes (cima e baixo).
            else
                ball.yVelocity--;
            ball.setXDirection(-ball.xVelocity);
            ball.setYDirection(ball.yVelocity);

        }

        //Stops paddles at window edges.
        //Impede que as barras saiam do alcance da janela.

        if (paddle1.y <= 0)
            paddle1.y = 0;

        if (paddle1.y >= (GAME_HEIGHT - PADDLE_HEIGHT))
            paddle1.y = GAME_HEIGHT - PADDLE_HEIGHT;

        if (paddle2.y <= 0)
            paddle2.y = 0;

        if (paddle2.y >= (GAME_HEIGHT - PADDLE_HEIGHT))
            paddle2.y = GAME_HEIGHT - PADDLE_HEIGHT;

        //Dá ponto á um jogador e cria novas barras e nova bola.
        if (ball.x <= 0){
            score.player2++;

            //Reseta as barras e a bola no meio da tela:
            newPaddles();
            newBall();

            //Mostrando o jogador que fez ponto e a pontuação total no console:
            System.out.println( "-------------" + "\nPlayer 2: " + score.player2 +
                    "\nTotal Score: \nPlayer 1: | Player 2:" +
                    "\n        " + score.player1 + " | " + score.player2);
        }

        if (ball.x >= GAME_WIDTH - BALL_DIAMETER){
            score.player1++;
            //Reseta as barras e a bola no meio da tela:
            newPaddles();
            newBall();
            //Mostrando o jogador que fez ponto e a pontuação total no console:
            System.out.println( "-------------" + "\nPlayer 1: " + score.player1 +
                    "\nTotal Score: \nPlayer 1: | Player 2:" +
                    "\n        " + score.player1 + " | " + score.player2);
        }
    }

    public void run(){
        long lastTime = System.nanoTime();
        double amountOfTicks = 60.0;
        double ns = 1000000000 / amountOfTicks;
        double delta = 0;
        while (true) {
            long now = System.nanoTime();
            delta += (now - lastTime) / ns;
            lastTime = now;
            if (delta >= 1){
                move();
                checkCollision();
                repaint();
                delta--;
            }
        }
    }

    public class AL extends KeyAdapter{
        public void keyPressed(KeyEvent e){
            paddle1.keyPressed(e);
            paddle2.keyPressed(e);
        }

        public void keyReleased(KeyEvent e){
            paddle1.keyReleased(e);
            paddle2.keyReleased(e);
        }
    }

}
