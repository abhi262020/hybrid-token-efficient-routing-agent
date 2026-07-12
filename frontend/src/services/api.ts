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

const API_BASE = "http://127.0.0.1:8000";

export async function routePrompt(
  request: RouteRequest
): Promise<RouteResponse> {

  const response = await fetch(
    `${API_BASE}/route`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to contact backend");
  }

  return response.json();
}