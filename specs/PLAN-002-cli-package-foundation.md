# Implementation Plan — CLI Package Foundation

## Progress Tracking
- [x] Phase 0: Package Structure Setup
- [x] Phase 1: Core CLI Implementation
- [x] Phase 2: Manual Testing & Refinement
- [x] Phase 3: Package Distribution Readiness

## Implementation Complete

**Commit**: `7faadeb` - feat(SPEC-002): implement CLI package foundation

All phases completed successfully. CLI package is ready for distribution and use.

## Specification Summary

**SPEC-002** establishes the foundational CLI package for the OpenAPI MCP tool. This is a **feature specification** focused on creating a working, installable CLI package with minimal ceremony and maximum pragmatism.

### Validation Checklist
- [x] SPEC document exists and is readable
- [x] No "NEEDS CLARIFICATION" tags remain (all resolved)
- [x] All functional requirements are clear
- [x] All acceptance scenarios are complete

## Technical Approach

**Pragmatic Development Philosophy:**
- Manual testing over exhaustive unit tests for packaging mechanics
- Command-line validation over pytest ceremonies
- Rapid iteration with real user workflows
- Focus on working software over testing infrastructure

**Technology Stack:**
- ✅ **Click**: Industry standard CLI framework
- ✅ **FastMCP**: Core MCP functionality
- ✅ **HTTPX**: Modern HTTP client
- ✅ **pipx**: Preferred installation method
- ✅ **uv**: Modern Python package management

## Requirements Mapping

| Requirement | Implementation Approach |
|-------------|------------------------|
| FR-001: pip/pipx installable | Configure pyproject.toml, manual install testing |
| FR-002: `openapimcp` command | CLI entry point with Click |
| FR-003: Help information | Click auto-generated help + custom descriptions |
| FR-004: Runtime dependencies | Proper dependency declaration in pyproject.toml |
| FR-005: Auto dependency mgmt | Let pip/pipx handle this (no custom testing needed) |
| FR-006: Installation verification | Manual workflow testing |

## Implementation Phases

### Phase 0: Package Structure Setup (1-2 hours)

**SETUP-001: Create Package Structure**
- Create `src/openapimcp/` directory structure
- Set up `__init__.py`, `main.py`, `cli.py`
- Configure pyproject.toml with project metadata and dependencies
- **Validation**: `uv sync` works, package structure is correct

**SETUP-002: CLI Entry Point**
- Configure `[project.scripts]` in pyproject.toml
- Create basic Click CLI application
- **Validation**: `uv run openapimcp --help` shows something useful

### Phase 1: Core CLI Implementation (2-3 hours)

**IMPL-001: Basic CLI Framework**
- Implement main CLI group with Click
- Add `--version` flag with package version
- Add `--help` with proper descriptions
- **Validation**: Manual testing of help and version output

**IMPL-002: Core Dependencies Integration**
- Import and initialize FastMCP components
- Import HTTPX for future HTTP functionality
- Ensure all imports work without errors
- **Validation**: `uv run python -c "import openapimcp; print('OK')"` succeeds

**IMPL-003: Professional CLI Polish**
- Add proper CLI descriptions and help text
- Configure Click for extensibility (command groups)
- Add basic error handling and user-friendly messages
- **Validation**: CLI feels professional when testing manually

### Phase 2: Manual Testing & Refinement (1-2 hours)

**TEST-001: Local Installation Testing**
- Test `pip install -e .` (editable install)
- Test `pipx install .` (isolated install)
- Verify command availability and functionality
- **Validation**: Fresh shell session can run `openapimcp` commands

**TEST-002: User Workflow Validation**
- Test all acceptance scenarios manually
- Verify help information is useful and complete
- Test version information display
- Fix any issues discovered
- **Validation**: All acceptance scenarios work in practice

**TEST-003: Cross-Platform Verification**
- Test on different environments if available
- Verify dependency resolution works correctly
- Check for common installation issues
- **Validation**: Installation works reliably

### Phase 3: Package Distribution Readiness (1 hour)

**DIST-001: Package Metadata Completion**
- Complete all pyproject.toml metadata fields
- Add proper README, license information
- Ensure package description is accurate
- **Validation**: Package metadata is professional and complete

**DIST-002: Build System Validation**
- Test `python -m build` creates proper wheel/sdist
- Verify package contents are correct
- Test installation from built artifacts
- **Validation**: Built package installs and works correctly

## Manual Testing Script

Create this simple validation script to replace excessive pytest ceremonies:

```bash
#!/bin/bash
# test-cli.sh - Manual CLI validation

echo "=== Testing CLI Package ==="

# Test 1: Clean install
pipx uninstall openapimcp 2>/dev/null || true
pipx install .

# Test 2: Command availability
echo "Testing command availability..."
which openapimcp || exit 1

# Test 3: Help output
echo "Testing help output..."
openapimcp --help || exit 1

# Test 4: Version output
echo "Testing version output..."
openapimcp --version || exit 1

# Test 5: Import validation
echo "Testing imports..."
python -c "import openapimcp, fastmcp, click, httpx; print('All imports OK')" || exit 1

echo "=== All tests passed ==="
```

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Dependency conflicts | Medium | Use uv for reliable resolution |
| Package metadata issues | Low | Manual testing catches problems |
| CLI UX problems | Medium | Focus on manual workflow testing |

## Effort Estimation

- **Phase 0**: 1-2 hours (package setup)
- **Phase 1**: 2-3 hours (core implementation)
- **Phase 2**: 1-2 hours (manual testing)
- **Phase 3**: 1 hour (distribution prep)
- **Total**: 5-8 hours (vs 18-25 hours in over-engineered version)

## Success Criteria

✅ Users can install with `pipx install openapimcp` in under 2 minutes
✅ `openapimcp --help` shows useful information immediately
✅ `openapimcp --version` displays correct version
✅ All core dependencies import and work correctly
✅ Package ready for PyPI distribution
✅ Professional CLI user experience

## Key Differences from Previous Plan

**Removed Excessive Testing:**
- No tests for basic import functionality (uv handles dependency resolution)
- No tests for pip/pipx installation mechanics (these are well-tested tools)
- No TDD cycles for packaging boilerplate

**Added Practical Focus:**
- Manual testing with real user workflows
- Command-line validation over pytest ceremonies
- Rapid iteration and real-world validation
- Focus on user experience over test coverage metrics

**Pragmatic Philosophy:**
- Trust the tools (uv, pip, pipx) to do their job correctly
- Test what matters: CLI functionality and user workflows
- Build working software quickly and iterate based on real usage
- Manual testing is often more valuable than unit tests for CLI tools

This approach gets us to a working, installable CLI package much faster while ensuring it actually works well for end users.