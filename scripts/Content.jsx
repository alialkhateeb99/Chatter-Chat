import React, { useState,useEffect,useRef } from "react";

import  {Button} from './Button';
import {Users} from './Users';
import { Socket } from './Socket';
import './myStyles.css';


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
    <div className="parent-div">
    <Users />
    <div className="Content">

        <ol>
        { 
          messages.map((message,index) => 
          <li key={index} > { message } </li>)
        }
        </ol>
    </div>
 
      <div className="texts">
          <Button > </Button>
      </div>
    </div>
  );
}