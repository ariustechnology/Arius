"""Gunicorn configuration for arius."""

import logging
import multiprocessing
import os

# Logger configuration
logger = logging.getLogger('arius')
accesslog = '-'
errorlog = '-'
loglevel = os.environ.get('ARIUS_LOG_LEVEL', 'warning').lower()
capture_output = True

# Worker configuration
#  TODO: Implement support for gevent
# worker_class = 'gevent'  # Allow multi-threading support
worker_tmp_dir = '/dev/shm'  # Write temp file to RAM (faster)
threads = 4


# Worker timeout (default = 90 seconds)
timeout = os.environ.get('ARIUS_GUNICORN_TIMEOUT', 90)

# Number of worker processes
workers = os.environ.get('ARIUS_GUNICORN_WORKERS', None)

if workers is not None:
    try:
        workers = int(workers)
    except ValueError:
        workers = None

if workers is None:
    workers = multiprocessing.cpu_count() * 2 + 1

logger.info(f"Starting gunicorn server with {workers} workers")

max_requests = 1000
max_requests_jitter = 50
