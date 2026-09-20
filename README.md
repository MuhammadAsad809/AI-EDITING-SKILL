# AI Video Editor Skill

A modular knowledge and reasoning system for producing professional video-editing plans from footage descriptions, music, platforms, genres, and software constraints. This repository is **not a video editor UI**. It teaches an AI how to make editorial decisions, construct timelines, synchronize visuals to music, and communicate executable steps.

## What it covers

- Story, continuity, montage, music-video, documentary, gaming, sports, anime/AMV, phonk, travel, fashion, car, and short-form editing.
- Beat maps, BPM math, song-structure analysis, cut density, anticipation, impact, release, and energy curves.
- Cutting theory, motivated transitions, speed ramps, motion design, sound design, color grading, typography, footage analysis, and export planning.
- Software-aware workflows for Premiere Pro, After Effects, DaVinci Resolve, CapCut, VN, Final Cut Pro, and Alight Motion.

## Start here

Read [`SKILL.md`](SKILL.md) for the agent instructions. Then load only the references required by the task. The highest-priority path for a music-led montage is:

`SKILL.md` → `knowledge/footage-analysis.md` → `knowledge/montage.md` → `knowledge/beat-sync.md` → `knowledge/speed-ramping.md` → `knowledge/sound-design.md` → `workflows/montage-workflow.md` → relevant genre/software file.

Use [`templates/montage-template.md`](templates/montage-template.md) for a deliverable and [`scripts/validate_plan.py`](scripts/validate_plan.py) to check required headings and timecode formatting.

## Design principles

1. Story and readable visual intent come before effects.
2. Every cut and effect needs a reason, timing, strength, and fallback.
3. Beat synchronization is a hierarchy: structure first, downbeats second, accents third, subdivisions last.
4. A plan must distinguish facts, assumptions, and items to verify.
5. Instructions must respect the selected software and platform.

## Repository map

| Directory | Purpose |
|---|---|
| `knowledge/` | General editing theory and technical decision rules |
| `genres/` | Genre-specific editorial grammar and examples |
| `software/` | Application-aware workflows and feature limits |
| `workflows/` | Repeatable end-to-end production sequences |
| `templates/` | Copyable plan, beat-map, and timeline structures |
| `examples/` | Worked plans showing the reasoning standard |
| `scripts/` | Small validation utilities for plan authors |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). New material should add decision rules and examples, not generic lists of effects. Keep the core skill concise and place deep detail in the appropriate reference file.
