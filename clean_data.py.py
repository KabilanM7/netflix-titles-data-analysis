import pandas as pd
import re


df = pd.read_csv("Data_Cleaning_Project.csv")

raw_rows, raw_cols = df.shape

print("Original Dataset:", df.shape)


old_columns = list(df.columns)

df.columns = [
    re.sub(r"[^0-9a-z]+", "_", col.strip().lower()).strip("_")
    for col in df.columns
]

print("\nColumn Names Cleaned")


text_columns = df.select_dtypes(include="object").columns

for col in text_columns:

    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    df[col] = df[col].replace(
        ["", "nan", "NaN", "NULL", "null", "N/A", "n/a", "?"],
        pd.NA
    )

print("Text Values Standardized")


if "date_added" in df.columns:

    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

    print("Date Column Converted")


before = len(df)

df = df.drop_duplicates().reset_index(drop=True)

duplicates_removed = before - len(df)

print("Duplicates Removed:", duplicates_removed)


missing_before = df.isnull().sum()

for col in df.columns:

    missing_count = df[col].isnull().sum()

    if missing_count > 0:

        if col == "date_added":

            
            continue

        elif pd.api.types.is_numeric_dtype(df[col]):

            median_value = df[col].median()

            df[col] = df[col].fillna(median_value)

        else:

            df[col] = df[col].fillna("Unknown")

print("Missing Values Handled")


if "date_added" in df.columns:

    df["date_added"] = df["date_added"].dt.strftime("%d-%m-%Y")

print("Date Format Standardized")


df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")


with open("cleaning_summary.md", "w", encoding="utf-8") as file:

    file.write("# Netflix Data Cleaning Report\n\n")

    file.write(f"Original Rows: {raw_rows}\n\n")

    file.write(f"Original Columns: {raw_cols}\n\n")

    file.write(f"Duplicates Removed: {duplicates_removed}\n\n")

    file.write("## Missing Values Before Cleaning\n\n")

    file.write(missing_before.to_string())

    file.write("\n\n## Missing Values After Cleaning\n\n")

    file.write(df.isnull().sum().to_string())

    file.write("\n\n## Final Dataset Shape\n\n")

    file.write(str(df.shape))

    file.write("\n\n## Final Data Types\n\n")

    file.write(df.dtypes.to_string())

print("Cleaning Summary Generated!")

print("\nFinal Dataset:", df.shape)

print("\nDATA CLEANING COMPLETED!")
