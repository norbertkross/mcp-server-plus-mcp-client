import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("littlemcp")


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    # doc string
    """Calculate Body Mass Index (BMI) for a person.

    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: The calculated BMI value (weight in kg divided by height in meters squared)

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight_kg / (height_m**2)


@mcp.tool()
async def fetch_weather(lat: str, long: str) -> str:
    # doc string
    """Fetch current weather forecast data for a specific location using Open-Meteo API.

    Args:
        lat (str): Latitude coordinate of the location
        long (str): Longitude coordinate of the location

    Returns:
        str: JSON string containing weather forecast data including temperature,
             precipitation, wind speed, and other meteorological parameters

    Note:
        Uses the free Open-Meteo API (https://open-meteo.com) for weather data
    """
    async with httpx.AsyncClient() as client:
        # response = await client.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}")
        response = await client.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
        return response.text

if __name__ == "__main__":
    # Uses Standard Input Output
    # mcp.run()

    # Uses SSE
    mcp.run(transport="sse")