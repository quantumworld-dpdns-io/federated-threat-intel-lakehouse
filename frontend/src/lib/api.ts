const API_BASE = "/api/v1";

export async function fetchAPI<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...options?.headers },
    ...options,
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

export const api = {
  listIoCs: () => fetchAPI<any[]>("/iocs"),
  getIoC: (id: string) => fetchAPI<any>(`/iocs/${id}`),
  createIoC: (data: any) => fetchAPI<any>("/iocs", { method: "POST", body: JSON.stringify(data) }),
  listCampaigns: () => fetchAPI<any[]>("/campaigns"),
  healthCheck: () => fetchAPI<any>("/health"),
};
