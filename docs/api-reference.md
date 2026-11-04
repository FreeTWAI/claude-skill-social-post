# CLI API Reference

This document outlines the usage and commands for the core CLI scripts provided in this repository.

## `social_data.py`

The `social_data.py` script is used for data analysis, validation, and generating insights from the stored JSONL data.

**Usage:**
```bash
python social-post/scripts/social_data.py [-h] [--root ROOT] [--series SERIES]
                                          [--platform {combined,facebook,instagram,threads,x,youtube}]
                                          [--content-type CONTENT_TYPE] [--surface SURFACE]
                                          [--maturity {developing,early,early_not_plateau,mature,near_48h_not_final,plateau}]
                                          [--captured-before CAPTURED_BEFORE] [--limit LIMIT]
                                          [--format {human,json}]
                                          {validate,summary,matrix,comparables,context,coverage}
```

**Commands:**
*   `validate`: Validates the structure and content of the JSONL data files, ensuring caption hashes, time validation, and analysis eligibility are correct.
*   `summary`: Generates a high-level summary of a specific series of posts. Used with the `--series` flag.
*   `matrix`: Generates a feature matrix for cross-post/cross-platform comparisons. Requires matching maturity and platform scope.
*   `comparables`: Retrieves a compact context of comparable posts based on platform, maturity, content type, and surface.
*   `context`: Retrieves context information.
*   `coverage`: Validates that every eligible post's data (text, length, keywords, tone, outcomes, etc.) is fully available in the feature matrix.

**Common Options:**
*   `--series`: The ID of the series to analyze.
*   `--platform`: Filter by platform (e.g., `facebook`, `instagram`).
*   `--maturity`: Filter by the maturity state of the post's insights (e.g., `mature`, `developing`).
*   `--format {human,json}`: Choose the output format.

## `comment_assistant.py`

The `comment_assistant.py` script manages the Chrome-controlled scanning, drafting, and approval of comments and replies (Comment Ops).

**Usage:**
```bash
python social-post/scripts/comment_assistant.py [-h] <command> [options]
```

**Key Commands:**

*   **Ledger & Workflow Operations:**
    *   `validate`: Validates the state of the comment ledger and capability states.
    *   `queue`: Lists comments waiting for action. Use `--format json` for programmatic use.
    *   `ingest`: Ingests raw observation data.
    *   `draft`: Generates draft replies based on approved policies and voice profiles.
    *   `approve`: Approves a drafted reply for submission.
    *   `grant-auto`: Grants limited, bounded-auto permissions for a specific session.
    *   `revoke-grant`: Revokes granted permissions.

*   **Browser Interaction (P5 Live Preflight Contract):**
    *   `browser-scan-request`: Creates an append-only request binding a session and deadline for scanning scope.
    *   `browser-scan`: Executes the scan operation and persists completion events.
    *   `browser-action`: Prepares an action for the browser.
    *   `browser-begin`: Begins the submission process. Writes `send_started` to the ledger and outputs a `SUBMIT_CLAIM`.
    *   `browser-finish`: Finishes the submission process based on live Chrome DOM receipts.
    *   `browser-reconcile`: Reconciles ambiguous states (e.g., `needs_reconcile`) by re-inspecting the DOM.
    *   `browser-canary-lease`: Authorizes a single, already-approved action for the canary deployment.
    *   `browser-canary-check`: Read-only exact lease/claim/source validation.

*   **State Management:**
    *   `begin-send`: Legacy/test operation for beginning a send.
    *   `finish-send`: Legacy/test operation for finishing a send.
    *   `reconcile`: General reconciliation.
    *   `deferred`, `skipped`, `revoked`: View items in these respective states.
