from assets.ressources import bles

def get_item_coordinates(item_name: str) -> dict:
    """
    Retrieve the coordinates of a specified item on the map.
    Args:
        item_name (str): The name of the item to find coordinates for.
    Returns:
        dict: A dictionary containing the coordinates of the specified item and the associated quantity.
    """

    if item_name == "ble":
        return bles
