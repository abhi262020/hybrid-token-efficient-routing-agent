interface ModelBadgeProps {
  model?: string;
}

export default function ModelBadge({
  model,
}: ModelBadgeProps) {
  if (!model) return null;

  const getColor = () => {
    if (model.toLowerCase().includes("llama"))
      return "#2563eb";

    if (model.toLowerCase().includes("qwen"))
      return "#10b981";

    if (model.toLowerCase().includes("deepseek"))
      return "#8b5cf6";

    return "#6b7280";
  };

  return (
    <div
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "8px",
        background: getColor(),
        color: "#fff",
        padding: "8px 18px",
        borderRadius: "25px",
        fontWeight: "bold",
        marginTop: "15px",
      }}
    >
      🤖 {model}
    </div>
  );
}