import pandas as pd
from instruct_query import self_instruct_query
import time
import pyautogui
import pyperclip
from self_instruct_prompt import get_prompt
from csv_generator import format_generated_output, save_csv

# run an entire pipeline for extracting thai slef-instruct dataset
def main():
    self_instruct_query() # query self-instruct dataset
    time.sleep(3)
    # set this to be your own path
    dataset = format_generated_output('./thai_self_instruct_output.txt')
    save_csv('./', dataset)


if __name__ == "__main__":
    main()
