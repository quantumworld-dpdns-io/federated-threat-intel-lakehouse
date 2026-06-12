export interface IoC {
  id: string;
  ioc_type: string;
  value: string;
  severity: string;
  confidence: string;
  tlp: string;
  tags: string[];
  source: string;
  description?: string;
  created_at: string;
}

export interface Campaign {
  id: string;
  name: string;
  description: string;
  severity: string;
  status: string;
  created_at: string;
}

export interface ThreatActor {
  id: string;
  name: string;
  description: string;
  country?: string;
  created_at: string;
}

export interface Vulnerability {
  id: string;
  cve_id: string;
  description: string;
  severity: string;
  cvss_score?: number;
}

export interface FederatedRound {
  round_number: number;
  status: string;
  loss?: number;
  accuracy?: number;
  participants: string[];
}

export interface QuantumResult {
  circuit_id: string;
  counts: Record<string, number>;
  execution_time_ms: number;
}
