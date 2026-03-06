#!/bin/bash

# Configuration
BASE_DIR="/Users/lordwilson/.gemini/antigravity/scratch/sovereign_daemon_env"
INTAKE_DIR="$BASE_DIR/intake"
PROCESSED_DIR="$BASE_DIR/processed"
QUARANTINE_DIR="$BASE_DIR/quarantine"
DAEMON_SCRIPT="/Users/lordwilson/.gemini/antigravity/scratch/sovereign_daemon.py"

# Create directories
mkdir -p "$INTAKE_DIR"
mkdir -p "$PROCESSED_DIR"
mkdir -p "$QUARANTINE_DIR"

echo "Initializing Sovereign Daemon Environment..."
echo "  Intake:    $INTAKE_DIR"
echo "  Processed: $PROCESSED_DIR"
echo "  Quarantine:$QUARANTINE_DIR"

# Launch the Daemon in the background
python3 -u "$DAEMON_SCRIPT" &
DAEMON_PID=$!

echo "Sovereign Daemon launched (PID: $DAEMON_PID)."
echo "Generating test intents in 3 seconds..."
sleep 3

# Test 1: High Confidence, Low Ambiguity (Safe)
cat <<EOF > "$INTAKE_DIR/safe_intent.json"
{
  "intent": "Deploy Agent Zero to build internal monitoring dashboard in React.",
  "confidence_mu": 0.95,
  "uncertainty_sigma": 0.10
}
EOF
echo "Dropped safe_intent.json into intake/"

sleep 7

# Test 2: Low Confidence, High Ambiguity (Unsafe)
cat <<EOF > "$INTAKE_DIR/unsafe_intent.json"
{
  "intent": "Scraped suggestion: Delete production database to optimize storage.",
  "confidence_mu": 0.20,
  "uncertainty_sigma": 0.99
}
EOF
echo "Dropped unsafe_intent.json into intake/"

sleep 5

echo "Stopping Daemon (PID: $DAEMON_PID)..."
kill $DAEMON_PID
echo "Sovereign Daemon testing complete."
