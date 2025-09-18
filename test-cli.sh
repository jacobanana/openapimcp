#!/bin/bash
# test-cli.sh - Manual CLI validation

echo "=== Testing CLI Package ==="

# Test 1: Command availability
echo "Testing command availability..."
if command -v openapimcp &> /dev/null; then
    echo "✅ openapimcp command found"
else
    echo "❌ openapimcp command not found"
    exit 1
fi

# Test 2: Help output
echo "Testing help output..."
uv run openapimcp --help > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Help command works"
else
    echo "❌ Help command failed"
    exit 1
fi

# Test 3: Version output
echo "Testing version output..."
uv run openapimcp --version > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Version command works"
else
    echo "❌ Version command failed"
    exit 1
fi

# Test 4: Info command (dependency validation)
echo "Testing info command..."
uv run openapimcp info > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Info command works (dependencies functional)"
else
    echo "❌ Info command failed"
    exit 1
fi

# Test 5: Command groups
echo "Testing command groups..."
uv run openapimcp serve --help > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Serve command group works"
else
    echo "❌ Serve command group failed"
    exit 1
fi

uv run openapimcp validate --help > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Validate command group works"
else
    echo "❌ Validate command group failed"
    exit 1
fi

# Test 6: Import validation
echo "Testing imports..."
uv run python -c "import openapimcp, fastmcp, click, httpx; print('All imports OK')" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ All core dependencies import successfully"
else
    echo "❌ Import test failed"
    exit 1
fi

echo "=== All tests passed! ==="
echo "CLI package is working correctly."