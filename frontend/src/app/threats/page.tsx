"use client";
import { useEffect, useState } from "react";

export default function ThreatsPage() {
  const [threats, setThreats] = useState([]);
  useEffect(() => {
    fetch("/api/v1/iocs").then(r => r.json()).then(setThreats).catch(() => {});
  }, []);
  return (
    <main>
      <h1>Threat Indicators</h1>
      <table>
        <thead>
          <tr><th>Type</th><th>Value</th><th>Severity</th><th>Source</th></tr>
        </thead>
        <tbody>
          {threats.map((t: any) => (
            <tr key={t.id}><td>{t.ioc_type}</td><td>{t.value}</td><td>{t.severity}</td><td>{t.source}</td></tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
