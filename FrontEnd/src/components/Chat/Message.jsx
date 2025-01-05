import React from "react";
import Markdown from "react-markdown";

function Message({ message, sender }) {
  const isUser = sender === "user";
  return (
    <div
      className={`flex flex-wrap py-[18px] ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <p
        className={`markdown space-y-4 rounded-lg py-[10px] px-[20px]  max-w-max ${
          isUser ? "bg-gray-200 justify-end" : ""
        }`}
      >
        {isUser ? message : <Markdown>{message}</Markdown>}
      </p>
    </div>
  );
}

export default Message;
