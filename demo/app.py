import os
import json
import requests
import time
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file into environment

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL")

if not GEMINI_API_KEY:
    print("\nERROR: GEMINI_API_KEY not found. Make sure it's set in your .env file.\n")
 
if not GEMINI_MODEL:
    print("\nERROR: GEMINI_MODEL not found. Make sure it's set in your .env file.\n")
    GEMINI_MODEL = "gemini-2.0-flash-latest"
    print(f"Warning: GEMINI_MODEL not found, using default: {GEMINI_MODEL}")


API_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
HEADERS = {"Content-Type": "application/json"}

TARGET_INFO = {
    "type": "Organization",
    "name": "Innovatech Solutions",
    "domain": "innovatech.solutions",
    "industry": "Technology Consulting",
    "locations": ["San Francisco", "Austin"],
    "wifi_ssid": "InnovatechGuest",
    "wifi_bssid_oui": "00:1A:11",
    "osint_leaks": [
        "User 'jsmith' mentioned weak guest passwords in a forum.",
        "Company picnic photos tagged #InnovatechFunRun2023",
        "Job posting for 'Network Admin' mentions Cisco infrastructure.",
    ]
}

app = Flask(__name__)

def call_gemini_api(prompt):
    """Makes an API call to Gemini and returns the text response or an error message."""
    logs = []
    if not GEMINI_API_KEY or not GEMINI_MODEL:
        logs.append("Error: API Key or Model not configured correctly.")
        return None, logs


    payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]})

    try:
        logs.append(f"Contacting Gemini API (Model: {GEMINI_MODEL})...") # Log the model being used
        response = requests.post(API_ENDPOINT, headers=HEADERS, data=payload, timeout=60)
        response.raise_for_status()
        response_json = response.json()

        if 'candidates' in response_json and len(response_json['candidates']) > 0:
            candidate = response_json['candidates'][0]
            if 'content' in candidate and 'parts' in candidate['content'] and len(candidate['content']['parts']) > 0:
                generated_text = candidate['content']['parts'][0]['text']
                logs.append("Received analysis from Gemini.")
                return generated_text.strip(), logs
            else:
                finish_reason = candidate.get('finishReason', 'UNKNOWN')
                logs.append(f"Warning: Gemini response missing content. Finish Reason: {finish_reason}")
                if 'safetyRatings' in candidate:
                    logs.append(f"Safety Ratings: {candidate.get('safetyRatings')}")
                return None, logs
        else:
             logs.append(f"Error: Unexpected Gemini response format or no candidates.")
             print(f"Problematic Response: {response_json}")
             return None, logs


    except requests.exceptions.RequestException as e:
        logs.append(f"Error calling Gemini API: {e}")
        return None, logs
    except json.JSONDecodeError:
        logs.append(f"Error decoding Gemini API response: {response.text}")
        return None, logs
    except Exception as e:
        logs.append(f"An unexpected error occurred during API call: {e}")
        return None, logs


def parse_ai_analysis(ai_analysis_text):
    """Rudimentary parsing of the AI response."""
    analysis_parts = {
        "themes_keywords": "N/A",
        "potential_usernames": "N/A",
        "targeted_password_ideas": [],
        "suggested_vector": "N/A"
    }
    current_section = None
    if not ai_analysis_text:
        return analysis_parts

    lines = ai_analysis_text.splitlines()
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        if line_stripped.lower().startswith("1. key themes/keywords"):
            current_section = "themes_keywords"
            analysis_parts[current_section] = line_stripped.split(":", 1)[-1].strip()
        elif line_stripped.lower().startswith("2. potential usernames"):
            current_section = "potential_usernames"
            analysis_parts[current_section] = line_stripped.split(":", 1)[-1].strip()
        elif line_stripped.lower().startswith("3. targeted password ideas"):
            current_section = "targeted_password_ideas"
        elif line_stripped.lower().startswith("4. suggested initial access vector"):
            current_section = "suggested_vector"
            analysis_parts[current_section] = line_stripped.split(":", 1)[-1].strip()
        elif current_section == "targeted_password_ideas":
             password = line_stripped.lstrip('-* ').strip()
             if password: # Avoid adding empty lines if formatting is weird
                analysis_parts["targeted_password_ideas"].append(password)
        elif current_section == "themes_keywords" and not line_stripped.lower().startswith("2."):
            analysis_parts[current_section] += " " + line_stripped # Append continuation lines
        elif current_section == "potential_usernames" and not line_stripped.lower().startswith("3."):
             analysis_parts[current_section] += " " + line_stripped
        # Ignore lines if section is not identified or continuation logic isn't needed

    return analysis_parts

@app.route('/')
def index():
    """Render the main UI page."""
    return render_template('index.html', target_info=TARGET_INFO)

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint to trigger the analysis workflow."""
    logs = []
    results = {}

    if not GEMINI_API_KEY or not GEMINI_MODEL:
         logs.append("Error: Backend configuration incomplete (API Key or Model missing). Check .env file.")
         return jsonify({"logs": logs, "results": {}, "status": "error"})

    # --- Phase 1: Recon (Simulated) ---
    logs.append("Starting Aether PoC Workflow...")

    logs.append(f"Target Profile Loaded: {TARGET_INFO['name']}")
    logs.append("[SIMULATE] Running OSINT gathering...")
    time.sleep(0.5) # Short delay for effect
    logs.append("[SIMULATE] Running Network Scan...")
    time.sleep(0.5)
    logs.append(f"[RESULT] Discovered Wi-Fi: '{TARGET_INFO['wifi_ssid']}' (OUI: {TARGET_INFO['wifi_bssid_oui']})")


    # --- Phase 2: AI Analysis ---
    logs.append("Compiling context for AI...")
    prompt = f"""
    Analyze the following intelligence report for a red team engagement against '{TARGET_INFO['name']}' and suggest actionable insights, focusing on potential initial access vectors and password guessing strategies for the Wi-Fi network '{TARGET_INFO['wifi_ssid']}'.

    Target Information:
    - Name: {TARGET_INFO['name']}
    - Domain: {TARGET_INFO['domain']}
    - Industry: {TARGET_INFO['industry']}
    - Locations: {', '.join(TARGET_INFO['locations'])}
    - Discovered Wi-Fi SSID: {TARGET_INFO['wifi_ssid']}
    - Wi-Fi Router OUI: {TARGET_INFO['wifi_bssid_oui']} (Suggests potential vendor defaults?)
    - OSINT Findings: {'; '.join(TARGET_INFO['osint_leaks'])}

    Based ONLY on the information provided, provide:
    1. Key Themes/Keywords: Extract potential themes (company name variations, locations, event names, tech) relevant for password guessing. (Provide a concise summary).
    2. Potential Usernames: Suggest likely username formats or specific usernames hinted at. (Provide a concise summary).
    3. Targeted Password Ideas: Generate a concise list (around 10-15) of *specific*, plausible password ideas for the '{TARGET_INFO['wifi_ssid']}' network. Consider variations of the company name, SSID, locations, common patterns, and hints from OSINT (like 'jsmith', 'FunRun2023', 'Cisco', defaults for OUI {TARGET_INFO['wifi_bssid_oui']}). Output *only* the password list under this point, one password per line, with no extra explanation in this section.
    4. Suggested Initial Access Vector: Recommend the most plausible initial access vector based *only* on the Wi-Fi and OSINT data provided (e.g., Wi-Fi attack, potential credential stuffing if leaks suggest). (Provide a single recommendation).

    Be concise and actionable. Structure the output clearly using the numbered points above.
    """
    ai_analysis_text, api_logs = call_gemini_api(prompt)
    logs.extend(api_logs)

    analysis_structured = {}
    ai_wordlist = []
    if ai_analysis_text:
        analysis_structured = parse_ai_analysis(ai_analysis_text)
        ai_wordlist = analysis_structured.get("targeted_password_ideas", [])
        logs.append(f"Extracted {len(ai_wordlist)} password ideas from AI analysis.")
        results['ai_analysis_raw'] = ai_analysis_text # Send raw too if needed
        results['ai_analysis_structured'] = analysis_structured
    else:
        logs.append("AI analysis failed. Cannot proceed with attack simulation.")
        results['ai_analysis_raw'] = "Error during analysis."
        results['ai_analysis_structured'] = parse_ai_analysis(None) # Get default structure
        return jsonify({"logs": logs, "results": results, "status": "error"})


    # --- Phase 3: Initial Access Simulation ---
    logs.append(f"[SIMULATE] Targeting Wi-Fi Network '{TARGET_INFO['wifi_ssid']}'...")
    logs.append("[SIMULATE] Capturing handshake...")
    time.sleep(1)
    logs.append("[SIMULATE] Handshake captured!")
    logs.append("[SIMULATE] Preparing cracking environment...")

    if ai_wordlist:
        logs.append(f"[SIMULATE] Running crack attempt with {len(ai_wordlist)} AI-generated passwords...")
        time.sleep(1.5)
        # Simulate success
        simulated_password_found = "InnovatechGuest2023!"
        results['attack_success'] = True
        results['cracked_password'] = simulated_password_found
        logs.append(f"[RESULT] SUCCESS! Password cracked: '{simulated_password_found}' (Simulated)")
    else:
        logs.append("[SIMULATE] No AI wordlist available. Skipping crack attempt.")
        results['attack_success'] = False
        results['cracked_password'] = None
        logs.append("[RESULT] FAILURE. Cannot attempt crack without wordlist. (Simulated)")


    # --- Phase 4: Reporting ---
    logs.append("Workflow simulation complete.")
    results['final_message'] = "PoC demonstrates AI analysis driving targeted actions."


    return jsonify({"logs": logs, "results": results, "status": "success"})


# --- Main Execution ---
if __name__ == '__main__':
    if not GEMINI_API_KEY or not GEMINI_MODEL:
         print("="*60)
         print("ERROR: Configuration missing in .env file (GEMINI_API_KEY or GEMINI_MODEL).")
         print("Please create a .env file in the project root with these values.")
         print("="*60)
         # Optionally exit here:
         # import sys
         # sys.exit(1)
    else:
        print(f"Starting Flask server... Loaded config using model '{GEMINI_MODEL}'.")
        print("Access UI at http://127.0.0.1:5000")
        app.run(debug=True)
