import sys


def md(file_path: str, lang: str = "python", redo=False):
    """

    :param file_path:
    :param lang:
    :param redo: execute even if theres a codeblock output underneath
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

    gen_cnt = ""
    for block in blocks:
        gen_cnt += block + "```"
        if block.startswith(lang):
            block = "result_array_with_an_unique_name = []" + block[len(lang):]
            work_around = dict()
            # smart? way of replacing each occurrence of "print" with a unique variable
            block = block.replace("print", f"result_array_with_an_unique_name.append")
            exec(block, work_around)
            gen_cnt += "\n> " + "  \n".join([str(r) for r in work_around["result_array_with_an_unique_name"]]) + "\n"
    gen_cnt = gen_cnt[:-3]
    with open(file_path, 'w') as f:
        f.write(gen_cnt)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a markdown file location.")
    md(sys.argv[1])
