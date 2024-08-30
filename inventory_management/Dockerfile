# Your Solution
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY inventory_management/requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY inventory_management/app/ /usr/src/app/inventory_management/

# Run the application
CMD ["uvicorn", "inventory_management.main:app", "--host", "0.0.0.0", "--port", "8000"]