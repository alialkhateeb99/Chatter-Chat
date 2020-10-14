import * as React from 'react';
import { Socket } from './Socket';

import './myStyles.css';

function handleSubmit(event){
    let newMessage = document.getElementById("msg_input")
    
    Socket.emit('new message',{
        'message': newMessage.value
    });
    console.log("Sent the message " + newMessage.value + " to the server!");
    
    newMessage.value =''
    event.preventDefault();
}

export function Button(){
    return(
        <form onSubmit={handleSubmit}>
            <input className="input-box" id="msg_input" placeholder="Enter message here"/>
            <button className="buttonStyle" > Send Message </button>
        </form>
    );
}