# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .exceptions import ConfigurationError

load_dotenv()  # EAFP: load if exists

@dataclass(frozen=True)
class CalculatorConfig:
    history_file: str = "history.csv"
    autosave: bool = True

    @staticmethod
    def from_env() -> "CalculatorConfig":
        # LBYL: get envs and validate types
        history_file = os.getenv("HISTORY_FILE", "history.csv")
        autosave_str = os.getenv("AUTOSAVE", "true").strip().lower()
        if autosave_str not in {"true", "false"}:
            raise ConfigurationError("AUTOSAVE must be 'true' or 'false'")
        autosave = autosave_str == "true"
        return CalculatorConfig(history_file=history_file, autosave=autosave)
