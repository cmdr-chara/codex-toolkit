#!/usr/bin/env python3
"""Canonical skill-pack validator entrypoint with toolkit route extensions."""
from __future__ import annotations

import validate_skill_pack_core as core

if "unlazy" not in core.EXPECTED_SKILLS:
    core.EXPECTED_SKILLS = [*core.EXPECTED_SKILLS, "unlazy"]
core.TOOLKIT_SKILLS = ["delegate-with-mission-cards", *core.EXPECTED_SKILLS]

_original_provenance_validation = core.validate_responsibility_and_provenance


def validate_responsibility_and_provenance(result: core.Result) -> None:
    """Run core checks plus provenance contracts added after the core snapshot."""
    _original_provenance_validation(result)

    unlazy_reference = result.root / "skills/unlazy/references/upstream-provenance.md"
    unlazy_text = core.read_text(unlazy_reference, result)
    for phrase in (
        "Leonxlnx/unlazy",
        "ed9e8d2b5919698cf2c54bda270d507e10b69617",
        "Copyright (c) 2026 Leonxlnx",
        "No endorsement by Leonxlnx is stated or implied",
    ):
        if phrase not in unlazy_text:
            result.error(f"skills/unlazy: upstream provenance missing {phrase!r}")

    provenance_reference = (
        result.root
        / "skills/content-provenance-hygiene/references/service-protocol.md"
    )
    provenance_text = core.read_text(provenance_reference, result)
    for phrase in (
        "guillaumemeyer/watermarks-remover",
        "fcebf533583d7a313b348dbe421f3b4b17163b66",
        "License:** MIT",
        "does not vendor, redistribute, or silently install",
    ):
        if phrase not in provenance_text:
            result.error(
                "content-provenance-hygiene: service provenance missing "
                f"{phrase!r}"
            )

    notice = core.read_text(result.root / "THIRD_PARTY_NOTICES.md", result)
    for phrase in (
        "## Leonxlnx/unlazy",
        "ed9e8d2b5919698cf2c54bda270d507e10b69617",
        "## guillaumemeyer/watermarks-remover",
        "Copyright (c) 2026 watermarks-remover contributors",
    ):
        if phrase not in notice:
            result.error(f"THIRD_PARTY_NOTICES.md: missing {phrase!r}")


core.validate_responsibility_and_provenance = validate_responsibility_and_provenance

# Re-export canonical lists for callers that inspect this module.
EXPECTED_SKILLS = core.EXPECTED_SKILLS
TOOLKIT_SKILLS = core.TOOLKIT_SKILLS

main = core.main

if __name__ == "__main__":
    raise SystemExit(main())
