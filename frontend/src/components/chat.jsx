import React, { useState } from "react";
import { extractGoals } from "../api/api";

export default function Chat() {
  const [input, setInput] = useState("");
  const [goals, setGoals] = useState([]);

  const send = async () => {
    const res = await extractGoals(input);
    setGoals(res.data.goals || []);
  };

  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={send}>Send</button>

      <ul>
        {goals.map((g, i) => (
          <li key={i}>{g.title} - {g.type}</li>
        ))}
      </ul>
    </div>
  );
}