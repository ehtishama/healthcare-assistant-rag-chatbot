import { useChat } from "../../contexts/ChatContext";

function DefaultScreen() {
  const { addUserMsg, askBot } = useChat();
  const questions = [
    "I have a headache, what should I do?",
    "Could my headache be due to stress?",
    "What could be the cause of a persistent headache?",
    "I'm having a headache, is it a migraine?",
    "What are the common reasons for a headache?",
  ];

  return (
    <>
      <div className=" max-w-xl">
        <h1 className="text-3xl font-semibold">
          Feeling Unwell? Let’s Find Out Why
        </h1>

        <ul className="flex gap-2 flex-wrap mt-5">
          {questions.map((q, i) => (
            <li key={i}>
              <button
                className="border border-black rounded-3xl py-2 px-3 text-sm transition hover:bg-gray-400"
                onClick={() => {
                  addUserMsg({ text: q, sender: "user" });
                  askBot(q);
                }}
              >
                {q}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default DefaultScreen;
