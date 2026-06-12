use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StixBundle {
    #[serde(rename = "type")]
    pub bundle_type: String,
    pub id: String,
    pub spec_version: Option<String>,
    pub objects: Vec<serde_json::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ParsedStixObject {
    pub id: String,
    #[serde(rename = "type")]
    pub object_type: String,
    pub name: Option<String>,
    pub description: Option<String>,
    pub created: Option<String>,
    pub modified: Option<String>,
    pub labels: Vec<String>,
}

pub fn parse_stix_bundle(json_str: &str) -> Result<Vec<ParsedStixObject>, String> {
    let bundle: StixBundle = serde_json::from_str(json_str)
        .map_err(|e| format!("Failed to parse STIX bundle: {}", e))?;

    let mut parsed = Vec::new();

    for obj in &bundle.objects {
        let parsed_obj = ParsedStixObject {
            id: obj.get("id")
                .and_then(|v| v.as_str())
                .unwrap_or("unknown")
                .to_string(),
            object_type: obj.get("type")
                .and_then(|v| v.as_str())
                .unwrap_or("unknown")
                .to_string(),
            name: obj.get("name")
                .and_then(|v| v.as_str())
                .map(|s| s.to_string()),
            description: obj.get("description")
                .and_then(|v| v.as_str())
                .map(|s| s.to_string()),
            created: obj.get("created")
                .and_then(|v| v.as_str())
                .map(|s| s.to_string()),
            modified: obj.get("modified")
                .and_then(|v| v.as_str())
                .map(|s| s.to_string()),
            labels: obj.get("labels")
                .and_then(|v| v.as_array())
                .map(|arr| arr.iter()
                    .filter_map(|l| l.as_str().map(|s| s.to_string()))
                    .collect())
                .unwrap_or_default(),
        };
        parsed.push(parsed_obj);
    }

    Ok(parsed)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_indicator() {
        let json = r#"{
            "type": "bundle",
            "id": "bundle--test",
            "objects": [{
                "type": "indicator",
                "id": "indicator--1234",
                "name": "Test IP",
                "description": "A malicious IP",
                "created": "2024-01-01T00:00:00Z",
                "modified": "2024-01-01T00:00:00Z",
                "labels": ["malicious-activity"]
            }]
        }"#;
        let result = parse_stix_bundle(json).unwrap();
        assert_eq!(result.len(), 1);
        assert_eq!(result[0].name.as_deref(), Some("Test IP"));
    }
}
