import React, { useState,useEffect,useRef } from "react";

import  {Button} from './Button';
import {Users} from './Users';
import { Socket } from './Socket';
import Linkify from 'react-linkify';
import Interweave from 'interweave';
import renderHTML from 'react-render-html';
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
    <div className="title-style"> Chatter-chat app</div>
    { /*<div> {renderHTML("<img src='https://www.outsideonline.com/sites/default/files/styles/width_1200/public/2019/12/11/zion-national-park_h.jpg' width='200' height='200' >")}  </div>*/}
    <Users />
   {/* <Interweave content="<img src='https://www.outsideonline.com/sites/default/files/styles/width_1200/public/2019/12/11/zion-national-park_h.jpg' "  /> */}
    <div className="Content">
        <ol>
        { 
          messages.map((message,index) => 
          <li className="list-style" key={index} >
          <Linkify properties={{target: '_blank', 
          style: {color: 'red', fontWeight: 'bold'}}}>
          { renderHTML( message) } </Linkify> </li>  )
        }
        </ol>
    </div>
      <div className="texts">
          <Button > </Button>
      </div>
    </div>
  );
}