/* eslint-disable import/no-extraneous-dependencies */

import React, { useState, useEffect } from 'react';

import Linkify from 'react-linkify';
import renderHTML from 'react-render-html';
import Button from './Button';
import  Users  from './Users';
import { Socket } from './Socket';
import './myStyles.css';

export default function Content() {
  const [messages, setMessages] = useState([]);

  function getNewMessages() {
    useEffect(() => {
      Socket.on('all messages', (data) => {
        // console.log("Received messages from the server: " + data["allMessages"]);
        setMessages(data.allMessages);
      });
    });
  }

  getNewMessages();

  return (
    <div className="parent-div">
      <div className="title-style"> Chatter-chat app</div>
      <Users />
      <div className="Content">
        <ol>
          {
          messages.map((message, index) => (
            <li className="list-style" key={index}>
              <Linkify properties={{
                target: '_blank',
                style: { color: 'red', fontWeight: 'bold' },
              }}
              >
                { renderHTML(message) }
              </Linkify>
            </li>
          ))
        }
        </ol>
      </div>
      <div className="texts">
        <Button> </Button>
      </div>
    </div>
  );
}
