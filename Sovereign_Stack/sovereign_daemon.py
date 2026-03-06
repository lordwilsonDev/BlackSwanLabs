#!/usr/bin/env python3
"""
The Sovereign Daemon: Master Orchestrator

This script runs continuously, monitoring the `intake` directory for new intent files.
When a new file arrives, it parses the content and passes it through the Sovereign
Belief Engine for Epistemic Validation. 

If safe (low ambiguity), it orchestrates the full Sovereign Pipeline:
1. NotebookLM Briefing Generation (Simulated)
2. Dashboard Assembly (Simulated)
3. Workspace CLI Distribution (Simulated)
4. Whisper Network Confirmation (Simulated ultrasonic pulse)

If unsafe (high ambiguity), it moves the file to quarantine and halts execution.
"""

import os
import time
import json
import glob
import shutil
import shadow_processor

# ---------------------------------------------------------------------------
# The Sovereign Belief Engine (Inline for Daemon efficiency)
# ---------------------------------------------------------------------------
class BeliefState:
    def __init__(self, target_concept, confidence_mu, uncertainty_sigma):
        self.target = target_concept
        self.mu = confidence_mu
        self.sigma = uncertainty_sigma

class SafetyFilter:
    def __init__(self, safety_threshold=0.4):
        self.threshold = safety_threshold

    def calculate_ambiguity(self, sigma):
        return sigma

    def is_safe(self, sigma):
        return self.calculate_ambiguity(sigma) <= self.threshold

# ---------------------------------------------------------------------------
# Daemon Configuration
# ---------------------------------------------------------------------------
BASE_DIR = "/Users/lordwilson/.gemini/antigravity/scratch/sovereign_daemon_env"
INTAKE_DIR = os.path.join(BASE_DIR, "intake")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
QUARANTINE_DIR = os.path.join(BASE_DIR, "quarantine")

POLL_INTERVAL_SECONDS = 3

safety_engine = SafetyFilter(safety_threshold=0.4)

def ensure_directories():
    for d in [INTAKE_DIR, PROCESSED_DIR, QUARANTINE_DIR]:
        os.makedirs(d, exist_ok=True)

def process_intent(filepath):
    filename = os.path.basename(filepath)
    print(f"\n[DAEMON] 📥 New Intent Detected: {filename}")
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[DAEMON] ❌ Error parsing JSON in {filename}: {e}")
        shutil.move(filepath, os.path.join(QUARANTINE_DIR, filename))
        return

    intent_text = data.get("intent", "Unknown Goal")
    mu = data.get("confidence_mu", 1.0)
    sigma = data.get("uncertainty_sigma", 1.0) # Assume maximum uncertainty if not provided
    
    print(f"[DAEMON] 🧠 Routing to Sovereign Belief Engine...")
    print(f"         Intent: '{intent_text}'")
    print(f"         Gaussian Stats: μ={mu}, Σ={sigma}")
    
    time.sleep(1)
    
    if safety_engine.is_safe(sigma):
        print(f"[DAEMON] ✅ SAFETY CHECK PASSED (Σ {sigma} <= {safety_engine.threshold}).")
        execute_sovereign_pipeline(intent_text)
        dest = os.path.join(PROCESSED_DIR, filename)
        shutil.move(filepath, dest)
        print(f"[DAEMON] 📦 Intent archived to {dest}")
        
    else:
        print(f"\n[DAEMON] 🚨 SAFETY HALT: EPISTEMIC AMBIGUITY ({sigma}) EXCEEDS THRESHOLD ({safety_engine.threshold}) 🚨")
        print(f"[DAEMON] Routing highly ambiguous intent to the Shadow Processor...")
        
        # Move to quarantine
        dest = os.path.join(QUARANTINE_DIR, filename)
        shutil.move(filepath, dest)
        
        # Execute Inversion via Shadow Processor on the quarantined file
        illuminated_intent, torsion_type = shadow_processor.run_shadow_forge(dest)
        
        if torsion_type == "PHILOSOPHICAL":
           print(f"[DAEMON] Shadow Processor successfully inverted a destructive philosophical axiom.")
           print(f"[DAEMON] Synthesized aligned intent: {illuminated_intent}")
           print(f"[DAEMON] Waiting for Biometric Harmonic Lock (528Hz) to authorize re-injection...")
        else:
           print(f"[DAEMON] Lack of Technical Context. Awaiting human resolution in Quarantine: {dest}")


def execute_sovereign_pipeline(intent_text):
    """Simulates the orchestration of the full Sovereign Stack."""
    print(f"\n{'='*50}")
    print("🚀 INITIATING SOVEREIGN PIPELINE 🚀")
    print(f"{'='*50}")
    
    print(f"[Swarm->NotebookLM] Generating Cinematic Video Overview for: {intent_text}...")
    time.sleep(1.5)
    
    print(f"[Swarm->Dashboard]  Assembling Glassmorphic HTML Artifacts...")
    time.sleep(1)
    
    print(f"[Swarm->Workspace]  $ workspace-cli drive files upload dashboard.html")
    time.sleep(1)
    print(f"[Swarm->Workspace]  $ workspace-cli gmail send --to=operative --subject=\"Briefing Ready\"")
    time.sleep(1)
    
    print(f"[Swarm->Whisper]    Initializing DSP FSK Modulator...")
    print(f"[Swarm->Whisper]    🔊 Transmitting 18kHz ultrasonic success tone payload...")
    time.sleep(1.5)
    
    print(f"{'='*50}")
    print("✅ PIPELINE EXECUTION COMPLETE ✅")
    print(f"{'='*50}\n")


def daemon_loop():
    print("======================================================")
    print("🧿 SOVEREIGN DAEMON ONLINE. LISTENING FOR INTENTS...")
    print("======================================================")
    
    while True:
        # Search for .json intent files in the intake directory
        search_pattern = os.path.join(INTAKE_DIR, "*.json")
        files = glob.glob(search_pattern)
        
        for f in files:
            process_intent(f)
            
        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == "__main__":
    ensure_directories()
    try:
        daemon_loop()
    except KeyboardInterrupt:
        print("\n[DAEMON] Shutting down Sovereign Daemon.")
