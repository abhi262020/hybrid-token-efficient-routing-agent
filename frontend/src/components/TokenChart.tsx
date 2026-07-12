interface TokenChartProps {
  tokens?: number;
}

export default function TokenChart({
  tokens,
}: TokenChartProps) {
  if (tokens === undefined) return null;

  const percentage = Math.min((tokens / 4096) * 100, 100);

  let color = "#22c55e";

  if (percentage > 70)
    color = "#f97316";

  if (percentage > 90)
    color = "#ef4444";

  return (
    <div
      style={{
        marginTop: "25px",
        padding: "20px",
        background: "#fff",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,.08)",
      }}
    >
      <h2>🪙 Token Usage</h2>

      <div
        style={{
          marginTop: "15px",
          height: "18px",
          background: "#e5e7eb",
          borderRadius: "20px",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: `${percentage}%`,
            height: "100%",
            background: color,
            transition: "0.4s",
          }}
        />
      </div>

      <div
        style={{
          marginTop: "10px",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        <span>
          <strong>{tokens}</strong> Tokens
        </span>

        <span>{percentage.toFixed(1)}%</span>
      </div>

      <small
        style={{
          color: "#666",
        }}
      >
        Maximum Context: 4096 Tokens
      </small>
    </div>
  );
}