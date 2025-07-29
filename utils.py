import hashlib

def hash_command(cmd):
    """Generate MD5 hash of a command string."""
    return hashlib.md5(cmd.encode()).hexdigest()

# 2. Input Validation and Normalization
def normalize_command(cmd):
    """Clean and normalize a command (optional use)."""
    return cmd.strip().lower()
