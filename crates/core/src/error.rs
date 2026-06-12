use thiserror::Error;

#[derive(Error, Debug)]
pub enum FtilError {
    #[error("IoC not found: {0}")]
    IoCNotFound(String),

    #[error("Campaign not found: {0}")]
    CampaignNotFound(String),

    #[error("Threat actor not found: {0}")]
    ThreatActorNotFound(String),

    #[error("Vulnerability not found: {0}")]
    VulnerabilityNotFound(String),

    #[error("Storage error: {0}")]
    StorageError(String),

    #[error("Query error: {0}")]
    QueryError(String),

    #[error("Serialization error: {0}")]
    SerializationError(String),

    #[error("Authentication error: {0}")]
    AuthError(String),

    #[error("Authorization error: {0}")]
    Forbidden(String),

    #[error("Validation error: {0}")]
    ValidationError(String),

    #[error("Rate limit exceeded")]
    RateLimitExceeded,

    #[error("Service unavailable: {0}")]
    ServiceUnavailable(String),

    #[error("Internal error: {0}")]
    Internal(#[from] anyhow::Error),

    #[error("Arrow error: {0}")]
    ArrowError(#[from] arrow::error::ArrowError),

    #[error("JSON error: {0}")]
    JsonError(#[from] serde_json::Error),
}

pub type Result<T> = std::result::Result<T, FtilError>;

impl From<FtilError> for i32 {
    fn from(err: FtilError) -> Self {
        match err {
            FtilError::IoCNotFound(_) => 404,
            FtilError::CampaignNotFound(_) => 404,
            FtilError::ThreatActorNotFound(_) => 404,
            FtilError::VulnerabilityNotFound(_) => 404,
            FtilError::StorageError(_) => 500,
            FtilError::QueryError(_) => 400,
            FtilError::SerializationError(_) => 500,
            FtilError::AuthError(_) => 401,
            FtilError::Forbidden(_) => 403,
            FtilError::ValidationError(_) => 422,
            FtilError::RateLimitExceeded => 429,
            FtilError::ServiceUnavailable(_) => 503,
            FtilError::Internal(_) => 500,
            FtilError::ArrowError(_) => 500,
            FtilError::JsonError(_) => 400,
        }
    }
}
