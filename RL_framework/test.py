import numpy as np
result = np.linspace(0, 11.0, 12)[1:-1]
result1 = np.digitize(1, bins=result)
print(result)
print(result1)
