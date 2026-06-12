use regex::Regex;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IoCMatch {
    pub ioc_type: String,
    pub value: String,
    pub start: usize,
    pub end: usize,
}

pub fn parse_iocs(text: &str) -> Vec<IoCMatch> {
    let mut matches = Vec::new();

    let ip_regex = Regex::new(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    ).unwrap();

    let domain_regex = Regex::new(
        r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b"
    ).unwrap();

    let url_regex = Regex::new(
        r"https?://[^\s<>\"']+"
    ).unwrap();

    let md5_regex = Regex::new(r"\b[0-9a-fA-F]{32}\b").unwrap();
    let sha1_regex = Regex::new(r"\b[0-9a-fA-F]{40}\b").unwrap();
    let sha256_regex = Regex::new(r"\b[0-9a-fA-F]{64}\b").unwrap();

    let email_regex = Regex::new(
        r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    ).unwrap();

    let cve_regex = Regex::new(r"\bCVE-\d{4}-\d{4,}\b").unwrap();

    for m in ip_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "ip_address".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in url_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "url".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in sha256_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "file_hash_sha256".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in sha1_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "file_hash_sha1".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in md5_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "file_hash_md5".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in email_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "email_address".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in cve_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "cve".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    for m in domain_regex.find_iter(text) {
        matches.push(IoCMatch {
            ioc_type: "domain".to_string(),
            value: m.as_str().to_string(),
            start: m.start(),
            end: m.end(),
        });
    }

    matches.sort_by(|a, b| a.start.cmp(&b.start));
    matches.dedup_by(|a, b| a.start == b.start && a.end == b.end);
    matches
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_ip() {
        let text = "Malicious IP: 192.168.1.100 found in logs";
        let iocs = parse_iocs(text);
        assert!(!iocs.is_empty());
        assert!(iocs.iter().any(|i| i.ioc_type == "ip_address" && i.value == "192.168.1.100"));
    }

    #[test]
    fn test_parse_hash() {
        let text = "Hash: d41d8cd98f00b204e9800998ecf8427e";
        let iocs = parse_iocs(text);
        assert!(!iocs.is_empty());
        assert!(iocs.iter().any(|i| i.ioc_type == "file_hash_md5"));
    }

    #[test]
    fn test_parse_cve() {
        let text = "Vulnerability CVE-2024-12345 was exploited";
        let iocs = parse_iocs(text);
        assert!(!iocs.is_empty());
        assert!(iocs.iter().any(|i| i.ioc_type == "cve" && i.value == "CVE-2024-12345"));
    }
}
