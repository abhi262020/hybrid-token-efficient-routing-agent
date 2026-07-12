import { useState } from "react";

interface PromptBoxProps {
  onSubmit: (prompt: string) => void;
  loading: boolean;
}

export default function PromptBox({
  onSubmit,
  loading,
}: PromptBoxProps) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = () => {
    if (!prompt.trim()) return;

    onSubmit(prompt);
  };

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "24px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        marginBottom: "25px",
      }}
    >
      <h2
        style={{
          marginTop: 0,
          color: "#1e3a8a",
        }}
      >
        💬 Enter Your Prompt
      </h2>

      <p
        style={{
          color: "#666",
          marginBottom: "15px",
        }}
      >
        Type any question below. The routing agent will automatically choose
        the most efficient AI model.
      </p>

      <textarea
        rows={7}
        value={prompt}
        placeholder="Example: Explain quantum computing in simple terms..."
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={(e) => {
          if (e.ctrlKey && e.key === "Enter") {
            handleSubmit();
          }
        }}
        style={{
          width: "100%",
          padding: "15px",
          fontSize: "16px",
          borderRadius: "10px",
          border: "1px solid #d1d5db",
          resize: "vertical",
          outline: "none",
          boxSizing: "border-box",
        }}
      />

      <div
        style={{
          marginTop: "10px",
          fontSize: "14px",
          color: "#777",
        }}
      >
        💡 Press <b>Ctrl + Enter</b> to submit.
      </div>

      <button
        onClick={handleSubmit}
        disabled={loading}
        style={{
          marginTop: "20px",
          background: "#2563eb",
          color: "#fff",
          border: "none",
          borderRadius: "8px",
          padding: "12px 28px",
          fontSize: "16px",
          cursor: loading ? "not-allowed" : "pointer",
          opacity: loading ? 0.7 : 1,
        }}
      >
        {loading ? "🔄 Routing Prompt..." : "🚀 Route Prompt"}
      </button>

      <div
        style={{
          marginTop: "20px",
          fontSize: "14px",
          color: "#555",
        }}
      >
        <b>Example Prompts</b>

        <ul style={{ marginTop: "8px" }}>
          <li>Explain recursion with an example.</li>
          <li>Write a Python REST API.</li>
          <li>Summarize this research paper.</li>
          <li>Generate SQL for this database schema.</li>
          <li>Explain AI to a 10-year-old.</li>
        </ul>
      </div>
    </div>
  );
}