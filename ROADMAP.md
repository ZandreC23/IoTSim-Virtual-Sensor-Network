# Roadmap

## Current State
The IoTSim Virtual Sensor Network Simulator is feature-complete with:
- Sensor simulation (temperature, humidity, water flow)
- REST API with FastAPI
- In-memory repository layer
- CI/CD pipeline with GitHub Actions

## Planned Features

### Short Term
| Feature | Description | Difficulty |
|---------|-------------|------------|
| Add GPS sensor | Simulate GPS location data | Easy |
| Add pressure sensor | Simulate atmospheric pressure readings | Easy |
| Improve anomaly detection | Add configurable thresholds per sensor type | Medium |
| Add pagination to GET /api/readings | Return readings in pages instead of all at once | Easy |

### Medium Term
| Feature | Description | Difficulty |
|---------|-------------|------------|
| Database storage | Replace in-memory storage with SQLite or PostgreSQL | Medium |
| Redis caching | Cache frequent API responses using Redis | Medium |
| Authentication | Add API key or JWT authentication to endpoints | Medium |
| Dashboard UI | Build a web dashboard to visualize sensor data | Hard |

### Long Term
| Feature | Description | Difficulty |
|---------|-------------|------------|
| MQTT support | Allow real IoT devices to publish data via MQTT | Hard |
| Docker support | Containerize the API for easy deployment | Medium |
| Cloud deployment | Deploy to AWS or Azure | Hard |

## How to Contribute
Pick any feature from the table above and open an issue. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.