"""Main CLI entry point."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="ftil",
        description="Federated Threat Intelligence Lakehouse CLI",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("serve", help="Start the API server")
    subparsers.add_parser("scan", help="Scan for IoCs in a file")
    subparsers.add_parser("enrich", help="Enrich IoCs with external data")
    subparsers.add_parser("analyze", help="Analyze threat data")
    subparsers.add_parser("quantum", help="Quantum operations")
    subparsers.add_parser("federated", help="Federated learning operations")
    subparsers.add_parser("export", help="Export threat data")
    subparsers.add_parser("import", help="Import threat data")

    args = parser.parse_args()

    if args.command == "serve":
        import uvicorn
        from src.api.app import create_app
        uvicorn.run(create_app(), host="0.0.0.0", port=8000)
    elif args.command == "scan":
        print("IoC scanning...")
    elif args.command == "enrich":
        print("IoC enrichment...")
    elif args.command == "analyze":
        print("Threat analysis...")
    elif args.command == "quantum":
        print("Quantum operations...")
    elif args.command == "federated":
        print("Federated learning...")
    elif args.command == "export":
        print("Data export...")
    elif args.command == "import":
        print("Data import...")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
