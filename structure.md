# MLOps Repository Structure

Overview of the workspace projects categorized into **End-to-End Production Projects** and **Tutorials & Standalone Proofs-of-Concept**[cite: 1].

---

## 1. End-to-End Projects

Production-grade pipelines covering complete machine learning and data engineering lifecycle orchestration, versioning, and cloud deployments[cite: 1].

* **`pipeline/ml-pipeline`**
  * **Scope:** End-to-end MLOps production pipeline[cite: 1].
  * **Stack:** DVC (Data Version Control), DagsHub (Remote Storage & Collaboration), and MLflow (Experiment Tracking & Model Registry)[cite: 1].
  * **Purpose:** Manages data versioning, reproducible pipeline execution, and model lifecycle tracking from raw input to final artifact[cite: 1].

* **`airflow-etl-pipeline`**
  * **Scope:** End-to-end Airflow ETL pipeline with Postgres and API integration.
  * **Stack:** Apache Airflow, PostgreSQL, REST APIs, Astro Cloud, and AWS.
  * **Purpose:** Orchestrates production data extraction via APIs, transformation workflows, and loading into PostgreSQL with deployment on Astro Cloud and AWS infrastructure.

### `DockerImage`

- **Scope:** Containerized application development and CI/CD pipeline.
- **Stack:** Python, Flask, Docker, Docker Hub, GitHub Actions, and pytest.
- **Purpose:** Demonstrates the software delivery lifecycle from application development and automated testing to Docker image creation, containerization, and automated publishing through a CI/CD pipeline.
- **Architecture:** The Flask application is packaged as a Docker image and published to a container registry. GitHub Actions automates testing and image building, providing the foundation for promoting the same application artifact across **DEV → UAT → PROD** environments.
- **Key Concepts:** Dockerfiles, container images, container portability, automated testing, CI/CD workflows, container registries, artifact promotion, and environment-based deployment.
---

## 2. Tutorials & Proof of Concepts

Isolated modules and walkthroughs focused on learning individual tools and cloud integrations[cite: 1].

* **`airflow-astro`**
  * **Scope:** Apache Airflow fundamentals with Astronomer Astro CLI[cite: 1].
  * **Focus:** Workflow orchestration, DAG authoring, task dependencies, and TaskFlow API execution in containerized environments[cite: 1].

* **`mlflowbasics`**
  * **Scope:** Core MLflow tracking introductory module[cite: 1].
  * **Focus:** Local experiment tracking, metric/parameter logging, and artifact generation[cite: 1].

* **`aws_dsproject`**
  * **Scope:** Cloud experiment tracking with AWS[cite: 1].
  * **Focus:** Connecting MLflow runs to remote AWS infrastructure and cloud storage backends[cite: 1].