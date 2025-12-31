# YouTube Comment Opportunity Finder AI Agent

## Project Overview
An AI-powered agent that monitors YouTube channels, cleans comment data using the **IBM Data Prep Kit**, and uses **Agentic AI** logic to identify engagement opportunities.

## Tech Stack
- **Language:** Python
- **Model:** Google Flan-T5 (via Hugging Face)
- **Data Engineering:** IBM Data Prep Kit (DPK)
- **Automation:** Relay.app

## Project Phases
1. **Fundamentals:** Built the reasoning loop (Perception -> Reasoning -> Action).
2. **Data Prep:** Implemented hashing-based deduplication and noise filtering.
3. **Application:** Integrated with Relay.app for automated notifications.
To make the agent functional, I integrated the pipeline with Relay.app.
- **Workflow:** Python -> Google Sheets -> Relay.app -> Gmail.
- **Human-in-the-loop:** The agent drafts replies but waits for my approval via email before finalizing.
