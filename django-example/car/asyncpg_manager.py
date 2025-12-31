from typing import Any

import asyncpg
from django.conf import settings


class AsyncpgManager:
    """Manager for asyncpg connections with Django settings integration."""

    def __init__(self):
        self.pool = None

    async def get_pool(self) -> asyncpg.Pool:
        """Get or create connection pool."""
        if self.pool is None:
            db_config = settings.DATABASES["default"]
            self.pool = await asyncpg.create_pool(
                host=db_config["HOST"],
                port=db_config["PORT"],
                user=db_config["USER"],
                password=db_config["PASSWORD"],
                database=db_config["NAME"],
                min_size=5,
                max_size=20,
            )
        return self.pool

    async def get_cars(self, limit: int = None) -> list[dict[str, Any]]:
        """
        Bypasses Django ORM.
        """

        pool = await self.get_pool()

        query = """
SELECT
    c.id,
    c.vin,
    c.owner,
    c.created_at,
    c.updated_at,
    c.model_id as car_model_id,
    cm.name as car_model_name,
    cm.year as car_model_year,
    cm.color
FROM car_car c
JOIN car_carmodel cm ON c.model_id = cm.id
ORDER BY c.id
        """

        if limit:
            query += f" LIMIT {limit}"

        async with pool.acquire() as conn:
            rows = await conn.fetch(query)

            return [dict(row) for row in rows]

    async def close(self):
        """Close the connection pool."""

        if self.pool:
            await self.pool.close()

            self.pool = None


# Global instance
asyncpg_manager = AsyncpgManager()
