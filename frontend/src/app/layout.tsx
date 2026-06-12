export const metadata = {
  title: "Federated Threat Intelligence Lakehouse",
  description: "Privacy-preserving CTI for SMEs",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
