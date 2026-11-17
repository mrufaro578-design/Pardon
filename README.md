# ClassBook

A simple Flask discussion board app that is ready to run locally and can be installed as a web app.

## Run locally

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app
   ```bash
   python app.py
   ```
4. Open http://localhost:5000 in your browser

## Notes

- The app includes a `manifest.json` and service worker so it can be installed like an app.
- Add your final icons and branding assets later when you have them ready.
