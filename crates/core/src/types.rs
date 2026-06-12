use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum IoCType {
    IpAddress,
    Domain,
    Url,
    FileHashMd5,
    FileHashSha1,
    FileHashSha256,
    EmailAddress,
    Cve,
    Mutex,
    RegistryKey,
    FilePath,
    UserAgent,
    Certificate,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, PartialOrd, Ord)]
pub enum Severity {
    Info,
    Low,
    Medium,
    High,
    Critical,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum Tlp {
    White,
    Green,
    Amber,
    Red,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum Confidence {
    None,
    Low,
    Medium,
    High,
    Verified,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ThreatIndicator {
    pub id: Uuid,
    pub ioc_type: IoCType,
    pub value: String,
    pub severity: Severity,
    pub confidence: Confidence,
    pub tlp: Tlp,
    pub tags: Vec<String>,
    pub source: String,
    pub first_seen: DateTime<Utc>,
    pub last_seen: DateTime<Utc>,
    pub description: Option<String>,
    pub mitre_tactics: Vec<String>,
    pub mitre_techniques: Vec<String>,
    pub campaign_id: Option<Uuid>,
    pub threat_actor_id: Option<Uuid>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Campaign {
    pub id: Uuid,
    pub name: String,
    pub description: String,
    pub severity: Severity,
    pub status: CampaignStatus,
    pub threat_actor_id: Option<Uuid>,
    pub first_seen: DateTime<Utc>,
    pub last_seen: DateTime<Utc>,
    pub tags: Vec<String>,
    pub mitre_tactics: Vec<String>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum CampaignStatus {
    Active,
    Dormant,
    Closed,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ThreatActor {
    pub id: Uuid,
    pub name: String,
    pub aliases: Vec<String>,
    pub description: String,
    pub motivation: Option<String>,
    pub sophistication: Option<String>,
    pub resource_level: Option<String>,
    pub country: Option<String>,
    pub first_seen: DateTime<Utc>,
    pub last_seen: DateTime<Utc>,
    pub tags: Vec<String>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Vulnerability {
    pub id: Uuid,
    pub cve_id: String,
    pub description: String,
    pub severity: Severity,
    pub cvss_score: Option<f64>,
    pub affected_software: Vec<String>,
    pub exploit_available: bool,
    pub patch_available: bool,
    pub first_seen: DateTime<Utc>,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Enrichment {
    pub id: Uuid,
    pub ioc_id: Uuid,
    pub provider: EnrichmentProvider,
    pub raw_response: serde_json::Value,
    pub parsed_data: serde_json::Value,
    pub fetched_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum EnrichmentProvider {
    VirusTotal,
    Shodan,
    AbuseIPDB,
    OTX,
    GreyNoise,
    Censys,
    HybridAnalysis,
    MalwareBazaar,
    Custom(String),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FederatedNode {
    pub id: Uuid,
    pub name: String,
    pub organization: String,
    pub endpoint: String,
    pub status: NodeStatus,
    pub last_heartbeat: DateTime<Utc>,
    pub data_samples: u64,
    pub model_version: Option<String>,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum NodeStatus {
    Online,
    Offline,
    Training,
    Evaluating,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FederatedRound {
    pub round_number: u32,
    pub started_at: DateTime<Utc>,
    pub completed_at: Option<DateTime<Utc>>,
    pub participants: Vec<Uuid>,
    pub strategy: String,
    pub loss: Option<f64>,
    pub accuracy: Option<f64>,
    pub privacy_epsilon: Option<f64>,
    pub status: RoundStatus,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum RoundStatus {
    Pending,
    InProgress,
    Completed,
    Failed,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ModelUpdate {
    pub node_id: Uuid,
    pub round_number: u32,
    pub parameters: Vec<u8>,
    pub num_samples: u64,
    pub loss: f64,
    pub accuracy: Option<f64>,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuantumCircuit {
    pub id: Uuid,
    pub name: String,
    pub num_qubits: u32,
    pub depth: u32,
    pub gates: Vec<QuantumGate>,
    pub measurements: Vec<Measurement>,
    pub backend: String,
    pub shots: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuantumGate {
    pub name: String,
    pub qubits: Vec<u32>,
    pub parameters: Vec<f64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Measurement {
    pub qubit: u32,
    pub classical_bit: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuantumResult {
    pub circuit_id: Uuid,
    pub counts: std::collections::HashMap<String, u32>,
    pub metadata: serde_json::Value,
    pub execution_time_ms: u64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuantumKey {
    pub id: Uuid,
    pub key_material: Vec<u8>,
    pub algorithm: String,
    pub key_size: u32,
    pub created_at: DateTime<Utc>,
    pub expires_at: Option<DateTime<Utc>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AuditLog {
    pub id: Uuid,
    pub timestamp: DateTime<Utc>,
    pub actor: String,
    pub action: String,
    pub resource_type: String,
    pub resource_id: Uuid,
    pub details: serde_json::Value,
    pub ip_address: Option<String>,
}
