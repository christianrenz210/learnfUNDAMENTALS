import sys
sys.path.insert(0, '.')
import app

print('=== AI System Components ===')
print('APP_VERSION:', app.APP_VERSION)
print('EREN_SYSTEM_PROMPT exists:', hasattr(app, 'EREN_SYSTEM_PROMPT'))
if hasattr(app, 'EREN_SYSTEM_PROMPT'):
    print('EREN_SYSTEM_PROMPT starts with "You are E.R.E.N":', app.EREN_SYSTEM_PROMPT.startswith('You are E.R.E.N'))
    print('EREN_SYSTEM_PROMPT length:', len(app.EREN_SYSTEM_PROMPT))

print('\n=== Gemini Configuration ===')
print('_gemini_model():', app._gemini_model())
print('_gemini_api_key():', bool(app._gemini_api_key()))