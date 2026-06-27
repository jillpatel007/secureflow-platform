# SecureFlow Platform

A secure GitOps platform on local Kubernetes — built to demonstrate end-to-end
DevOps and DevSecOps practices on a single machine.

## What this is

A small two-service application wrapped in a complete, security-hardened delivery
pipeline: containerized, scanned, signed, deployed to a hardened Kubernetes cluster,
monitored at runtime, and triaged by an AI agent.

## Architecture (high level)

- **app/api** — backend API service
- **app/frontend** — frontend service
- **infra** — infrastructure as code (Terraform) for the local cluster
- **.github/workflows** — CI/CD pipeline with security gates
- **docs** — architecture notes and diagrams

## Tech stack

Docker · Kubernetes (kind) · Terraform · GitHub Actions · and a security
toolchain added across the build (SAST, SCA, secret scanning, image signing,
runtime detection) plus an AI-driven triage agent.

## Status

🚧 Under active development — built over three days as a hands-on upskilling project.
