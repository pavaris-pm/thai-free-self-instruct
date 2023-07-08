import time
import pyautogui
import pyperclip
from self_instruct_prompt import get_prompt


def self_instruct_query():
    
    # Open the OpenAI website
    prompt = get_prompt()
    pyperclip.copy(prompt)

    # for open the notepad of your screen (Window User)
    pyautogui.press('winleft')
    pyautogui.write('notepad')
    pyautogui.press('enter')
    time.sleep(2)
    #pyautogui.write(prompt)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(5) # let it write the prompt
    # to copy prompt from the notepad to paste in on OpenAI prompt
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

    # for open the window tab of your screen (Window User)
    pyautogui.press('winleft')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(3)

    # Simulate keyboard shortcut to open a new tab
    pyautogui.hotkey('ctrl', 't')

    # Enter the OpenAI website
    pyautogui.write('https://chat.openai.com/?model=text-davinci-002-render-sha')
    pyautogui.press('enter')
    time.sleep(5)

    # enter the prompt
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(20) # this part is for text generation output

    # for demo part, we will copy it by hand
    pyautogui.press('winleft')
    pyautogui.write('notepad')
    pyautogui.press('enter')
    time.sleep(5)

    # to copy prompt from the notepad to paste in on OpenAI prompt
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)

    # Save the text from Notepad to a file
    file_path = 'thai_self_instruct_output.txt'
    pyautogui.hotkey('ctrl', 's')
    pyautogui.write(file_path)
    pyautogui.press('enter')

    print("Output saved to:", file_path)



