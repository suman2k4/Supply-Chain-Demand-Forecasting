# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from your project folder to the container
COPY . .

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for Streamlit (8501) and Flask (5000)
EXPOSE 8501 5000

# Run both apps when the container starts
CMD ["bash", "-c", "streamlit run app.py & python template.py"]
