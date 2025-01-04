# Create a script named run_codebase.sh

echo "#!/bin/bash

# Step a: Install dependencies
pip install -r requirements.txt

# Step b: Run the main code
python src/main.py

# Run tests
pytest tests/test_agent_manager.py
" > run_codebase.sh

# Make the script executable
chmod +x run_codebase.sh

# Execute the script
./run_codebase.sh
