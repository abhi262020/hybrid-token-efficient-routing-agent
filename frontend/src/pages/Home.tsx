import { useState } from "react";

import Navbar from "../components/Navbar";
import PromptBox from "../components/PromptBox";
import ModelBadge from "../components/ModelBadge";
import MetricsCard from "../components/MetricsCard";
import TokenChart from "../components/TokenChart";
import ResponseCard from "../components/ResponseCard";

interface RouteResponse {
  model: string;
  task: string;
  complexity: number;
  confidence: number;
  tokens: number;
  response: string;
}

const API_BASE =
  import.meta.env.VITE_API_URL ||
  "http://127.0.0.1:8000";

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<RouteResponse | null>(null);

  async function handlePrompt(prompt: string) {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      console.log("Backend:", API_BASE);

      const response = await fetch(`${API_BASE}/route`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          prompt,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || data.error || "Backend Error"
        );
      }

      setResult(data);
    } catch (err: any) {
      setError(err.message || "Unknown Error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        background: "#f5f7fb",
        minHeight: "100vh",
        padding: "30px",
      }}
    >
      <div
        style={{
          maxWidth: "1100px",
          margin: "0 auto",
        }}
      >
        <Navbar />

        <PromptBox
          onSubmit={handlePrompt}
          loading={loading}
        />

        {loading && (
          <div
            style={{
              marginTop: "25px",
              padding: "20px",
              textAlign: "center",
              background: "#ffffff",
              borderRadius: "10px",
              boxShadow: "0 4px 10px rgba(0,0,0,.08)",
            }}
          >
            <h3>🚀 Routing Prompt...</h3>
            <p>Selecting the most efficient AI model...</p>
          </div>
        )}

        {error && (
          <div
            style={{
              marginTop: "20px",
              background: "#ffe5e5",
              color: "#c62828",
              padding: "20px",
              borderRadius: "10px",
              border: "1px solid #f5bcbc",
            }}
          >
            <strong>Error</strong>
            <br />
            {error}
          </div>
        )}

        {result && (
          <>
            <ModelBadge model={result.model} />

            <MetricsCard
              model={result.model}
              task={result.task}
              complexity={result.complexity}
              confidence={result.confidence}
              tokens={result.tokens}
            />

            <TokenChart tokens={result.tokens} />

            <ResponseCard response={result.response} />
          </>
        )}
      </div>
    </div>
  );
}