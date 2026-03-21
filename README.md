# LinkNayan

> **WORK IN PROGRESS** - This project is currently under active development as part of my AI learning journey.

**Your bridge to mental health support in the Philippines**

---

## What is this?

LinkNayan is an AI-powered CLI tool I'm building to help Filipinos find mental health resources. Instead of Googling and getting overwhelmed, users can describe their situation in plain language and get matched with appropriate resources like crisis hotlines, therapists, and support groups.


---

## Important Disclaimer

This is **NOT** medical advice or a replacement for professional help. It's an information tool to help people find resources. Always consult mental health professionals for actual treatment.

**Crisis?** Call **NCMH: 0917-899-8727** or **Emergency: 911**

---

## Current Status

**Phase:** Building core features (Active development)

**What works:**
- Project setup with UV
- OpenRouter AI integration (config.py done)
- Resource database structure (hotlines, professionals, resources JSON files)
- Resource loader (resources.py done)
- Crisis detection logic (detect_crisis() done and tested)

**In progress:**
- AI situation analysis (call_ai() and analyze_situation() in ai.py)
- Currently blocked by OpenRouter free model availability issues — free models are either rate-limited or returning 404 errors. Actively testing alternative free models.

**Not started yet:**
- CLI interface (main.py)
- Web app (Streamlit)

Honest note: Progress has been slow — this is a solo project built while studying full-time as a first-year CS student. Current blocker is finding a stable free AI model through OpenRouter that works consistently without rate limits or endpoint errors. Building it properly matters more than building it fast.

---

## Tech Stack

- **Python 3.11+**
- **UV** - Fast package manager (replaces pip/venv)
- **OpenRouter** - Free AI models (model under evaluation due to availability issues)
- **OpenAI SDK** - API integration

---

## Installation (for testing)

Prerequisites:
- Python 3.11+
- UV package manager
```bash
# Clone repo
git clone https://github.com/CyberJeshz/LinkNayan.git
cd linknayan

# Install UV (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup project
uv sync

# Add your OpenRouter API key
echo "OPENROUTER_API_KEY=your-key-here" > .env

# Run (when ready)
uv run linknayan
```

Get free API key: https://openrouter.ai/keys

---

## Project Structure
```
linknayan/
├── src/linknayan/
│   ├── config.py      # Done
│   ├── resources.py   # Done
│   ├── ai.py          # In progress
│   ├── main.py        # Not started
│   └── __init__.py
├── data/
│   ├── hotlines.json       # Done
│   ├── professionals.json  # Done
│   └── resources.json      # Done
├── pyproject.toml
└── README.md
```

---

## Known Blockers

- **OpenRouter free model instability** — The primary free model (openai/gpt-oss-120b:free) is rate-limited upstream. Alternative free models are returning 404 errors. Currently evaluating stable free model options before continuing with analyze_situation().
- Resource database needs more verified Philippine-specific entries before launch.

---

## What I'm Learning

This is my first AI project as a first-year CS student. Through this I'm learning:

- Working with AI APIs (OpenRouter)
- Modern Python tooling (UV)
- JSON data management
- Python project structure
- Prompt engineering
- Building ethical AI (crisis detection, safety)
- Debugging API integration issues in production
- CLI design and user experience

---

## Goals

**Immediate (this week):**
- Resolve OpenRouter model availability issue
- Finish ai.py (analyze_situation)
- Build main.py (CLI interface)
- Get working end-to-end prototype

**Short-term:**
- Convert CLI to Streamlit web app
- Deploy to public URL
- User testing with 5-10 people

**Long-term:**
- Tagalog language support
- Location-based filtering
- Messenger bot integration
- Partnership with mental health orgs

---

## Crisis Resources

If you or someone needs help NOW, don't wait for this tool:

- NCMH Crisis Hotline: 0917-899-8727 (24/7, free)
- Emergency: 911
- In Touch Crisis Line: (02) 8893-7603

---

## Contact

**Developer:** Jezreel E. Guillermo
**GitHub:** [@CyberJeshz](https://github.com/CyberJeshz/LinkNayan.git)
**Email:** jezreeleguillermo@gmail.com

---

## License

MIT License - feel free to learn from or fork this code!

---

Solo project. Built slowly but built properly.

Made with love by CyberJeshz
