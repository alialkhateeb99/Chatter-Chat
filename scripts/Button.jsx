import * as React from 'react';
import { Socket } from './Socket';
import GoogleLogin from 'react-google-login';
import ReactDOM from 'react-dom';

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
function handleLogin(){
    
}

export function Button(){
    return(
        <div>
        <form onSubmit={handleSubmit}>
            <input className="input-box" id="msg_input" placeholder="Enter message here"/>
            <button className="buttonStyle" > Send Message </button>
        </form>
         <GoogleLogin
    clientId="757562204494-pcbfe34ktb0ku10dhrm5v8hv4qh41jnd.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={handleLogin}
    onFailure={handleLogin}
    isSignedIn={false}
    />
        </div>
    );
}