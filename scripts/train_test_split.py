import pandas as pd
from sklearn.model_selection import train_test_split


def split_and_save(
    input_csv: str,
    output_dir: str = "data/split",
    test_size: float = 0.2,
    random_state: int = 42
):
    df = pd.read_csv(input_csv)

    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        shuffle=True,
        random_state=random_state
    )

    train_df.to_csv(f"{output_dir}/train.csv", index=False)
    test_df.to_csv(f"{output_dir}/test.csv", index=False)

    print(f"Train rows: {len(train_df)}")
    print(f"Test rows: {len(test_df)}")


def main():
    split_and_save("./data/kaggle_train.csv")


if __name__ == "__main__":
    main()
