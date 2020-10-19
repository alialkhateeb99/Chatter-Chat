import React, { useState,useEffect } from "react";
import { Socket } from './Socket';

import './myStyles.css';

export function Users(){
    
    const [activeUsers,setActiveUsers] = useState(0)
      
       useEffect(() => {
        Socket.on('connected',(data) => {
            console.log("Another user has joined!")
            setActiveUsers( activeUsers+ 1)
            console.log("number of active users" + activeUsers)
      })
        Socket.on('disconnect',(data) => {
            console.log("A user has left the chat!")
            setActiveUsers( activeUsers - 1)
            console.log("number of active users" + activeUsers)
      })
    })

    return(
        <div className="users-style">
       Active Users In Session {activeUsers } 
        </div>
    );
}
