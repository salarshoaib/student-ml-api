# Traceability Documentation

## Version 1.1.0 — Full Chain

| Step | Value |
|------|-------|
| Pull Request Number | #3 |
| Merge Commit SHA | bdb2d476fe1599f105a54b6c460118c7a1a9f22a |
| Git Tag | v1.1.0 |
| Docker Image Tag | student-ml-api:1.1.0 |
| Docker Image Digest | sha256:020d1776e99f49b5b8e5b4001eedf57e1bb3e82fe7cef2bcc1a81202b6347ab0 |

## Version 1.0.0 — Full Chain

| Step | Value |
|------|-------|
| Pull Request Number | #1 |
| Merge Commit SHA | ef00246fc572cc90bcdaf32888899291389f001c |
| Git Tag | v1.0.0 |
| Docker Image Tag | student-ml-api:1.0.0 |
| Docker Image Digest | sha256:b8fd489d5b5c61bc3a5008d99098d1c2de27925821c6f9e4ced12a9e09ca3003 |

## How to Verify

1. Check PR: `gh pr view <number>`
2. Check merge commit: `git log --merges --oneline`
3. Check tag: `git tag -l` and `git show v1.1.0`
4. Check image digest: `docker inspect ghcr.io/salarshoaib/student-ml-api:1.1.0 --format='{{index .RepoDigests 0}}'`
