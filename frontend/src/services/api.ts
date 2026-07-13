export interface RouteRequest {
  prompt: string;
}

export interface RouteResponse {
  model: string;
  task: string;
  complexity: number;
  confidence: number;
  tokens: number;
  response: string;
}

// Render Backend
const API_BASE =
  "https://hybrid-token-efficient-routing-agent-j5ht.onrender.com";

export async function routePrompt(
  request: RouteRequest
): Promise<RouteResponse> {

  const response = await fetch(`${API_BASE}/route`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(error || "Failed to contact backend");
  }

  return await response.json();
}