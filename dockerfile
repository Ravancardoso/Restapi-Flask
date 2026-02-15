# 1️⃣ Lightweight and official Python base image
FROM python:3.10-alpine


HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -sf http://localhos:5000/health || exit 1

# 2️⃣ Environment variables for better Python behavior
# - Prevents Python from writing .pyc files
# - Ensures logs are sent directly to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ System dependencies (only required if Python packages need compilation)
RUN apk add --no-cache gcc musl-dev linux-headers

# 4️⃣ Set working directory inside the container
WORKDIR /app

# 5️⃣ Install application dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copy application source code
COPY api.py .

# 7️⃣ Create and switch to a non-root user for security
RUN addgroup -S app && adduser -S app -G app
USER app

# 8️⃣ Expose application port (documentation purpose)
EXPOSE 5000

# 9️⃣ Define the main process
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api:app"]