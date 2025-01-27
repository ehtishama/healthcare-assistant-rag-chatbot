function MessageToolbar({ input, onInputChange, onBtnClick }) {
  return (
    <form className="self-end gap-2 w-full max-w-xl flex items-center rounded-lg  bg-white">
      <input
        className="flex-1 py-4 px-2 rounded-lg border border-black"
        type="text"
        value={input}
        onChange={onInputChange}
        placeholder="Type a message..."
      />
      <button
        className="py-4 px-2 rounded-lg bg-primary border border-transparent"
        onClick={onBtnClick}
      >
        Send
      </button>
    </form>
  );
}

export default MessageToolbar;
