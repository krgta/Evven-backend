import pytest
from sqlalchemy import text

from database import engine


@pytest.mark.anyio
async def test_database_connection():
    async with engine.begin() as conn:
        result = await conn.execute(
            text("SELECT 1")
        )
        assert result.scalar() == 1