import React, { useState } from "react";

// import "primereact/resources/themes/lara-dark-green/theme.css"; //theme
import "primereact/resources/primereact.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import "./App.css";
import ChatWindow from "./components/Chat/ChatWindow";

function App() {
  return (
    <>
      <ChatWindow />
    </>
  );
}

export default App;
