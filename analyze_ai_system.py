import sys
sys.path.insert(0, '.')
import app

# Check current AI system configuration
print('=== Current AI System Configuration ===')
print(f"App Version (APP_VERSION): {app.APP_VERSION}")
print(f"E.R.E.N AI Version: Not defined - system prompt exists but no version variable")
print(f"Gemini Model: {app._gemini_model()}")
print(f"Has EREN_SYSTEM_PROMPT: {hasattr(app, 'EREN_SYSTEM_PROMPT')}")
print(f"EREN_SYSTEM_PROMPT length: {len(app.EREN_SYSTEM_PROMPT) if hasattr(app, 'EREN_SYSTEM_PROMPT') else 0}")

print('\n=== Issues Found ===')
print('1. No dedicated E.R.E.N AI version variable (only APP_VERSION exists)')
print('2. System cannot report its own version independently')
print('3. AI assistant version should be separate from app version')

print('\n=== Solution ===')
print('1. Add EREN_VERSION variable for the AI assistant')
print('2. Update code to use EREN_VERSION')
print('3. Ensure system can report both versions independently')