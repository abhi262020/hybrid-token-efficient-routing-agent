interface MetricsCardProps {
  model?: string;
  task?: string;
  complexity?: string | number;
  confidence?: number;
  tokens?: number;
}

export default function MetricsCard({
  model,
  task,
  complexity,
  confidence,
  tokens,
}: MetricsCardProps) {
  if (!model) return null;

  const confidencePercent = confidence
    ? Math.round(confidence * 100)
    : 0;

  return (
    <div
      style={{
        marginTop: "25px",
        padding: "20px",
        borderRadius: "12px",
        border: "1px solid #ddd",
        background: "#ffffff",
        boxShadow: "0 4px 10px rgba(0,0,0,0.08)",
      }}
    >
      <h2 style={{ marginBottom: "20px" }}>
        📊 Routing Metrics
      </h2>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
        }}
      >
        <tbody>
          <tr>
            <td><strong>Selected Model</strong></td>
            <td>
              <span
                style={{
                  background: "#2563eb",
                  color: "#fff",
                  padding: "4px 10px",
                  borderRadius: "20px",
                }}
              >
                {model}
              </span>
            </td>
          </tr>

          <tr>
            <td><strong>Task</strong></td>
            <td>{task}</td>
          </tr>

          <tr>
            <td><strong>Complexity</strong></td>
            <td>{complexity}</td>
          </tr>

          <tr>
            <td><strong>Confidence</strong></td>
            <td>
              {confidencePercent}%

              <div
                style={{
                  marginTop: "6px",
                  height: "8px",
                  background: "#e5e7eb",
                  borderRadius: "8px",
                  overflow: "hidden",
                }}
              >
                <div
                  style={{
                    width: `${confidencePercent}%`,
                    height: "100%",
                    background: "#22c55e",
                  }}
                />
              </div>
            </td>
          </tr>

          <tr>
            <td><strong>Token Usage</strong></td>
            <td>{tokens}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}