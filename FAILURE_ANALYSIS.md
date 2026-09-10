# Failure Analysis

## Failure 1: Deliberate Test Failure (Part 6)

**Symptom:** CI pipeline fails on the `test` job. pytest reports `AssertionError`.

**Root Cause:** The health endpoint test was intentionally modified to assert an incorrect value:
```
assert data["status"] == "wrong"
```
The actual endpoint returns `"healthy"`, so the assertion always fails.

**Evidence:** GitHub Actions workflow run shows failed test step with output:
```
FAILED tests/test_app.py::test_health - assert "healthy" == "wrong"
```

**Correction:** Changed the assertion back to the correct value:
```
assert data["status"] == "healthy"
```

---

## Failure 2: GHCR Push Denied (Part 15)

**Symptom:** Release workflow completed tests and Docker build successfully, but failed on the "Build and push Docker image" step with:
```
ERROR: denied: permission_denied: write_package
```

**Root Cause:** The default `GITHUB_TOKEN` did not have sufficient permissions to push to GitHub Container Registry. The repository's GHCR package permissions were not configured for the automatic token.

**Evidence:** GitHub Actions release workflow logs show the push step failing after a successful build.

**Correction:** Created a Personal Access Token with `write:packages` scope, stored it as a repository secret (`GHCR_TOKEN`), and updated the release workflow to use this secret instead of `GITHUB_TOKEN` for registry authentication.
