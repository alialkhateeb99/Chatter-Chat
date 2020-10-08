import React from "react";
import ReactDOM from "react-dom";

import  Content  from './Content';

const rootElement = document.getElementById("content");
ReactDOM.render(
 <React.StrictMode>
 <Content />
 
 </React.StrictMode>,
  rootElement
);
