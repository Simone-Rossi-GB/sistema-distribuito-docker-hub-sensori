# Smart City Hub — Distributed IoT Sensor Platform

A microservices architecture for collecting and analyzing real-time data from IoT environmental sensors in a smart city scenario.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=eclipse-mosquitto&logoColor=white)

---

## Architecture

```
Browser :80 ──► Caddy (API Gateway + Load Balancer)
                    ├──► app1:5000 (Flask)
                    └──► app2:5000 (Flask)
                              │
                         Forward Auth
                         └──► Authelia:9091
                              │
                         EMQX:1883 (MQTT Broker)
                              │
                         Worker (MQTT Subscriber)
```

| Component | Role |
|-----------|------|
| **Caddy** | Reverse proxy, load balancer, API gateway |
| **Flask** (×2 replicas) | Web app and REST API for sensor data |
| **EMQX** | MQTT broker for async IoT communication |
| **Worker** | Python microservice that processes MQTT messages |
| **Authelia** | Forward authentication to protect sensitive routes |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white)

---

## Quick Start

```bash
# Start all services (rebuilds images)
docker compose up --build

# Stop all services
docker compose down

# Full reset (removes volumes)
docker compose down -v

# View logs for a specific service
docker compose logs -f worker
```

### Send a test sensor reading

```bash
curl -X POST http://localhost/publish \
  -H "Content-Type: application/json" \
  -d '{"sensore": "temperatura", "valore": 22.5}'
```

---

## Test Credentials

| Service | Username | Password |
|---------|----------|----------|
| Authelia | `studente` | `password123` |
| EMQX Dashboard | `admin` | `public` |

---

## Exposed Ports

| Service | Port | URL |
|---------|------|-----|
| Caddy (web app) | 80 | http://localhost |
| EMQX Dashboard | 18083 | http://localhost:18083 |
| Authelia | 9091 | http://localhost:9091 |

---

## Project context

School project at IIS B. Castelli, Brescia.  
The assignment covered load balancing, asynchronous MQTT communication, microservice architecture, and forward authentication — all running locally in Docker.

**Author:** Simone Rossi
