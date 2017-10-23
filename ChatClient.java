// Simple Client
// Importing Libs

import java.net.*;
import java.io.*;

public class ChatClient{
    private Socket socket = null;
    private DataInputStream console = null;
    private DataOutputStream streamOut = null;

    public ChatClient(String serverName, int serverPort){
        System.out.println("Connecting ...");
        try{
            socket = new Socket(serverName, serverPort);
            System.out.println("Conncted: " + socket);
            start();
        }
        catch(UnknownHostException uhe){
            System.out.println("Host unknown: " + uhe.getMessage());
        }
       

        String line = "";
        while(!line.equals("exit chat")){
            try{
                line = console.readLine();
                streamOut.writeUTF(line);
                streamOut.flush();
            }
            catch(IOException ioe){
                System.out.println("Sending error: " + ioe.getMessage());
            }
        }
    }

    public void start() throws IOException{
        console = new DataInputStream(System.in);
        streamOut = new DataOutputStream(socket.getOutputStream());
    }

    public void stop(){
        try{
            if(console != null)
                console.close();
            if(streamOut != null)
                streamOut.close();
            if(socket != null)
                socket.close();
        }
        catch(IOException ioe){
            System.out.println("error closing ..");
        }
    }

    public static void main(String args[]){
        ChatClient client = null;
        if(args.length != 2){
            System.out.println("Usage: java ChatCLient host port");
        }
        else{
            client = new ChatClient(args[0], Integer.parseInt(args[1]));
        }
    }
}
