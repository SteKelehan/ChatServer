// Implementation of simple ChatServer
// Importing libs

import java.net.*;
import java.io.*;


// Creating Server Object!
public class ChatServer{
    // creatring P2P vars
    private Scoket socket = null;
    private ServerSocket server = null;
    private DataInputStream streamIN = null;

    public ChatServer(int port){
        try{
            // Printing the port number and creating a socket connection
            System.out.println("Binding to port " + port + " ....");
            server = new ServerSocket(port);
            System.out.println(server);
            start();
        }
        catch(IOExecption ioe){
            System.out.println(ioe);
        }
    }

    public void run(){
        while(thread != null){
            try{
                System.out.println("Weighting for client ...");
                socket = server.accept();
                System.out.println("Connected to CLient: " = socket);
                open();
                boolean done = false;
                while(!done){
                    try{
                        String line = streamIn.readUTF();
                        System.out.println(line);
                        done = line.equals("exit chat");        // disconnects if you message server exit chat
                    }
                    catch{
                        done = true;
                    }
                }
                close();
            }
            catch(IOExecption ie){
                System.out.println("Acceptance Error: " + ie);
            }
        }
    }


    public void open () throws IOExecption{
        streamIn = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
    }

    public void close() throws IOExecption{
        if(socket != null){
            socket.close()
        }
        if(streamIn != null){
            streamIn.close();
        }
    }

    public static void main(String args[]){
        ChatServer server = null;
        if(args.lenght != 1){
            System.out.println("Usage: java ChatServer port");
        }
        else{
            server = new ChatServer(Integer.parseInt(args[0]));
        }
    }

}

