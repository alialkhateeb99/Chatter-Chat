import React, { useState,useEffect } from "react";

import  {Button} from './Button';
import { Socket } from './Socket';


export default function Content(){
  const [messages,setMessages] = useState([])
  
  function getNewMessages(){
    useEffect(() => {
      Socket.on('message received',(data) =>{
        console.log("Received messages from the server: " + data["message"]);
        setMessages(data["message"])
      })
    });
  }
  
  getNewMessages();
  
  return(
    <div>
    <ul>
        { /* {messages.map((msg) => (   //// TODO HERE
           <li> {msg} </li>
         ))}
         */
        }
    </ul>
    <Button />
    </div>
  );
}