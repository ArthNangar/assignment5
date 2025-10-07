# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import os
import importlib
import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError

def test_defaults(monkeypatch):
    monkeypatch.delenv("HISTORY_FILE", raising=False)
    monkeypatch.setenv("AUTOSAVE", "true")
    cfg = CalculatorConfig.from_env()
    assert cfg.history_file == "history.csv" and cfg.autosave is True

def test_invalid_autosave(monkeypatch):
    monkeypatch.setenv("AUTOSAVE", "maybe")
    with pytest.raises(ConfigurationError):
        CalculatorConfig.from_env()

def test_history_file_override(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "x.csv")
    monkeypatch.setenv("AUTOSAVE", "false")
    cfg = CalculatorConfig.from_env()
    assert cfg.history_file == "x.csv" and cfg.autosave is False
