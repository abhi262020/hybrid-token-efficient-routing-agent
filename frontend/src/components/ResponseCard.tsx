import { useState } from "react";

interface ResponseCardProps {
  response?: string;
}

export default function ResponseCard({
  response,
}: ResponseCardProps) {
  const [copied, setCopied] = useState(false);

  if (!response) return null;

  const copyResponse = async () => {
    await navigator.clipboard.writeText(response);
    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  const words = response.trim().split(/\s+/).length;

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "24px",
        marginTop: "25px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "15px",
          flexWrap: "wrap",
        }}
      >
        <h2
          style={{
            margin: 0,
            color: "#1e3a8a",
          }}
        >
          🤖 AI Response
        </h2>

        <button
          onClick={copyResponse}
          style={{
            background: "#2563eb",
            color: "#fff",
            border: "none",
            padding: "8px 16px",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          {copied ? "✅ Copied" : "📋 Copy"}
        </button>
      </div>

      <div
        style={{
          background: "#f8fafc",
          border: "1px solid #e5e7eb",
          borderRadius: "10px",
          padding: "18px",
          maxHeight: "450px",
          overflowY: "auto",
          whiteSpace: "pre-wrap",
          lineHeight: 1.7,
          fontSize: "15px",
        }}
      >
        {response}
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginTop: "15px",
          fontSize: "14px",
          color: "#666",
          flexWrap: "wrap",
        }}
      >
        <span>📝 {words} words</span>

        <span>
          ⏱ {new Date().toLocaleTimeString()}
        </span>
      </div>
    </div>
  );
}