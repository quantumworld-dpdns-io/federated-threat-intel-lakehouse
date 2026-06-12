# Contributing

## Development Setup

```bash
# Install dependencies
make install-dev

# Run linting
make lint

# Run tests
make test

# Run all checks
make all
```

## Code Style

- Python: Ruff (line length 120)
- Rust: rustfmt + clippy
- TypeScript: ESLint + Prettier

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `test:` adding tests
- `chore:` maintenance

## Pull Request Process

1. Create feature branch from `main`
2. Make changes with tests
3. Run `make all` to verify
4. Open PR with description
5. Wait for CI to pass
6. Request review
