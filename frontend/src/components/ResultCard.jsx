import React from "react";
import { motion } from "framer-motion";

function ResultCard({ result }) {
  if (!result) return null; // hide if no result yet

  const isPlaced = result.toLowerCase() === "yes";

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.4 }}
      className={`mt-6 p-6 rounded shadow-xl w-120 text-center ${
        isPlaced
          ? "bg-green-50 border-2 border-green-400"
          : "bg-red-50 border-2 border-red-400"
      }`}
    >
      <h2
        className={`text-2xl font-bold mb-3 ${
          isPlaced ? "text-green-700" : "text-red-700"
        }`}
      >
        {isPlaced ? "🎉 Congratulations!" : "⚠️ Better Luck Next Time!"}
      </h2>

      <p className="text-lg font-medium text-gray-800">
        Placement Result:{" "}
        <span
          className={`font-bold ${
            isPlaced ? "text-green-600" : "text-red-600"
          }`}
        >
          {result}
        </span>
      </p>

      {isPlaced ? (
        <p className="mt-3 text-green-600 font-medium">
          You are likely to get placed 🚀
        </p>
      ) : (
        <p className="mt-3 text-red-600 font-medium">
          Keep working hard, success is coming 💪
        </p>
      )}
    </motion.div>
  );
}

export default ResultCard;
