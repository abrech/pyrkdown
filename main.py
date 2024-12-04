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
            block = block[len(lang):]
            work_around = dict()
            i = 0
            while "print" in block:
                block = block.replace("print", f"my_personal_var_{i} = ", 1)
                i += 1
            exec(block, work_around)
            gen_cnt += "\n> " + "  \n".join([str(work_around[f"my_personal_var_{i}"]) for i in range(i)]) + "\n"
    gen_cnt = gen_cnt[:-3]
    with open(file_path, 'w') as f:
        f.write(gen_cnt)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a markdown file location.")
    md(sys.argv[1])
