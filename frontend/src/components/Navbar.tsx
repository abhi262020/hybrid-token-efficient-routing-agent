export default function Navbar() {
  return (
    <header
      style={{
        background: "linear-gradient(90deg, #1e3a8a, #2563eb)",
        color: "#ffffff",
        padding: "18px 30px",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 6px 15px rgba(0,0,0,0.15)",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          flexWrap: "wrap",
        }}
      >
        <div>
          <h1
            style={{
              margin: 0,
              fontSize: "28px",
            }}
          >
            🚀 Hybrid Token-Efficient Routing Agent
          </h1>

          <p
            style={{
              marginTop: "8px",
              opacity: 0.9,
              fontSize: "15px",
            }}
          >
            Intelligent AI Model Selection using Fireworks AI & AMD
          </p>
        </div>

        <div
          style={{
            background: "rgba(255,255,255,0.15)",
            padding: "10px 18px",
            borderRadius: "25px",
            fontWeight: "bold",
          }}
        >
          AMD Developer Hackathon 2026
        </div>
      </div>
    </header>
  );
}