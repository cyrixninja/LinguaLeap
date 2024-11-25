# LinguaLeap
![Omi Plugin Banner](/assets/Banner.png)

LinguaLeap is an innovative AI-powered communication enhancement app built for the Omi device ecosystem. It provides real-time language and communication improvements by analyzing your conversations as you speak.

## 🎯 Hackathon Context
Built for the Omi Apps Challenge, LinguaLeap leverages Omi's AI necklace capabilities to enhance users' daily conversations. The app processes real-time audio transcriptions to provide valuable language insights and improvements.

## ✨ Key Features

- **Vocabulary Enhancement**: Suggests sophisticated alternatives for commonly used words
- **Grammar Correction**: Real-time grammar and style improvements
- **Sentence Simplification**: Makes complex sentences more clear and concise
- **Cultural Sensitivity Check**: Flags potentially insensitive phrases and suggests improvements
- **Tone Adjustment**: Adapts your speech to different tones:
  - Professional
  - Friendly
  - Casual

## 🛠 How It Works

1. Wear your Omi device and start speaking
2. LinguaLeap processes your speech in real-time
3. Receives feedback and suggestions after every 150 characters
4. Choose your preferred analysis mode through the setup process

## 🔧 Technical Requirements

- Python 3.7+
- Flask web framework
- Groq API access
- Omi device for audio capture

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/LinguaLeap.git

# Install dependencies
pip install -r [requirements.txt](http://_vscodecontentref_/0)

# Set up environment variables
# Create a .env file with:
GROQ_API_KEY=your_api_key_here