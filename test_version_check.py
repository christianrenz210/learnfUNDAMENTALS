import sys
sys.path.insert(0, '.')
import app

print('=== Final AI System Version Check ===')
print('APP_VERSION:', app.APP_VERSION)
print('EREN_VERSION:', app.EREN_VERSION)
print('Gemini Model:', app._gemini_model())
print('Has EREN_SYSTEM_PROMPT:', hasattr(app, 'EREN_SYSTEM_PROMPT'))
if hasattr(app, 'EREN_SYSTEM_PROMPT'):
    print('EREN_SYSTEM_PROMPT starts with "You are E.R.E.N":', app.EREN_SYSTEM_PROMPT.startswith('You are E.R.E.N'))