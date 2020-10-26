/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from 'react';
import { Socket } from './Socket';

import './myStyles.css';

export default function Users() {
  const [activeUsers, setActiveUsers] = useState(0);

  useEffect(() => {
    Socket.on('connected', (data) => {
      setActiveUsers(activeUsers + 1);
    });
    Socket.on('disconnect', (data) => {
      setActiveUsers(activeUsers - 1);
    });
  });

  return (
    <div className="users-style">
      Active Users In Session
      {' '}
      {activeUsers }
    </div>
  );
}
