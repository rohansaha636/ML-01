import React, { useState } from "react";
import API from "../api";

function InputForm({ setResult }) {
  const [cgpa, setCgpa] = useState("");
  const [iq, setIq] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("/predict", { cgpa: parseFloat(cgpa), iq: parseInt(iq) });
      setResult(res.data.placement);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input type="number" step="0.1" placeholder="Enter CGPA"
             value={cgpa} onChange={(e) => setCgpa(e.target.value)}
             className="border p-2 w-full" />
      <input type="number" placeholder="Enter IQ"
             value={iq} onChange={(e) => setIq(e.target.value)}
             className="border p-2 w-full" />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded cursor-pointer">Predict</button>
    </form>
  );
}

export default InputForm;
