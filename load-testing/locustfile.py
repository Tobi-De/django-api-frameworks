import threading

from locust import FastHttpUser, between, tag, task

# Create a global lock object
task_lock = threading.Lock()


class ApiLoadTest(FastHttpUser):
    wait_time = between(1, 3)  # Time between tasks (1 to 3 seconds)
    host = "http://localhost"

    @tag("drf_with_serializer")
    @task(1)
    def test_drf_with_serializer(self):
        with task_lock:  # Only one task can run at a time due to this lock
            self.client.get("http://django-drf:8000/drf/with-serializer/")

    @tag("drf_without_serializer")
    @task(1)
    def test_drf_without_serializer(self):
        with task_lock:
            self.client.get("http://django-drf:8000/drf/without-serializer/")

    @tag("ninja_with_schema")
    @task(1)
    def test_ninja_with_schema(self):
        with task_lock:
            self.client.get("http://django-ninja:8001/ninja/with-schema/")

    @tag("ninja_without_schema")
    @task(1)
    def test_ninja_without_schema(self):
        with task_lock:
            self.client.get("http://django-ninja:8001/ninja/without-schema/")

    @tag("fastapi_with_pydantic")
    @task(1)
    def test_fastapi_with_pydantic(self):
        with task_lock:
            self.client.get("http://fastapi:8002/fastapi/")

    @tag("django_rapid")
    @task(1)
    def test_django_rapid(self):
        with task_lock:
            self.client.get("http://django-rapid:8004/api/cars/")

    @tag("django_bolt")
    @task(1)
    def test_django_bolt(self):
        with task_lock:
            self.client.get("http://django-bolt:8005/api/cars/")

    @tag("djrest2")
    @task(1)
    def test_djrest2(self):
        with task_lock:
            self.client.get("http://djrest2:8006/api/cars/")

    @tag("shinobi_with_schema")
    @task(1)
    def test_django_shinobi(self):
        with task_lock:
            self.client.get("http://django-shinobi:8007/ninja/with-schema/")

    @tag("shinobi_without_schema")
    @task(1)
    def test_django_shinobi(self):
        with task_lock:
            self.client.get("http://django-shinobi:8007/ninja/without-schema/")

    @tag("fast_drf")
    @task(1)
    def test_fast_drf(self):
        with task_lock:
            self.client.get("http://fast-drf:8008/api/v1/cars/")
