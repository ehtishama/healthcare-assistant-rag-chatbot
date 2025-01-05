import React from "react";

function Message({ message, sender }) {
  const isUser = sender === "user";
  return (
    <div
      className={`flex flex-wrap py-[18px] ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <p
        className={` rounded-lg py-[10px] px-[20px]  max-w-max ${
          isUser ? "bg-gray-200 justify-end" : ""
        }`}
      >
        {message}
      </p>
    </div>
  );
}

export default Message;
