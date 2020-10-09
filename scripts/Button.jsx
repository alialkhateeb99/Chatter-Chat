import * as React from 'react';
import { Socket } from './Socket';


function handleSubmit(event){
    let newMessage = document.getElementById("msg_input")
    
    Socket.emit('new message',{
        'message': newMessage.value
    });
    console.log("Sent the message" + newMessage.value + " to the server!");
    
    newMessage.value =''
    
    event.preventDefault();
}

export function Button(){
    return(
        <form onSubmit={handleSubmit}>
            <input id="msg_input" placeholder="enter message here"/>
            <button> Send </button>
        </form>
    );
}