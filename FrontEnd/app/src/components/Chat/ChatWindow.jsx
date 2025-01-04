import React, { useEffect, useRef, useState } from "react";
import Message from "./Message";
import { useChat } from "../../contexts/ChatContext";
import TypingIndicator from "./TypingIndicator";
import DefaultScreen from "../DefaultScreen/DefaultScreen";
import MessageToolbar from "./MessageToolbar";

function ChatWindow() {
  const [input, setInput] = useState("Fever");
  const messagesEndRef = useRef(null);

  const {
    loading,
    messages,
    addUserMsg,
    askBot,
    showDefaultScreen,
    setShowDefaultScreen,
  } = useChat();

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (input.trim() !== "") {
      setShowDefaultScreen(false);
      setInput(e.target.value);
      addUserMsg({ text: input, sender: "user" });
      askBot(input);
    }
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chatbot-ui max-w-xl mx-auto relative min-h-screen py-8 grid">
      {/* ======================== */}
      {/* Messages */}
      {/* ======================== */}
      <div>
        {messages && (
          <>
            {messages?.map((msg, index) => (
              <Message key={index} message={msg.text} sender={msg.sender} />
            ))}
          </>
        )}
        {loading && <TypingIndicator />}
      </div>
      <div className="h-[10px]" ref={messagesEndRef} />

      {/* ======================== */}
      {/* Default Quick Questions */}
      {/* ======================== */}
      <div className="self-center">
        {showDefaultScreen && <DefaultScreen />}
      </div>

      {/* ================== */}
      {/* Message Toolbar    */}
      {/* ================== */}

      <MessageToolbar
        input={input}
        onInputChange={handleInputChange}
        onBtnClick={handleSendMessage}
      />
    </div>
  );
}

export default ChatWindow;
