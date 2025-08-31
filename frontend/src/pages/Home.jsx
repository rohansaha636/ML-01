import React, { useState } from "react";
import InputForm from "../components/InputForm";
import ResultCard from "../components/ResultCard";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <h1 className="text-3xl font-bold mb-6">Placement Predictor</h1>
      <InputForm setResult={setResult} />
      <ResultCard result={result} />
    </div>
  );
}

export default Home;
