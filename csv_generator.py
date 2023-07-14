import pandas as pd
from instruct_query import self_instruct_query

# this class will be used to format an output data and return as a csv file
def save_csv(path: str, dataframe: pd.DataFrame) -> None:
    file_path = f"{path}/self_instruct.csv"
    dataframe.to_csv(file_path, index=False)
    print(f"Self-Instruct Dataset Successfully saved to {file_path}")


def format_generated_output(output_path: str) -> pd.DataFrame:
    with open(output_path, 'r', encoding='utf-8') as file:
        txt_output = file.read()

    # preprocess text output in order to format it into dataframe
    print(txt_output)
    
    batch = txt_output.split("###")
    # convert to dataframe
    instr_batch = []
    input_batch = []
    output_batch = []

    for idx, sample in enumerate(batch):
      # must split from the back
      output = sample.split('Output:')
      input_txt = output[0].split('Input:')
      instr = input_txt[0].split('Instruction:')

      instr_batch.append(instr[-1])
      input_batch.append(input_txt[-1])
      output_batch.append(output[-1])


    print("Total Instruction Records", len(instr_batch))
    print("Total Input Records",len(input_batch))
    print("Total Output Records",len(output_batch))

    format_df = pd.DataFrame({
        'Instructions' : instr_batch,
        'Inputs' : input_batch,
        'Outputs' :output_batch,
    })

    return format_df
