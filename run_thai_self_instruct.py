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
    dataset = format_generated_output('D:/SIIT Personal information/thai_self_instruct_output.txt')
    save_csv('D:/SIIT Personal information/', dataset)


if __name__ == "__main__":
    main()
