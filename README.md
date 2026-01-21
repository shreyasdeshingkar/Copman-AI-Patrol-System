# CopMap AI Patrol System

An AI-driven system to assist police operations such as **patrolling, bandobast, and nakabandi** by analyzing visual and operational data and generating actionable insights.

---

## Candidate Details

- **Full Name:** <Shreyas Shriram Deshingkar>
- **Email:** <shreyasdeshingkar@gmail.com>
- **Phone:** <8625839941>
- **GitHub Repository:** <Public Repo URL>
- **Explanation Video:** <YouTube / Drive Link>
- **Resume:** <PDF Link or Attached in Email>

---

## 1. Problem Understanding

### 1.1 Background

Police operations require continuous situational awareness across large geographic areas.  
Current systems rely heavily on:
- Manual CCTV monitoring  
- Static dashboards  
- Human-written patrol reports  

This leads to:
- Delayed responses  
- Missed patterns  
- High cognitive load on officers  

---

### 1.2 Where AI Fits Realistically

This system uses AI as **decision support**, not decision replacement.

AI assists officers by:
- Monitoring crowd density
- Detecting objects such as people and vehicles
- Flagging abnormal patterns
- Generating concise patrol and bandobast summaries

**Final authority and enforcement always remain with human officers.**

---

### 1.3 What Is Automated vs Assisted

#### Automated
- Crowd density estimation  
- Object detection (people, vehicles, barricades)  
- Rule-based event detection  
- Patrol & bandobast summaries using LLM  

#### Assisted (Human-in-the-loop)
- Suspicious activity confirmation  
- Alert escalation decisions  
- Legal and enforcement actions  

---

### 1.4 Risk of False Positives

| Risk | Example | Mitigation |
|----|----|----|
| Crowd false alerts | Festival or rally | Time + persistence validation |
| Object misclassification | Police vehicle flagged | Object whitelisting |
| Behavior misinterpretation | Group discussion flagged | Multi-frame & duration checks |

No alert is escalated without **confidence thresholds and temporal validation**.

---

## 2. System Architecture

### 2.1 High-Level Flow

1. Camera feeds (CCTV / bodycam / drone)
2. Frame extraction using OpenCV
3. Computer vision models:
   - Object detection
   - Crowd analysis
4. Event engine applies rule-based logic
5. Backend validates and stores events
6. Alerts sent to CopMap platform
7. LLM + RAG generates patrol summaries

---

### 2.2 Architecture Diagram

```mermaid
flowchart TD
    A[CCTV / Camera Feed] --> B[Frame Extractor]
    B --> C[Object Detection]
    B --> D[Crowd Analysis]
    C --> E[Event Engine]
    D --> E
    E --> F[FastAPI Backend]
    F --> G[CopMap Dashboard]
    F --> H[Patrol Logs]
    H --> I[Vector DB]
    I --> J[LLM Summary Engine]
    J --> G


## 3. AI / ML Components

### 3.1 Computer Vision

The system uses computer vision models to analyze visual inputs from CCTV cameras, bodycams, or drones.

Implemented components:
- **Object Detection:** Detects people, vehicles, and barricades using a YOLO-style inference pipeline (mocked for demo purposes).
- **Crowd Density Analysis:** Counts detected persons per frame and applies rolling thresholds to identify crowd spikes.
- **Anomaly Detection:** Uses rule-based heuristics such as loitering duration and sudden crowd increase.

Rule-based logic is intentionally used alongside ML to ensure explainability and reduce false positives.

---

## 4. LLM & RAG (Mandatory)

### 4.1 Purpose of LLM Usage

Police officers require concise, actionable summaries rather than raw dashboards.  
The LLM is used to:
- Generate patrol and bandobast summaries
- Highlight repeated alerts and patterns
- Reduce manual reporting workload

---

### 4.2 Retrieval Augmented Generation (RAG) Design

To prevent hallucination and ensure grounded insights, the system uses RAG.

Flow:
1. Patrol logs, alerts, and events are embedded
2. Embeddings are stored in a vector database (FAISS)
3. Relevant historical context is retrieved
4. Context is passed to the LLM for summary generation

This ensures summaries are based on real operational data.

---

### 4.3 Cost-Aware Prompt Strategy

The system is designed to be cost-efficient:
- One LLM call per patrol shift (not per event)
- Short, focused prompts
- Offline embedding generation
- Support for open-source LLMs

---

## 5. Backend & API Integration

### 5.1 Backend Design

The backend is built using **FastAPI** and acts as the integration layer between AI components and the CopMap platform.

Responsibilities:
- Receive AI-detected events
- Validate alert severity
- Store patrol logs and alerts
- Expose APIs for dashboards and summaries

---

### 5.2 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/api/alerts` | Fetch active alerts |
| POST | `/api/patrol/summary` | Generate patrol summary |
| GET | `/api/cameras` | Fetch camera metadata |
| GET | `/` | Health check |

FastAPI automatically provides OpenAPI documentation and validation schemas.

---

## 6. Database Design

### 6.1 Schema Overview

The database is designed for auditability, traceability, and RAG compatibility.

```mermaid
erDiagram
CAMERA ||--o{ EVENT : generates
EVENT ||--o{ ALERT : triggers
PATROL_LOG ||--o{ ALERT : summarizes

CAMERA {
    string camera_id
    string location
    string zone
}
EVENT {
    string event_id
    string camera_id
    int people_count
    datetime timestamp
}
ALERT {
    string alert_id
    string type
    string severity
    float confidence
}
PATROL_LOG {
    string patrol_id
    string zone
    datetime start_time
    datetime end_time
}

## 7. Output Integration with CopMap

### 7.1 Alert Flow

The system integrates AI-generated outputs with the CopMap backend to ensure timely and actionable insights.

**Alert Generation Flow:**
1. AI models detect events from camera feeds (crowd spike, anomaly, object detection)
2. Backend validates confidence and severity
3. Alerts are generated with contextual metadata
4. Alerts are delivered to the CopMap dashboard or mobile application

---

### 7.2 Officer Consumption of Insights

Police officers and station users interact with the system through:

- Real-time alerts (severity-based)
- Zone-wise heatmaps for crowd and activity density
- End-of-shift AI-generated patrol and bandobast summaries
- Historical trend and pattern analysis for planning

The system is designed to reduce cognitive load and improve situational awareness.

---

## 8. What Was Implemented vs Skipped

### 8.1 Implemented Features

- Crowd density detection from camera feeds
- Object detection (people, vehicles, barricades)
- Rule-based suspicious activity detection
- FastAPI backend for AI output integration
- LLM-based patrol and bandobast summaries using RAG
- Vector database for historical context retrieval

---

### 8.2 Skipped Features (With Justification)

- **Facial recognition:** Avoided due to privacy, legal, and ethical concerns
- **Predictive policing models:** Risk of bias and ethical misuse
- **Fully autonomous alerting:** Human validation is required for safety and accountability

---

## 9. Environment Setup

### 9.1 Create Virtual Environment

```bash
python -m venv venv

### 9.2 Activate Virtual Environment

```bash
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

9.3 Install Dependencies
pip install -r requirements.txt

9.4 Run the Application
uvicorn backend.main:app --reload

Access the API documentation at:

http://127.0.0.1:8000/docs


## 10. Repository Structure

copmap-ai-patrol-system/
├── backend/
├── vision/
├── llm/
├── data/
├── diagrams/
├── postman/
├── samples/
├── requirements.txt
└── README.md


---

## 11. Sample Outputs

The repository includes sample outputs to demonstrate system behavior:

- JSON responses for generated alerts
- AI-generated patrol and bandobast summaries
- Crowd density and heatmap examples
- Postman collection for API testing

Refer to the `/samples` directory for details.

---

## 12. Conclusion

This project demonstrates a **practical, ethical, and scalable application of AI** for police patrolling and bandobast operations.  
The system prioritizes **decision support**, **human-in-the-loop validation**, and **cost-aware design**, making it suitable for real-world law enforcement deployments.
