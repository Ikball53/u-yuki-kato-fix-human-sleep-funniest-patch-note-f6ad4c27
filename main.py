import os

LINE = "Fixed a bug where sleep crashed at 3 AM whenever you remembered that one embarrassing thing you said in 2019."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
