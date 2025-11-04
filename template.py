import os

# Root project folder name
project_name = "multimodal-voice-agent"

# List of folders to create
folders = [
    f"{project_name}/app",
    f"{project_name}/app/routes",
    f"{project_name}/app/services",
    f"{project_name}/app/models",
    f"{project_name}/app/utils",
    f"{project_name}/app/data/audio_input",
    f"{project_name}/app/data/audio_output",
    f"{project_name}/app/data/conversation_logs",
    f"{project_name}/app/static/css",
    f"{project_name}/app/static/js",
    f"{project_name}/app/templates",
    f"{project_name}/app/tests",
    f"{project_name}/deployment",
    f"{project_name}/scripts",
    f"{project_name}/notebooks",
]

# List of files to create with placeholder comments
files = {
    f"{project_name}/README.md": "# Multimodal Voice Agent\n\nEnd-to-End AI Voice Assistant using STT + LLM + TTS.",
    f"{project_name}/requirements.txt": "# Add Python dependencies here",
    f"{project_name}/.gitignore": "__pycache__/\n.env\ndata/\n*.pyc\n",
    f"{project_name}/.env": "# Environment variables (example)\nOPENAI_API_KEY=\n",
    f"{project_name}/Dockerfile": "# Dockerfile template",
    f"{project_name}/docker-compose.yml": "# Docker Compose setup",
    f"{project_name}/app/__init__.py": "",
    f"{project_name}/app/main.py": "# Entry point for FastAPI app",
    f"{project_name}/app/config.py": "# Configuration for environment and paths",
    f"{project_name}/app/routes/__init__.py": "",
    f"{project_name}/app/routes/speech_to_text.py": "# STT route",
    f"{project_name}/app/routes/text_to_speech.py": "# TTS route",
    f"{project_name}/app/routes/generate_response.py": "# LLM route",
    f"{project_name}/app/routes/chat_pipeline.py": "# Combined STT -> LLM -> TTS route",
    f"{project_name}/app/services/__init__.py": "",
    f"{project_name}/app/services/stt_service.py": "# Handles Whisper or DeepSpeech STT",
    f"{project_name}/app/services/llm_service.py": "# Handles GPT-2 / LLaMA / Falcon",
    f"{project_name}/app/services/tts_service.py": "# Handles Coqui / Bark / gTTS",
    f"{project_name}/app/services/memory_service.py": "# Manages conversational memory",
    f"{project_name}/app/services/audio_utils.py": "# Utility functions for audio processing",
    f"{project_name}/app/services/pipeline_manager.py": "# Manages full pipeline logic",
    f"{project_name}/app/models/__init__.py": "",
    f"{project_name}/app/models/whisper_model.py": "# Load and run Whisper model",
    f"{project_name}/app/models/llm_model.py": "# Load or connect to LLM",
    f"{project_name}/app/models/tts_model.py": "# Load TTS model",
    f"{project_name}/app/utils/__init__.py": "",
    f"{project_name}/app/utils/logger.py": "# Logging setup",
    f"{project_name}/app/utils/audio_handler.py": "# Read/write audio files",
    f"{project_name}/app/utils/response_formatter.py": "# Clean up text for TTS output",
    f"{project_name}/app/utils/config_loader.py": "# Load .env configurations",
    f"{project_name}/app/templates/index.html": "<!-- Frontend HTML -->",
    f"{project_name}/app/tests/__init__.py": "",
    f"{project_name}/app/tests/test_stt.py": "# Unit test for STT",
    f"{project_name}/app/tests/test_llm.py": "# Unit test for LLM",
    f"{project_name}/app/tests/test_tts.py": "# Unit test for TTS",
    f"{project_name}/app/tests/test_pipeline.py": "# Unit test for full pipeline",
    f"{project_name}/deployment/nginx.conf": "# Nginx configuration",
    f"{project_name}/deployment/gunicorn_conf.py": "# Gunicorn setup for FastAPI",
    f"{project_name}/deployment/aws_ec2_setup.md": "# Instructions for AWS EC2 deployment",
    f"{project_name}/deployment/huggingface_deploy.md": "# Hugging Face Space deployment guide",
    f"{project_name}/scripts/run_local.sh": "#!/bin/bash\nuvicorn app.main:app --reload",
    f"{project_name}/scripts/convert_audio.py": "# Convert or preprocess audio files",
    f"{project_name}/scripts/evaluate_latency.py": "# Measure latency of STT/LLM/TTS steps",
    f"{project_name}/scripts/generate_readme_summary.py": "# Auto-generate README logs",
    f"{project_name}/notebooks/stt_experiments.ipynb": "",
    f"{project_name}/notebooks/llm_finetuning.ipynb": "",
    f"{project_name}/notebooks/tts_quality_test.ipynb": "",
    f"{project_name}/notebooks/pipeline_integration.ipynb": "",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {file_path}")

print("\n✅ Project structure created successfully!")
