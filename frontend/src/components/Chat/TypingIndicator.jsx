import { Skeleton } from "primereact/skeleton";

function TypingIndicator() {
  return (
    <>
      <div className="flex gap-1">
        <Skeleton
          shape="circle"
          size="0.8rem"
          className="w-6 h-6 bg-green-100 animate-dot-bounce delay-200"
        />
        <Skeleton
          shape="circle"
          size="0.8rem"
          className="w-6 h-6 bg-green-100 animate-dot-bounce delay-300"
        />
        <Skeleton
          shape="circle"
          size="0.8rem"
          className="w-6 h-6 bg-green-100 animate-dot-bounce delay-400"
        />
      </div>
      <p className="animate-pulse text-sm text-green-500 font-medium font-primary py-[10px]">
        Bot is typing...
      </p>
    </>
  );
}

export default TypingIndicator;
