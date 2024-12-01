import pandas as pd
import numpy as np

# Generate synthetic data
def generate_data(samples=1000):
    np.random.seed(42)
    data = {
        "height": np.random.normal(170, 10, samples),
        "weight": np.random.normal(75, 15, samples),
        "preference": np.random.choice(["tight", "regular", "loose"], samples),
        "age": np.random.randint(18, 60, samples),
        "body_shape": np.random.choice(["slim", "average", "athletic", "plus-size"], samples),
        "size": np.random.choice(["XXS", "XS", "S", "M", "L", "XL", "XXL"], samples)
    }
    return pd.DataFrame(data)

# Save the data to a CSV file
if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/generated_data.csv", index=False)
    print("Synthetic data generated and saved to data/generated_data.csv")
