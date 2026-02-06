# Voice AI Assistant

A simple voice-enabled AI assistant built using Python.  
You can speak to it, and it will listen, understand, and speak back.

This project was created as part of an AI Intern technical assessment, with a focus on clean architecture and real-world engineering practices.

## Features
- Speech-to-Text using Whisper
- Low-latency LLM responses using Groq + LLaMA-3
- Text-to-Speech output
- Intent detection for date and time
- Summarized responses for better voice output
- Graceful handling of silence and errors
- Logging and basic latency metrics

## How It Works
Voice Input → Speech to Text → Intent Detection → LLM or Local Tools → Summarized Response → Text to Speech

## Setup

### Install dependencies
pip install -r requirements.txt

**Windows users:**  
If `pyaudio` fails:
pip install pipwin
pipwin install pyaudio

### Add environment variables
Create a `.env` file:
GROQ_API_KEY=your_api_key_here

### Run the assistant
python main.py

## Windows Setup (Native)

> **Recommended:** Use WSL2 for the best experience. Native Windows is supported but requires additional configuration.

### Prerequisites
- **Python 3.11+** ([Download](https://www.python.org/downloads/)) - Python 3.12 or 3.13 recommended
- **Git** for Windows
- **PowerShell 7+** (preferred) or PowerShell 5.1+ 
- **VS Code** (recommended)

### Step 1: Install Python Correctly

1. Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
2. **During installation:**
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install for all users" (requires admin)
3. Verify:
```powershell
   python --version  # Should show 3.11 or higher
```

### Step 2: Disable App Execution Aliases

Windows may intercept `python` commands and redirect to Microsoft Store.

1. Open **Settings** → **Apps** → **App Execution Aliases**
2. Turn **OFF**:
   - `python.exe`
   - `python3.exe`
3. Close and reopen PowerShell

### Step 3: Clone Repository
```powershell
git clone https://github.com/adenhq/hive.git
cd hive
```

### Step 4: Run Setup Script
```powershell
# Option A: Using Git Bash (if available)
./quickstart.sh

# Option B: Manual PowerShell setup (if quickstart.sh fails)
pip install uv
cd core
uv pip install -e .
cd ..\tools
uv pip install -e .
cd ..
```

### Step 5: Configure Environment Variables
```powershell
# Add to your PowerShell profile (~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1)
$env:ANTHROPIC_API_KEY = "your-key-here"
$env:PYTHONPATH = "exports"

# Or set for current session only:
$env:PYTHONPATH = "exports"
```

**To edit your PowerShell profile:**
```powershell
notepad $PROFILE
# If file doesn't exist, create it first:
New-Item -Path $PROFILE -Type File -Force
```

### Step 6: Verify Installation
```powershell
uv run python -c "import framework; import aden_tools; print('✓ Setup complete')"
```

### Common Windows Issues

#### Issue: ModuleNotFoundError when running agents

**Problem:** `ModuleNotFoundError: No module named 'my_agent'`

**Solution:**
```powershell
# Always set PYTHONPATH before running agents
$env:PYTHONPATH = "exports"
uv run python -m my_agent run --input '{...}'
```

**Permanent fix:** Add to your PowerShell profile:
```powershell
$env:PYTHONPATH = "exports"
```

#### Issue: Permission Errors

**Problem:** Access denied during pip install

**Solution:** Run PowerShell as Administrator or use `--user` flag:
```powershell
pip install --user uv
```

#### Issue: Path Separator Issues

**Problem:** Scripts expect `/` but Windows uses `\`

**Solution:** Python handles this automatically. Use forward slashes in code:
```python
path = "exports/my_agent"  # Works on Windows too
```

#### Issue: 'python' is not recognized

**Problem:** Command not found even after installation

**Solutions:**
1. Restart your terminal/PowerShell
2. Check Python is in PATH:
```powershell
   $env:PATH -split ';' | Select-String python
```
3. Reinstall Python and ensure "Add to PATH" is checked

#### Issue: quickstart.sh won't run

**Problem:** Script format not recognized

**Solutions:**
1. Use Git Bash (comes with Git for Windows)
2. Use manual installation (Step 4, Option B)
3. Install WSL2 for better compatibility

### Running Agents on Windows

When running agents, always remember to set PYTHONPATH:
```powershell
# Validate agent structure
$env:PYTHONPATH = "exports"
uv run python -m my_agent validate

# Run agent
$env:PYTHONPATH = "exports"
uv run python -m my_agent run --input '{"task": "Your input here"}'

# Run tests
$env:PYTHONPATH = "exports"
uv run python -m my_agent test
```

### PowerShell vs Command Prompt

**Use PowerShell** (recommended):
- Better scripting capabilities
- Native support for environment variables
- More modern tooling

**If using Command Prompt:**
```cmd
set PYTHONPATH=exports
uv run python -m my_agent run --input "{\"task\": \"Your input here\"}"
```

Note the escaped quotes (`\"`) in Command Prompt.
