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

// Local development uses localhost.
// Production uses the Vercel environment variable.
const API_BASE =
  import.meta.env.VITE_API_URL ||
  "http://127.0.0.1:8000";

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
    const message = await response.text();
    throw new Error(message || "Failed to contact backend");
  }

  return await response.json();
}