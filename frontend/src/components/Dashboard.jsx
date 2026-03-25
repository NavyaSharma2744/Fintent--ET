import React, { useState } from "react";
import { getScore } from "../api/api";

export default function Dashboard() {
  const [score, setScore] = useState(null);

  const fetchScore = async () => {
    const res = await getScore({
      income: 50000,
      emergency_fund: 100000,
      monthly_expense: 20000,
      has_insurance: true,
      asset_types: 3,
      debt: 10000,
      tax_saving: true,
      retirement_savings: 200000
    });

    setScore(res.data);
  };

  return (
    <div>
      <h1>Fintent Dashboard</h1>
      <button onClick={fetchScore}>Calculate Score</button>
      {score && <h2>{score.total_score}</h2>}
    </div>
  );
}