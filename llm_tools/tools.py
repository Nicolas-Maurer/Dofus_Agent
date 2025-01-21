from assets.ressources import ressources
from utils.helpers import normalize_input

## Need to find a way to give knowledge of the avaiable ressources to the model so it understand the user question
# Add this to the prompt when necessary, like in a RAG manner?
@normalize_input()
def get_item_coordinates(item_name: str) -> dict:
    """
    Retrieve the coordinates of a specified resource item on the map.
    
    Args:
        item_name (str): The name of the resource to find coordinates for.

    Raises:
        ValueError: If the specified item_name is not found in the available resources list.
        
    Returns:
        dict: A dictionary containing the coordinates (`x`, `y`) and the associated quantity of 
              the specified resource.
    """

    available_ressources = ressources.keys()

    if item_name not in available_ressources:
        raise ValueError(f"Resource '{item_name}' not found. "
               f"Available resources are: {', '.join(available_ressources)}.")
    else:
        return ressources[item_name]