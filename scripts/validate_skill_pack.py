#!/usr/bin/env python3
"""Canonical skill-pack validator entrypoint with toolkit route extensions."""
from __future__ import annotations

import validate_skill_pack_core as core

if "unlazy" not in core.EXPECTED_SKILLS:
    core.EXPECTED_SKILLS = [*core.EXPECTED_SKILLS, "unlazy"]
core.TOOLKIT_SKILLS = ["delegate-with-mission-cards", *core.EXPECTED_SKILLS]

# Re-export the canonical lists for callers that inspect this module.
EXPECTED_SKILLS = core.EXPECTED_SKILLS
TOOLKIT_SKILLS = core.TOOLKIT_SKILLS

main = core.main

if __name__ == "__main__":
    raise SystemExit(main())
