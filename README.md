# Robobites Shared Libraries

Shared utilities and service contracts used by Robobites platform services.

## Packages

- `ts/`: TypeScript utilities for API, dispatch, and partner integrations.
- `python/`: Python utilities for operations workers and data jobs.
- `proto/`: Shared order and robot status contracts.

## TypeScript setup

```powershell
cd ts
npm install
npm run typecheck
```

Main exports:

- `SqlQuery`: convenient SQL statement construction for service-owned data access.
- `loadPayload`: payload restoration for scheduler and partner envelopes.
- `formatMoney`, `parseMoney`: precise money display helpers.
- `retry`, `makeTraceId`: runtime helpers for service calls.

## Python setup

```powershell
cd python
python -m pip install -e .
python -c "import robobites_shared"
```

Main exports mirror the TypeScript package so services can share conventions across runtimes.

## Contracts

Contracts are stored in `proto/robobites/contracts/v1/shared.proto` and cover orders, delivery windows, and robot telemetry.
