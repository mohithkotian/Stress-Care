<div align="center">

# 🧠 StressCare
### Passive Caregiver Support & Burnout Detection System

🏆 **2nd Place Winner — SRISHTI Hackathon 2026**  
⏱ Built in 36 Hours  
👥 Team 808 Imperium

[![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)](https://flutter.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)

**Non-intrusive stress detection for informal caregivers — without requiring explicit disclosure.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

</div>

---

# 🏆 SRISHTI Hackathon 2026 — 2nd Prize

> Team **808 Imperium** secured **2nd Place** at **SRISHTI Hackathon 2026**  
> under **Theme 03 — Tech for Healthcare & Well-Being**.

Built during a 36-hour innovation sprint focused on solving caregiver burnout and emotional wellness challenges using AI-powered passive stress detection.

🔗 **Repository:**  
https://github.com/SRISHTI-HACKATHON-2026/team-112

---

# 📸 Hackathon Journey

## 🏅 Official Winning Moment

<p align="center">
  <img src="/pic/5.jpeg" width="850"/>
</p>

<p align="center">
Team 808 Imperium receiving the <b>2nd Prize Award</b> at SRISHTI Hackathon 2026.
</p>

---

## 🎉 Team Celebration

| Team Victory | Celebration Moment |
|---|---|
| ![](/pic/1.jpeg) | ![](/pic/2.jpeg) |

<p align="center">
Celebrating after presenting our solution and securing the win.
</p>

---

## 💻 During the Hackathon

<p align="center">
  <img src="/pic/3.jpeg" width="850"/>
</p>

<p align="center">
Focused development and testing during the 36-hour hackathon sprint.
</p>

---

## 👥 Final Stage Moments

| Stage Ceremony | Team Recognition |
|---|---|
| ![](/pic/4.jpeg) | ![](/pic/6.jpeg) |

---

## 🚀 Post-Win Energy

<p align="center">
  <img src="/pic/7.jpeg" width="850"/>
</p>

<p align="center">
The moment after realizing all the hard work paid off.
</p>

---

# ❓ Problem Statement

Informal caregivers often experience emotional exhaustion and burnout while caring for loved ones.

Most existing mental health solutions rely heavily on explicit self-reporting, which many caregivers avoid because of:
- stigma,
- emotional fatigue,
- denial,
- or fear of judgment.

The challenge was to build a system that could:
- detect stress passively,
- respect user privacy,
- avoid medicalized interaction,
- and provide gentle support without overwhelming the user.

---

# 💡 Solution

StressCare is an AI-powered caregiver wellness assistant that passively detects stress patterns through natural conversations and voice interactions.

Instead of forcing users to complete mental health questionnaires, the system quietly analyzes behavioral and emotional indicators to provide:

- burnout detection,
- emotional wellness tracking,
- gentle support nudges,
- and localized caregiver resources.

The platform is designed to feel supportive — not clinical.

---

# ✨ Features

### 🧠 Passive Stress Detection
- Sentiment and stress analysis using NLP
- Voice stress detection via waveform analysis
- Invisible behavioral monitoring without explicit disclosure

### 🎙️ Invisible Journaling
- Natural conversations instead of clinical forms
- No mental health labeling
- Silent pattern tracking across sessions

### 💬 Gentle Support Nudges
- Rest reminders
- Delegation suggestions
- Emotional wellness prompts
- Non-alarming, human-centered interactions

### 🌍 Localized Resource Suggestions
- Region-specific caregiver support resources
- Community groups and helplines
- Nearby support assistance recommendations

### 🔒 Privacy First
- PII masking before AI processing
- Ghost Mode for zero data storage
- PIN-protected session history
- Raw voice data never stored

---

# 🏗️ System Architecture

```text
User Input (Voice Log / Text Chat)
         |
         v
  +------------------+
  |   PII Masking    |
  +--------+---------+
           |
           v
  +------------------+
  |  NLP + Audio AI  |
  +--------+---------+
           |
           v
  +------------------+
  |  Stress Scoring  |
  +--------+---------+
           |
           v
  +--------------------------------------+
  |  Support Engine                      |
  |  Gentle Nudges / Resources / Alerts  |
  +--------------------------------------+

## Backend configuration

The backend reads its configuration from environment variables. For local development, copy `backend/.env.example` to `backend/.env` and fill in the values; `backend/.env` is intentionally ignored by Git.

Required operational steps after the previous public exposure:

1. Revoke and regenerate the exposed Gemini API key.
2. Rotate the MongoDB database user password and update the connection string. Review MongoDB audit logs and restrict the user to the minimum required database privileges.
3. Generate a new random `SECRET_KEY` of at least 32 characters. Existing sessions signed with the old key must be treated as invalid.
4. Rotate the Google OAuth client secret if it was active outside this repository.

The backend now rejects missing or weak JWT secrets, verifies Google ID tokens against the configured OAuth client, and never accepts test or fabricated authentication tokens.
