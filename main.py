import sys
import uuid


def md(file_path: str, lang: str = "python", generate_duplicates=False):
    """

    :param file_path:
    :param lang:
    :param generate_duplicates: execute even if theres a codeblock output underneath
    :return:
    """
    content = ""
    with open(file_path, 'r') as f:
        content = f.read()
    if content == "":
        print("The given file was empty.")
        return

    blocks = content.split("```")
    if len(blocks) == 1:
        print("The given file did not contain any codeblocks.")
        return

    # print statements
    gen_cnt = ""
    for block in blocks:
        gen_cnt += block + "```"
        if block.startswith(lang):
            block = "result_array_with_an_unique_name = []" + block[len(lang):]
            work_around = dict()
            block = block.replace("print", f"result_array_with_an_unique_name.append")
            block = block.replace("plt.show()",
                                  f"plt.savefig(f'plot.png');(result_array_with_an_unique_name.remove('![a plot](plot.png)') or result_array_with_an_unique_name.append('![a plot](plot.png)')) if '![a plot](plot.png)' in result_array_with_an_unique_name else result_array_with_an_unique_name.append('![a plot](plot.png)')")

            exec(block, work_around)
            gen_cnt += "\n> ### Output" + "".join(["  \n> " + str(r) for r in work_around["result_array_with_an_unique_name"]]) + "\n"
    gen_cnt = gen_cnt[:-3]
    with open(file_path, 'w') as f:
        f.write(gen_cnt)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a markdown file location.")
    #md(sys.argv[1])

import matplotlib.pyplot as plt
for i in range(3):
  plt.plot([1 + i, 2, 3], [1, 4, 9 - i])
  plt.savefig("test.png")
print("hi")
plt.savefig("test2.png")