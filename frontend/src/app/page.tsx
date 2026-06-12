export default function Home() {
  return (
    <main>
      <h1>Federated Threat Intelligence Lakehouse</h1>
      <p>Privacy-preserving CTI contribution using federated learning and Apache Iceberg/Trino</p>
      <div>
        <h2>Dashboard</h2>
        <ul>
          <li><a href="/threats">Threat Indicators</a></li>
          <li><a href="/campaigns">Campaigns</a></li>
          <li><a href="/federated">Federated Learning</a></li>
          <li><a href="/quantum">Quantum Module</a></li>
          <li><a href="/analytics">Analytics</a></li>
        </ul>
      </div>
    </main>
  );
}
