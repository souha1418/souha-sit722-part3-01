# Your Solution
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY book_catalog/requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY book_catalog/app/ /usr/src/app/book_catalog/

# Run the application
CMD ["uvicorn", "book_catalog.main:app", "--host", "0.0.0.0", "--port", "8000"]