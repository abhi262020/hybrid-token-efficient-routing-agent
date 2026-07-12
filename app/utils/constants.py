"""
Global constants used throughout the project.
"""

# ==========================================
# Application
# ==========================================

APP_NAME = "Hybrid Token-Efficient Routing Agent"
APP_VERSION = "1.0.0"

# ==========================================
# Routing
# ==========================================

CONFIDENCE_THRESHOLD = 0.85
MAX_COMPLEXITY = 10
MIN_COMPLEXITY = 1

ESCALATION_LIMIT = 2

# ==========================================
# Token Limits
# ==========================================

DEFAULT_MAX_TOKENS = 512
MAX_INPUT_TOKENS = 4096
MAX_OUTPUT_TOKENS = 1024

# ==========================================
# Cache
# ==========================================

CACHE_TTL = 300           # seconds
CACHE_PREFIX = "router"

# ==========================================
# Logging
# ==========================================

LOG_FILE = "logs/router.log"
LOG_LEVEL = "INFO"

# ==========================================
# API
# ==========================================

DEFAULT_TIMEOUT = 30      # seconds

# ==========================================
# Task Types
# ==========================================

TASK_GENERAL = "general"
TASK_CODING = "coding"
TASK_MATH = "math"
TASK_SQL = "sql"
TASK_TRANSLATION = "translation"
TASK_SUMMARIZATION = "summarization"
TASK_REASONING = "reasoning"
TASK_GRAMMAR = "grammar"

# ==========================================
# Complexity Levels
# ==========================================

EASY = 3
MEDIUM = 6
HARD = 10

# ==========================================
# Confidence Levels
# ==========================================

HIGH_CONFIDENCE = 0.90
MEDIUM_CONFIDENCE = 0.75
LOW_CONFIDENCE = 0.50