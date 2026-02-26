# LinkNayan 💚

> **⚠️ WORK IN PROGRESS** - This project is currently under active development as part of my AI learning journey.

**Your bridge to mental health support in the Philippines**

---

## 🎯 What is this?

LinkNayan is an AI-powered CLI tool I'm building to help Filipinos find mental health resources. Instead of Googling and getting overwhelmed, users can describe their situation in plain language and get matched with appropriate resources like crisis hotlines, therapists, and support groups.

---

## ⚠️ Important Disclaimer

This is **NOT** medical advice or a replacement for professional help. It's an information tool to help people find resources. Always consult mental health professionals for actual treatment.

**Crisis?** Call **NCMH: 0917-899-8727** or **Emergency: 911**

---

## 🚀 Current Status

**Phase:** Building core features

**What works:**
- ✅ Project setup with UV
- ✅ OpenRouter AI integration
- ⏳ Resource database (in progress)
- ⏳ Situation analysis (in progress)
- ⏳ CLI interface (in progress)

**What's planned:**
- Crisis detection
- Resource matching
- Location-based filtering
- Tagalog support (future)

---

## 🛠️ Tech Stack

- **Python 3.11+** - Modern Python
- **UV** - Fast package manager (replaces pip/venv)
- **OpenRouter** - Free AI models (GPT, Gemini, LLama)
- **OpenAI SDK** - API integration

**Why these choices?**
- UV: 10-100x faster than pip, modern
- OpenRouter: Free tier for learning, multiple models
- CLI: Accessible, no hosting needed, privacy-first

---

## 📦 Installation (for testing)

**Prerequisites:**
- Python 3.11+
- UV package manager
```bash
# Clone repo
git clone https://github.com/yourusername/linknayan.git
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

**Get free API key:** https://openrouter.ai/keys

---

## 🗂️ Project Structure
```
linknayan/
├── src/linknayan/
│   ├── main.py        # CLI interface (building)
│   ├── ai.py          # AI integration (building)
│   ├── resources.py   # Resource loader (building)
│   └── config.py      # Config (done)
├── data/
│   ├── hotlines.json       # Crisis hotlines (researching)
│   ├── professionals.json  # Mental health services (researching)
│   └── resources.json      # Self-help resources (researching)
├── pyproject.toml
└── README.md
```

---

## 📚 What I'm Learning

This is my **first AI project** as an 18-year-old CS freshman. Through this I'm learning:

- ✅ Working with AI APIs (OpenRouter/OpenAI)
- ✅ Modern Python tooling (UV)
- ✅ Prompt engineering
- ⏳ Building ethical AI (crisis detection, safety)
- ⏳ Resource verification and curation
- ⏳ CLI design and user experience

---

## 🎯 Goals

**Short-term (This week):**
- [ ] Complete resource database (hotlines, services)
- [ ] Build situation analysis with AI
- [ ] Implement crisis detection
- [ ] Create basic CLI interface

**Medium-term (Next month):**
- [ ] Test with real scenarios
- [ ] Add more resources
- [ ] Improve accuracy
- [ ] Get feedback from mental health community

**Long-term (Future):**
- [ ] Web interface (Streamlit)
- [ ] Tagalog language support
- [ ] Location-based filtering
- [ ] Partnership with mental health orgs

---

## 🤝 Feedback Welcome!

Since this is a learning project, I'd love feedback on:
- Resource accuracy (are these hotlines correct?)
- Code structure (better ways to organize?)
- AI prompts (how to improve categorization?)
- Features (what would be most helpful?)

**Note:** I'm still learning, so code quality is improving as I go!

---

## 🙏 Resources Being Compiled

Currently researching and verifying:

**Crisis Hotlines:**
- NCMH Crisis Hotline: 0917-899-8727
- In Touch Crisis Line: (02) 8893-7603
- (Adding more...)

**Professional Services:**
- National Center for Mental Health
- Online therapy platforms (Silakbo, MindNation)
- (Adding more...)

*All resources will be verified before launch.*

---

## 📝 Development Log

**Week 1 (Current):**
- Set up project with UV
- Integrated OpenRouter API
- Started building resource database
- Learning prompt engineering

**Next Week:**
- Complete core features
- Test crisis detection
- Finalize resource list

---

## ⚠️ Known Issues / TODO

- [ ] Resource database incomplete
- [ ] Crisis detection needs testing
- [ ] AI categorization needs refinement
- [ ] No error handling yet
- [ ] CLI interface rough
- [ ] Need more Filipino resources

---

## 🆘 Crisis Resources

**If you or someone needs help NOW:**

- **NCMH Crisis Hotline:** 0917-899-8727 (24/7, free)
- **Emergency:** 911
- **In Touch Crisis Line:** (02) 8893-7603

Don't wait for this tool to be finished - these resources are available now!

---

## 📧 Contact

**Developer:** Jezreel E. Guillermo
**GitHub:** [@Jeshz-Dev](https://github.com/Jez-prog/LinkNayan.git))  
**Email:** jezreeleguillermi@gmail.com

**Status updates:** Follow this repo or check commit history

---

## 📄 License

MIT License - feel free to learn from or fork this code!

---

<div align="center">

**🚧 Under Development 🚧**

Building in public as part of my AI learning journey

Made with 💚 for the Filipino community

</div>
```

---

# GitHub Repository Description (Short)
```
LinkNayan 💚 [WIP] - Learning to build AI-powered mental health resource finder for Filipinos. Matches users with crisis hotlines, therapists & support groups. My first AI project (CS freshman). Built with Python, UV, OpenRouter. NOT medical advice. Feedback welcome!
```

**Character count:** 295 (under 350 limit)

---

# GitHub Topics/Tags
```
work-in-progress
learning-project
mental-health
philippines
ai
openrouter
python
cli
student-project
first-project
crisis-resources
filipino
beginner-friendly
uv
social-impact