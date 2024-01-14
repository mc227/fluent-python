# mobility_profiles.py
from datetime import datetime
from display_menu import display_menu
from create_folder import create_folder
from create_ipynb import create_ipynb
import os
my_dict = {1:'1905295', 2:'1904066', 3:'1904065', 4:'1905296'}
def process_chosen_file(chosen_file):
    '''
    Placeholder for processing the chosen file.
    Implement your actual logic here.
    
    Parameters:
    - chosen_file (str): The name of the chosen file.

    Returns:
    - str: The path to the created folder.
    '''
    print(f'Processing {chosen_file}...')
    folder = create_folder(chosen_file)
    return folder

if __name__ == '__main__':
    chosen_file_main = display_menu()

    if chosen_file_main:
        print(f'You chose: {chosen_file_main}')
        folder_path = process_chosen_file(chosen_file_main)
        
        # ... (previous code)

        for i in range(1, 5):
            filename = os.path.normpath(os.path.join(folder_path, f'mmc{i}_{chosen_file_main}.ipynb'))
            markdown_content = f'# MMC{i} {chosen_file_main}'
            mmc_number = my_dict.get(i, None)  # Get the value from the dictionary based on i

            code_content = (
                f'# imports\n'
                f'import pandas as pd\nimport plotly.express as px\n'
                f'# variables\nCONSTANT = "../data/{chosen_file_main}"\n'
                f'relevant = []\nrelevant_filtered = []\nmmc{i} = []\nmmc{i}_times = []\n'
                f'# functions\n'
                f'def get_relevant_lines(filename,relevant):\n'
                f'    """\n'
                f'    get lines that start with Node URN to get just the relevant lines\n'
                f'    """\n'
                f'    keep_phrases = ["Node URN"]\n'
                f'    with open(filename, encoding="utf8") as f:\n'
                f'        f = f.readlines()\n'
                f'    for line in f:\n'
                f'        for phrase in keep_phrases:\n'
                f'            if phrase in line:\n'
                f'                relevant.append(line)\n'
                f'                break\n'
                f'def remove_backslash_n(array):\n'
                f'    """\n'
                f'    loop through array and remove /n at the end of the string\n'
                f'    """\n'
                f'    for i, s in enumerate(array):\n'
                f'        array[i] = s.strip()\n'
                f'def get_node_urn_and_time(array, new_array):\n'
                f'    """\n'
                f'    extract URN and time from string\n'
                f'    and populate new array\n'
                f'    reducing lines in a string to just \n'
                f'    Node URN = xxxx, Time = xxxx\n'
                f'    """\n'
                f'    for s in array:\n'
                f'        new_array.append(s.split(",")[0]+","+s.split(",")[-1])\n'
                f'def get_mmc(array, new_array, URN):\n'
                f'    """\n'
                f'    filter out specific mmc lines\n'
                f'    """\n'
                f'    for item in array:\n'
                f'        if URN in item:\n'
                f'            new_array.append(item)\n'
                f'def get_time(array, new_array):\n'
                f'    """\n'
                f'    get the last part of the string, which is just the numbers\n'
                f'    """\n'
                f'    for item in array:\n'
                f'        new_array.append(int(item.split("Time = ", 1)[1]))\n'
                f'get_relevant_lines(CONSTANT, relevant)\n'
                f'remove_backslash_n(relevant)\n'
                f'get_node_urn_and_time(relevant, relevant_filtered)\n'
                f'get_mmc(relevant_filtered, mmc{i}, "{{{mmc_number}}}")\n'
                f'get_time(mmc{i},mmc{i}_times)\n'
                f'mmc{i}_CONSTANT = pd.DataFrame({"time":mmc{i}_times})\n'
                f'mmc{i}_CONSTANT["time2"] = mmc{i}_CONSTANT["time"].shift(1)\n'
                f'mmc{i}_CONSTANT["difference"] = mmc{i}_CONSTANT.time - mmc{i}_CONSTANT.time2\n'
                f'# Using plotly.express\n'
                f'fig = px.line(mmc{i}_CONSTANT, y="difference", title = "{chosen_file_main} mmc{i}",x="time")\n'
                f'fig.show()\n'
            )

            create_ipynb(filename, markdown_content, code_content)

        # ... (remaining code)


        
    else:
        print('Exiting the script.')
