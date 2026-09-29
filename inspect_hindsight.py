try:
    from hindsight_client import Hindsight
    print(Hindsight.retain.__doc__)
    print("---")
    print(Hindsight.recall.__doc__)
except ImportError as e:
    print(f"Error: {e}")
