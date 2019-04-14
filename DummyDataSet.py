import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = 1000
data = pd.DataFrame(
    {
        "A" : np.random.randn(n),
        "B" : 1.5 + 2.5 * np.random.randn(n),
        "C" : np.random.uniform(5, 32, n)
    }
)

print('data: ', data.head(5))
print(data.describe())
plt.hist(data["C"])
plt.show()