# LinguaLeap
![Omi Plugin Banner](/assets/Banner.png)

LinguaLeap is an innovative AI-powered communication enhancement app built for the Omi device ecosystem. It provides real-time language and communication improvements by analyzing conversations as you speak. LinguaLeap leverages Omi's AI necklace capabilities to enhance users' daily conversations by processing real-time audio transcriptions to provide valuable language insights and improvements.

## 🚀 Impact and User Benefits

### ✨ Key User Impact Areas

- **Personal Confidence Boost**: Reduces communication anxiety through instant, constructive feedback.
- **Professional Growth**: Elevates communication skills in real-world contexts.
- **Inclusive Communication**: Supports diverse language learners and communication styles.
- **Continuous Learning**: Provides personalized language improvement without formal training.

### ✨ Key Features

- **Vocabulary Enhancement**: Suggests sophisticated alternatives for commonly used words.
- **Grammar Correction**: Real-time grammar and style improvements.
- **Sentence Simplification**: Makes complex sentences more clear and concise.
- **Cultural Sensitivity Check**: Flags potentially insensitive phrases and suggests improvements.
- **Tone Adjustment**: Adapts your speech to different tones:
  - Professional
  - Friendly
  - Casual

### 🌐 Solving Real-World Communication Challenges

#### Who Benefits Most

- Non-native speakers
- Professionals in international settings
- Individuals seeking to improve communication skills
- People with communication-related challenges

## 🛠 How It Works

1. Wear your Omi device and start speaking.
2. LinguaLeap processes your speech in real-time.
3. Receives feedback and suggestions after every 150 characters.
4. Choose your preferred analysis mode through the setup process.

## 🔧 Technical Requirements

- Python 3.7+
- Flask web framework
- Groq API access
- Omi device for audio capture

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/cyrixninja/LinguaLeap.git

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with:
GROQ_API_KEY=your_api_key_here