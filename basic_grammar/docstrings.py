# Pythonの関数の説明は次のように関数内にコメントする
def example_func(param1, param2):
    """Example function with types documented in the docstring

    Args:
        param1 (int): The first parameter
        param2 (str): The second parameter
    
    Returns:
        bool: The return value. True for success, False otherwise.
    
    """
    print(param1)
    print(param2)
    return True

# 関数のコメントを出力する
print(example_func.__doc__)
# Example function with types documented in the docstring

#     Args:
#         param1 (int): The first parameter
#         param2 (str): The second parameter
    
#     Returns:
#         bool: The return value. True for success, False otherwise.