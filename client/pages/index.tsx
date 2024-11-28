import React, { useState } from "react";

const Index = () => {
  const [sentence, setSentence] = useState<string>("");
  const [accuracy, setAccuracy] = useState<number | null>(null);

  const [error, setError] = useState<string | null>(null);
  const [modelName, setModelName] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // Prevent page reload

    setError(null); // Reset errors
    setAccuracy(null); // Reset emotion
    setModelName(null);

    try {
      const response = await fetch(`http://localhost:8080/api/run`, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error("Failed to fetch emotion.");
      }

      const data = await response.json();
      console.log(data);
      setAccuracy(data.accuracy);
      setModelName(data.model_name);
    } catch (error) {
      console.log("An error occurred while processing your request.", error);
    }
  };

  return (
    <div className="p-8 font-sans">
      <h1 className="text-2xl font-bold mb-4">Emotion Detector</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <textarea
          value={sentence}
          onChange={(e) => setSentence(e.target.value)}
          placeholder="Enter your sentence here..."
          rows={4}
          className="w-full p-4 mb-2 text-lg border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        ></textarea>
        <button
          type="submit"
          className="px-4 py-2 text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Analyze Emotion
        </button>
      </form>
      {error && <p className="text-red-600">{error}</p>}
      {accuracy && (
        <p
          className={`text-lg font-bold p-2 rounded-md ${
            accuracy > 0.5
              ? "bg-green-200 text-green-800"
              : accuracy < 0.2
              ? "bg-red-200 text-red-800"
              : "bg-gray-200 text-gray-800"
          }`}
        >
          Accuracy: {accuracy}
          <br></br>
          Model Name: {modelName}
        </p>
      )}
    </div>
  );
};

export default Index;
