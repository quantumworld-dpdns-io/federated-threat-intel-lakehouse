"use client";

interface Column<T> {
  key: string;
  header: string;
  render?: (value: any, row: T) => React.ReactNode;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
}

export default function DataTable<T extends Record<string, any>>({ columns, data }: DataTableProps<T>) {
  return (
    <table>
      <thead>
        <tr>{columns.map(c => <th key={c.key}>{c.header}</th>)}</tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>{columns.map(c => (
            <td key={c.key}>{c.render ? c.render(row[c.key], row) : row[c.key]}</td>
          ))}</tr>
        ))}
      </tbody>
    </table>
  );
}
