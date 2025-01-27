import React, { useEffect, useState } from "react";

// import "primereact/resources/themes/lara-dark-green/theme.css"; //theme
import "primereact/resources/primereact.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import "./App.css";
import ChatWindow from "./components/Chat/ChatWindow";
import { v4 as uuidv4 } from "uuid";
import { useChat } from "./contexts/ChatContext";

function App() {
  const randomId = uuidv4();
  const { threadId, setThreadId } = useChat();

  useEffect(() => {
    setThreadId(randomId);
  }, []);
  return (
    <>
      <ChatWindow />
    </>
  );
}

export default App;
