import React, { useState,useEffect } from "react";


import  {Button} from './Button';
import {Users} from './Users';
import { Socket } from './Socket';


export default function Content(){
  const [messages,setMessages] = useState([])

  function getNewMessages(){
    
    useEffect(() => {
      Socket.on('all messages',(data) =>{
        console.log("Received messages from the server: " + data["allMessages"]);
        setMessages(data["allMessages"])
        
      })
    });
  }
  
  getNewMessages();

  return(
    <div>
    <Users />
        
        <ol>
        { 
          messages.map((message,index) => 
          <li key={index} > { message } </li>)
        }
        </ol>
    <Button />
    
    </div>
  );
}